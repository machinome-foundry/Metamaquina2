# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The lasercut plate that hangs the Y motor off the rear bars."""

from simulation.part import SheetPart
from simulation.scad import machine


class YMotorHolder(SheetPart):
    """One plate, slotted so the motor can be moved to tension the belt."""

    def profile(self):
        return machine.YMotorHolder_face()
