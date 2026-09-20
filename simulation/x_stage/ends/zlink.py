# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The printed link between an X end and its Z threaded bar."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import zlink


class ZLink(ScadPart):
    """One Z link.

    It captures a nut on the threaded bar and pushes it against a
    spring, so backlash in the Z axis is taken up rather than left to
    show up in the print.
    """

    color = materials.ABS

    def render(self):
        return zlink.ZLink()
