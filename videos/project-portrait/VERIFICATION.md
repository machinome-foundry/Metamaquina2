# Metamaquina 2 sample / verification

AI-authored production record, 4 October 2026. Technical sample checks passed;
human editorial approval and listening review are still pending.

## Delivered file

- `_build/rehearsal.mp4`: 1920 × 1080, 24 fps, H.264 picture and AAC audio.
- Duration: 148.416667 seconds; 3,562 decoded frames.
- SHA-256: `5f6cf702fa1434f0b6b2b4780dd8cddef719190d0e153bc82d935204ac1e8102`.
- SRT and VTT captions, chapter-seeking review HTML, and `delivery.json` beside it.
- This render captured 2,631 frames and reused 931 verified cached frames.

## Evidence checked

- The original export and capture envelope have identical parts, machine tree
  and original XYZ controls. Only the filming clock/control surface differs.
- `inspect.mjs`: 36 compositions passed text bounds, no horizontal overflow,
  correct adopted XYZ units, and byte-identical pixels after a non-local seek.
  The Z driver's negative scale is respected. Screenshot checks allow extra
  time for software WebGL; earlier concurrent runs hit the default timeout.
- `verify-motion.mjs`: the head rises without reversal during the measured
  phrases “lift the crossbeam” and “carrying the head.” Separate carriage, bed
  and lift shots correct an earlier draft whose motion did not match the words.
- The four overview sheets decoded from the final MP4 were visually inspected
  across its full duration. Full-size decoded frames 76, 684, 1710, 2166 and
  3268 were also inspected for the opening, shared-dimension example, upward
  lift, licence card and rolling credits.
- The final file's dimensions, rate, duration, frame count and audio were
  checked with ffprobe. Captions retain the written spelling “Machinome.”
- The saved synthesis request records Jessica `cgSgspJ2msm6clMCkdW9`, Eleven v3,
  and Leonardo's approved pronunciation dictionary/version. The original WAV
  decodes cleanly; measured mean volume is −19.0 dB and sample peak is −0.3 dB.
  These checks are not a claim that the voice was listened to.

Build evidence is under `_build/inspection/`, `motion-language-check.json`,
`capture-adapter.json`, `rehearsal-manifest.json`, and `review-packs/`.

## Boundaries

No original CAD or simulation file was changed. The six-millimetre example is
source evidence, not a parameter morph or proof that another material works.
The authors' six-millimetre dependency warning is retained. The film shows
posed kinematics with editorial timing, not manufacturing validation.

The manifest honestly records the project's uncommitted video sources at
capture time, the capture export's dirty state, and unrelated pre-existing
Videomaker working-tree changes. It reports `releaseReady: false`; a later
source commit does not rewrite that historical provenance. Nothing was pushed,
uploaded or publicly published. The description and the film still need the
pilot's editorial and listening review.
