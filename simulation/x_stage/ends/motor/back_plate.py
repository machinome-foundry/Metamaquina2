# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The outer face of the motor-side X end."""

from simulation.part import SheetPart
from simulation.scad import machine


class XEndMotorBackPlate(SheetPart):
    """The plate facing out of the machine, cut with the slots the two
    Z bearings ride in."""

    def profile(self):
        return machine.XEndMotor_back_face()
