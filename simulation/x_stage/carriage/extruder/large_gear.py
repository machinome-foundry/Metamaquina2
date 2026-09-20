# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The big printed gear on the hobbed bolt."""

from machinome.parameters import Count

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import large_gear


class ExtruderGear(ScadPart):
    """37 teeth, driven by the 11-tooth motor gear: the reduction that
    turns motor speed into filament force."""

    color = materials.ABS
    teeth = Count(37, min=1)

    def render(self):
        return large_gear.extruder_gear(teeth=self.teeth)
