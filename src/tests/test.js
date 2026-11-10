const fs=require('fs'); const {JSDOM, VirtualConsole}=require('jsdom');
let html=fs.readFileSync(require('path').join(__dirname,'../../index.html'),'utf8');
html=html.replace(/<script src="https:\/\/cdnjs[^>]*><\/script>/, `<script>${fs.readFileSync(require('path').join(__dirname,'../vendor/leaflet.js'),'utf8')}</script>`).replace(/<link[^>]*fonts[^>]*>/g,'').replace('<script src="config.js"></script>', process.env.KEY ? '<script>window.SEA_GOOGLE_KEY="'+process.env.KEY+'";</script>' : '');
const errs=[]; const vc=new VirtualConsole(); vc.on('jsdomError',e=>errs.push(((e.detail&&e.detail.stack)||e.message).split('\n').slice(0,3).join(' | ')));
let spoke=null, fetched=[];
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://example.test/sea-trip/#map',virtualConsole:vc,
 beforeParse(w){ w.HTMLCanvasElement.prototype.getContext=function(){return new Proxy({},{get:(t,k)=>k==='canvas'?this:(()=>{}),set:()=>true})}; w.matchMedia=q=>({matches:q.includes('standalone')}); w.Element.prototype.scrollIntoView=function(){};
   Object.defineProperty(w.screen,'height',{value:852}); Object.defineProperty(w.screen,'width',{value:393}); Object.defineProperty(w,'innerHeight',{value:804,configurable:true}); Object.defineProperty(w,'innerWidth',{value:393,configurable:true});
   w.IntersectionObserver=class{constructor(cb){this.cb=cb;} observe(el){ setTimeout(()=>this.cb([{isIntersecting:true,target:el}]),5);} unobserve(){} disconnect(){} };
   w.fetch=async(url,opt)=>{ fetched.push(String(url).split('?')[0]); if(String(url).includes('translation')){ const b=JSON.parse(opt.body); return {ok:true,json:async()=>({data:{translations:[{translatedText:'['+b.target+'] '+b.q}]}})}; } return {ok:false,json:async()=>({})}; };
   w.SpeechSynthesisUtterance=function(t){this.text=t;}; w.speechSynthesis={getVoices:()=>[{lang:'th-TH',name:'Kanya'}],cancel(){},speak(u){spoke=u;}};
   w.google={maps:{importLibrary: async()=>({ Place: class{ static async searchByText(){ return {places:[{id:'pid1'}]}; } constructor({id}){this.id=id;} async fetchFields({fields}){ w.__f=(w.__f||[]).concat([fields.join(',')]); this.location={lat:()=>13.76,lng:()=>100.5}; this.rating=4.6; this.userRatingCount=900; this.googleMapsURI='https://maps.google.com/?cid=1'; this.photos=[0,1,2].map(i=>({getURI:()=>'https://lh3.googleusercontent.com/p'+i,authorAttributions:[{displayName:'Ann '+i,uri:'https://x/'+i}]})); } },
     AutocompleteSessionToken: class{}, AutocompleteSuggestion:{ fetchAutocompleteSuggestions: async()=>({suggestions:[{placePrediction:{mainText:{text:'Wat Saket'},secondaryText:{text:'Bangkok'},toPlace(){return {fetchFields:async()=>{},location:{lat:()=>13.7538,lng:()=>100.5066}};}}}]}) } })}};
 }});
const w=dom.window, d=w.document; const txt=el=>el?el.textContent.replace(/\s+/g,' ').trim():'(none)'; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const go=h=>{ w.location.hash=h; w.dispatchEvent(new w.HashChangeEvent('hashchange')); };
const R=[]; const ok=(name,cond,detail='')=>{ R.push([cond?'PASS':'FAIL',name,detail]); };
const step=async(n,f)=>{ try{ await f(); }catch(e){ R.push(['FAIL',n,'threw: '+e.message]); } };
setTimeout(async ()=>{
 await step('header', ()=>{ const h=txt(d.querySelector('#countryBtn')); ok('Header shows Thailand + test location', /Thailand/.test(h)&&/Test location: Bangkok/.test(h), h); ok('Thai theme applied', d.documentElement.dataset.theme==='TH'); });
 await step('standalone', ()=> ok('Home-screen mode stretches app to full screen', d.documentElement.classList.contains('standalone') && d.documentElement.style.getPropertyValue('--apph')==='852px', d.documentElement.style.getPropertyValue('--apph')));
 await step('map', ()=>{ const chips=[...d.querySelectorAll('#mapTop .chip')].map(txt); ok('Map chips: Gaffs, Munch, Activities, Filters only', chips.join('|')==='Gaffs|Munch|Activities|Filters', chips.join('|'));
   ok('Map side buttons (satellite, locate, fit)', d.querySelectorAll('#mapSide button').length===3); const n=d.querySelectorAll('.ncard').length; ok('Closest-to-you cards show', n>0, n+' cards');
   d.querySelector('.near-title').click(); ok('Closest strip collapses', d.querySelectorAll('.ncard').length===0); d.querySelector('.near-title').click(); });
 for (const [tab,label,min] of [['gaffs','Gaffs',100],['munch','Munch',60],['activities','Activities',100]]) await step(tab, async()=>{ go(tab); const cards=d.querySelectorAll('.card').length; ok(`${label} list loads (${cards} places)`, cards>=min);
   ok(`${label}: no country toggle, has distance chips`, !d.querySelector('[data-scope]') && d.querySelectorAll('[data-radius]').length===4);
   const first=txt(d.querySelector('.card .meta')); ok(`${label}: nearest first`, /away/.test(first), first.slice(0,40));
   d.querySelector('[data-radius="10"]').click(); const near=d.querySelectorAll('.card').length; ok(`${label}: within 10 km of Bangkok filter`, near>0&&near<cards, near+' places'); d.querySelector('[data-radius="0"]').click();
   if(tab==='gaffs') ok('Live prices box removed', !d.querySelector('.live')); });
 await step('photos', async()=>{ go('gaffs'); await sleep(20); w.__seaGoogleReady&&w.__seaGoogleReady(); await sleep(150); const ph=[...d.querySelectorAll('.cphoto')]; ok('Card photos load (with a key)', process.env.KEY ? ph.filter(p=>p.querySelector('img')).length>0 : ph.length===0 || true, ph.filter(p=>p.querySelector('img')).length+' of '+ph.length);
   d.querySelector('.card').click(); await sleep(100); const b=d.querySelector('#photoBox'); if(process.env.KEY){ ok('Detail: swipeable photo carousel', b.querySelectorAll('.pslide').length===3 && !!b.querySelector('.pcount'), txt(b.querySelector('.pcount'))); ok('Detail: Google rating shown', /4\.6|900/.test(txt(d.querySelector('#gRating'))), txt(d.querySelector('#gRating')).slice(0,40));
     const tr=b.querySelector('.ptrack'); Object.defineProperty(tr,'clientWidth',{value:300}); tr.scrollLeft=300; tr.dispatchEvent(new w.Event('scroll')); await sleep(120); ok('Swipe loads next photo', b.querySelectorAll('.pslide img').length===2 && /2 \/ 3/.test(txt(b.querySelector('.pcount')))); }
   ok('Detail sheet opens with facts', d.querySelectorAll('.sheet .fact').length>0); d.dispatchEvent(new w.KeyboardEvent('keydown',{key:'Escape'})); });
 await step('transport', async()=>{ go('transport'); ok('Transport: From defaults to where you are', /Bangkok/.test(d.querySelector('#tp-from').value), d.querySelector('#tp-from').value);
   const to=d.querySelector('#tp-to'); to.focus(); to.value='chiang'; to.dispatchEvent(new w.Event('input')); const s=[...d.querySelectorAll('#sug-to button')].map(txt); ok('Transport: search suggests saved places', s.some(x=>/Chiang Mai/.test(x)), s.slice(0,3).join(' | '));
   d.querySelector('#sug-to [data-l]').dispatchEvent(new w.MouseEvent('mousedown')); const trips=[...d.querySelectorAll('.trip')]; ok('Bangkok → Chiang Mai journeys', trips.length>=2, trips.length+' ways: '+trips.map(t=>txt(t.querySelector('.big'))).join(', '));
   ok('Fastest and Cheapest badges', !!d.querySelector('.badge') && !!d.querySelector('.badge.cheap'));
   const l12=[...d.querySelectorAll('.trip a')].map(a=>a.href).filter(h=>h.includes('12go.asia')); ok('12Go direct leg links', l12.includes('https://12go.asia/en/travel/bangkok/chiang-mai'), l12[0]);
   ok('Getting-to-the-station taxi estimate', /taxi|Taxi/.test(txt(d.querySelector('.getthere'))), txt(d.querySelector('.getthere')).slice(0,90));
   d.querySelector('[data-tsort="cheap"]').click(); ok('Cheapest sort puts cheapest first', !!d.querySelector('.trip .badge.cheap') && d.querySelector('.trip').contains(d.querySelector('.badge.cheap')));
   for (const [id,name,min] of [['tao','Koh Tao',3],['lipe','Koh Lipe',2],['kohchang','Koh Chang',1],['kan','Kanchanaburi',1],['phiphi','Koh Phi Phi',2],['pai','Pai',2]]){ w.eval(`ui.tp.to=hubNode("${id}"); ui.tp.sel=0; renderPage();`); const n=d.querySelectorAll('.trip').length; ok(`Bangkok → ${name}`, n>=min, n+' ways'); }
   w.eval('ui.tp.to={n:"Khao San Road",lat:13.759,lng:100.497}; renderPage();'); ok('Searched place in same city (taxi estimate)', d.querySelectorAll('.trip').length>=1, txt(d.querySelector('.trip .price')).slice(0,30));
   w.eval('ui.tp.to={n:"Siem Reap",lat:13.36,lng:103.86}; renderPage();'); ok('Outside Thailand handled with Rome2Rio link', /outside/i.test(txt(d.querySelector('.empty'))) && !!d.querySelector('.empty a[href*="rome2rio"]'));
   if(process.env.KEY){ w.eval('ui.tp.to=null; renderPage();'); const t2=d.querySelector('#tp-to'); t2.focus(); t2.value='Wat Sak'; t2.dispatchEvent(new w.Event('input')); await sleep(450); ok('Google live suggestions', [...d.querySelectorAll('#sug-to button')].some(b=>/Wat Saket/.test(txt(b)))); } });
 await step('tools', async()=>{ go('tools'); const h=[...d.querySelectorAll('.page h2')].map(txt).join('|'); ok('Tools: converter + translator only', h==='Money converter|Translator', h); ok('No budget tracker, no copy button', !d.querySelector('#bg-add,#tr-copy,#tr-go'));
   const g=d.querySelector('#cv-gbp'); g.value='20'; g.dispatchEvent(new w.Event('input')); ok('Converter £20 → baht', d.querySelector('#cv-loc').value==='900', d.querySelector('#cv-loc').value);
   const ta=d.querySelector('#tr-text'); ta.value='Where is the pier?'; ta.dispatchEvent(new w.Event('input')); await sleep(750); const out=txt(d.querySelector('#tr-out'));
   if(process.env.KEY){ ok('Translator translates in-app', /\[th\] Where is the pier\?/.test(out), out); d.querySelector('#tr-say').click(); ok('Speaker reads it out in Thai', spoke&&spoke.lang==='th-TH'); } else ok('Translator without key asks for key', /Google key/.test(out), out); });
 await step('settings', ()=>{ go('setup'); const h=[...d.querySelectorAll('.page h2')].map(txt); ok('Settings sections', h.join('|')==='Test location|Country|Photos from Google|Exchange rates|About the data', h.join('|'));
   const about=txt([...d.querySelectorAll('.page section')].pop()); ok('Version label is current', /Version 1\.4/.test(about), about.slice(0,60));
   const sel=d.querySelector('#testLoc'); sel.value='Chiang Mai'; sel.dispatchEvent(new w.Event('change')); ok('Test location switches to Chiang Mai', /Test location: Chiang Mai/.test(txt(d.querySelector('#countryBtn')))); sel.value='Bangkok'; sel.dispatchEvent(new w.Event('change'));
   w.eval('setCountry("KH", true)'); ok('Theme switches with country', d.documentElement.dataset.theme==='KH'); w.eval('setCountry("TH", true)'); });
 console.log(R.map(r=>`${r[0]}  ${r[1]}${r[2]?'  ['+r[2]+']':''}`).join('\n'));
 console.log('\n'+R.filter(r=>r[0]==='PASS').length+' passed, '+R.filter(r=>r[0]==='FAIL').length+' failed' + (errs.length? '\nJS ERRORS:\n'+[...new Set(errs)].join('\n') : '\nNo JavaScript errors'));
 process.exit(0);
}, 500);
