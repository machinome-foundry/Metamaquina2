// Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
// Match directional language to the measured voice clock, not guessed seconds.
import assert from 'node:assert/strict';
import {readFile,readdir,writeFile} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
const base=dirname(fileURLToPath(import.meta.url)), tool=resolve(process.argv[2]);
const {loadEpisode}=await import(pathToFileURL(resolve(tool,'src/episode.mjs')));
const {frameAt}=await import(pathToFileURL(resolve(tool,'src/timeline.mjs')));
const film=await loadEpisode(resolve(base,'_build/movie.json'));
const motion=JSON.parse(await readFile(resolve(base,'_build/driver-motion.json'),'utf8'));
const files=await readdir(resolve(base,'_build/audio'));
const takes=[];
for(const name of files.filter(n=>n.endsWith('.json')))takes.push(JSON.parse(await readFile(resolve(base,'_build/audio',name),'utf8')));
const chapter=film.chapters[0], take=takes.find(t=>t.request?.text===chapter.narration);
assert.ok(take, 'No matching complete narration take');
const text=take.alignment.characters.join('');
function controls(t) {
  let previous={...motion.keys[0][1]}, at=0;
  for(const [end,changes] of motion.keys.slice(1)) {
    const next={...previous,...changes};
    if(t<=end){const f=(t-at)/(end-at);return Object.fromEntries(Object.keys(previous).map(id=>[id,previous[id]+f*(next[id]-previous[id])]));}
    previous=next;at=end;
  }
  return previous;
}
const phrases=["lift the crossbeam","carrying the head"];
const checks=[];
for(const phrase of phrases){
 const i=text.indexOf(phrase);
 assert.ok(i>=0 && text.indexOf(phrase,i+1)===-1, 'Phrase must be unique: '+phrase);
 const start=(chapter.speechOffset??.2)+take.alignment.character_start_times_seconds[i];
 const end=(chapter.speechOffset??.2)+take.alignment.character_end_times_seconds[i+phrase.length-1];
 const samples=Array.from({length:9},(_,j)=>{
   const t=start+(end-start)*j/8;
   const frame=frameAt(film,t),view=Object.values(frame.elements).find(e=>e.kind==='view');
   assert.ok(view,'No machine shown on '+phrase);
   return {time:t,shot:frame.shotId,z:controls(view.time*motion.duration).z};
 });
 assert.ok(samples.at(-1).z-samples[0].z>1, 'Head does not rise during: '+phrase);
 samples.slice(1).forEach((s,j)=>assert.ok(s.z>=samples[j].z-1e-6,'Head reverses during: '+phrase));
 checks.push({phrase,start,end,samples});
}
await writeFile(resolve(base,'_build/motion-language-check.json'),JSON.stringify({checks},null,2)+'\n');
console.log('Directional language matches upward head motion for '+checks.length+' measured phrases.');
