# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The inner face of an X end."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import machine


class XEndFrontPlate(SheetPart):
    """The plate facing into the machine.  Both X ends use it."""

    def profile(self):
        return machine.XEnd_front_face()
