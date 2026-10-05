# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""An X belt clamp and the bolts that tighten it."""

from machinome.node.assembly import AssemblyNode
from machinome.parameters import Flag, Length

from simulation.hardware.bolt import Bolt
from simulation.hardware.m3_washer import M3Washer
from simulation.params import m3_washer_thickness
from simulation.x_stage.carriage.belt_clamp_plate import XBeltClampPlate


class XBeltClamp(AssemblyNode):
    """One clamp: a plate and two M3x20 through it into the carriage.

    `flipped` is the other end of the belt.  The design mirrors the
    clamp there, and a flat plate mirrored in its own plane is the same
    piece turned over -- so it is turned over, and lifted back by its
    own thickness so it still lies where it was.  The bolts are on the
    mirror line, so they are the same either way.
    """

    # where the two bolts stand either side of the clamp's centre
    bolt_offset = 9

    bolt_length = Length(20.0, min=0)

    flipped = Flag(False)

    plate = XBeltClampPlate()
    washers = M3Washer().repeat(2)
    bolts = Bolt(diameter=3, length=bolt_length).repeat(2)

    def render(self):
        if self.flipped:
            (self.plate
             .rotate(180, [1, 0, 0])
             .translate([0, 0, XBeltClampPlate.clamp_thickness]))

        for index, side in enumerate((-1, 1)):
            (self.washers[index]
             .translate([side * self.bolt_offset, 0, 0])
             .rotate(180, [1, 0, 0]))
            (self.bolts[index]
             .translate([0, 0, m3_washer_thickness])
             .translate([side * self.bolt_offset, 0, 0])
             .rotate(180, [1, 0, 0]))
