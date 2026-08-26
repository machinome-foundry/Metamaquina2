# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M4 flat washer."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import washers


class M4Washer(ScadPart):
    """A washer for an M4 bolt, sitting on the XY plane."""

    color = materials.METAL

    def render(self):
        return washers.M4_washer()
