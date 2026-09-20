# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The hot end, as the five parts a builder puts together."""

from machinome.node import AssemblyNode

from simulation import jhead
from simulation.x_stage.carriage.extruder.hotend.heater_resistor import (
    HeaterResistor)
from simulation.x_stage.carriage.extruder.hotend.liner import PTFELiner
from simulation.x_stage.carriage.extruder.hotend.nozzle import Nozzle
from simulation.x_stage.carriage.extruder.hotend.nozzle_holder import (
    NozzleHolder)
from simulation.x_stage.carriage.extruder.hotend.thermistor import Thermistor


class HotEnd(AssemblyNode):
    """The J-head: five bought parts, on the filament's own axis.

    An assembly rather than a part because that is how it arrives and
    how it is serviced.  A builder pushes the PTFE liner down the PEEK
    holder, runs the brass nozzle into the holder's foot until its
    block comes up against the shoulder, and pushes the heater resistor
    and the thermistor into the two holes the block is drilled with.
    The nozzle is the one of the five that ever comes out again, and it
    comes out on its own thread.

    Drawn on the mount plane -- z nought is the face the extruder's
    underside clamps the holder's shoulder against -- and about the
    filament axis, which is where the machine's X and Y put the print.
    `jhead` holds the arithmetic that says where each of the five
    stands; nothing here decides a dimension.

    Which way the block faces is not decided here either, and cannot
    be: the nozzle is held by a thread, so the block's angle about the
    axis is whatever the last quarter turn of tightening left, and the
    design's own call draws it square with the machine.  That is kept.
    """

    holder = NozzleHolder()
    liner = PTFELiner()
    nozzle = Nozzle()
    resistor = HeaterResistor()
    thermistor = Thermistor()

    def render(self):
        block = jhead.FOOT - jhead.BLOCK_HEIGHT

        self.liner.translate([0, 0, jhead.INSTALLATION])

        self.nozzle.translate(
            [-jhead.BLOCK_BORE_X, -jhead.BLOCK_BORE_Y, block])

        (self.resistor
         .rotate(90, [1, 0, 0])
         .translate([jhead.HEATER_X, 0, block + jhead.HEATER_HEIGHT]))

        (self.thermistor
         .rotate(90, [0, 1, 0])
         .translate([-jhead.THERMISTOR_FACE, jhead.THERMISTOR_Y,
                     block + jhead.THERMISTOR_HEIGHT]))
