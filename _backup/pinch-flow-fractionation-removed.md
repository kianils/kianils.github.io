# Stored 2026: Pinch Flow Fractionation (microfluid) project — removed temporarily.
# To restore: copy this file to _portfolio/PinchFlowFractionation.md and add the fab_projects entry below back into _data/fab_projects.yml.
# Drawing PDF: assets/img/fluids/50x75-Base-Model Drawing v1.pdf

---
title: "Pinch Flow Fractionation Device (μFluidic Device)"
layout: single
classes: wide
excerpt: "Resin-printed microfluidic mold for particle separation by size using pinch flow fractionation; CHBE 4200."
header:
  teaser: /assets/img/fluids/teaser.jpg
---

## Project Overview

I built a microfluidic device that separates particles by size using **pinch flow fractionation (PFF)**. Two streams meet at a narrow pinch: one has particles, the other is a faster buffer. The buffer pushes the particles against one wall. Because bigger and smaller particles sit on different streamlines, they spread out when the channel gets wide and I could collect them at separate outlets. I designed the layout in Fusion, printed the mold on the Form 3+/4, then cast PDMS and bonded it to glass.

This kind of sorting shows up in things like biomedical diagnostics, where cells or beads are separated by size without filters that clog. PFF does it in one flow-through device.

## What I Learned Along the Way

As a Computer Science student, I was not familiar with a lot of the calculations or microfluidics altogether, which made this assignment hard for me to grasp the calculations and justifications. I got through it by breaking the design into small steps and tackling one at a time. I started with the pinch width (so the biggest particles don't clog), then the broad section length, then the equation for where particles end up, and finally outlet placement and flow balancing. Doing it section by section made the math and the design choices click.

## Design

### Device layout

| Inlets | Pinched section | Broad section | Outlets |
|--------|-----------------|---------------|---------|
| Particle stream + buffer stream | One narrow channel | Wide channel for separation | Small-particle outlet, large-particle outlet, buffer outlet |

The buffer runs faster and squashes the particle stream to one wall before the channel widens. In the broad part, particles stay on the streamlines they got in the pinch, so small and large ones end up at different positions across the channel and can be sent to different outlets.

### Where particles end up in the broad channel

I estimated a particle's position across the channel from the pinch width, broad width, and particle diameter:

**Relationship:** `Y_0 = (w_p - D/2) × (w_b / w_p)`

| Symbol | Meaning |
|--------|--------|
| Y_0 | Position across the broad channel |
| w_p | Width of the pinched section |
| w_b | Width of the broad channel |
| D | Particle diameter |

Bigger particles (larger D) have their centers farther from the wall and land on streamlines farther out; smaller ones stay closer. I placed the outlets to line up with these positions for the two size ranges we had: 125–150 μm and 425–500 μm.

## Design calculations

### Pinch section width

I sized the pinch so the largest particles (up to 500 μm) wouldn't clog. The rule of thumb is pinch width about 1.2 to 1.5 times the largest particle diameter.

| Largest particle | Factor | Pinch width w_p |
|-----------------|--------|-----------------|
| 500 μm | 1.3× | 1.3 × 500 μm ≈ 650 μm |

So I set the pinched section to about 0.65 mm wide.

### Broad section length

The broad section has to be long enough for the streamlines to separate. Guidelines said at least around 15 mm; I used about 33–34 mm so the separation was stable before the outlets.

### Outlet placement

| Outlet | Role |
|--------|------|
| Small-particle outlet | Catches 125–150 μm particles (closer to the wall). |
| Large-particle outlet | Catches 425–500 μm particles (farther from the wall). |
| Buffer outlet | Downstream; collects the particle-free part of the flow. |

## Flow balancing

If one outlet has much higher flow resistance than the others, flow that should go there will go to the neighbors instead and the particle streams will mix. So the three outlets need balanced hydraulic resistance so each carries the right share of flow.

What I did: I made the two particle outlet channels longer and a bit narrower so their resistance is higher and they don't steal too much flow from the buffer outlet. I kept the buffer outlet shorter so it can take the larger fraction of flow. That kept the flow split closer to what the streamlines predict and cut down cross-talk between outlets.

## Fabrication

| Step | What I did |
|------|------------|
| 1 | Designed the microfluidic mold in Autodesk Fusion. |
| 2 | Exported and prepared the model in PreForm for SLA. |
| 3 | Printed the mold on the Form 3+/4 resin printer. |
| 4 | Washed the mold in IPA (FormWash). |
| 5 | Cured the mold (about 60 s). |
| 6 | Removed supports and cleaned the mold. |
| 7 | Mixed PDMS 10:1 and poured over the mold. |
| 8 | Cured PDMS and peeled it off the mold. |
| 9 | Plasma-treated PDMS and glass slide. |
| 10 | Bonded PDMS to the glass slide to seal the channels. |

## Why resin printing for the mold

Resin printing provides the resolution and smooth channel surfaces needed for small features and predictable flow. Compared to machining or FDM, it was the right choice for prototyping this geometry.

## Scaling and limits

I could change the pinch width and outlet positions for different particle size ranges, or add more outlets to sort into more size bins. The smallest particles I could separate are limited by channel roughness, diffusion, and the printer's minimum feature size; below that, streamlines get messy and separation isn't reliable.

## Possible improvements

Tuning outlet widths for better resistance balance, adjusting outlet angles to cut recirculation, and trying asymmetric layouts or different flow-rate ratios are all things I'd try next.

## Drawing (GitHub Entry: Pinch Flow Fractionation Device)

| Drawing | Link |
|--------|------|
| 50×75 Base Model (v1) | [PDF](/assets/img/fluids/50x75-Base-Model%20Drawing%20v1.pdf) |

---
# fab_projects.yml entry to restore (add under the other entries):
# - title: "Pinch Flow Fractionation Device"
#   excerpt: "Resin-printed microfluidic mold for particle separation by size; PFF device design and PDMS casting."
#   image_path: /assets/img/fluids/teaser.jpg
#   url: /portfolio/PinchFlowFractionation/
#   btn_label: "View Project"
