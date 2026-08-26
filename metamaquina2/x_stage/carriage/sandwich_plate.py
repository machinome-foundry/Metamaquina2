# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The plate that traps the X carriage's bearings."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class XCarriageSandwichPlate(SheetPart):
    """One plate under the carriage, cut with the outline of all four
    linear bearings so they seat in it."""

    def profile(self):
        return machine.XCarriage_sandwich_face()
