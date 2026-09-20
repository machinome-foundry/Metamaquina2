# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The arc panel that closes the back of the machine."""

from simulation.part import SheetPart
from simulation.scad import machine


class ArcPanel(SheetPart):
    """The curved rear panel, joined to the side panels by t-slots."""

    def profile(self):
        return machine.MachineArcPanel_face()
