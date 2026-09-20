# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""A stick-on cable clip."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import cable_clips


class CableClip(ScadPart):
    """One Hellermann right-angle clip, in whichever size is called for.

    The machine uses three sizes -- RA6, RA9 and RA13 -- and the design
    picks them from tables of positions per panel.  The size is a
    constructor argument, so each size is its own part with its own
    artifacts.
    """

    color = materials.NYLON

    def __init__(self, kind, **kwargs):
        self.kind = kind
        super().__init__(kind, **kwargs)

    def render(self):
        return cable_clips.cable_clip(self.kind)
