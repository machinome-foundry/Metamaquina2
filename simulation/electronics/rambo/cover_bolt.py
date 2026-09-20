# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The bolt that holds the RAMBo cover down."""

from machinome.parameters import Length

from simulation import materials
from simulation.part import ScadPart, curve
from simulation.params import M3_bolt_head


class CoverBolt(ScadPart):
    """One M3x10 into a hex spacer.

    The design draws only the head, as a plain cylinder, so that is
    what this renders -- the part is real, its shank is simply not
    modelled.
    """

    color = materials.METAL
    head_radius = Length(3.0, min=0)

    def render(self):
        return curve('cylinder', r=self.head_radius, h=M3_bolt_head)
