# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The idler the X belt turns around."""

from solid_node.node import AssemblyNode

from metamaquina2.hardware.bearing_608zz import Bearing608zz
from metamaquina2.hardware.smooth_rod import SmoothRod


class XIdlerPulley(AssemblyNode):
    """A 608 bearing on a short shaft.

    A plain bearing rather than a toothed pulley: the belt runs on it
    back-side out, so it only needs to be round.
    """

    shaft_length = 80

    def __init__(self, *args, **kwargs):
        self.shaft = SmoothRod(self.shaft_length).translate(
            [0, 0, -self.shaft_length / 2])
        self.bearing = Bearing608zz()
        super().__init__(*args, **kwargs)

    def render(self):
        return [self.shaft, self.bearing]
