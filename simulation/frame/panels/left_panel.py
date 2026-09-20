# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The left side panel."""

from simulation.part import SheetPart
from simulation.scad import machine


class LeftPanel(SheetPart):
    """The panel the electronics and the Z endstops mount to.

    Cut from the same stock as the right panel but a different part:
    it carries the RAMBo, the cable clips and both Z endstops, and its
    profile has the holes for all of them.
    """

    def profile(self):
        return machine.MachineLeftPanel_face()
