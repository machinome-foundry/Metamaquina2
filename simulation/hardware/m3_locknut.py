# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M3 nylon-insert lock nut."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import nuts


class M3Locknut(ScadPart):
    """The nut used everywhere a joint must not shake loose."""

    color = materials.METAL

    def render(self):
        return nuts.M3_locknut()
