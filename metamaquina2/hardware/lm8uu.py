# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""LM8UU linear ball bearing."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import lm8uu


class LM8UU(ScadPart):
    """The linear bearing every axis rides on.

    Drawn lying along +Y, centred on the origin, as the design draws
    it -- so a caller places it by pointing +Y down the rod.
    """

    color = materials.METAL

    def render(self):
        return lm8uu.LM8UU()
