# Belt pulley angle migration verification

This narrow migration replaces the local X- and Y-axis pulley rotation laws
with `machinome_mechanics.belt_pulley_angle`. It retains each fitted pitch
radius, tangent phase, clamp-to-belt projection, Y global station offset, and
rotation sense.

## Source identity

- Project base: `bd56d5211311ef4449f94c975a45190688ee430b` (`main`, clean)
- Project branch: `mechanics-belt-pulley-angle`
- Mechanics worktree: `WTs/mechanics-belt-pulley-angle`
- Mechanics planning HEAD: `2e73354b5adb62bde3462302537edd0fca2e22ab`
- Tested `machinome_mechanics/belts.py` SHA-256:
  `c5f170dee942172dba37eb5b3d8d43f182f263e52c5c2c43331f8bb3427664ed`
- Framework before and after: clean
  `8d2bd71171be81f13ba5dd492851ed8b3a9ababb`
- Viewer before and after: clean
  `4355da1a7f64dacd7d86eb27dbdfdf7ced94598f`

The mechanics implementation was uncommitted cycle content at the stated
planning HEAD, so its file digest identifies the code actually exercised.
Every command below used the project checkout and workspace virtual
environment without changing an installed package:

```sh
PATH=/home/asa/devel/machinome-studio/.venv/bin:$PATH \
PYTHONPATH=$PWD:/home/asa/devel/machinome-studio/WTs/mechanics-belt-pulley-angle \
...
```

## Independent law comparison

```sh
python docs/probes/belt_pulley_angle.py
```

Passed. The probe embeds the pre-migration arithmetic rather than importing a
second implementation. At positions `-400, -100, 0, 100, 400` mm it compared
both axes to `1e-12` absolute tolerance:

- X: `2481.1182839582143, -894.3693976321686, -2019.5319581622964,
  -3144.6945186924245, -6520.1822002828085` degrees
- Y: `-583.5596470520231, 2790.026055265325, 3914.554622704441,
  5039.083190143557, 8412.668892460906` degrees

Both ranges exceed two complete turns, proving that rotation remains signed
and unwrapped. The same probe passes actual Solid2 `$t` expressions through
each project function, parses the exported expressions with machinome, and
evaluates them at all five positions against the independent laws to `1e-10`.
This covers the X clockwise default and the Y reverse-bend `sense=-1`, including
the Y contact-station subtraction.

## Machine contracts and build

```sh
SOLID_BUILD_DIR=_build/belt-pulley-angle \
machinome test metamaquina2/metamaquina2.py --exact
```

Passed **67/67** in **358.46 seconds**. This includes the X/Y driven-belt
redraw, tooth travel, pulley mesh, and one-groove-per-tooth rotation contracts.
The established imported `jhead.scad` line 107 parser diagnostics and one
`FilamentSpoolHolder.scad` parameter warning remained in the log; they did not
fail any contract and are unrelated to these Python laws.

```sh
SOLID_BUILD_DIR=_build/belt-pulley-angle \
machinome build metamaquina2/metamaquina2.py
```

Passed in 17.65 seconds with the exact-suite cache warm.

## Driven visual check

```sh
SOLID_BUILD_DIR=_build/belt-pulley-angle \
machinome snapshot metamaquina2/metamaquina2.py \
  -o _build/belt-pulley-angle-driven-web.png --renderer web \
  --autocenter --viewall --imgsize 1280x720 \
  --drive x=90 --drive y=-80 --drive z=140
```

The fresh capture completed successfully and was inspected at
`_build/belt-pulley-angle-driven-web.png`. The driven printer remains assembled:
the translated carriage and bed are carried by their axes, the frame and Z
system are coherent, and no detached or exploded exterior component is
visible. At this whole-machine scale the small motor-pulley tooth contacts and
pulley rotation cannot be certified visually; the exact mesh/rotation
contracts and direct law probe provide that evidence. This image also depends
on the clean viewer HEAD stated above rather than constituting a renderer
release or contact certificate.
