# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
"""Reproduce the public declaration gate without editing production nodes.

Run from the project root with PYTHONPATH=. and the workspace Python.
World-frame fit is adapted from the AGPL-3.0-or-later project diagnostics
in Prusa3-vanilla, AlbertPro, SO-ARM100 and open_manipulator, copyright
2026 Luis Henrique Cassis Fagundes. Generated evidence stays outside _build.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil

import numpy as np
import trimesh

from machinome.motion.mates import declared_mates
from machinome.node.assembly import AssemblyNode
from machinome.node.declarative import declared_children
from machinome.node.frames import Frame

from simulation.electronics.endstops.acrylic_spacer import ZEndstopSpacer
from simulation.electronics.endstops.wood_spacer import YEndstopSpacer
from simulation.electronics.endstops.y_endstop import YEndstop
from simulation.electronics.endstops.z_endstop import ZEndstop
from simulation.params import acrylic_thickness, thickness


class FramedYSpacer(YEndstopSpacer):
    """Diagnostic-only connector on the actual string-selected leaf."""

    stack_axis = Frame()


class FramedZSpacer(ZEndstopSpacer):
    stack_axis = Frame()


class StaticKindControl(AssemblyNode):
    upper_seat = Frame(at=(0, 0, thickness))
    upper_spacer = FramedYSpacer('ymin')
    upper_mount = upper_spacer.stack_axis.on(upper_seat)


class ForwardedLegacyString(StaticKindControl):
    """Isolate the original constructor's positional-string forwarding."""

    def __init__(self, limit, **kwargs):
        self.limit = limit
        super().__init__(limit, **kwargs)


class CallableYKind(AssemblyNode):
    upper_seat = Frame(at=(0, 0, thickness))
    upper_spacer = FramedYSpacer(kind=lambda node: f'y{node.limit}')
    upper_mount = upper_spacer.stack_axis.on(upper_seat)

    def __init__(self, limit, **kwargs):
        self.limit = limit
        # Diagnostic only: omit original identity forwarding so the probe
        # reaches the arbitrary child argument's resolution, independently
        # of ForwardedLegacyString's earlier constructor refusal.
        super().__init__(**kwargs)


class CallableZKind(AssemblyNode):
    upper_seat = Frame(at=(0, 0, acrylic_thickness))
    upper_spacer = FramedZSpacer(kind=lambda node: f'z{node.limit}2')
    upper_mount = upper_spacer.stack_axis.on(upper_seat)

    def __init__(self, limit, **kwargs):
        self.limit = limit
        super().__init__(**kwargs)


def fitted_matrix(local, world):
    """Measure all three basis directions, independently of frame declarations."""
    left, right = local - local.mean(axis=0), world - world.mean(axis=0)
    u, _, vt = np.linalg.svd(left.T @ right)
    correction = np.eye(3)
    correction[2, 2] = np.linalg.det(u @ vt)
    rotation = (u @ correction @ vt).T
    translation = world.mean(axis=0) - rotation @ local.mean(axis=0)
    matrix = np.eye(4)
    matrix[:3, :3], matrix[:3, 3] = rotation, translation
    residual = float(np.max(np.abs(local @ rotation.T + translation - world)))
    assert residual < 1e-8, residual
    return matrix, residual


def capture_legacy(output):
    output.mkdir(parents=True, exist_ok=True)
    raw = output / 'raw-stl'
    raw.mkdir(exist_ok=True)
    result = {}
    for cls in (YEndstop, ZEndstop):
        for limit in ('min', 'max'):
            node = cls(limit)
            node.assemble()
            node.build_stls()
            label = f'{cls.__name__}:{limit}'
            children = []
            for child in node.children:
                artifact = Path(child.stl_file)
                archived = raw / artifact.name
                if archived.exists():
                    assert archived.read_bytes() == artifact.read_bytes()
                else:
                    shutil.copy2(artifact, archived)
                local = trimesh.load_mesh(archived, process=True).vertices
                matrix, residual = fitted_matrix(local, child.mesh.vertices)
                expected = np.eye(4)
                z = (0, thickness, 2 * thickness) if cls is YEndstop else (
                    0, acrylic_thickness, 2 * acrylic_thickness)
                index = len(children)
                expected[2, 3] = z[index]
                if cls is ZEndstop and limit == 'min' and index < 2:
                    expected[0, 3] = 20
                np.testing.assert_allclose(matrix, expected, atol=1e-9, rtol=0)
                children.append({
                    'name': child.name,
                    'class': type(child).__name__,
                    'kind': getattr(child, 'kind', None),
                    'identity': child.uniq_id,
                    'color': child.color,
                    'artifact': str(archived.relative_to(output)),
                    'sha256': hashlib.sha256(archived.read_bytes()).hexdigest(),
                    'world_matrix': matrix.tolist(),
                    'residual_mm': residual,
                })
            assert [child['name'] for child in children] == [
                'lower_spacer', 'upper_spacer', 'switch']
            for _ in range(3):
                node.assemble()
                assert [child.name for child in node.children] == [
                    child['name'] for child in children]
                for child, entry in zip(node.children, children):
                    local = trimesh.load_mesh(output / entry['artifact'], process=True).vertices
                    repeated, _ = fitted_matrix(local, child.mesh.vertices)
                    np.testing.assert_allclose(repeated, entry['world_matrix'], atol=1e-9, rtol=0)
            result[label] = {'identity': node.uniq_id, 'children': children,
                             'idempotent_assemblies': 3}
            print(f'captured original {label}: three direct leaves; three repeated assemblies', flush=True)
        for invalid in ('', 'middle', 'MIN', None, 1):
            try:
                cls(invalid)
            except ValueError as error:
                assert 'min or max' in str(error)
            else:
                raise AssertionError(f'{cls.__name__} accepted invalid limit {invalid!r}')
    return result


def source_tables():
    """An import-time table expansion, never a per-instance placement helper."""
    results = []
    for count in (0, 1, 3, 7):
        table = tuple((11 * index, -7 * index, 3 * index) for index in range(count))

        class TableControl(AssemblyNode):
            for _index, _point in enumerate(table):
                locals()[f'spacer_{_index}'] = FramedYSpacer('ymin', name=f'spacers-{_index}')
                locals()[f'seat_{_index}'] = Frame(at=_point)
                locals()[f'mount_{_index}'] = locals()[f'spacer_{_index}'].stack_axis.on(
                    locals()[f'seat_{_index}'])
            # Loop variables do not exist for the empty table.
            if table:
                del _index, _point

            @property
            def spacers(self):
                return tuple(getattr(self, f'spacer_{index}') for index in range(len(table)))

            def render(self):
                # An empty assembly explicitly returns an empty child list.
                return list(self.spacers)

        node = TableControl()
        node.assemble()
        node.build_stls()
        names = [child.name for child in node.children]
        assert names == [f'spacers-{index}' for index in range(count)]
        assert list(declared_children(TableControl)) == [f'spacer_{index}' for index in range(count)]
        assert len(declared_mates(TableControl)) == count
        assert tuple(node.children) == node.spacers
        matrices = []
        for index, child in enumerate(node.children):
            local = trimesh.load_mesh(child.stl_file, process=True).vertices
            matrix, _ = fitted_matrix(local, child.mesh.vertices)
            expected = np.eye(4)
            expected[:3, 3] = table[index]
            np.testing.assert_allclose(matrix, expected, atol=1e-9, rtol=0)
            matrices.append(matrix.tolist())
        results.append({'count': count, 'ordered_names': names,
                        'mates': len(declared_mates(TableControl)), 'world_matrices': matrices})
        print(f'source-table scalar control: {count} entries, {count} mates, names and full matrices preserved', flush=True)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('_build_p1-07_evidence/feasibility'))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    control = StaticKindControl()
    control.assemble()
    control.build_stls()
    local = trimesh.load_mesh(control.upper_spacer.stl_file, process=True).vertices
    measured, _ = fitted_matrix(local, control.upper_spacer.mesh.vertices)
    expected = np.eye(4)
    expected[2, 3] = thickness
    np.testing.assert_allclose(measured, expected, atol=1e-9, rtol=0)
    print('actual scalar spacer declaration/mate control: accepted', flush=True)
    try:
        ForwardedLegacyString('min')
    except TypeError as error:
        constructor_refusal = str(error)
        assert 'takes no positional arguments' in constructor_refusal
        print(f'original string identity forwarding with declared children refused: {constructor_refusal}', flush=True)
    else:
        raise AssertionError('original positional identity forwarding unexpectedly admitted')
    refusals = {}
    for cls in (CallableYKind, CallableZKind):
        for limit in ('min', 'max'):
            try:
                node = cls(limit)
                node.assemble()
            except ValueError as error:
                message = str(error)
                assert 'endstop spacer' in message and 'function' in message, message
                refusals[f'{cls.__name__}:{limit}'] = message
                print(f'callable string child kind refused: {cls.__name__}({limit!r}): {message}', flush=True)
            else:
                raise AssertionError(f'callable kind unexpectedly resolved: {cls.__name__}({limit!r})')
    for cls in (YEndstop, ZEndstop):
        assert not declared_children(cls), cls
        assert not hasattr(cls, 'lower_spacer'), cls
        print(f'{cls.__name__}: lower_spacer/upper_spacer/switch are instance-created, not declared mate ends', flush=True)
    result = {'status': 'blocked_public_declaration_route',
              'scalar_control_world_matrix': measured.tolist(),
              'constructor_refusal': constructor_refusal,
              'callable_kind_refusals': refusals,
              'source_table_controls': source_tables(),
              'original_variants': capture_legacy(args.output)}
    (args.output / 'results.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Finding reproduced. Production endstop code is unchanged; no complete-model certification.', flush=True)


if __name__ == '__main__':
    main()
