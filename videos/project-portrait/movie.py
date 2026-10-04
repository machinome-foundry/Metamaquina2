"""Metamaquina 2: its editable design is the project's central promise."""
# Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
from pathlib import Path
import json
from machinome_movie import (
    Camera, Chapter, Credits, Cue, Dissolve, Evidence, FadeIn, FadeOut,
    Format, Layer, Mark, Move, Movie, Narration, Narrator, Release,
    Shot, Style, Loop, View, evaluate, write,
)
from playback import PortraitPrinter
from editorial import PortraitStage, CreditStage, CreditRoll, Footnote, panel, group


MOTION = [[0, {"x":0,"y":0,"z":150}], [4, {"x":-75}], [10, {"x":75}],
          [13, {"x":0}], [17, {"y":-100}], [21, {"y":0}],
          [41, {"z":30}], [56, {"z":115}]]


class PrinterTake(Loop):
    model = PortraitPrinter
    export = "_build/take-export"
    readiness = "Source-derived geometry and existing XYZ controls, set by a project capture adapter. Posed motion, edited timing; no parameter morph or manufacturing validation."
    marks = {"ready":0, "left":4, "right":10, "center":13,
             "present":17, "back":21, "low":41, "finish":56}
    hero = Camera(position=(850, -1130, 760), target=(140, 0, 255), fov=38)
    hero_end = Camera(position=(740, -1190, 690), target=(140, 0, 255), fov=38)
    frame = Camera(position=(-670, -920, 620), target=(0, 0, 250), fov=35)
    frame_end = Camera(position=(-850, -780, 610), target=(0, 0, 250), fov=35)
    detail = Camera(position=(-370, -540, 460), target=(-80, 0, 260), fov=35)
    detail_end = Camera(position=(-460, -560, 490), target=(-80, 0, 260), fov=35)
    motion = Camera(position=(520, -870, 570), target=(0, -15, 235), fov=38)
    bed = Camera(position=(430, -750, 390), target=(0, -55, 115), fov=36)
    build = Camera(position=(840, -980, 690), target=(130, 0, 230), fov=38)
    build_end = Camera(position=(670, -1120, 660), target=(130, 0, 230), fov=38)
    reel = Layer(PortraitPrinter.spool_holder, PortraitPrinter.filament)


class Portrait(Chapter):
    lines = Narration(
        "This is Metamaquina Two, by the Metamaquina team. "
        "Why publish a printer as a parametric design, instead of just a fixed set of parts? "
        "Because the relationships are part of the project. The frame is made from laser-cut panels, "
        "but its source describes how dimensions, slots and joints fit together. "
        "Take the material thickness. In this design, it is six millimeters. The joints use that dimension; "
        "the slots add a separate allowance. Those are linked choices in the source, not unrelated shapes to redraw. "
        "From that same project, builders can inspect the assembled printer and generate the cutting outlines. "
        "That is what makes this more than a download to reproduce: it is a design to work on. "
        "Changing material still means checking the result. The authors explicitly warn that some parts depend on six-millimeter stock. "
        "Once assembled, the carriage moves across the frame. The bed travels beneath it. "
        "Two threaded bars lift the crossbeam, carrying the head to the next height. "
        "These are the parts and relationships you can inspect before building your own machine. "
        "Metamaquina Two is open source. The original files retain their GNU GPL grants, including version three or later. "
        "The simulation combines GPL version three design adaptations with original helpers under the Affero GPL, version three or later. "
        "Visit the Metamaquina team's repository through the links below. Subscribe for more open machines, "
        "and star Machinome on GitHub to support this collection."
    )
    wide = View(PrinterTake, camera=PrinterTake.hero)
    structure = View(PrinterTake, camera=PrinterTake.frame, hide=[PrinterTake.reel])
    close = View(PrinterTake, camera=PrinterTake.detail, hide=[PrinterTake.reel])
    moving = View(PrinterTake, camera=PrinterTake.motion, hide=[PrinterTake.reel])
    bed_view = View(PrinterTake, camera=PrinterTake.bed, hide=[PrinterTake.reel])
    lift_view = View(PrinterTake, camera=PrinterTake.motion, hide=[PrinterTake.reel])
    assembly = View(PrinterTake, camera=PrinterTake.build)
    identity = panel("OPEN MACHINES / 02", "METAMAQUINA\n2", "A parametric 3D printer\nby the Metamáquina team.", ("Felipe Sanches, Rafael Moretti", "and the project contributors"))
    question = panel("THE DESIGN QUESTION", "Why share\nthe dimensions,\nnot just the parts?", "A printer you can build.\nA design you can work on.", variant="question")
    relationships = panel("THE CHOICE", "Share the\nrelationships.", "Laser-cut panels, slots and joints belong to one parametric design.", ("Editable OpenSCAD source", "Source-defined assembly and cut outlines"))
    dimensions = panel("ONE REAL EXAMPLE", "6 mm.\nOne shared input.", "Panel thickness feeds the joint dimensions and the slot calculation.", ("Material thickness: 6.0 mm", "Slot allowance: +0.5 mm", "Slot thickness argument: 6.5 mm"))
    making = panel("FROM DESIGN TO PARTS", "Inspect.\nGenerate.\nBuild.", "The repository includes the full assembly and laser-cutting sources.", ("6 mm MDF frame", "Separate acrylic cutting files"))
    caution = panel("A DESIGN YOU CAN EDIT", "Change it.\nCheck it.", "Some parts depend on 6 mm stock. A material change still needs a design review.", ("The authors' own manufacturing guidance",))
    motion = panel("WATCH THE MACHINE", "Carriage.\nBed.\nCrossbeam.", "Belts move X and Y.\nThreaded bars raise the head.", ("Original source-derived parts", "Existing simulation controls"))
    licenses = panel("OPEN SOURCE", "Yours to study.\nYours to build.", "Design: per-file GNU GPL grants\nSimulation: scoped GPL / AGPL grants", ("Upstream includes GPL-3.0-or-later", "Design adaptations: GPL-3.0-only", "Original helpers: AGPL-3.0-or-later"), variant="license")
    invitation = panel("CONTINUE WITH THE CREATORS", "Explore\nMetamaquina 2.", "github.com/Metamaquina/\nMetamaquina2", ("Subscribe for more open machines", "Star github.com/machinome/machinome", "All source links in the description"))
    note = Footnote(left="METAMAQUINA 2 / PROJECT PORTRAIT", right="KINEMATIC SIMULATION · NOT A MANUFACTURING VALIDATION")
    credits = CreditRoll(
        eyebrow="OPEN MACHINES / SOURCE CREDITS", title="Metamaquina 2",
        footer="Full notices and clickable links accompany this film.  /  machinome.org",
        groupHeight=18, startY=8, travelExtra=-44,
        groups=[
            group("Original project", "Metamáquina and contributors", "Felipe Corrêa da Silva Sanches · Rafael H. de L. Moretti", "https://github.com/Metamaquina/Metamaquina2"),
            group("Original design", "© 2013 Metamáquina · per-file GNU GPL grants", "Includes GPL-3.0-or-later; original notices remain authoritative", "https://github.com/Metamaquina/Metamaquina2/blob/main/README.md"),
            group("Inherited gear sources", "Guy 'DeuxVis' P. · Giles Bathgate · GregFrost", "External MCAD involute_gears.scad: GNU LGPL 2.1", "https://github.com/elmom/MCAD · exact pinned file linked in the description"),
            group("Simulation and modifications", "Luis Fagundes", "https://github.com/machinome-foundry/Metamaquina2", "© 2026 Luis Henrique Cassis Fagundes"),
            group("Simulation licences", "Original helpers: AGPL-3.0-or-later", "Source-integrating design adaptations: GPL-3.0-only", "https://github.com/machinome-foundry/Metamaquina2/blob/main/NOTICE"),
            group("Simulation tools", "Machinome · Machinome Viewer · molejo", "https://github.com/machinome/machinome", "https://github.com/machinome/machinome-viewer · https://github.com/LibreSolid/molejo"),
            group("Film production", "AI-written script and direction · Jessica narration", "ElevenLabs / Eleven v3 · approved Machinome pronunciation", "Videomaker · editable film sources in this project's videos/ directory"),
            group("Keep building", "Visit the creators. Subscribe for the next project.", "Metamaquina: https://github.com/Metamaquina/Metamaquina2", "Support the collection: https://github.com/machinome/machinome"),
        ],
    )
    opening = Shot(PortraitStage, {PortraitStage.machine:wide, PortraitStage.copy:identity, PortraitStage.note:note},
        until=lines.spoken("Why publish"), model=PrinterTake.run("ready","ready"), fade_in=FadeIn(.5),
        cues=[Cue(0, wide.move(PrinterTake.hero_end, until=lines.spoken("Why publish"), ease="smooth"))])
    hook = Shot(PortraitStage, {PortraitStage.machine:wide, PortraitStage.copy:question, PortraitStage.note:note},
        until=lines.spoken("Because the relationships"), model=PrinterTake.run("ready","ready"), transition=Dissolve(.4))
    design = Shot(PortraitStage, {PortraitStage.machine:structure, PortraitStage.copy:relationships, PortraitStage.note:note},
        until=lines.spoken("Take the material"), model=PrinterTake.run("ready","ready"), transition=Dissolve(.5),
        cues=[Cue(0, structure.highlight(PortraitPrinter.frame, others="dim"), until=lines.spoken("Take the material")),
              Cue(0, structure.move(PrinterTake.frame_end, until=lines.spoken("Take the material"), ease="smooth"))])
    shared_input = Shot(PortraitStage, {PortraitStage.machine:close, PortraitStage.copy:dimensions, PortraitStage.note:note},
        until=lines.spoken("From that same project"), model=PrinterTake.run("ready","ready"), transition=Dissolve(.5),
        cues=[Cue(0, close.highlight(PortraitPrinter.frame.panels, others="dim"), until=lines.spoken("From that same project")),
              Cue(0, close.move(PrinterTake.detail_end, until=lines.spoken("From that same project"), ease="smooth"))])
    manufacturing = Shot(PortraitStage, {PortraitStage.machine:assembly, PortraitStage.copy:making, PortraitStage.note:note},
        until=lines.spoken("Changing material"), model=PrinterTake.run("ready","ready"), transition=Dissolve(.5),
        cues=[Cue(0, assembly.move(PrinterTake.build_end, until=lines.spoken("Changing material"), ease="smooth"))])
    review = Shot(PortraitStage, {PortraitStage.machine:structure, PortraitStage.copy:caution, PortraitStage.note:note},
        until=lines.spoken("Once assembled"), model=PrinterTake.run("ready","ready"), transition=Dissolve(.5))
    carriage_travel = Shot(PortraitStage, {PortraitStage.machine:moving, PortraitStage.copy:motion, PortraitStage.note:note},
        until=lines.spoken("The bed travels"),
        model=PrinterTake.keys({0:"ready", lines.spoken("The bed travels"):("center","out")}), transition=Dissolve(.5))
    bed_travel = Shot(PortraitStage, {PortraitStage.machine:bed_view, PortraitStage.copy:motion, PortraitStage.note:note},
        until=lines.spoken("Two threaded bars"),
        model=PrinterTake.keys({0:"center", lines.spoken("Two threaded bars"):("back","out")}), transition=Dissolve(.4))
    # A separate shot starts at the lower pose and shows an actual upward move
    # on the words "lift the crossbeam". This is an editorial cut between
    # demonstrations, not a claim that the three shots are one continuous run.
    screw_lift = Shot(PortraitStage, {PortraitStage.machine:lift_view, PortraitStage.copy:motion, PortraitStage.note:note},
        until=lines.spoken("Metamaquina Two is open source"),
        model=PrinterTake.keys({0:"low", lines.spoken("These are the parts"):("finish","out"), lines.spoken("Metamaquina Two is open source"):"finish"}), transition=Dissolve(.4))
    open_source = Shot(PortraitStage, {PortraitStage.machine:wide, PortraitStage.copy:licenses, PortraitStage.note:note},
        until=lines.spoken("Visit the Metamaquina"), model=PrinterTake.run("finish","finish"), transition=Dissolve(.5))
    invitation_shot = Shot(PortraitStage, {PortraitStage.machine:wide, PortraitStage.copy:invitation, PortraitStage.note:note},
        until=lines.end(plus=1), model=PrinterTake.run("finish","finish"), transition=Dissolve(.5))
    closing_credits = Shot(CreditStage, {CreditStage.roll:credits}, until=36,
        model=PrinterTake.run("finish","finish"), transition=Dissolve(.8), fade_out=FadeOut(.8),
        cues=[Cue(0, credits.roll(), until=36)])


class MetamaquinaPortrait(Movie):
    title = "Metamaquina 2 — a printer you can change"
    series = "OPEN MACHINES / PROJECT PORTRAITS"
    status = "sample / editorial review pending"
    learning_goal = "Meet Metamaquina 2 through its parametric construction, existing movement, build sources and authors."
    format = Format(1920, 1080, fps=24)
    narrator = Narrator(provider="elevenlabs", model="eleven_v3", voice="cgSgspJ2msm6clMCkdW9", label="Jessica", output="pcm_24000", settings={"stability":.5,"similarity_boost":.75})
    style = Style(background="#f5f2e9", foreground="#202623", accent="#c65d2f", font="DejaVu Sans, sans-serif", safe_inset=.05)
    evidence = Evidence(model="../../simulation/metamaquina2.py", research="brief.md")
    credits = Credits(project="Metamaquina 2", creator="Metamáquina and contributors", license="Per-file GNU GPL grants; simulation scopes in NOTICE", license_file="../../NOTICE")
    release = Release(source_url="https://github.com/Metamaquina/Metamaquina2", simulation_url="https://github.com/machinome-foundry/Metamaquina2", description="description.md")
    portrait = Portrait()


if __name__ == "__main__":
    output = Path(__file__).resolve().parent / "_build/movie.json"
    write(evaluate(MetamaquinaPortrait, name="project-portrait", out=output), output)
    (output.parent / "driver-motion.json").write_text(json.dumps({"duration":60,"keys":MOTION}, indent=2) + "\n")
