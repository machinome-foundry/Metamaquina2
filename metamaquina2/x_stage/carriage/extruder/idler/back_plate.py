# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The back plate of the extruder idler arm."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import extruder


class IdlerBackPlate(SheetPart):
    """The plate the handle bolts press against, joined to the two
    side plates by t-slots."""

    def profile(self):
        return extruder.idler_back_face()
