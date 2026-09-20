# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The plate that locates a Z rod at the bottom of the machine."""

from simulation.part import SheetPart
from simulation.scad import machine


class RodEndBottom(SheetPart):
    """One of the two lower rod-end plates, under the bottom panel."""

    def profile(self):
        return machine.RodEndBottom_face()
