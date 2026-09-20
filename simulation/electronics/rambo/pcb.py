# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The RAMBo board."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import rambo


class RamboPcb(ScadPart):
    """The controller board itself.

    The design draws the bare board -- its outline and its mounting
    holes -- and not the components on it, so that is what this is.
    Not a `SheetPart`: the design never named the board's outline as a
    2D module, so there is no profile to author separately from the
    extrusion.
    """

    color = materials.PCB

    def render(self):
        return rambo.RAMBo_pcb()
