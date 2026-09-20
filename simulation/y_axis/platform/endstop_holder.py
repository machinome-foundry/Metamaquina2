# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The tab that trips a Y endstop."""

from simulation.part import SheetPart
from simulation.scad import machine


class YEndstopHolder(SheetPart):
    """A small plate standing off the platform's edge; one at each end
    of the travel, each hitting its microswitch on the bottom panel."""

    def profile(self):
        return machine.YEndstopHolder_face()
