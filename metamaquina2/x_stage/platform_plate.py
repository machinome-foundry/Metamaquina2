# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The floor of the X beam."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class XPlatformPlate(SheetPart):
    """The long sheet that spans between the two X ends, under the rods."""

    def profile(self):
        return machine.XPlatform_bottom_face()
