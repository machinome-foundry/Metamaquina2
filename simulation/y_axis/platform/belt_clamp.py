# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A lasercut clamp that grips the Y belt under the platform."""

from machinome.parameters import Length

from simulation.part import SheetPart
from simulation.scad import belt_clamp


class YBeltClamp(SheetPart):
    """One of four plates; two stacked at each end of the belt run,
    pinching the belt between them."""

    width = Length(28.0, min=0)
    radius = Length(5.0, min=0)

    def profile(self):
        return belt_clamp.beltclamp_curves(
            self.width, self.radius, for_y_platform=True)
