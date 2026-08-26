# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The blank side of the idler-side X end box."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class XEndIdlerPlainPlate(SheetPart):
    """The side of the box away from the belt."""

    def profile(self):
        return machine.XEndIdler_plain_face()
