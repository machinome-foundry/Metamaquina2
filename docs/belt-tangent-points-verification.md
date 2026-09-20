# Belt tangent-points migration verification

This records the 2026-09-20 behavior-preserving migration of the GT2 loop
tangent construction to `machinome_mechanics.belt_tangent_points`.  The
project's `clockwise` marker remains the default `+1` sense and its literal
`counterclockwise` marker remains the reverse `-1` sense.  `spans()` now uses
the helper's two contact points while retaining the project's direction,
length, wrap, station, fitted-radius, fitted-period, and tooth logic.
`_normals()` recovers the shared normal from the first nonzero signed radius;
when the first radius is zero it uses the second contact, and when both are
zero it uses the left perpendicular to the centre line.  Thus existing point
and zero-radius routes keep the normal needed by downstream arc logic.

The branch started clean from `main` at
`a652e8369551c540cd5dd71d82c34af28cf4080a`.  Validation imported mechanics
from `/home/asa/devel/machinome-studio/WTs/mechanics-belt-tangent-points` at
planning HEAD `38fa3bf6d084738ca7c75534a36d0fd1a6dc88e0`.  Because the helper
implementation was not yet committed there, the exact tested
`machinome_mechanics/belts.py` is identified by SHA-256
`28e693a5b2b213526c6f235615306fbad0a47f0ad0fca579d2aa1142f5db8cab`.

## Independent parity probe

`docs/probes/belt_tangent_points.py` retains an independent copy of the old
normal/contact/arc/station arithmetic and compares it with the migrated
implementation at absolute tolerance `1e-12`.  Run from the repository root:

`PATH=/home/asa/devel/machinome-studio/.venv/bin:$PATH PYTHONPATH="$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-belt-tangent-points" python docs/probes/belt_tangent_points.py`

It passed the actual X and Y routes, a nondefault route containing a back
idler, equal-radius collinear circles, a first-zero-radius route, and a
both-zero-radius route.  Contacts, directions, span lengths, wrap-derived loop
lengths, and every station agreed.  The X loop remained
`803.8854513557229` mm with stations
`[0.0, 374.9606340005496, 413.11480912405784, 788.0754431246074]`.
The Y loop remained `1036.4343190090678` mm with stations
`[0.0, 397.15991741362825, 430.7802454629051, 467.6272682196904,
481.4977010141353, 543.6081114622965, 578.1315400519219,
1002.1315400519219]`.  There was no fitted tooth-count or period change.

The probe also constructs contacts from Solid2's supported animation-time
expression and verifies every returned coordinate remains deferred in `$t`.
The mechanics helper's own cycle tests evaluate this expression family at five
time samples for every sense pair against an independent angular reference;
plain SymPy was not used as a substitute for that nonlinear expression face.

## Machine validation and image

With the workspace virtual environment, the same `PYTHONPATH`, and isolated
`SOLID_BUILD_DIR=_build/belt-tangent-points`,
`machinome test metamaquina2/metamaquina2.py --exact` ran 67 tests in
462.66 seconds: 67 passed, 0 failed.  Relevant passing contracts include both
closed flexible loops, X and Y belt redraw/travel, idler routing, pulley mesh,
and one groove per belt tooth.  The build repeated the existing `jhead.scad`
line-107 parser diagnostic while completing normally.

The representative image command was:

`machinome snapshot metamaquina2/metamaquina2.py -o _build/belt-tangent-points-driven-web.png --renderer web --autocenter --viewall --imgsize 1280x720 --drive x=90 --drive y=-80 --drive z=140`

Visual inspection is limited to the whole-machine exterior pose: carriage and
bed displacement, frame, raised beam, hot end, and filament run are coherent.
Tangency and pulley contact are too small for this image to certify; the
independent metrics and exact contracts above are that evidence.

Framework HEAD was
`0ce71cdea6cc4a2e7fd7e85dc68847daef3d34cc` and viewer HEAD was
`4355da1a7f64dacd7d86eb27dbdfdf7ced94598f` before validation.  Their final
heads were identical and the viewer checkout was clean after the capture.  A
web image establishes visible exterior pose only, not a contact certificate.
No shared installation was repointed.
