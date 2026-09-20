# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The left bearing sandwich plate of the Y platform."""

from simulation.part import SheetPart
from simulation.scad import machine


class LeftBearingSandwich(SheetPart):
    """The plate that traps the single left-hand Y bearing.

    Asymmetric on purpose: the design shapes and places it so the
    heated bed's wiring can move freely past it instead of catching in
    a corner.
    """

    def profile(self):
        return machine.YPlatform_left_sandwich_face()
