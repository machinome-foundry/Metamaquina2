// Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
// Production adapter only: operate the viewer's PUBLIC posed-driver controls.
// No change to the distributed viewer, CAD, kinematic laws or Videomaker.
import assert from 'node:assert/strict';
import {readFile, writeFile} from 'node:fs/promises';
import {resolve, dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const base=dirname(fileURLToPath(import.meta.url));
assert.ok(process.argv[2], 'Pass the original viewer bundle.');
const source=resolve(process.argv[2]);
const original=JSON.parse(await readFile(resolve(base,'_build/export/manifest.json'),'utf8'));
const film=JSON.parse(await readFile(resolve(base,'_build/take-export/manifest.json'),'utf8'));
assert.deepEqual(film.root.children, original.root.children, 'Capture envelope changed the machine tree.');
assert.deepEqual(film.drivers, original.drivers, 'Capture envelope changed the machine controls.');
assert.deepEqual(film.pieces, original.pieces, 'Capture envelope changed the parts.');
const motion=JSON.parse(await readFile(resolve(base,'_build/driver-motion.json'),'utf8'));
assert.equal(motion.keys[0][0],0);
let previous=-1, state={};
for(const [t,values] of motion.keys) {
  assert.ok(t>previous && t<=motion.duration);
  previous=t;
  state={...state,...values};
  assert.deepEqual(Object.keys(state).sort(), ['x','y','z']);
  for(const [id,value] of Object.entries(state)) {
    assert.ok(Number.isFinite(value));
    const range=film.drivers[id].range;
    assert.ok(value>=range[0] && value<=range[1], id+' leaves declared design range');
  }
}
const viewer=await readFile(source,'utf8');
const adapter=String.raw`
;(() => {
  const original = window.MachinomeViewer;
  const motion = __MOTION__;
  function controls(t) {
    const seconds = Math.max(0, Math.min(1,t)) * motion.duration;
    let previous = {...motion.keys[0][1]}, at = 0;
    for (const [end, changes] of motion.keys.slice(1)) {
      const next = {...previous,...changes};
      if (seconds <= end) {
        const f = (seconds-at)/(end-at);
        return Object.fromEntries(Object.keys(previous).map(id =>
          [id, previous[id]+f*(next[id]-previous[id])]));
      }
      previous=next; at=end;
    }
    return previous;
  }
  window.MachinomeViewer = {...original, async mount(...args) {
    const viewer = await original.mount(...args);
    const declarations = viewer.drivers();
    const host = typeof args[0] === 'string' ? document.querySelector(args[0]) : args[0];
    let lastTime = null, lastView = null, lastSize = null, lastParent = null;
    const surface = () => {
      const canvas = host.querySelector('canvas');
      const size = canvas ? canvas.width + '/' + canvas.height : '';
      if (size !== lastSize || host.parentNode !== lastParent) {
        lastTime = null; lastView = null;
        lastSize = size; lastParent = host.parentNode;
      }
    };
    const setTime = t => {
      surface();
      if (t !== lastTime) {viewer.setTime(t); lastTime = t; lastView = null;}
      for (const [id,design] of Object.entries(controls(t))) {
        const native = design / (declarations[id].scale ?? 1);
        if (!Number.isFinite(native)) throw new Error('Non-finite film driver '+id);
        if (viewer.driver(id)!==native) {viewer.setDriver(id,native); lastView = null;}
        if (Math.abs(viewer.driver(id)-native)>1e-7)
          throw new Error('Film driver did not adopt requested value: '+id);
      }
    };
    const setView = value => {
      surface();
      const signature = JSON.stringify(value);
      if (signature !== lastView) {viewer.setView(value); lastView = signature;}
    };
    setTime(args[2]?.time ?? 0);
    return new Proxy(viewer, {get(target,key) {
      if(key==='setTime') return setTime;
      if(key==='setView') return setView;
      return Reflect.get(target,key);
    }});
  }};
  window.portraitMotionAt = controls;
})();
`.replace('__MOTION__',JSON.stringify(motion));
const output=resolve(base,'_build/portrait-viewer.js');
await writeFile(output,viewer+'\n'+adapter);
const hash=s=>createHash('sha256').update(s).digest('hex');
await writeFile(resolve(base,'_build/capture-adapter.json'),JSON.stringify({
  originalViewer:source,originalViewerSha256:hash(viewer),adapterViewerSha256:hash(viewer+'\n'+adapter),
  method:'Public ViewerHandle.setDriver; deterministic function of normalized film model time',
  sameParts:true,sameTree:true,sameControls:true,motion,
},null,2)+'\n');
console.log('Prepared capture adapter; original machine tree, parts and controls match exactly.');
