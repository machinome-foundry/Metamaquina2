# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The top panel."""

from simulation.part import SheetPart
from simulation.scad import machine


class TopPanel(SheetPart):
    """The panel that ties the two side panels together at the top and
    carries the wiring pass-through for the extruder."""

    def profile(self):
        return machine.MachineTopPanel_face()
