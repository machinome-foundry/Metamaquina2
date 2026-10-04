// Copyright (C) 2026 Luis Henrique Cassis Fagundes. AGPL-3.0-or-later.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir,readdir} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
const base=dirname(fileURLToPath(import.meta.url)), build=resolve(base,'_build');
const movie=JSON.parse(await readFile(resolve(build,'movie-resolved.json'),'utf8'));
const video=resolve(build,'rehearsal.mp4');
const probe=JSON.parse(execFileSync('ffprobe',['-v','error','-count_frames','-show_streams','-show_format','-of','json',video],{encoding:'utf8'}));
const stream=probe.streams.find(s=>s.codec_type==='video');
assert.ok(stream && probe.streams.some(s=>s.codec_type==='audio'));
assert.equal(stream.codec_name,'h264');
assert.equal(probe.streams.find(s=>s.codec_type==='audio').codec_name,'aac');
assert.equal(stream.width,1920); assert.equal(stream.height,1080);
assert.equal(stream.avg_frame_rate,'24/1');
assert.ok(Math.abs(Number(probe.format.duration)-movie.output.durationSeconds)<.06);
const srt=await readFile(resolve(build,'rehearsal.srt'),'utf8');
assert.ok(srt.includes('Machinome'));
await writeFile(resolve(build,'rehearsal.vtt'),'WEBVTT\n\n'+srt.replace(/(\d{2}:\d{2}:\d{2}),(\d{3})/g,'$1.$2'));
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
const shots=movie.chapters.flatMap(c=>c.shots).map(s=>({id:s.id,time:s.start}));
const links=shots.map(s=>'<button data-time="'+s.time+'">'+esc(s.id.replaceAll('-',' '))+'</button>').join('');
const html='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>'+esc(movie.title)+'</title>'+
'<style>body{margin:30px auto;max-width:1100px;padding:0 20px;background:#f5f2e9;color:#202623;font:16px system-ui}h1{font-size:28px}video{display:block;width:100%;background:#171a19}nav{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}button{padding:8px 12px;background:none;border:1px solid #c65d2f;border-radius:4px;cursor:pointer}a{color:#96441f}</style>'+
'<h1>'+esc(movie.title)+'</h1><p>Editorial sample · Jessica narration · 1080p / 24 fps</p>'+
'<video controls preload="metadata" src="rehearsal.mp4"><track kind="subtitles" srclang="en" label="English" src="rehearsal.vtt"></video>'+
'<nav>'+links+'</nav><p><a href="rehearsal.mp4">Download MP4</a> · <a href="rehearsal.srt">Subtitles</a> · <a href="../description.md">Source links and credits</a> · <a href="../movie.py">Editable film</a></p>'+
'<script>document.querySelectorAll("button").forEach(b=>b.onclick=()=>{const v=document.querySelector("video");v.currentTime=Number(b.dataset.time);v.play()});</script></html>';
await writeFile(resolve(build,'review.html'),html);
const audio=[];
for(const name of await readdir(resolve(build,'audio')))if(name.endsWith('.json')){
 const a=JSON.parse(await readFile(resolve(build,'audio',name),'utf8'));
 if(a.request){assert.equal(a.voice,'cgSgspJ2msm6clMCkdW9');assert.equal(a.request.pronunciation_dictionary_locators[0].pronunciation_dictionary_id,'a0DE9zcAKBZxde7BDjmt');
 audio.push({metadata:name,duration:a.duration,sha256:a.sha256,voice:a.voice,dictionary:a.pronunciation});}
}
const sha256=createHash('sha256').update(await readFile(video)).digest('hex');
assert.equal(audio.length,1,'Exactly one approved Jessica take must be recorded.');
const result={video,sha256,duration:Number(probe.format.duration),width:stream.width,height:stream.height,
 fps:stream.avg_frame_rate,frames:Number(stream.nb_read_frames),audio,chapters:shots,
 caveats:['Editorial review pending','Narration timing and encoding checked; human listening review pending','No publication performed'],
 checks:['H.264 picture and audio present','24 fps, 1920x1080','encoded duration matches resolved film','captions retain written Machinome','Jessica and approved dictionary verified']};
await writeFile(resolve(build,'delivery.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({video,duration:result.duration,frames:result.frames,sha256},null,2));
