# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M4 hex nut."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import nuts


class M4Nut(ScadPart):
    """A plain M4 hex nut, sitting on the XY plane."""

    color = materials.METAL

    def render(self):
        return nuts.M4_nut()
