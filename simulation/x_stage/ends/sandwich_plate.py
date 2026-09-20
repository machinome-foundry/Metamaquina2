# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The plate that traps an X end's Z bearings."""

from simulation.part import SheetPart
from simulation.scad import machine


class XEndSandwichPlate(SheetPart):
    """One plate, cut with the bearings' own outline so they seat in
    it.  Both X ends use it."""

    def profile(self):
        return machine.xend_bearing_sandwich_face()
