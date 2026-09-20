# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M3 flat washer."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import washers


class M3Washer(ScadPart):
    """A washer for an M3 bolt, sitting on the XY plane."""

    color = materials.METAL

    def render(self):
        return washers.M3_washer()
