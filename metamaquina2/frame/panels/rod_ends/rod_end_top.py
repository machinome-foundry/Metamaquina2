# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The plate that caps a Z rod and Z bar at the top of the machine."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class RodEndTop(SheetPart):
    """One of the two upper rod-end plates, above the top panel."""

    def profile(self):
        return machine.RodEndTop_face()
