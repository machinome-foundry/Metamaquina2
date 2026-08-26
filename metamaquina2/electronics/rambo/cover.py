# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The acrylic cover over the RAMBo board."""

from metamaquina2 import materials
from metamaquina2.part import SheetPart
from metamaquina2.params import RAMBo_cover_thickness
from metamaquina2.scad import rambo


class RamboCover(SheetPart):
    """A lasercut acrylic plate standing off the board on hex spacers,
    so the electronics can be seen but not touched."""

    color = materials.ACRYLIC
    sheet_thickness = RAMBo_cover_thickness

    def profile(self):
        return rambo.RAMBo_cover_curves()
