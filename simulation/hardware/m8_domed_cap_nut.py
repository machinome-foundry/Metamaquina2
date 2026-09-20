# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M8 domed cap nut."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import domed_cap_nuts


class M8DomedCapNut(ScadPart):
    """The finished end of a threaded bar where it leaves a side panel."""

    color = materials.METAL

    def render(self):
        return domed_cap_nuts.M8_domed_cap_nut()
