/* fit-club v4 — rendered from DATA (built by build.py). State is per phone (localStorage), per shopping week (Sat–Fri). */
const NOW = new Date();
function satOf(n){const d=new Date(n);d.setHours(0,0,0,0);d.setDate(d.getDate()-((d.getDay()+1)%7));return d;}
function ymd(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');}
const WKEY = ymd(satOf(NOW));
const SKEY = 'fc4:'+WKEY;
function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function fmt(n){return Number(n).toLocaleString('en-US');}

/* ---- state ---- */
let S;
try{ S = JSON.parse(localStorage.getItem(SKEY)) || {}; }catch(e){ S = {}; }
S.shop = S.shop || {}; S.prep = S.prep || {}; S.log = S.log || {};
function persist(){
  try{
    Object.keys(localStorage).filter(k=>(k.startsWith('fc4:')&&k!==SKEY)||k.startsWith('fc4train:')||k.startsWith('fc4fish:')||k.startsWith('fc4shop:')).forEach(k=>localStorage.removeItem(k));
    localStorage.setItem(SKEY, JSON.stringify(S));
  }catch(e){}
}

/* ---- adherence ---- */
function adherence(){
  const out={a:[0,0],n:[0,0]};
  for(const k in S.log){ const who=k.split('|')[1]; if(!out[who]) continue; out[who][1]++; if(S.log[k]==='p') out[who][0]++; }
  const part=(w,l)=>{const [p,t]=out[w]; return t?`${l} <b>${p}/${t}</b> (${Math.round(100*p/t)}%)`:`${l} —`;};
  document.getElementById('adh').innerHTML='As planned: '+part('a','A')+' · '+part('n','Ana');
}

/* ---- plan ---- */
const D = DATA.days;
const todayIdx = (NOW.getDay()+1)%7;   // Saturday = 0 … Friday = 6
let current = todayIdx;
const chipBox=document.getElementById('dayChips'), dayBox=document.getElementById('dayContent');
const MAIN=document.querySelector('main');
function chips(){
  chipBox.innerHTML=D.map((d,i)=>`<button class="day-chip${i===current?' active':''}${i===todayIdx?' today':''}" data-i="${i}">${d.name.slice(0,3)}<span class="r">${d.name==='Saturday'?'social':d.name==='Sunday'?'cook-up':'&nbsp;'}</span></button>`).join('');
  chipBox.querySelectorAll('.day-chip').forEach(b=>b.onclick=()=>{current=+b.dataset.i;chips();renderDay();MAIN.scrollTop=0;});
}
const LABEL={p:'✓ As planned',s:'↔ Swapped',x:'+ Extra'};
function chkRow(mid,who,name){
  const st=S.log[mid+'|'+who];
  return `<div class="chk"><span class="who ${who}">${name}</span>`+['p','s','x'].map(k=>
    `<button class="${k}${st===k?' on':''}" data-m="${mid}" data-w="${who}" data-k="${k}">${LABEL[k]}</button>`).join('')+`</div>`;
}
function renderDay(){
  const d=D[current];
  let h=`<div class="dayhead"><h2>${d.name}</h2>${d.name==='Saturday'?'<span class="badge gym">SOCIAL DINNER</span>':d.name==='Sunday'?'<span class="badge rest">COOK-UP DAY</span>':''}</div>`;
  for(const m of d.meals){
    h+=`<div class="meal${m.budget?' free-meal':''}"><div class="meal-top"><div class="meal-time">${esc(m.slot)}</div>`+
       `<div class="meal-name">${esc(m.name)}</div><div class="meal-kcal"><span class="kc a">${m.budget?'≤ ':''}${fmt(m.ka)} kcal · ${m.pa} g P</span>`+
       `<span class="kc n">${m.budget?'≤ ':''}${fmt(m.kn)} kcal · ${m.pn} g P</span></div></div>`;
    if(m.budget){ h+=`<div class="budget">Budget — Alireza ≤ ${fmt(m.ka)} kcal · Ana ≤ ${fmt(m.kn)} kcal</div>`; }
    else{
      h+=`<div class="rows"><div class="row head"><span class="it">Item</span><span class="qa">Alireza</span><span class="qn">Ana</span></div>`+
         m.rows.map(r=>`<div class="row"><span class="it">${esc(r[0])}</span><span class="qa">${esc(r[1])}</span><span class="qn">${esc(r[2])}</span></div>`).join('')+`</div>`;
    }
    if(m.note) h+=`<div class="mcard-note">${esc(m.note)}</div>`;
    if(m.recipe) h+=`<details class="rec"><summary>Recipe</summary><p>${esc(m.recipe)}</p></details>`;
    h+=chkRow(m.id,'a','Alireza')+chkRow(m.id,'n','Ana')+`</div>`;
  }
  const pass=ok=>ok?'<span class="pass">PASS</span>':'<span class="fail">CHECK</span>';
  h+=`<div class="total"><h3>Day total</h3>`+
     `<div class="tr"><span class="who"><i class="dotA"></i>Alireza</span><span>${fmt(d.a[0])} kcal · ${d.a[1]} g P<small>${d.a[2]} g fibre</small> ${pass(d.a[3])}</span></div>`+
     `<div class="tr"><span class="who"><i class="dotN"></i>Ana</span><span>${fmt(d.n[0])} kcal · ${d.n[1]} g P<small>${d.n[2]} g fibre</small> ${pass(d.n[3])}</span></div></div>`;
  dayBox.innerHTML=h;
  /* update only the tapped row: no redraw, so open recipes stay open and the page never jumps */
  dayBox.querySelectorAll('.chk button').forEach(b=>b.onclick=()=>{
    const k=b.dataset.m+'|'+b.dataset.w;
    if(S.log[k]===b.dataset.k) delete S.log[k]; else S.log[k]=b.dataset.k;
    b.parentNode.querySelectorAll('button').forEach(x=>x.classList.toggle('on',S.log[k]===x.dataset.k));
    persist(); adherence();
  });
}

/* ---- prep ---- */
function renderPrep(){
  document.getElementById('prepWeek').textContent='Week from Saturday '+WKEY;
  const box=document.getElementById('prepContent');
  box.innerHTML=`<div class="store"><h3>Sunday cook-up &amp; weekly prep</h3>`+DATA.prep.map(p=>
    `<div class="si${S.prep[p.id]?' done':''}" data-id="${p.id}"><span class="box"></span><span class="tx"><span class="prep-when">${esc(p.when)}</span>${esc(p.text)}</span></div>`).join('')+`</div>`;
  box.querySelectorAll('.si').forEach(el=>el.onclick=()=>{const id=el.dataset.id; if(S.prep[id]) delete S.prep[id]; else S.prep[id]=true; el.classList.toggle('done',!!S.prep[id]); persist();});
}

/* ---- shop ---- */
const TRIPS=['Saturday','Tuesday','Pantry','Persian'];
function nextTrip(){const g=NOW.getDay(); return (g===0||g===1||g===2)?'Tuesday':'Saturday';}  // Sun–Tue → Tuesday; Wed–Sat → Saturday
let trip=nextTrip();
function stClass(s){s=(s||'').toLowerCase();return s.startsWith('lidl')?'lidl':s.startsWith('ah')?'ah':s.startsWith('jumbo')?'jumbo':'';}
function item(id,title,sub,st){
  return `<div class="si${S.shop[id]?' done':''}" data-id="${esc(id)}"><span class="box"></span><span class="tx"><b>${esc(title)}</b>${st?`<span class="st ${stClass(st)}">${esc(st)}</span>`:''}${sub}</span></div>`;
}
function renderShop(){
  document.getElementById('tripSel').innerHTML=TRIPS.map(t=>`<button class="${t===trip?'on':''}" data-t="${t}">${t}<small>${t==='Saturday'?'Sat–Tue lunch':t==='Tuesday'?'Tue dinner–Fri':t==='Pantry'?'when it runs out':'once a month'}</small></button>`).join('');
  document.querySelectorAll('#tripSel button').forEach(b=>b.onclick=()=>{trip=b.dataset.t;renderShop();MAIN.scrollTop=0;});
  document.getElementById('firstWeek').innerHTML=(trip==='Tuesday'&&ymd(NOW)<DATA.firstWeekUntil)?`<div class="fw"><h3>First week only — Tuesday 10 Nov</h3>${DATA.firstWeek}</div>`:'';
  let h='';
  if(trip==='Saturday'||trip==='Tuesday'){
    for(const sec of DATA.shop[trip]){
      h+=`<div class="store"><h3>${esc(sec.aisle)}</h3>`+sec.items.map(it=>item(it.id,it.name,
        `<small><span class="need">need ${esc(it.need)}</span></small><span class="buy">${esc(it.buy)}</span>${it.note?`<small>${esc(it.note)}</small>`:''}`,it.st)).join('')+`</div>`;
    }
  }else if(trip==='Pantry'){
    h+=`<div class="store"><h3>Pantry — buy when it runs out</h3>`+DATA.pantry.map(p=>item(p.id,p.name,
      `<small>${esc(p.week)} · lasts ${esc(p.lasts)}</small><span class="buy">${esc(p.pack)}</span>`,'')).join('')+
      `<div class="si"><span class="tx"><b>Spices</b><small>${esc(DATA.spices)}</small></span></div></div>`;
  }else{
    h+=`<div class="store"><h3>Persian pantry — Iranian/Turkish shop, once a month</h3>`+DATA.persian.map(p=>item(p.id,p.name,
      `<small>${esc(p.use)}</small><span class="buy">${esc(p.buy)}</span>`,'')).join('')+`</div>`;
  }
  const box=document.getElementById('shopContent'); box.innerHTML=h;
  box.querySelectorAll('.si[data-id]').forEach(el=>el.onclick=()=>{const id=el.dataset.id; if(S.shop[id]) delete S.shop[id]; else S.shop[id]=true; el.classList.toggle('done',!!S.shop[id]); persist();});
}

/* ---- static tabs ---- */
document.getElementById('trainContent').innerHTML=DATA.train;
document.getElementById('rulesContent').innerHTML=DATA.rules;

/* ---- nav: each tab keeps its own scroll position ---- */
let view='plan'; const POS={};
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{
  if(b.dataset.v===view){ MAIN.scrollTop=0; return; }   // tapping the open tab again jumps to the top
  POS[view]=MAIN.scrollTop; view=b.dataset.v;
  document.querySelectorAll('nav button').forEach(x=>x.classList.toggle('on',x===b));
  document.querySelectorAll('.view').forEach(v=>v.classList.toggle('on',v.id==='view-'+view));
  chipBox.style.display=view==='plan'?'':'none';
  MAIN.scrollTop=POS[view]||0;
});
document.addEventListener('touchstart',()=>{},{passive:true});   // lets iOS show the pressed state

chips(); renderDay(); renderPrep(); renderShop(); adherence(); persist();
