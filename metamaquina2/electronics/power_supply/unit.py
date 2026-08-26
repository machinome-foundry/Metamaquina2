# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The switching power supply itself."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import power_supply


class PowerSupplyUnit(ScadPart):
    """A Hiqua T-200-12 brick.

    Bought assembled, so one leaf, even though the design draws its
    steel case and the board inside it as separate shapes -- which is
    what they are inside the real unit.
    """

    color = materials.METAL

    def render(self):
        return power_supply.HiquaPowerSupply()
