"""Independent parity probe for the mechanics belt-tangent migration.

Run from the repository root with the cycle mechanics worktree on PYTHONPATH.
The legacy calculation is restated here so this remains useful after the
production implementation has stopped carrying it.
"""

import math

from machinome_mechanics import belt_tangent_points
from solid2 import get_animation_time

from metamaquina2 import gt2
from metamaquina2.x_stage import x_belt
from metamaquina2.y_axis import y_belt


def legacy_normal(here, there):
    between = (there['center'][0] - here['center'][0],
               there['center'][1] - here['center'][1])
    distance = math.hypot(*between)
    unit = (between[0] / distance, between[1] / distance)
    delta = (gt2._sense(here) * here['radius']
             - gt2._sense(there) * there['radius']) / distance
    sideways = math.sqrt(1.0 - delta * delta)
    return (delta * unit[0] - sideways * unit[1],
            delta * unit[1] + sideways * unit[0])


def legacy_spans(circles):
    result = []
    for index, here in enumerate(circles):
        there = circles[(index + 1) % len(circles)]
        normal = legacy_normal(here, there)
        start = gt2._touch(here, normal)
        end = gt2._touch(there, normal)
        result.append((start, (normal[1], -normal[0]),
                       math.hypot(end[0] - start[0], end[1] - start[1])))
    return result


def legacy_arcs(circles):
    normals = [legacy_normal(circle, circles[(index + 1) % len(circles)])
               for index, circle in enumerate(circles)]
    lengths = []
    for index in range(len(circles)):
        following = (index + 1) % len(circles)
        onward = gt2._sense(circles[following])
        arrival = math.atan2(onward * normals[index][1],
                             onward * normals[index][0])
        departure = math.atan2(onward * normals[following][1],
                               onward * normals[following][0])
        turn = (onward * (arrival - departure)) % (2 * math.pi)
        lengths.append(circles[following]['radius'] * turn)
    return lengths


def legacy_metrics(circles):
    spans = legacy_spans(circles)
    arcs = legacy_arcs(circles)
    lengths = []
    for index, span in enumerate(spans):
        lengths.extend((span[2], arcs[index]))
    stations, travelled = [], 0.0
    for distance in lengths:
        stations.append(travelled)
        travelled += distance
    return travelled, stations


def close_nested(old, new, tolerance=1e-12):
    if isinstance(old, tuple):
        return len(old) == len(new) and all(
            close_nested(a, b, tolerance) for a, b in zip(old, new))
    return math.isclose(old, new, rel_tol=0.0, abs_tol=tolerance)


routes = {
    'x-machine': x_belt.CIRCLES,
    'y-machine': y_belt.CIRCLES,
    'back-idler': [
        gt2.on_pulley((0, 0), 5),
        gt2.on_idler((30, 4), 4, face='outer'),
        gt2.on_pulley((60, 0), 7),
    ],
    'collinear-equal': [
        {'center': [0, 0], 'radius': 2},
        {'center': [20, 0], 'radius': 2},
    ],
}

for name, circles in routes.items():
    old, new = legacy_spans(circles), gt2.spans(circles)
    assert close_nested(tuple(old), tuple(new)), (name, old, new)
    old_length, old_stations = legacy_metrics(circles)
    assert math.isclose(old_length, gt2.length(circles),
                        rel_tol=0.0, abs_tol=1e-12)
    assert close_nested(tuple(old_stations), tuple(gt2.stations(circles)))
    print(name, 'span/station parity', len(new), 'loop length',
          gt2.length(circles))

degenerate = {
    'first-zero': [
        {'center': [0, 0], 'radius': 0},
        {'center': [10, 0], 'radius': 2},
    ],
    'both-zero': [
        {'center': [0, 0], 'radius': 0},
        {'center': [10, 0], 'radius': 0},
    ],
}

for name, circles in degenerate.items():
    old, new = legacy_spans(circles), gt2.spans(circles)
    assert close_nested(tuple(old), tuple(new)), (name, old, new)
    old_length, old_stations = legacy_metrics(circles)
    assert math.isclose(old_length, gt2.length(circles),
                        rel_tol=0.0, abs_tol=1e-12)
    assert close_nested(tuple(old_stations), tuple(gt2.stations(circles)))
    assert all(math.isclose(math.hypot(*normal), 1.0)
               for normal in gt2._normals(circles))
    print(name, 'span/normal parity', new)

# Exercise the helper's supported deferred-expression face.  The mechanics
# cycle evaluates this same Solid2 expression family against independent
# angular references at five animation-time samples for every sense pair.
time = get_animation_time()
symbolic = belt_tangent_points(
    (time, 2 * time), 2 + time / 10, (20 - time, 7), 3, 1, -1)
assert all('$t' in str(coordinate)
           for point in symbolic for coordinate in point)
print('Solid2 deferred contacts', symbolic)
