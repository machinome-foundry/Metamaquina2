# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The flexible coupling between a Z motor shaft and a Z bar."""

from metamaquina2 import materials
from metamaquina2.part import ScadPart
from metamaquina2.scad import coupling


class ShaftCoupling(ScadPart):
    """Bought as one piece, so one leaf."""

    color = materials.ABS

    def render(self):
        return coupling.coupling()
