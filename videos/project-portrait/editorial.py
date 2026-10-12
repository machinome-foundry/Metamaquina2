"""Project-portrait visual vocabulary. Words and timing live in movie.py."""
# Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
from machinome.movie import Action, Element, Set, Slot


class PortraitStage(Set):
    module = "stage.jsx"
    machine = Slot()
    copy = Slot()
    note = Slot()


class CreditStage(Set):
    module = "stage.jsx"
    roll = Slot()


class Panel(Element):
    module = "stage.jsx"


class Footnote(Element):
    module = "stage.jsx"


class CreditRoll(Element):
    module = "stage.jsx"
    roll = Action()


def panel(eyebrow, title, body="", items=(), variant="normal"):
    return Panel(eyebrow=eyebrow, title=title, body=body,
                 items=list(items), variant=variant)


def group(role, names, *lines):
    return {"role": role, "names": names, "lines": list(lines)}
