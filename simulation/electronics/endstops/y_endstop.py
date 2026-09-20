# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A Y endstop: two lasercut spacers and a switch."""

from machinome.node import AssemblyNode

from simulation.electronics.endstops.microswitch import Microswitch
from simulation.electronics.endstops.wood_spacer import YEndstopSpacer
from simulation.params import thickness


class YEndstop(AssemblyNode):
    """One end of the Y travel, standing on the bottom panel.

    Two identical spacers stack to bring the switch up to where the
    platform's endstop tab passes.  Drawn in the bottom panel's plane.
    """

    limits = ('min', 'max')

    def __init__(self, limit, **kwargs):
        if limit not in self.limits:
            raise ValueError(
                f'a Y endstop is min or max, not {limit!r}')
        self.limit = limit

        self.lower_spacer = YEndstopSpacer(f'y{limit}')
        self.upper_spacer = YEndstopSpacer(f'y{limit}').translate(
            [0, 0, thickness])
        self.switch = Microswitch().translate([0, 0, 2 * thickness])

        super().__init__(limit, **kwargs)

    def render(self):
        return [self.lower_spacer, self.upper_spacer, self.switch]
