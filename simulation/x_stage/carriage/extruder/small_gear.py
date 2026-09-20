# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The small printed gear on the extruder motor shaft."""

from machinome.parameters import Count

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import small_gear


class MotorGear(ScadPart):
    """11 teeth, pressed onto the stepper shaft."""

    color = materials.ABS
    teeth = Count(11, min=1)

    def render(self):
        return small_gear.motor_gear(teeth=self.teeth)
