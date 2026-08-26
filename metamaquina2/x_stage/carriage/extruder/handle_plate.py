# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The lasercut lever that releases the extruder idler."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import extruder


class HandlePlate(SheetPart):
    """One plate, with the Metamaquina M cut into it."""

    def profile(self):
        return extruder.handle_face()
