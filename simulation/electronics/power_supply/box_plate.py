# SPDX-License-Identifier: GPL-3.0-only
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""One of the four lasercut plates of the power supply box."""

from simulation.part import SheetPart
from simulation import scad


class PowerSupplyBoxPlate(SheetPart):
    """A side, bottom, front or back plate.

    All four are cut from the same stock and joined by t-slots; only
    the profile differs, and `face` names which one.
    """

    faces = ('side', 'bottom', 'front', 'back')

    def __init__(self, face, **kwargs):
        if face not in self.faces:
            raise ValueError(
                f'no such power supply box plate {face!r}; '
                f'expected one of {", ".join(self.faces)}')
        self.face = face
        super().__init__(face, **kwargs)

    def profile(self):
        return getattr(
            scad.power_supply, f'PowerSupplyBox_{self.face}_face')()
