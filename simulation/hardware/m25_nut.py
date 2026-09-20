# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M2.5 hex nut, the one the microswitches mount with."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import nuts


class M25Nut(ScadPart):
    """A plain M2.5 hex nut, sitting on the XY plane."""

    color = materials.METAL

    def render(self):
        return nuts.M25_nut()
