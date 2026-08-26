# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The right bearing sandwich plate of the Y platform."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class RightBearingSandwich(SheetPart):
    """The plate that traps the two right-hand Y bearings."""

    def profile(self):
        return machine.YPlatform_right_sandwich_face()
