# Belt path-metrics migration verification

This records the 2026-09-20 behavior-preserving migration of the GT2 route
measurements to `machinome_mechanics.belt_path_metrics`.  A narrow `_metrics`
adapter translates the project's circle dictionaries and its preserved
`clockwise`/`counterclockwise` markers.  Public `spans()` and `stations()`
remain lists.  The helper's circle-indexed arc lengths are rotated left once
so `_arcs()` retains the project's historical after-span indexing: span 0 is
followed by the arc about circle 1.  Loop length, fitted tooth count and pitch,
anchor stations, pulley phase, and all mounting-frame conventions remain in
the project.  The now-unused local normal and contact implementations were
removed after adapting and rerunning their independent probe.

The branch started clean from `main` at
`42013334c43b036bacbf68b881f01704bae20ba6`.  Validation imported mechanics
from `/home/asa/devel/machinome-studio/WTs/mechanics-belt-path-metrics` at
planning HEAD `7c5193aa2446b36549804c847d24d3995ccbfa7b`.  The helper
implementation was uncommitted there.  An initial run used `belts.py` SHA-256
`8e7dc4203f44a62569f2de3062bdc89e6e93d2c206c50b6249ac659cd72e372f`.
Package review then found a seam reduction that could round a tiny negative
zero-wrap to 360 degrees; after its red regression and branch-free repeated
floor reduction, final project validation used SHA-256
`09388c2cb4a3839f8c542c04cebfd5f29344dbee240023ccef7382171aa1a9dd`.

## Independent parity probe

`docs/probes/belt_tangent_points.py` retains independent copies of the legacy
normal, contact, arc, length and station arithmetic.  It was adapted to read
normals from the current public span output, then run with:

`PATH=/home/asa/devel/machinome-studio/.venv/bin:$PATH PYTHONPATH="$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-belt-path-metrics" python docs/probes/belt_tangent_points.py`

The corrected helper passed actual X and Y routes, a mixed back-idler route,
equal-radius collinear circles, a limiting inner-tangent route with zero span,
a first-zero-radius route, and a both-zero-radius route at absolute tolerance
`1e-12`.  Contacts, directions, spans, rotated arcs, total lengths and every
station agreed.  The X loop remained `803.8854513557229` mm with stations
`[0.0, 374.9606340005496, 413.11480912405784, 788.0754431246074]`.
The Y loop remained `1036.4343190090678` mm with stations
`[0.0, 397.15991741362825, 430.7802454629051, 467.6272682196904,
481.4977010141353, 543.6081114622965, 578.1315400519219,
1002.1315400519219]`.  The limiting route remained length zero.  No fitted
tooth count or period changed.  The existing Solid2 deferred tangent probe
also remained runnable; the nonlinear helper's own suite supplies sampled
deferred metrics comparisons.

## Machine validation and image

All project commands used the workspace virtual environment,
`PYTHONPATH="$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-belt-path-metrics"`,
and isolated `SOLID_BUILD_DIR=_build/belt-path-metrics`.

Before the seam correction, `machinome test metamaquina2/metamaquina2.py
--exact` ran 67 tests in 421.84 seconds: 67 passed, 0 failed.  After the
correction, the same command reran against the final helper source and ran 67
tests in 203.04 seconds: 67 passed, 0 failed.  Relevant contracts include both
closed flexible loops, X and Y belt redraw/travel, idler routing, pulley mesh,
and one groove per belt tooth.  The existing `jhead.scad` line-107 parser
diagnostic occurred during the cold build but did not prevent completion.

After the corrected run, `machinome build metamaquina2/metamaquina2.py`
completed successfully in the same isolated build directory and reported the
published artifacts current.  The fresh representative image command was:

`machinome snapshot metamaquina2/metamaquina2.py -o _build/belt-path-metrics-driven-web.png --renderer web --autocenter --viewall --imgsize 1280x720 --drive x=90 --drive y=-80 --drive z=140`

Visual inspection is limited to the whole-machine exterior pose: carriage and
bed displacement, frame, raised beam, hot end, and filament run are coherent.
Tangency and pulley contact are too small for this image to certify; the
independent metrics and exact contracts above are that evidence.

Framework HEAD was initially clean at
`0ce71cdea6cc4a2e7fd7e85dc68847daef3d34cc` and advanced concurrently to
clean `8d2bd71171be81f13ba5dd492851ed8b3a9ababb` (ancestor-joint work, not
path math).  The corrected exact rerun began before that new HEAD was observed,
so it is not claimed as a pinned framework identity; the corrected explicit
build and image ran after the new HEAD was recorded.  Viewer HEAD remained
clean at `4355da1a7f64dacd7d86eb27dbdfdf7ced94598f`.  The image establishes
visible exterior pose only, not contact certification.  No shared installation
was repointed.
