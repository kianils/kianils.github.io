---
title: "Multi-Material Plier Print"
layout: single
classes: wide
excerpt: "Multi-material 3D-printed functional pliers with dovetail join and TPU buffer."
header:
  teaser: /assets/img/pliers/final.jpg
---

## Project Overview

This project explores multi-material 3D printing for functional pliers. The pliers combine rigid PLA/PETG handles and jaws with a flexible TPU buffer that acts as a print-in-place element—printed as part of the same build without separate assembly. The design was iterated twice to handle deformation under load, improve modularity, and integrate that buffer for reliable grip and release.

**Print-in-place** means parts that move relative to each other are fabricated in one print job, with no post-print assembly. The flexible buffer in this project is a print-in-place component: it is printed between the rigid pieces and provides the return force that opens the jaws. Multi-material printers (e.g., dual-extrusion) can switch between rigid and flexible filaments in the same layer, so hinges, buffers, and similar elements can be integrated directly.

Print-in-place has been used in many other applications. [InstaGrasp](https://arxiv.org/abs/2305.17029) is an entirely 3D-printed adaptive robotic gripper using PLA and TPU, with printed tendons, flexure joints, and finger pads—assembly in under 10 minutes. [Printegrated Circuits](https://arxiv.org/html/2509.08459v1) embed PCBs into 3D prints and create electrical connections through the printing process. [4D-printed deployable stents](https://www.nature.com/articles/s43246-021-00165-8) use print-in-place reconfigurable structures that change shape when activated. These examples show that print-in-place is valuable wherever integrated, low-assembly functional objects are needed.

**What I learned from this assignment:** (1) **Material must drive iteration.** Early on I did not account for TPU in the design. The buffer needs to flex; rigid geometry and rigid assumptions led to failure. Iterating with material behavior in mind—how TPU deforms, where stress concentrates—fixed the design. (2) **Diagnose at the source, one issue at a time.** When the buffer was too stiff, I could have tweaked several things at once. Instead I traced it to base layers in the slicer, fixed that, then addressed fillets, then angles. Fixing one root cause before moving on kept the process clear and avoidable mistakes to a minimum.

---

## Iteration One: Plier Base Design

The first iteration defined the core body and jaw geometry. It was modeled as a single, rigid assembly. At this stage I did not yet account for how the material would deform when gripping objects, or how to make the design modular for easier printing and assembly.

<img src="/assets/img/pliers/iteration-1-pliers.png" alt="Iteration 1 pliers" style="width:100%; max-width:800px;"/>

---

## Iteration Two: Dovetail Join and Deformation Buffer

The second iteration addressed the main gaps in the first design.

**Dovetail join** — I switched to a dovetail joint to connect the handle and jaw components. This gives a strong mechanical connection without fasteners and makes parts easy to swap or reprint.

**Buffer for 3D printing** — The buffer is the part that returns the jaws to an open position. I redesigned it specifically for 3D printing and for deformation: it is meant to be printed in TPU so it can flex and absorb strain instead of cracking. The geometry was sized so the flexible buffer would allow the pliers to grip and release reliably over many cycles.

---

## CAD Models

### Iteration One

<iframe src="https://a360.co/4aCrW6i?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4aCrW6i">View CAD Model</a></p>
</iframe>

### Iteration Two

<iframe src="https://a360.co/40bFa5d?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/40bFa5d">View CAD Model</a></p>
</iframe>

---

## Errors and Lessons Learned

1. **TPU oversight** — The first design did not consider flexible materials. The buffer needs TPU to function correctly.

2. **Base layers** — I forgot to turn off base layers in the slicer. The buffer printed solid and was too stiff to move.

3. **Fillets** — I added fillets to reduce stress concentrations and slow degradation from repeated flexing.

<img src="/assets/img/pliers/b4fillet.jpg" alt="Buffer before fillets" style="width:100%; max-width:800px;"/>

4. **Angles** — I adjusted the angles so the handles and jaws return to position more consistently after each squeeze.

---

## Final Assembly

<img src="/assets/img/pliers/final.jpg" alt="Final prototype" style="width:100%; max-width:800px;"/>
