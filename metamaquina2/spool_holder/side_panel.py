# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A side panel of the spool holder."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import spool_holder


class SpoolHolderSidePanel(SheetPart):
    """One of two uprights, slotted at the top so the bar drops in."""

    def profile(self):
        return spool_holder.FilamentSpoolHolder_sidepanel_face()
