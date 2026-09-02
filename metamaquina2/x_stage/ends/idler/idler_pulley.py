# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The idler the X belt turns around."""

from solid_node.node import AssemblyNode

from metamaquina2.hardware.bearing_608zz import Bearing608zz
from metamaquina2.hardware.smooth_rod import SmoothRod


#: How long the shaft the bearing runs on is.
SHAFT_LENGTH = 80


class XIdlerPulley(AssemblyNode):
    """A 608 bearing on a short shaft.

    A plain bearing rather than a toothed pulley: the belt runs on it
    back-side out, so it only needs to be round.
    """

    shaft_length = SHAFT_LENGTH

    shaft = SmoothRod(length=SHAFT_LENGTH)
    bearing = Bearing608zz()

    def render(self):
        self.shaft.translate([0, 0, -self.shaft_length / 2])
