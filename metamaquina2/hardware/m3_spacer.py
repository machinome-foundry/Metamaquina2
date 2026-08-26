# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A lasercut M3 spacer washer."""

from metamaquina2.part import SheetPart
from metamaquina2.scad import spacers


class M3Spacer(SheetPart):
    """A ring of sheet stock used to space a sandwich by one thickness."""

    def profile(self):
        return spacers.M3_spacer_face()
