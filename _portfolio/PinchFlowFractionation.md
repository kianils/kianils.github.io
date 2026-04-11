---
title: "Pinch Flow Fractionation Device (μFluidic Device)"
layout: single
classes: wide
excerpt: "Resin-printed microfluidic mold for particle separation by size using pinch flow fractionation; CHBE 4200."
header:
  teaser: /assets/img/fluids/teaser.jpg
---

## Introduction

### What is pinch flow fractionation (PFF), and how does it work?

**Pinch flow fractionation** is a technique in microfluidics to sort different particles by size inside a small fluid channel. In this technique, you bring two streams together in a **narrow pinch**. One stream will be our sample while the other which will have a faster flow rate would be the buffer.  The buffer pushes the particles against **one wall** which prevents bigger or smaller particles from joining the same paths in the flow. When the channel **opens up** downstream, those paths **split apart**, so you can collect different sizes at **different outlets**.

### Application and why PFF beats filters for that case

**Application:** The goal is to separate a mixture by particle size. A **mesh filter** works like a sieve where liquids can passes through, and **particles that are too large get stuck on the mesh**. That buildup is **why** filters **clog**, and our fluids slow down, and need cleaning or replacement for the sieve. The separation method is literally **blocking** material. **PFF beats filters in this case because it does not separate by blocking:** there is **no mesh** in the flow path, so **nothing accumulates on a screen**. Instead, **smooth, layered flow** carries each size along a **different path** so they exit at **different outlets**. Reference- ([*Microfluidics and Nanofluidics*, 2009](https://doi.org/10.1007/s10404-008-0319-0)).

## Design

### Symmetric or asymmetric approach?

I chose an **asymmetric** approach. The chip still follows the standard PFF flow path (sample + buffer inlet, pinch region, then broad channel), but the three outlets are not symmetric. I used **different outlet widths and lengths** on purpose so I could **tune resistance** per branch and match where the **small (about 125-150 um)**, **large (about 425-500 um)**, and **buffer** streams sit across the channel. A fully symmetric outlet layout looks clean, but in this case it is harder to **balance flow** and keep each outlet aligned with its target stream band.

### Where I put the outlet boundaries (small, large, buffer)
I used **Y_0 = (w_p - D/2) x (w_b / w_p)** to place the outlet boundaries. This predicts the ordering across the channel: **small particles travel closer to the wall**, and **large particles travel farther out**. The outlets were set so each branch taps the right region. The **small** outlet collects the wall-side band, the **large** outlet collects the mid-to-outer band, and the **buffer** outlet collects mostly clean fluid once the particle-rich streamlines have separated.

### Flow balancing (the problem from the start of the project)

I approached this through **iteration** mostly rather than getting it right the first time. As a CS student, this part was honestly pretty challenging because I am not used to thinking about fluid flow and pressure drops and I had never used any of the equations or worked with resistance. At first, I adjusted outlet widths and lengths mostly by intuition, but small changes would significantly affect how the flow split, and it was not very predictable. I also realized that making the outlets look symmetric or evenly spaced did not actually give balanced flow which is why I switched to implementing an asymmetric design.

When I couldn't get by with intuition, I used the **Y_0** flow-position equation to determine the range to keep outlet boundaries aligned with where each particle band should be. I then tuned branch resistance directly in the outlet design. I made the **smaller** particles outlet **longer and narrower** while the **buffer** outlet was kept **shorter** so it could carry more of the buffer-like flow without pulling particle bands off target.

### If I could change the outlets in a second version
If I could iterate on this design again, I would try a **more symmetric-looking outlet layout** while still keeping the resistance tuned per branch. Since I was not able to fully test this version, my best estimate from inspection is that the outlet junctions should be **more pronounced** so each stream band is captured more cleanly. I would also improve the **buffer outlet section** to better carry clean buffer flow without pulling particles across the boundary.

## Instructions

1. **Design the channel network in Fusion**  
   Design Microfluidics device on fusion then export the mold geometry for SLA printing.

2. **Set up the print in PreForm**  
   Import the model on preform, set up, and run on the correct formlabs printer

3. **Print and wash the mold**  
   After printing, run the mold in IPA for **5 minutes**, then run a **second 5-minute wash**. If IPA pools inside channels, leave the part **upside down for ~30 minutes** so trapped solvent drains out.

4. **Clean uncured resin from channel features**  
   Carefully remove any remaining uncured resin (without damaging channel edges), wipe gently as needed, and use **compressed air** (with safety glasses) to clear debris from channels.

5. **Curing procedure**  
   Do a short **surface cure (~60 s)** while supports are still attached, then remove supports and inspect the mold. The channel surfaces should look clean/glossy with no blocked regions.


## Multimedia

**Device photo**

![Microfluidic device photo](/assets/img/fluids/pinch-flow-device.jpg)

**Demo video**

<iframe width="100%" height="400" style="max-width:720px; border-radius:8px;" src="https://www.youtube.com/embed/ChUNb9b515A" title="Pinch flow fractionation device demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

[Watch on YouTube](https://youtu.be/ChUNb9b515A)



**Fusion 360 embed (mold)** — [Open in Fusion 360](https://a360.co/4snlirt)

<iframe src="https://a360.co/4snlirt?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4snlirt">View CAD model</a></p>
</iframe>

**Technical drawing (PDF)**

| Drawing | Link |
|--------|------|
| 50×75 Base Model (v1) | [PDF](/assets/img/fluids/50x75-Base-Model%20Drawing%20v1.pdf) |

## Discussion

### Why resin printing instead of something else?

I chose resin (SLA) printing because it offers much higher resolution and smoother surface finish compared to FDM, which is critical for microfluidic channels. The smoother walls reduce flow disturbances and improve separation performance. It also allows for complex internal geometries and faster iteration compared to machining.

### Making the design work for other particle sizes

To scale this design up, I would first increase **outlet channel widths** so the device can handle higher fluid throughput without destabilizing the split. I would also retune flow rates and outlet resistance to keep separation stable at the larger scale. For wider particle-size ranges, I would consider doing separation in **multiple staged sections** instead of trying to split everything through one buffer interaction in a single pass.

### How small can the particles be?

The lower limit is set by **Brownian diffusion**  which causes them to wander across streamlines, which weakens size-based separation. At the same time, channel **surface roughness** and finite **print resolution** become large relative to particle size, so the effective flow profile is less ideal.

## References

- Takagi, M., et al. Continuum particle separation by pinch flow fractionation. *Microfluidics and Nanofluidics* **2009**. [https://doi.org/10.1007/s10404-008-0319-0](https://doi.org/10.1007/s10404-008-0319-0)



