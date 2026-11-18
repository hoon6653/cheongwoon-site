(function(){
  var d=document;
  d.documentElement.classList.remove('js-off');
  var b=d.querySelector('.burger'),n=d.querySelector('nav');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});}
  // header: 스크롤하면 흰 배경으로
  var hd=d.querySelector('header');
  var onScroll=function(){if(hd)hd.classList.toggle('solid',window.scrollY>40);};
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  // tabs (hash based)
  var tabs=d.querySelectorAll('.tabs a');
  if(tabs.length){
    var show=function(){
      var id=(location.hash||'').slice(1)||tabs[0].getAttribute('href').slice(1);
      var found=false;
      tabs.forEach(function(a){var on=a.getAttribute('href')==='#'+id;if(on)found=true;});
      if(!found)id=tabs[0].getAttribute('href').slice(1);
      tabs.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+id);});
      d.querySelectorAll('.panel').forEach(function(p){p.classList.toggle('on',p.id===id);});
    };
    window.addEventListener('hashchange',show);show();
  }
  // board search
  d.querySelectorAll('.search').forEach(function(f){
    f.addEventListener('submit',function(e){e.preventDefault();
      var q=f.querySelector('input').value.trim().toLowerCase();
      var t=f.closest('.panel,main,section').querySelectorAll('tbody tr.row');
      t.forEach(function(r){r.style.display=r.textContent.toLowerCase().indexOf(q)>-1?'':'none';});});
  });
  // hero slider
  var sd=d.querySelector('.hero .slides');
  if(sd){
    var sl=[].slice.call(sd.children),si=0,timer=null;
    var go=function(n){sl[si].classList.remove('on');si=(n+sl.length)%sl.length;sl[si].classList.add('on');};
    var play=function(){if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;clearInterval(timer);timer=setInterval(function(){go(si+1);},6000);};
    var pv=d.querySelector('.hero .prev'),nx=d.querySelector('.hero .next');
    if(pv)pv.addEventListener('click',function(){go(si-1);play();});
    if(nx)nx.addEventListener('click',function(){go(si+1);play();});
    play();
  }
  // popup
  var pop=d.getElementById('pop');
  if(pop){
    var key='popHideDate',today=new Date().toDateString(),saved=null;
    try{saved=localStorage.getItem(key);}catch(e){}
    if(saved!==today)pop.classList.add('on');
    var close=function(){pop.classList.remove('on');};
    d.getElementById('ok').onclick=close;
    d.getElementById('xbtn').onclick=close;
    d.getElementById('hide').onclick=function(){try{localStorage.setItem(key,today);}catch(e){}close();};
    d.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  }
})();
