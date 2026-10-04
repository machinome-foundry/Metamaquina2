// Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
import assert from 'node:assert/strict';
import {mkdir,writeFile,readFile} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const base=dirname(fileURLToPath(import.meta.url));
assert.ok(process.argv[2], 'Pass the Videomaker checkout.');
const tool=resolve(process.argv[2]);
const {loadEpisode}=await import(pathToFileURL(resolve(tool,'src/episode.mjs')));
const {browserSession}=await import(pathToFileURL(resolve(tool,'src/render.mjs')));
const {hash}=await import(pathToFileURL(resolve(tool,'src/util.mjs')));
const film=await loadEpisode(resolve(base,'_build/movie.json'));
const directory=resolve(base,'_build/inspection');
await mkdir(directory,{recursive:true});
const shots=film.chapters.flatMap(c=>c.shots);
const {frames}=await browserSession(film,resolve(base,'_build/portrait-viewer.js'),1280,[],async({page,pose})=>{
  const result=[];
  for(const shot of shots.filter(s=>!process.argv.includes('--motion-only')||['demonstration','carriage-travel','bed-travel','screw-lift'].includes(s.id))) {
    for(const fraction of [.15,.5,.85]) {
      const t=shot.start+(shot.end-shot.start)*fraction;
      const posed=await pose(t);
      const view=Object.values(posed.elements).find(e=>e.kind==='view');
      const checks=await page.evaluate(({time})=>{
        const controls=time===null?null:window.portraitMotionAt(time);
        const viewer=window.film.viewer;
        const adopted=controls?Object.fromEntries(Object.keys(controls).map(id=>{
          const d=viewer.drivers()[id];
          return [id,viewer.driver(id)*(d.scale??1)];
        })):null;
        const elements=[...document.querySelectorAll('.panel,.panel h1,.deck,.fact,.footnote,.credits header,.credits footer')];
        const text=elements.map(e=>{
          const r=e.getBoundingClientRect();
          return {text:e.textContent,box:{x:r.x,y:r.y,w:r.width,h:r.height},
            width:e.clientWidth,scrollWidth:e.scrollWidth};
        });
        return {controls,adopted,text};
      },{time:view?.time??null});
      if(checks.controls)for(const [id,v] of Object.entries(checks.controls))
        assert.ok(Math.abs(v-checks.adopted[id])<1e-6, shot.id+' did not adopt '+id);
      for(const e of checks.text) {
        assert.ok(e.box.x>=-1 && e.box.y>=-1 && e.box.x+e.box.w<=1281 && e.box.y+e.box.h<=721,
          shot.id+': text outside frame: '+e.text);
        assert.ok(e.scrollWidth<=e.width+1, shot.id+': text overflows: '+e.text);
      }
      // Software WebGL can take longer than Playwright's default 30 seconds
      // after a non-local seek while a full-resolution capture is also running.
      const bytes=await page.screenshot({timeout:120000});
      // A non-local seek followed by return must reproduce the exact pixels.
      await pose(shots[0].end*.5);
      await pose(t);
      const replay=await page.screenshot({timeout:120000});
      if(!bytes.equals(replay)) {
        await writeFile(resolve(directory,shot.id+'-first.png'),bytes);
        await writeFile(resolve(directory,shot.id+'-replay.png'),replay);
      }
      assert.ok(bytes.equals(replay), shot.id+': pixels depend on seek history');
      const name=shot.id+'-'+Math.round(fraction*100)+'.png';
      if(process.argv.includes('--compare-existing') && shot.id!=='closing-credits') {
        let before; try {before=await readFile(resolve(directory,name));} catch(e) {if(e.code!=='ENOENT')throw e;}
        if(before)assert.ok(before.equals(bytes),shot.id+': capture optimization changed pixels');
      }
      await writeFile(resolve(directory,name),bytes);
      result.push({shot:shot.id,time:t,file:name,sha256:hash(bytes),...checks});
    }
  }
  return {frames:result};
});
await writeFile(resolve(directory,'report.json'),JSON.stringify({frames,checkedAt:new Date().toISOString(),
  assertions:['text stays inside frame','no horizontal text overflow','posed XYZ adopted in correct design units','exact seek/replay pixels']},null,2)+'\n');
console.log('Inspected '+frames.length+' compositions: controls, text bounds and exact pixel replay pass.');
