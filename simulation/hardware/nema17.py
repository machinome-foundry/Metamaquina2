# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""NEMA 17 stepper motor."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import nema


class Nema17(ScadPart):
    """The motor itself, shaft pointing down -Z from the origin.

    Body, shaft and connector come from the design as one module, so
    the motor is one leaf: it is bought assembled and never taken
    apart.
    """

    color = materials.METAL

    def render(self):
        return nema.NEMA17()
