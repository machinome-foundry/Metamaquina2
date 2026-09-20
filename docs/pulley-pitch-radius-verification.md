# Pulley pitch-radius migration verification

This records the 2026-09-20 behavior-preserving migration of the GT2 pulley
pitch-radius arithmetic to `machinome_mechanics.pulley_pitch_radius`.  The
audit found two natural calculations in `gt2.py`: `pulley_radius` now derives
the pitch circle through the helper before retaining the project's
`PITCH_LINE` subtraction, and `_passage` uses the same helper for the fitted
groove profile.  The fitted loop period and every downstream flank, seat,
angle, sign, and phase calculation are unchanged.  The inverse
`pulley_teeth` calculation is outside this helper's direction and remains
unchanged; no other runtime tooth-count/pitch radius was found.

The branch started clean from `main` at
`70ff30ed8af7617fa74a562de47234cdb7c35dea`.  Validation imported mechanics
from `/home/asa/devel/machinome-studio/WTs/mechanics-pulley-pitch-radius` at
planning HEAD `4870f32379fc9e0c966a0466a7a84f1ce4743ae5`.  Because the helper
implementation was not yet committed there, the exact tested
`machinome_mechanics/belts.py` is identified by SHA-256
`63f8d30a19d36b2cc4504919d6e3b989df1c0092348ad4c1930b31adb4ea482d`.

## Independent comparisons

The old expression `teeth * pitch / (2 * math.pi)` and the helper were
compared for tooth counts 12, 16, 20, and 37 and pitches 1.5, 2.0, and 2.037
mm.  All twelve results were bit-for-bit equal as Python floats.  Examples
include 16 teeth at 2 mm = `5.092958178940651` mm and 37 teeth at 2.037 mm
= `11.99534890589306` mm.  With raw SymPy symbols the helper returned
`0.159154943091895*pitch*teeth`, retaining `pitch` and `teeth` as its free
symbols.  These are supported raw expressions, not declared parameter tokens.

## Commands and results

Commands ran from this repository using the workspace virtual environment,
`PYTHONPATH="$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-pulley-pitch-radius"`,
and an isolated `SOLID_BUILD_DIR=_build/pulley-pitch-radius`.

`machinome test simulation/metamaquina2.py --exact` ran 67 tests in
453.23 seconds: 67 passed, 0 failed.  Relevant passing contracts include the
bought motor-pulley radius, X-end pulley dimension, X and Y pulley/belt mesh,
belt tooth travel, and one groove per belt tooth.  The build repeated the
existing `jhead.scad` line-107 parser diagnostic while completing normally.

The representative web snapshot command was:

`machinome snapshot simulation/metamaquina2.py -o _build/pulley-pitch-radius-driven-web.png --renderer web --autocenter --viewall --imgsize 1280x720 --drive x=90 --drive y=-80 --drive z=140`

Visual inspection is limited to the whole-machine exterior pose: carriage and
bed displacement, frame, raised beam, hot end, and filament run are coherent.
Pulley grooves and belt contact are too small for this image to certify; the
exact contracts above are that evidence.

Framework HEAD remained
`0ce71cdea6cc4a2e7fd7e85dc68847daef3d34cc`.  The concurrently developed
viewer began at `5dcbf4d476ff0d34bb42fe13f9b799ebd8ec5852` with unrelated dirty
source and later advanced to `4355da1a7f64dacd7d86eb27dbdfdf7ced94598f`.
Accordingly the image establishes visible exterior pose only, not
reproducible pinned-renderer or contact proof.  No shared installation was
repointed.
