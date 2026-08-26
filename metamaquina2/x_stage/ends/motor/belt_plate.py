# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The side of the motor-side X end box that carries the X motor."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class XEndMotorBeltPlate(SheetPart):
    """The plate the X stepper bolts through."""

    def profile(self):
        return machine.XEndMotor_belt_face()
