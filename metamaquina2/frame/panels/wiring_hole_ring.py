# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A ring that lines the extruder wiring hole in the top panel."""

from metamaquina2.part import SheetPart
from metamaquina2.params import extruder_wiring_radius
from metamaquina2.scad import machine


class WiringHoleRing(SheetPart):
    """One of the two rings, above and below the top panel, that keep
    the extruder loom from chafing on the cut edge."""

    def profile(self):
        return machine.top_wiring_hole_aux(r=extruder_wiring_radius)
