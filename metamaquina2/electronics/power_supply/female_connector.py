# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The mains inlet on the back of the power supply box."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import power_supply


class FemaleConnector(ScadPart):
    """An IEC-style panel inlet, snapped into the back plate."""

    color = materials.ABS

    def render(self):
        return power_supply.PowerSupply_FemaleConnector()
