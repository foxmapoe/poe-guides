---
title: Coast
act: "1"
order: 1
game_version: "3.29.3.3"
---

{% assign a = '/assets/guides/act-1/coast/' | relative_url %}

<div class="cp"><div class="cp-root"><b>Right · run north-east</b><img src="{{ a }}Right%20Entrance.webp" alt="Right orientation at the entrance"></div><div class="cp-q">Straight wall by the entrance?</div><ul><li style="flex:2"><i>Yes</i><div class="cp-q">Go a bit north. Second wall?</div><ul><li style="flex:1"><i>No</i><div class="cp-stem"></div><div class="cp-leaf"><b>Long</b><img src="{{ a }}The_Coast_Long_o0.webp" alt="Long route"><span>New instance, or inside path (−35 s)</span></div></li><li style="flex:1"><i>Narrow corridor</i><div class="cp-stem"></div><div class="cp-leaf"><b>Pistol</b><img src="{{ a }}The_Coast_pistol.webp" alt="Pistol route"><span>Wall north, up the ramp, then the top wall</span></div></li></ul></li><li style="flex:2"><i>No</i><div class="cp-q">Dildo?</div><ul><li style="flex:1"><i>Yes</i><div class="cp-stem"></div><div class="cp-leaf"><b>Dildo</b><img src="{{ a }}The_Coast_Dildo.webp" alt="Dildo route"><span>Over it, then left after the ledge</span></div></li><li style="flex:1"><i>No</i><div class="cp-stem"></div></li></ul></li></ul><div class="cp-row" style="grid-template-columns:repeat(4,1fr);--x:87.5000%;--y:83.3333%"><div class="cp-q" style="grid-column:4">Then:</div><div class="cp-rowkids" style="grid-column:2/5"><ul><li style="flex:1"><i>Ledge shape north</i><div class="cp-stem"></div><div class="cp-leaf"><b>Pocket</b><img src="{{ a }}The_Coast_Fast.webp" alt="Pocket route"><span>Keep going north-east</span></div></li><li style="flex:1"><i>Mountain bends into a U</i><div class="cp-stem"></div><div class="cp-leaf"><b>U Turn</b><img src="{{ a }}The_Coast_Uturn.webp" alt="U Turn route"><span>Round the U, then straight east</span></div></li><li style="flex:1"><i>Neither</i><div class="cp-stem"></div><div class="cp-leaf"><b>Right Ledge</b><img src="{{ a }}The_Coast_RightLedge.webp" alt="Right Ledge route"><span>Go right and follow the water</span></div></li></ul></div></div></div>
<div class="cp"><div class="cp-root"><b>Left · run south-east</b><img src="{{ a }}Left%20Orientation.webp" alt="Left orientation at the entrance"></div><div class="cp-q">Can you go up at the top wall?</div><ul><li style="flex:1"><i>No</i><div class="cp-stem"></div><div class="cp-leaf"><b>Top</b><img src="{{ a }}The_Coast_Top.webp" alt="Top route"><span>South, inside wall to the ledge, then the right wall</span></div></li><li style="flex:2"><i>Yes</i><div class="cp-q">Then:</div><ul><li style="flex:1"><i>Wall lets you go east</i><div class="cp-stem"></div><div class="cp-leaf"><b>Left Ledge</b><img src="{{ a }}The_Coast_LeftLedge.webp" alt="Left Ledge route"><span>To the wall, then the mountain south-east</span></div></li><li style="flex:1"><i>Path through the middle</i><div class="cp-stem"></div><div class="cp-leaf"><b>Fake Ledge</b><img src="{{ a }}The_Coast_FakeLedge.webp" alt="Fake Ledge route"><span>Take the middle. The edges are dead ends</span></div></li></ul></li></ul></div>

## Layouts

### Long Coast (Longest Layout)

![Coast terraces layout 1-1-1]({{ a }}The_Coast_macro_terraces1_1_1_o0.webp)
![Long route]({{ a }}The_Coast_Long_o0.webp)

### Pocket (Fastest Layout)

![Coast terraces layout 1-1-4]({{ a }}The_Coast_macro_terraces1_1_4_o0.webp)
![Pocket route]({{ a }}The_Coast_Fast.webp)

### Pistol

![Coast terraces layout 1-2-1]({{ a }}The_Coast_macro_terraces1_2_1_o0.webp)
![Pistol route]({{ a }}The_Coast_pistol.webp)

### Dildo Shape

![Coast terraces layout 1-2-2]({{ a }}The_Coast_macro_terraces1_2_2_o0.webp)
![Dildo route]({{ a }}The_Coast_Dildo.webp)

### Right Ledge

![Coast terraces layout 1-3-1]({{ a }}The_Coast_macro_terraces1_3_1_o0.webp)
![Right Ledge route]({{ a }}The_Coast_RightLedge.webp)

### U Turn

![Coast terraces layout 1-4-1]({{ a }}The_Coast_macro_terraces1_4_1_o0.webp)
![U Turn route]({{ a }}The_Coast_Uturn.webp)

### Top

![Coast terraces layout 1-4-2]({{ a }}The_Coast_macro_terraces1_4_2_o0.webp)
![Top route]({{ a }}The_Coast_Top.webp)

### Left Ledge

![Coast terraces layout 1-5-1]({{ a }}The_Coast_macro_terraces1_5_1_o0.webp)
![Left Ledge route]({{ a }}The_Coast_LeftLedge.webp)

### Fake Ledge

![Coast terraces layout 1-5-2]({{ a }}The_Coast_macro_terraces1_5_2_o0.webp)
![Fake Ledge route]({{ a }}The_Coast_FakeLedge.webp)

<style>
.guide-content:has(.cp){max-width:none}
.cp{display:flex;flex-direction:column;align-items:center;margin:0 0 3rem;font-size:.9rem;line-height:1.35}
.cp-root{width:min(100%,20rem);text-align:center}
.cp-root img{aspect-ratio:16/9;object-fit:cover}
.cp-root b{display:block;font-size:1.1rem;padding:0 0 .4rem}
.cp-root+.cp-q{margin-top:.6rem}
.cp .guide-image-zoom{margin:0;width:100%}
.cp img{width:100%}
.cp-q{font-weight:650;border:2px solid var(--focus);border-radius:.4rem;padding:.3rem .7rem;text-align:center;max-width:16rem}
.cp ul{flex:1;display:flex;align-self:stretch;margin:0;padding:1.1rem 0 0;position:relative;list-style:none}
.cp ul::before{content:"";position:absolute;top:0;left:50%;height:1.1rem;border-left:2px solid var(--line)}
.cp li{display:flex;flex-direction:column;align-items:center;position:relative;margin:0;padding:1.1rem 0 0;min-width:0}
.cp li::before,.cp li::after{content:"";position:absolute;top:0;right:50%;width:50%;height:1.1rem;border-top:2px solid var(--line)}
.cp li::after{right:auto;left:50%;border-left:2px solid var(--line)}
.cp li:first-child::before,.cp li:last-child::after{border-top:0}
.cp li:only-child::before{display:none}
.cp i{color:var(--accent-dark);font-style:normal;padding:0 0 .25rem;text-align:center}
.cp-stem{flex:1;border-left:2px solid var(--line);min-height:.5rem}
.cp-leaf{width:calc(100% - .5rem);max-width:14rem;display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--line);border-radius:.4rem;overflow:hidden}
.cp-leaf img{background:#131317;aspect-ratio:1;object-fit:contain;border:0;border-radius:0}
.cp-leaf b{padding:.35rem .5rem;text-align:center}
.cp-leaf span{min-height:5.6em;padding:.4rem .5rem .5rem;text-align:center;color:var(--muted);font-size:.85em}
.cp-row{align-self:stretch;display:grid;position:relative}
.cp-row::before{content:"";position:absolute;top:0;left:var(--x);height:3.8rem;border-left:2px solid var(--line)}
.cp-row>.cp-q{justify-self:center;align-self:start;margin-top:1.1rem;position:relative;background:var(--paper)}
.cp-row>.cp-q,.cp-rowkids{grid-row:1}
.cp-rowkids{display:flex;padding-top:3.8rem}
.cp-rowkids>ul{padding-top:0}
.cp-rowkids>ul::before{display:none}
</style>
