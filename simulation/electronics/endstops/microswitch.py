# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A mechanical endstop microswitch."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import endstop


class Microswitch(ScadPart):
    """A KW11-3Z lever microswitch.

    Bought as one part, so one leaf -- although the design draws the
    body and the lever as two separate shapes, which is what they are
    on the real switch.
    """

    color = materials.RUBBER

    def render(self):
        return endstop.mechanical_switch()
