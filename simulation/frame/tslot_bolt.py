# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The bolt, washer and nut that close one t-slot joint."""

from machinome.node import AssemblyNode
from machinome.parameters import Flag, Length

from simulation.hardware.bolt import Bolt
from simulation.hardware.m3_nut import M3Nut
from simulation.hardware.m3_washer import M3Washer
from simulation.params import m3_washer_thickness, thickness


class TSlotBolt(AssemblyNode):
    """One t-slot fastener: an M3 bolt through the slot into a captive
    nut in the mating sheet's edge.

    The design draws these from a table of slot positions, in the plane
    of the sheet being bolted; this is one entry of that table.  Its
    origin is the middle of the slot, and the bolt runs down -Z into
    the sheet below.

    `flipped` bolts the joint from the other face.  The design does
    that with `mirror([0, 0, 1])` around the whole group; node
    operations have no mirror, but every part here is a solid of
    revolution about the bolt axis, so flipping each part end for end
    and negating its offset is the same geometry.  It selects nothing:
    the same three parts are there either way, turned over.
    """

    length = Length(16.0, min=0)
    flipped = Flag(False)

    washer = M3Washer()
    bolt = Bolt(diameter=3.0, length=length)
    nut = M3Nut()

    def render(self):
        def place(node, z):
            if self.flipped:
                node.rotate(180, [1, 0, 0])
                z = -z
            node.translate([0, 0, z])

        place(self.washer, thickness)
        place(self.bolt, thickness + m3_washer_thickness)
        place(self.nut, 8 - self.length)
