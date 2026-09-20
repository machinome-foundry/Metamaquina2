# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The outer face of the idler-side X end."""

from simulation.part import SheetPart
from simulation.scad import machine


class XEndIdlerBackPlate(SheetPart):
    """The plate facing out of the machine on the right-hand end."""

    def profile(self):
        return machine.XEndIdler_back_face()
