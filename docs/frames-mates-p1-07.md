# Frames and mates — P1-07 Metamaquina 2

8 October 2026. Status: blocked at the public declaration gate; independently
reviewed. Production model source and existing tests are unchanged.
Investigation: Sol 6.1, xhigh; independent review and any commit belong to the
coordinating agent.

The project root is `/mnt/data/machinome-projects/3D-Printers/Metamaquina2`,
also reached through the workspace's `projects/3D-Printers/Metamaquina2`
link. The clean starting branch is `main`, at
`1451dd1903effa69ebda84fc93a3c90212db398c`; it is two commits ahead of its
upstream and no push is authorized. Framework content is
`6cc56a24529a47f3cb988754ece7d5ab654c5cc3`. The site retains its older pin
`4cc1da7b84726df38969d5704cda48b96e9852d6`; this work changes no site record.

## Scope and initial plan

The requested equivalent refactor covers the declared
`simulation.metamaquina2:Metamaquina2` root, every subordinate assembly and
shared hardware, including the source-table fasteners, controller, cable
clips, power supply, both variants of both endstop assemblies, spool stand,
three axes, belts, springs and filament. Assembly rest placement must become
named physical frames and mates while preserving ordered tree identities,
source-derived dimensions, constructor and parameter envelopes, leaf
geometry, joints, ports, drivers, instructions and motion.

Read the complete studio machining and public API skills, project README,
simulation README, NOTICE, CREDITS, manifest, the root's complete existing
test file and the assembly/design-reading/motion specifications. The prior
motion changes are archived; there is no active frames migration to reconcile.
This equivalent refactor needs a project-owned record, not a new interface
proposal.

First check declaration feasibility, before a large baseline or production
edit. Source-table lengths are probed at import and must remain variable when
the design changes. A successful ordinary Python class-body expansion can
declare scalar children, seats and mates from those tables, with explicit
legacy tree names and read-only grouping properties. Probe zero, one and
multiple entries, ordered names and complete matrices before spreading this
pattern. Clear loop temporary names rather than leaving child aliases.

If feasibility passes, capture the untouched complete model's ordered tree,
parameters, joints, ports, colors, raw rigid STL assets, full 4×4 world poses,
flexible geometry and entire viewer publication at defaults, nonzero poses,
travel endpoints/intermediate points and instruction states; verify
idempotence within each capture. Keep evidence in the separately ignored
`_build_p1-07_evidence/`, outside the swept live build. Establish existing mesh
and B-rep test/build verdicts, add independent red-first attachment checks,
refactor one assembly at a time, compare exact geometry and evaluated world
poses/publication, run full final B-rep regression and actual node-code
translation/attitude mutation checks, and inspect matching complete images.
Existing physical defects do not authorize geometry repairs or relaxed tests.

## Feasibility gate: string-selected endstop children

`simulation/electronics/endstops/y_endstop.py:YEndstop.__init__` accepts the
ordinary positional string `limit`, exactly `min` or `max`. It creates two
`YEndstopSpacer` instances with kind `ymin` or `ymax` and a microswitch, and
places the upper spacer and switch in the constructor. The string is forwarded
to `super().__init__` and participates in the assembly's existing artifact key.

`simulation/electronics/endstops/z_endstop.py:ZEndstop.__init__` similarly
selects `zmin1`/`zmin2` or `zmax1`/`zmax2`. Its minimum spacer offset is 20 mm;
the two acrylic thickness offsets and switch placement are also made in the
constructor. Both assemblies return those three instance-created children
from `render()` in lower-spacer, upper-spacer, switch order.

The studio's [machinome-api skill](/home/asa/devel/machinome/machinome-studio/shop-skills/machinome-api/SKILL.md),
in its frames-and-mates section, states: "The **moving end** is a frame of a
directly declared child." These children exist only after construction.
The documented callable resolution applies to frame/joint arguments; it does
not document resolving a callable passed as an arbitrary child-constructor
string argument. Numeric parameter tokens and formulas do not preserve the
ordinary string constructor envelope by themselves.

The narrow probe in `simulation/tools/check_endstop_mate_feasibility.py`
checks scalar declaration controls, source-table cardinality and the real
spacer constructors' treatment of callable `kind` arguments, then captures
the four untouched endstop variants. A new Flag schema, replacement subclasses
or wrapper tree would change the requested constructor/schema/identity
contract and needs the pilot's separate direction. This finding does not
claim that every possible Python workaround is impossible.

The same skill states that a declarative class rejects positional arguments.
The first fixture kept the original `super().__init__(limit, **kwargs)` and
hit that earlier gate. The reproducer now checks that refusal explicitly, and
omits the forwarding **only in its separate diagnostic callable fixtures** to
isolate the child argument's treatment. Omitting it from the production node
would discard the original assembly identity input, so it is not a solution.

The [machinome machining skill](/home/asa/devel/machinome/machinome-studio/shop-skills/machinome/SKILL.md)
requires an undocumented behavior to be reported as an API gap. Those two
documented declaration rules, the observed refusals and the queue's preserved
constructor/identity requirements stop this refactor before production edits.
A separately authorized framework investigation or a pilot-approved project
constructor/schema change is the next step; no new interface is proposed here.

## Measured results and evidence

Run from the project root:

```sh
mkdir -p _build_p1-07_evidence
set -o pipefail
PYTHONPATH=. PYTHONUNBUFFERED=1 /home/asa/devel/machinome/.venv/bin/python \
  simulation/tools/check_endstop_mate_feasibility.py \
  2>&1 | tee _build_p1-07_evidence/feasibility.log
```

The corrected reproducer exits **0**, meaning the diagnostic assertions all
hold, not that the printer migration passed. It measures:

- The real `YEndstopSpacer('ymin')` with a diagnostic-only declared connector
  accepts the scalar mate and lands at the full expected translation/attitude.
- Forwarding the original positional string from a class with declared
  children raises `TypeError`: `ForwardedLegacyString takes no positional
  arguments: its parameters are declared, pass them by name`.
- The actual Y spacer rejects callable `kind` for both limits: `no such Y
  endstop spacer <function ...>; expected one of ymin, ymax`. The actual Z
  spacer rejects both callable cases analogously, naming its four valid kinds.
  A callable reaches the constructor as a function, not a selected string.
- Generic import-time source-table expansions of **0, 1, 3 and 7** entries
  accept **0, 1, 3 and 7** scalar mates respectively. They retain direct
  ordered `spacers-N` paths, the same objects in the grouping property and all
  expected 4×4 world matrices. This proves the declaration pattern's
  feasibility, not a migration of the actual machine's source tables.
- The four untouched `YEndstop('min'/'max')` and
  `ZEndstop('min'/'max')` variants build with three direct leaves each in the
  original lower-spacer, upper-spacer, switch order. **12 baseline leaf
  poses** agree with independently written translation/attitude expectations;
  the maximum rigid vertex-fit residual is **7.11e-15 mm**, with a **1e-9**
  matrix-entry tolerance. Three repeated `assemble()` calls within every
  capture keep each leaf's matrix and order. Invalid limits `''`, `middle`,
  `MIN`, `None` and `1` retain the original `min or max` refusal.

The four assembly baseline artifact identities are:

| Original variant | Baseline identity |
| --- | --- |
| Y minimum | `YEndstop,min-71c2dc4446a4` |
| Y maximum | `YEndstop,max-920e5c0426c7` |
| Z minimum | `ZEndstop,min-066a75886a4d` |
| Z maximum | `ZEndstop,max-72371ef6ffbb` |

`_build_p1-07_evidence/feasibility/results.json` retains full leaf identities,
kinds, colors, matrices, residuals and raw STL hashes. Its `raw-stl/` directory
archives all **seven distinct original rigid assets** immediately, so a later
publication sweep cannot erase this baseline. The first, earlier-gate fixture
run is preserved in `feasibility-constructor-probe.log`; it is not claimed as
red-first regression evidence.

Observed existing source diagnostics remain: OpenSCAD reports the known
`jhead.scad:107` parser error through the inherited include chain, and the
microswitch source reports deprecated `child()`. The selected endstop assets
still build successfully. No geometry, warning or existing physical limitation
was repaired, waived or certified by this diagnostic.

## Independent review and disposition

The coordinating agent independently reran the tool with
`--output _build_p1-07_evidence/parent-review`. It exited **0** and confirmed the
scalar control, positional-constructor refusal, all four callable-kind
refusals, source-table cardinalities, four original variants and their three
reassemblies. Its original-variant witnesses and source-table matrices match
the implementer's captures exactly, including raw STL hashes. The parent
accepted **blocked** disposition under the preserved constructor/identity
contract.

Sol's initial diagnostic combined two refusal conditions; the earlier
constructor gate prevented reaching the callable-kind check. Splitting the
conditions corrected the reproducer before review. The parent clarified the
source-table cardinality and constructor/identity constraints, checked the
narrow finding and repeated it independently. No production correction was
made because no production migration was started.

This is a baseline witness and a bounded feasibility finding. There is no
after-migration model, whole-printer mesh/B-rep certification, complete pose or
publication comparison, mutation certification or snapshot pair. No project
row may be described as migrated from these results. Model source, root
README and existing model tests remain at the starting revision; NOTICE only
adds the original diagnostic tools to its existing AGPL software scope.

The finding/reproducer commit is left to the parent after this review. There
is no candidate migrated export revision. The old website pin is unchanged;
site intake, publication, push and framework implementation remain separate
work requiring their existing authority.
