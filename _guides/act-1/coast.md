---
title: Coast
act: "1"
order: 1
game_version: "3.29.3.3"
---

{% assign a = '/assets/guides/act-1/coast/' | relative_url %}

<div class="cp"><div class="cp-root"><img src="{{ a }}Right%20Entrance.webp" alt="Right orientation at the entrance"><b>Right · run north-east</b></div><div class="cp-q">Straight wall by the entrance?</div><ul><li style="flex:2"><i>Yes</i><div class="cp-q">Go a bit north. Second wall?</div><ul><li style="flex:1"><i>No</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_Long_o0.webp" alt="Long route"><b>Long</b><span>New instance, or inside path (−35 s)</span></div></li><li style="flex:1"><i>Narrow corridor</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_pistol.webp" alt="Pistol route"><b>Pistol</b><span>Wall north, up the ramp, then the top wall</span></div></li></ul></li><li style="flex:4"><i>No</i><div class="cp-q">Dildo?</div><ul><li style="flex:1"><i>Yes</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_Dildo.webp" alt="Dildo route"><b>Dildo</b><span>Over it, then left after the ledge</span></div></li><li style="flex:1"><i>No</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_RightLedge.webp" alt="Right Ledge route"><b>Right Ledge</b><span>Go right and follow the water</span></div></li><li style="flex:1"><i>Ledge shape north</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_Fast.webp" alt="Pocket route"><b>Pocket</b><span>Keep going north-east</span></div></li><li style="flex:1"><i>Mountain bends into a U</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_Uturn.webp" alt="U Turn route"><b>U Turn</b><span>Round the U, then straight east</span></div></li></ul></li></ul></div>
<div class="cp"><div class="cp-root"><img src="{{ a }}Left%20Orientation.webp" alt="Left orientation at the entrance"><b>Left · run south-east</b></div><div class="cp-q">Can you go up at the top wall?</div><ul><li style="flex:1"><i>No</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_Top.webp" alt="Top route"><b>Top</b><span>South, inside wall to the ledge, then the right wall</span></div></li><li style="flex:2"><i>Yes</i><div class="cp-q">Then:</div><ul><li style="flex:1"><i>Wall lets you go east</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_LeftLedge.webp" alt="Left Ledge route"><b>Left Ledge</b><span>To the wall, then the mountain south-east</span></div></li><li style="flex:1"><i>Path through the middle</i><div class="cp-stem"></div><div class="cp-leaf"><img src="{{ a }}The_Coast_FakeLedge.webp" alt="Fake Ledge route"><b>Fake Ledge</b><span>Take the middle. The edges are dead ends</span></div></li></ul></li></ul></div>

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
.cp{display:flex;flex-direction:column;align-items:safe center;overflow-x:auto;margin:0 0 3rem;font-size:.9rem;line-height:1.35}
.cp-root{width:min(100%,20rem);text-align:center}
.cp-root img{aspect-ratio:16/9;object-fit:cover}
.cp-root b{display:block;font-size:1.1rem;padding:.3rem 0}
.cp .guide-image-zoom{margin:0;width:100%}
.cp img{width:100%}
.cp-q{font-weight:650;border:2px solid var(--focus);border-radius:.4rem;padding:.3rem .7rem;text-align:center;max-width:16rem}
.cp ul{flex:1;display:flex;align-self:stretch;margin:0;padding:1.1rem 0 0;position:relative;list-style:none}
.cp>ul{min-width:40rem}
.cp ul::before{content:"";position:absolute;top:0;left:50%;height:1.1rem;border-left:2px solid var(--line)}
.cp li{display:flex;flex-direction:column;align-items:center;position:relative;margin:0;padding:1.1rem .2rem 0;min-width:0}
.cp li::before,.cp li::after{content:"";position:absolute;top:0;right:50%;width:50%;height:1.1rem;border-top:2px solid var(--line)}
.cp li::after{right:auto;left:50%;border-left:2px solid var(--line)}
.cp li:first-child::before,.cp li:last-child::after{border-top:0}
.cp li:only-child::before{display:none}
.cp i{color:var(--accent-dark);font-style:normal;padding:0 0 .25rem;text-align:center}
.cp-stem{flex:1;border-left:2px solid var(--line);min-height:.5rem}
.cp-leaf{width:100%;max-width:14rem;display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--line);border-radius:.4rem;overflow:hidden}
.cp-leaf img{background:#131317;aspect-ratio:1;object-fit:contain;border:0;border-radius:0}
.cp-leaf b{padding:.4rem .5rem 0}
.cp-leaf span{min-height:5.2em;padding:0 .5rem .5rem;color:var(--muted);font-size:.85em}
</style>
