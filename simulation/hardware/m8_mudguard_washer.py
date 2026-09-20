# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""M8 mudguard (penny) washer."""

from simulation import materials
from simulation.part import ScadPart
from simulation.scad import washers


class M8MudguardWasher(ScadPart):
    """The wide washer that spreads a bearing's load on the Y bars."""

    color = materials.METAL

    def render(self):
        return washers.M8_mudguard_washer()
