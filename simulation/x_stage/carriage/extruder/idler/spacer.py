# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""An acrylic spacer beside the extruder idler bearing."""

from simulation import materials
from simulation.part import SheetPart
from simulation.scad import extruder


class IdlerSpacer(SheetPart):
    """A 5 mm acrylic ring that keeps the idler bearing centred
    between the side plates."""

    color = materials.ACRYLIC
    sheet_thickness = 5

    def profile(self):
        return extruder.idler_spacer_face()
