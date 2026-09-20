# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The flexible coupling between a Z motor shaft and a Z bar."""

from machinome.motion.joints import Revolute

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import coupling


class ShaftCoupling(ScadPart):
    """Bought as one piece, so one leaf.

    `spin` needs no anchor: `coupling.scad`'s own `coupling()` module
    is a cylinder at the origin, so turning it about its own placed
    origin is turning it about the shaft it clamps, wherever it stands.
    """

    color = materials.ABS

    spin = Revolute(axis=(0, 0, 1), unit='deg')

    def render(self):
        return coupling.coupling()
