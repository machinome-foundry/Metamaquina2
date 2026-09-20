# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The power connector on the RAMBo board."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import rambo


class PsuConnector(ScadPart):
    """The screw terminal the power supply wires land on."""

    color = materials.NYLON

    def render(self):
        return rambo.PSU_connector()
