# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A Z endstop: two acrylic spacers and a switch."""

from machinome.node.assembly import AssemblyNode

from simulation.electronics.endstops.acrylic_spacer import ZEndstopSpacer
from simulation.electronics.endstops.microswitch import Microswitch
from simulation.params import acrylic_thickness


class ZEndstop(AssemblyNode):
    """One end of the Z travel.

    `limit` is `min` or `max`; the two use different spacer profiles.
    At the minimum end the design offsets the spacers along the panel
    from the switch, so the switch clears the Z rod and its spacers
    still land on solid material.  Drawn in the left panel's plane,
    switch facing out.
    """

    limits = ('min', 'max')
    minimum_spacer_offset = 20

    def __init__(self, limit, **kwargs):
        if limit not in self.limits:
            raise ValueError(
                f'a Z endstop is min or max, not {limit!r}')
        self.limit = limit

        offset = [self.minimum_spacer_offset if limit == 'min' else 0, 0, 0]
        self.lower_spacer = ZEndstopSpacer(f'z{limit}1').translate(offset)
        self.upper_spacer = (ZEndstopSpacer(f'z{limit}2')
                             .translate([0, 0, acrylic_thickness])
                             .translate(offset))
        self.switch = Microswitch().translate([0, 0, 2 * acrylic_thickness])

        super().__init__(limit, **kwargs)

    def render(self):
        return [self.lower_spacer, self.upper_spacer, self.switch]
