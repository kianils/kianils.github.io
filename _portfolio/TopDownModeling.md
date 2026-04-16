---
title: "Top-Down Modeled Handlebar Phone Mount"
layout: single
classes: wide
excerpt: "Fusion 360 top-down design: handlebar clamps, detent rotation, modular cover, and phone grip; FFF structure plus resin for fine phone-holder features."
header:
  teaser: /assets/img/detent/detentviews/detent.jpg
---

## Project Overview

This assignment uses **top-down modeling** in **Autodesk Fusion 360** to design a **phone holder** that mounts to a bicycle **handlebar**. The assembly includes a **clamp system**, a **rotating detent** mechanism, a **modular cover** with an access opening, and a **phone grip**.

---

## Top-Down Modeling

This assignment used a **top-down modeling** approach, which allowed me to build the design **around the handlebar**. By setting the handlebar as the **base geometry**, I was able to **iterate** more effectively and keep **accurate alignment** between components, including the **clamp system** and **heat-set inserts**.

---

## Design Process

The design process began with the **clamp mechanism** and making sure it **fit the handlebar**. I then designed a **rotating** interface. I initially explored a **ball-and-socket joint**, but after further consideration and feedback, I moved to a **detent mechanism** based on **class recommendations** and reference to **Solomon’s model**. I refined that design until the detent **worked in CAD and in test prints**.

After that, my professor suggested making the design **more modular** and adding a **cover** with an **access hole** for the **rotation / turning** feature. I implemented those changes and integrated the **phone grip** into the final assembly.

---

## Implementation of the Detent Mechanism

I started with a **simplified prototype** to learn the **geometry and motion** of the detent. After testing and refining that **smaller model**, I **scaled** the idea and **integrated** it into the full clamp and housing so the mechanism sits **inside a single structural flow** where possible, which helped **stability**, **assembly**, and part count.

**Micro detent (first prototype)** — first detent test before full integration.

![Micro detent prototype (first print)](/assets/img/detent/microdetent/microdetent.jpg)

Micro detent drawing: [PDF](/assets/img/detent/micro-detent.pdf)

---

## Design for 3D Printing

### Did you have to change any dimensions to account for 3D printing?

No **large** dimensional changes were driven only by **shrinkage tables**. The main iteration was **modularity**: splitting **cover**, **base**, and **grip** for better **orientation**, **supports**, and **assembly**, plus refining how the **detent** interfaced with the housing.

### Which printing technology—and why—for each part?

| Part / group | Process | Why |
|--------------|---------|-----|
| **Clamp body**, **detent housing**, **modular cover**, **structural brackets** | **FFF** (filament) | Larger, structural pieces; fast iteration on fit to the bar and on the detent before locking the full assembly. |
| **Phone holder / grip** (fine features, threads if modeled) | **Resin (SLA)** | Better **detail** and **surface finish** for **threads** and small **interfaces** that would be rough or unreliable in a single FFF pass. |

---

## Assembly Instructions

1. Print all **FFF** and **resin** parts; remove supports and clean **detent** and **sliding** surfaces. **Wash and cure** resin parts before assembly.
2. Install **heat-set inserts** where designed (clamp / detent region); align screw bosses before final torque.
3. Assemble the **detent** stack; confirm **rotation** and **locking** before fully tightening. **Clamp** to the handlebar **evenly** so the mount does not tilt or stress the bar.
4. Install the **cover**; confirm the **access hole** lines up with the **turning** feature. Mount the **phone** in the grip and check **full range of rotation**.

---

## CAD Models (Fusion 360)

### Phone holder

[Open in Fusion 360](https://a360.co/4cu0Fnw)

<iframe src="https://a360.co/4cu0Fnw?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4cu0Fnw">View CAD model</a></p>
</iframe>

![Phone holder component](/assets/img/detent/individual-parts/phoneholder.jpg)

### C-clamp with cover

[Open in Fusion 360](https://a360.co/3Q4vSX9)

<iframe src="https://a360.co/3Q4vSX9?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/3Q4vSX9">View CAD model</a></p>
</iframe>

![Clamp with cover component](/assets/img/detent/individual-parts/clamp-cover.jpg)

### Detent

[Open in Fusion 360](https://a360.co/3QepVa3)

<iframe src="https://a360.co/3QepVa3?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/3QepVa3">View CAD model</a></p>
</iframe>

![Detent component](/assets/img/detent/individual-parts/detent.jpg)

### Detent cover

[Open in Fusion 360](https://a360.co/4vwIshV)

<iframe src="https://a360.co/4vwIshV?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4vwIshV">View CAD model</a></p>
</iframe>

![Cover component](/assets/img/detent/individual-parts/cover.jpg)

### Base clamp

[Open in Fusion 360](https://a360.co/4ceGTxz)

<iframe src="https://a360.co/4ceGTxz?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/4ceGTxz">View CAD model</a></p>
</iframe>

![Base clamp component](/assets/img/detent/individual-parts/clamp.jpg)

---

## Detent Views (`assets/img/detent/detentviews/`)

### Overall detent assembly view

![Detent assembly view](/assets/img/detent/detentviews/detent.jpg)

### Detent with cover

![Detent with cover](/assets/img/detent/detentviews/detent-with-cover.jpg)

### Cross-section view (internal mechanism)

![Internal detent cross section](/assets/img/detent/detentviews/internaldetent.jpg)

---

## Real-Life Photos on Bike Handlebars

Add your in-use handlebar photos in this section as soon as they are exported into `assets/img/detent/`.

![Mount in use on handlebars - photo 1](/assets/img/detent/handlebar-in-use-1.jpg)

![Mount in use on handlebars - photo 2](/assets/img/detent/handlebar-in-use-2.jpg)

## GIF, Render, and Extra Figures

![Rotation GIF (landscape to portrait)](/assets/img/detent/rotation-landscape-portrait.gif)

![Fusion render with phone](/assets/img/detent/render-phone-holder-with-phone.jpg)

---
