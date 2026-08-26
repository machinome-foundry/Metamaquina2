# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A side plate of the extruder idler arm."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import extruder


class IdlerSidePlate(SheetPart):
    """One of two plates, one each side of the idler bearing."""

    def profile(self):
        return extruder.idler_side_face()
