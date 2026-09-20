# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""32 mm threaded hex spacer."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import spacers


class HexSpacer32mm(ScadPart):
    """The standoff that holds the RAMBo cover off the board."""

    color = materials.METAL

    def render(self):
        return spacers.hexspacer_32mm()
