# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (C) 2026 Luis Henrique Cassis Fagundes
# Upstream Metamaquina design retains its own notices and grants; see NOTICE.
# End Foundry notice
"""Sourced parts: the fasteners, bearings, motors and stock the machine
is bolted together from.

Nothing in here is specific to the Metamaquina 2 -- these are catalogue
parts, and they are leaves wherever they appear in the tree.  A part
that exists in several sizes is one node class taking the size as a
constructor argument, so each size keeps its own artifacts.
"""
