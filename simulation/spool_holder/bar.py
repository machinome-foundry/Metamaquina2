# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The bar the spool turns on."""

from simulation import materials
from simulation.part import SheetPart
from simulation.params import SpoolHolder_bar_length
from simulation.scad import spool_holder


class SpoolHolderBar(SheetPart):
    """A length of M8 threaded bar, drawn the way the design draws it:
    its circular section extruded along its length."""

    color = materials.THREADED_METAL
    sheet_thickness = SpoolHolder_bar_length

    def profile(self):
        return spool_holder.FilamentSpoolHolder_bar_face()
