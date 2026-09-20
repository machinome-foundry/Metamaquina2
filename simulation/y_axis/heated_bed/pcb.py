# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""The heated bed PCB."""

from simulation import materials
from simulation.part import SheetPart
from simulation.params import heated_bed_pcb_thickness
from simulation.scad import heated_bed


class HeatedBedPcb(SheetPart):
    """The heater itself: a PCB whose copper is the heating element.

    A board is a part cut from flat stock like any other, so it is
    authored the same way -- its outline, and the thickness it is made
    in.
    """

    color = materials.PCB
    sheet_thickness = heated_bed_pcb_thickness

    def profile(self):
        return heated_bed.heated_bed_pcb_curves()
