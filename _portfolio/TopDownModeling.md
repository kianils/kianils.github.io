---
title: "Top-Down Modeled Handlebar Phone Mount"
layout: single
classes: wide
excerpt: "Fusion 360 top-down design: handlebar clamps, detent rotation, modular cover, and phone grip; FFF structure plus resin for fine phone-holder features."
header:
  teaser: /assets/img/detent/teaser.jpg
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

**Micro detent (first prototype)** — photo below; technical drawing exported as PDF.

![Micro detent prototype (first print)](/assets/img/detent/micro-detent-prototype.jpg)

| Document | Link |
|----------|------|
| Micro detent drawing / export | [PDF](/assets/img/detent/micro-detent.pdf) |

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

## CAD Model (Fusion 360)

[Open in Fusion 360](https://a360.co/41BAzdw)

<iframe src="https://a360.co/41BAzdw?mode=embed" width="100%" height="600px" frameborder="0" allowfullscreen webkitallowfullscreen mozallowfullscreen>
  <p>Your browser does not support embedded CAD models. <a href="https://a360.co/41BAzdw">View CAD model</a></p>
</iframe>

---

## Figures (`assets/img/detent/`)

Add or replace files using the names below so every required figure resolves on the site. *(Right now several paths are placeholders—you can copy your exports into these filenames.)*

### Real life on the handlebar

![Mount on handlebars (in use)](/assets/img/detent/handlebar-in-use-1.jpg)

![Mount on handlebars (alternate view)](/assets/img/detent/handlebar-in-use-2.jpg)

*Tip: overwrite `teaser.jpg` in this folder with your best **in-use** shot for the portfolio archive thumbnail.*

### Rotation: landscape ↔ portrait

![Animation: rotating between landscape and portrait](/assets/img/detent/rotation-landscape-portrait.gif)

### Fusion rendering: holder with phone

![Fusion render: phone holder with phone](/assets/img/detent/render-phone-holder-with-phone.jpg)

### Cross section: internal rotation / detent

![Cross section: rotation mechanism (Fusion section analysis)](/assets/img/detent/cross-section-rotation-mechanism.jpg)

### Individual top-down components (real photos or Fusion renders)

| Component | Image |
|-----------|--------|
| Clamp / bar interface | ![Clamp component](/assets/img/detent/component-clamp.jpg) |
| Detent / rotating core | ![Detent core](/assets/img/detent/component-detent-core.jpg) |
| Cover | ![Cover](/assets/img/detent/component-cover.jpg) |
| Phone grip / holder | ![Phone grip](/assets/img/detent/component-phone-grip.jpg) |
| Base / housing (if separate) | ![Base or housing](/assets/img/detent/component-base.jpg) |

*Add or remove rows to match how you split the top-down tree; keep filenames consistent so you do not have to edit this page again.*

---

## What I Learned

**Datum discipline matters.** Keeping the handlebar as the root reference aligned clamps, inserts, and rotation on one axis. **A small detent prototype** saved time before a full build. **Modularity** made printing and final assembly easier as the part count grew.
