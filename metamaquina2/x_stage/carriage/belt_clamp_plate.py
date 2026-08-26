# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A lasercut clamp that grips the X belt at the carriage."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import belt_clamp


class XBeltClampPlate(SheetPart):
    """One clamp plate.  The two ends of the belt are clamped by a
    left-hand and a right-hand one -- which is the same part, turned
    over."""

    width = 28
    radius = 5
    clamp_thickness = 6
    sheet_thickness = clamp_thickness

    def profile(self):
        return belt_clamp.beltclamp_curves(
            self.width, self.radius, for_x_carriage=True)
