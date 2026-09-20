# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M8 flat washer."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import washers


class M8Washer(ScadPart):
    """A washer for an M8 bar or bolt, sitting on the XY plane."""

    color = materials.METAL

    def render(self):
        return washers.M8_washer()
