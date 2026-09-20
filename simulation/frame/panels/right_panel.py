# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The right side panel."""

from simulation.part import SheetPart
from simulation.scad import machine


class RightPanel(SheetPart):
    """The panel the power supply mounts to."""

    def profile(self):
        return machine.MachineRightPanel_face()
