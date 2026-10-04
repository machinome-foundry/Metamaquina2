# Metamaquina 2 / project portrait sample

AI-authored production, 4 October 2026. Editorial and listening review pending.

[Film](_build/rehearsal.mp4) · [local review player](_build/review.html) ·
[subtitles](_build/rehearsal.srt) · [upload-description draft](description.md)

Built: 1920 × 1080, 24 fps, 2:28.42, including 36 seconds of rolling credits.
Voice: Jessica / Eleven v3, using the approved Leonardo pronunciation dictionary.
No music or third-party imagery.

[Verification record](VERIFICATION.md) · [machine-readable delivery](_build/delivery.json)

The film begins with the project and its creators. Its question is:
“Why publish a printer as a parametric design, instead of just a fixed set of
parts?” The shared editorial fingerprint is identity → one design question
→ demonstration → build sources → scoped licences → creator-first invitation
→ scrolling credits. The printer is the subject; Machinome appears in the
closing invitation and production credits.

## Editable sources

- [movie.py](movie.py): complete narration, visual copy, shots, cameras, motion
  schedule, scoped licences, credits and links.
- [brief.md](brief.md): evidence, limits and production decisions.
- [editorial.py](editorial.py), [stage.jsx](stage.jsx), [stage.css](stage.css):
  project-owned visual vocabulary shared by the two comparison samples.
- [playback.py](playback.py), [prepare.mjs](prepare.mjs): capture envelope and
  adapter; unchanged original mechanical model, driven via the public viewer
  controls. The adapter asserts identical parts, tree and original controls.
- [speech.mjs](speech.mjs), [pronunciation record](assets/pronunciation.json):
  Jessica generation with the approved IPA dictionary. Adapted from Leonardo;
  the speech script retains its original AGPL-3.0-only notice.
- [inspect.mjs](inspect.mjs), [verify-motion.mjs](verify-motion.mjs),
  [finish.mjs](finish.mjs): repeatable checks of text, adopted driver values,
  random-access pixel replay, motion direction during spoken phrases, encoded
  video and captions.

The original CAD and simulation files are unchanged. This is a posed kinematic
film with editorial timing, not a physical performance or manufacturing test.
See the brief for the documented capture-tool limitation and local adapter.

## Reproduce

Run from this project's root with the existing workspace environment:

```sh
portrait_workspace=/home/asa/devel/machinome
"$portrait_workspace/.venv/bin/machinome" export -o videos/project-portrait/_build/export --no-widget
PYTHONPATH=.:videos/project-portrait "$portrait_workspace/.venv/bin/machinome" export playback:PortraitPrinter -o videos/project-portrait/_build/take-export --no-widget
PYTHONPATH=. "$portrait_workspace/.venv/bin/python" videos/project-portrait/movie.py
node videos/project-portrait/prepare.mjs "$portrait_workspace/machinome-viewer/machinome_viewer/widget/dist/machinome-viewer.js"
```

Only if a new narration is authorized (existing matching takes are reused):

```sh
node videos/project-portrait/speech.mjs "$portrait_workspace/videomaker"
```

The following commands cannot purchase speech:

```sh
node "$portrait_workspace/videomaker/bin/videomaker.mjs" check videos/project-portrait/_build/movie.json --viewer videos/project-portrait/_build/portrait-viewer.js
node "$portrait_workspace/videomaker/bin/videomaker.mjs" preview videos/project-portrait/_build/movie.json --viewer videos/project-portrait/_build/portrait-viewer.js --width 1280
node videos/project-portrait/inspect.mjs "$portrait_workspace/videomaker"
node videos/project-portrait/verify-motion.mjs "$portrait_workspace/videomaker"
node "$portrait_workspace/videomaker/bin/videomaker.mjs" render videos/project-portrait/_build/movie.json --viewer videos/project-portrait/_build/portrait-viewer.js
node videos/project-portrait/finish.mjs
```

Use the project capture adapter, **not** the unwrapped viewer bundle: the latter
would show a static printer. prepare.mjs rebuilds the adapter from the current
movie's driver-motion.json and pins the original bundle by SHA-256.

All generated artifacts stay in ignored `_build/`: original and capture
exports, paid speech, alignment, adapter bundle, previews, frame caches,
MP4/SRT/VTT, decoded-film review pack and delivery.json. Do not commit screenshots
or render caches. Re-rendering reuses speech and any valid per-shot cache.

## Review and publication boundaries

Open the MP4 directly, or serve this project locally and open the review HTML
for chapter seeking and optional English subtitles. Full notices and clickable
source links accompany the film in description.md.

The Videomaker skill supplied the project-owned production and encoded-film
inspection discipline. The pilot explicitly requested the project/author opening,
on-film licence names and rolling credits; those override the older skill's
no-credits policy for these samples.

This task neither publishes nor pushes. Public upstream/Foundry repositories
exist, but no live interactive gallery URL or public video-source URL is
promised. Working-tree/export provenance and the tool's existing unrelated
dirty files are preserved honestly; a sample render is not publication approval.
