# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The bottom panel."""

from simulation.part import SheetPart
from simulation.scad import machine


class BottomPanel(SheetPart):
    """The panel spanning the base of the machine, under the Y axis,
    carrying the two Y endstops."""

    def profile(self):
        return machine.MachineBottomPanel_face()
