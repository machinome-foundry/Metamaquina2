# Rolling-angle migration verification

This records the 2026-09-20 behavior-preserving migration of the X and Y
pulley laws to `machinome_mechanics.rolling_angle`.  The audit found both
natural inverse radius conversions: X retains its negative travel sign and
anchor projection, while Y retains its positive `gone` projection.  The
same-file degree-to-travel coefficients now use the already merged
`rolling_travel`; these were missed consumers in the earlier forward-helper
audit.  No unrelated degree/radian conversion was changed.

The branch started clean from `main` at
`c916f9b5f09ba27faaab9225fff0cdf6342fc00c`.  Validation imported mechanics
from `/home/asa/devel/machinome-studio/WTs/mechanics-rolling-angle` at planning
HEAD `c3665fc61291c895eb7719fbdc3c8fd274ec9e26`; because the implementation
was not yet committed there, the tested `machinome_mechanics/rolling.py` is
identified by SHA-256
`14a09ea6cee1c4af3aa2716242523253ad8b234154b4f68d6cac43868849664e`.

## Comparisons

Independent pre-change arithmetic and the helper were compared at positions
`-100`, `0`, and `100` mm.  X produced respectively
`-894.3693976321686`, `-2019.5319581622962`, and
`-3144.694518692424` degrees before migration; helper differences were 0,
`2.2737367544323206e-13`, and `4.547473508864641e-13` degrees.  Y produced
`2790.026055265325`, `3914.554622704441`, and `5039.083190143557`
degrees with exact float equality.  X's one-degree pitch arc changed only
from `0.08887622458327506` to `0.08887622458327507` mm; Y remained
`0.0889261534971313` mm.

With a raw SymPy `position` expression, X serialized as
`-11.2516256053013*position - 2019.5319581623` and Y as
`11.2452856743912*position + 3914.55462270444`; both retained `position` as
their sole free symbol.  Applying `rolling_angle` to each new `PITCH_ARC`
and fitted pitch radius returned exactly one degree, covering the inverse
pair used by `BEAM_PER_DEGREE` and `BED_PER_DEGREE`.

## Commands and results

All commands ran from this repository with the workspace virtual environment
and `PYTHONPATH="$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-rolling-angle"`.

`SOLID_BUILD_DIR=_build/rolling-angle machinome test simulation/metamaquina2.py --brep`
ran 67 tests in 172.70 seconds: 67 passed, 0 failed.  This includes both
axis motion, belt-tooth travel, pulley mesh, and one-groove-per-tooth checks,
so it covers the retained signs/projections and the complementary arc ratios.

The OpenSCAD snapshot command for pose `x=90`, `y=-80`, `z=140` generated
the scene but the renderer returned an empty failure after an existing
`jhead.scad` line-107 parser diagnostic.  The fallback web-renderer capture
used the same pose and independent `_build/rolling-angle-snapshot` directory:

`machinome snapshot simulation/metamaquina2.py -o _build/rolling-angle-driven-web.png --viewer web --autocenter --viewall --imgsize 1280x720 --drive x=90 --drive y=-80 --drive z=140`

Visual inspection found the carriage displaced toward +X and the bed toward
-Y as commanded; the frame, raised X beam, hot end, and filament run remained
visibly coherent.  At this whole-machine scale the belt-to-pulley contacts are
too small for the image to certify seating; the exact mesh and tooth-travel
tests above are the contact evidence.

The framework HEAD was
`0ce71cdea6cc4a2e7fd7e85dc68847daef3d34cc` before and after validation.
The viewer advanced concurrently from
`c6df93ddd1723f1b9be0fb7e73f19d6f6c2daffa` to
`5dcbf4d476ff0d34bb42fe13f9b799ebd8ec5852`; this is reported as dependency
drift rather than a pinned environment.  No shared installation was changed.
Because that viewer checkout also had concurrent dirty source, this web image
establishes the visible exterior pose only; it is not reproducible
pinned-renderer evidence or contact certification.
