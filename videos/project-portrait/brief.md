# Metamaquina 2 / sample project portrait

AI-authored production record, 2026-10-04. Human editorial review pending.

Purpose: introduce the team's buildable open-source printer through its
distinctive parametric design. Identity → one design question → visible evidence
→ buildable source → scoped licences → creator-first invitation → rolling credits.

Opening: “This is Metamaquina Two, by the Metamaquina team.”
Question: why share a parametric design instead of only fixed parts?
Answer: editable dimensional relationships, assembly and fabrication sources.
This is the project's distinguishing editorial angle, not a claim that it is the
only parametric printer.

Evidence:

- https://github.com/Metamaquina/Metamaquina2 and the local README explicitly call
  the project fully parametric and explain assembly and laser-cutting sources.
- Metamaquina2.h declares thickness=6 and slot_extra_thickness=0.5. TSlot_joints
  uses thickness; TSlot_holes uses thickness+slot_extra_thickness. The 6.5 mm
  on-screen value is the resulting source argument, not a measured finished cut.
- The README warns some parts depend on 6 mm. Retain this qualification; do not
  morph geometry or pretend arbitrary new material dimensions are validated.
- simulation/metamaquina2.py reads the design parameters and exposes XYZ motion.
  Z's native unit is angle; the capture adapter honors its negative scale when
  applying design-unit millimetres. This must not be treated as an unscaled Z.
- Local CREDITS and NOTICE: preserve per-file upstream GPL grants, inherited gear
  credits, external MCAD LGPL 2.1, and simulation GPL/AGPL scope separation.

No printed material, force, thermal process, motor capability or manufacturing
validation is shown. Timing is edited. This is not a general Cartesian-printer
lesson, a historical reconstruction or a claim of ready-to-build certification.

The Videomaker skill supplies project-owned sources and encoded-film inspection.
The pilot's explicit request overrides the skill's older ban on on-film credits.
The current movie/stage docs supersede its older YAML-only source examples.
Jessica and the approved Machinome pronunciation dictionary/adapter are taken
from Leonardo: cgSgspJ2msm6clMCkdW9, Eleven v3, stability 0.5, similarity 0.75,
IPA məˈʃiːnoʊm. Actual requests, hashes and alignment are retained without keys.

Native clocked take experiments were rejected by existing model/tool constraints;
none is retained. playback.py adds only a film clock and hides UI instructions.
prepare.mjs proves the tree, parts and original drivers match the original
export and wraps the public viewer controls for deterministic, posed XYZ motion.
It adds no mechanical law, source modification or physical state. This production
adapter is not presented as released Videomaker functionality.

No simulation/CAD change, publication, push or author contact is authorized here.
Original and Foundry repositories were verified public on 2026-10-04. No live
interactive gallery URL is invented or promised.
