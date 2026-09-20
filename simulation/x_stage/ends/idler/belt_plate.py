# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The side of the idler-side X end box that carries the idler."""

from simulation.part import SheetPart
from simulation.scad import machine


class XEndIdlerBeltPlate(SheetPart):
    """The plate the idler shaft passes through."""

    def profile(self):
        return machine.XEndIdler_belt_face()
