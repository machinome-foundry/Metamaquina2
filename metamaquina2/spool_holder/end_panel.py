# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A front or back panel of the spool holder."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import spool_holder


class SpoolHolderEndPanel(SheetPart):
    """One of two panels that hold the uprights apart and stop the
    stand rocking."""

    def profile(self):
        return spool_holder.FilamentSpoolHolder_front_and_back_panels_face()
