# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The washer and bolt that pull a bearing sandwich together."""

from machinome.node import AssemblyNode
from machinome.parameters import Length

from simulation.hardware.bolt import Bolt
from simulation.hardware.m3_washer import M3Washer
from simulation.params import m3_washer_thickness


class SandwichBolt(AssemblyNode):
    """One M3x30 through the platform, its spacers and its sandwich
    plate, with a washer under the head.

    Drawn head-up from the origin; the platform turns it over to drive
    it downwards.
    """

    length = Length(30.0, min=0)

    washer = M3Washer()
    bolt = Bolt(diameter=3, length=length)

    def render(self):
        self.bolt.translate([0, 0, m3_washer_thickness])
