"""Capture-only envelope around the original, unchanged printer.

The film host sets the printer's existing drivers through ViewerHandle.setDriver.
This envelope gives the host a 60-second editing clock and hides manual
instruction buttons for deterministic on-demand capture. It adds no geometry,
mechanical law, physical state or simulated capability.
"""
# Copyright (C) 2026 Luis Henrique Cassis Fagundes. GPL-3.0-only.
from machinome.motion.ports import Time
from simulation.metamaquina2 import Metamaquina2


class PortraitPrinter(Metamaquina2):
    time = Time(loop=60)
    instructions = {}
