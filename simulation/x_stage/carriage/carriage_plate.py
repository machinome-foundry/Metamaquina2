# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The main plate of the X carriage."""

from simulation.part import SheetPart
from simulation.scad import machine


class XCarriagePlate(SheetPart):
    """The plate the extruder bolts onto and the bearings hang under."""

    def profile(self):
        return machine.XCarriage_bottom_face()
