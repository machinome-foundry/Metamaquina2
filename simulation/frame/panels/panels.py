# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""Every lasercut panel of the frame, standing where it belongs."""

from machinome.node import AssemblyNode

from simulation import frames
from simulation.frame.panels.arc_panel import ArcPanel
from simulation.frame.panels.bottom_panel import BottomPanel
from simulation.frame.panels.left_panel import LeftPanel
from simulation.frame.panels.right_panel import RightPanel
from simulation.frame.panels.rod_ends.rod_ends import RodEnds
from simulation.frame.panels.top_panel import TopPanel
from simulation.frame.panels.wiring_hole_ring import WiringHoleRing
from simulation.params import thickness


class Panels(AssemblyNode):
    """The five big panels, the two wiring rings and the rod ends.

    The panels are separate parts that a builder bolts together, not
    one welded shell, so this is an assembly and each panel is its own
    leaf.  What holds them together is in `PanelJoints`.
    """

    # where the wiring rings sit in the top panel's plane
    wiring_hole_offset = 120

    left = LeftPanel()
    right = RightPanel()
    top = TopPanel()
    bottom = BottomPanel()
    arc = ArcPanel()
    wiring_ring_above = WiringHoleRing()
    wiring_ring_below = WiringHoleRing()
    rod_ends = RodEnds()

    def render(self):
        frames.left_panel(self.left)
        frames.right_panel(self.right)
        frames.top_panel(self.top)
        frames.bottom_panel(self.bottom)
        frames.arc_panel(self.arc)

        frames.top_panel(self.wiring_ring_above.translate(
            [0, self.wiring_hole_offset, thickness]))
        frames.top_panel(self.wiring_ring_below.translate(
            [0, self.wiring_hole_offset, -thickness]))
