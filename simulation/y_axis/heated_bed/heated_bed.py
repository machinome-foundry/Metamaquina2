# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The heated build platform: board plus glass."""

from machinome.node.assembly import AssemblyNode

from simulation.params import (
    glass_h,
    glass_w,
    heated_bed_pcb_thickness,
)
from simulation.y_axis.heated_bed.glass import HeatedBedGlass
from simulation.y_axis.heated_bed.pcb import HeatedBedPcb


class HeatedBed(AssemblyNode):
    """The board and the glass on top of it.

    Two separate parts, clipped together rather than bonded -- the
    glass comes off to release a print -- so they are an assembly.
    The design's silkscreen outline is not modelled here: it is ink on
    the board, not a part.
    """

    pcb = HeatedBedPcb()
    glass = HeatedBedGlass()

    def render(self):
        self.glass.translate(
            [-glass_w / 2, -glass_h / 2, heated_bed_pcb_thickness])
