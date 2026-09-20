# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The glass sheet the prints are made on."""

from solid2 import cube

from simulation import materials
from simulation.part import ScadPart
from simulation.params import glass_h, glass_w, heated_bed_glass_thickness


class HeatedBedGlass(ScadPart):
    """A plain rectangle of glass, clipped over the heated bed.

    The design draws it inline as a cube, so the cube is drawn here;
    unlike the design's version it stands on its own origin, and the
    heated bed assembly puts it on top of the board.
    """

    color = materials.GLASS

    def render(self):
        return cube([glass_w, glass_h, heated_bed_glass_thickness])
