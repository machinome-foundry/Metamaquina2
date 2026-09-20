# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The blank side of the motor-side X end box."""

from simulation.part import SheetPart
from simulation.scad import machine


class XEndMotorPlainPlate(SheetPart):
    """The side of the box away from the belt."""

    def profile(self):
        return machine.XEndMotor_plain_face()
