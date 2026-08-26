# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M8 nylon-insert lock nut."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import nuts


class M8Locknut(ScadPart):
    """The nut that holds the hobbed bolt in the extruder."""

    color = materials.METAL

    def render(self):
        return nuts.M8_locknut()
