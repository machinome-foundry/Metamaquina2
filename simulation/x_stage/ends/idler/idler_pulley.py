# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The idler the X belt turns around."""

from machinome.node import AssemblyNode
from machinome.parameters import Length

from simulation.hardware.bearing_608zz import Bearing608zz
from simulation.hardware.smooth_rod import SmoothRod


class XIdlerPulley(AssemblyNode):
    """A 608 bearing on a short shaft.

    A plain bearing rather than a toothed pulley: the belt runs on it
    back-side out, so it only needs to be round.
    """

    shaft_length = Length(80.0, min=0)

    shaft = SmoothRod(length=shaft_length)
    bearing = Bearing608zz()

    def render(self):
        self.shaft.translate([0, 0, -self.shaft_length / 2])
