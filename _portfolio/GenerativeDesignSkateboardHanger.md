---
title: "Generative Design of an Electric Skateboard Truck Hanger"
layout: single
classes: wide
excerpt: "Fusion 360 generative design workflow for a Paris V2 electric longboard hanger with integrated motor mount, five loads, and AlSi10Mg optimization."
---

## Project Overview

In this project, I used **Fusion 360 Generative Design** to redesign a **Paris V2 truck hanger** for my electric longboard. I wanted to **combine** the hanger and motor mount into one lighter part while still meeting a minimum **safety factor of 2.0**.

The setup uses a **Flipsky 6374** belt-drive system (36T wheel pulley, 18T motor pulley). I planned to print and test the final part, but I was **unable to print the design** in time, so I am submitting this as a **partial-credit generative design result**.

- Original generated design [https://a360.co/4eThAmj](https://a360.co/4eThAmj)
- Second version model [https://a360.co/4vUDfRc](https://a360.co/4vUDfRc)

---

## Generative Design Setup

I used preserve regions on the axle interfaces, pivot region, kingpin/bushing region, and motor plate so GD would keep the functional geometry. I also used obstacle bodies for both wheels, motor body, and pulleys to protect assembly clearances. The belt body itself was not included as an obstacle because Fusion would not let me select that linked body directly.

### Starting Shape

I used a **350 x 250 x 150 mm** bounding box (`StartingShape_Hanger`) as the starting shape, enclosing all preserves.

### Final Outcome

| Property | Value |
|---|---|
| Material | AlSi10Mg aluminum |
| Mass | 0.207 kg (207 g) |
| Mass reduction vs. commercial hanger | ~25% (commercial hanger ~250-300 g) |
| Minimum safety factor | 2.012 |
| Maximum von Mises stress | 119.3 MPa |
| Maximum displacement | 1.117 mm |
| Volume | 77,488 mm^3 |
| Iterations to convergence | 34 |
| Status | Converged |

For comparison, I also generated a 17-4 PH stainless result (3.332 kg, safety factor 24.07).

---

## Load Cases

A total of **5 structural loads** were applied. This satisfies the assignment minimum and captures the key real-use loading cases.

| # | Load Name | Magnitude | Direction | Target Face(s) | Physical Justification |
|---|---|---|---|---|---|
| 1 | Rider vertical weight | 1500 N | -Z | Both axle preserves | 100 kg rider with 1.5x dynamic amplification for terrain irregularities |
| 2 | Lateral carving force | 500 N | +Y | Both axle preserves | Cornering load at 10-15 mph with lateral rider weight transfer |
| 3 | Braking deceleration | 800 N | +X | Both axle preserves | Inertial reaction under hard braking or regenerative braking |
| 4 | Curb impact (asymmetric) | 2500 N | -Z | Left axle preserve only | Single-wheel curb strike introducing asymmetric torsional loading |
| 5 | Belt tension reaction | 200 N | +X | Motor plate shaft hole (inner cylindrical face) | Reaction force at motor shaft from belt-driven propulsion |

### Structural Constraints

I fixed two regions.

1. Pivot interface on the curved surface of `Preserve_Pivot` where the pivot ball seats in the pivot cup.
2. Kingpin and bushing region on the top and bottom flat faces of `Preserve_Kingpin_Region` for the clamping load path.

The **axles and motor plate were intentionally left unconstrained** so they could react loads more realistically.

---

## Lessons Learned

### First Study (Successful Submission)

The first study produced the converged **207 g AlSi10Mg** result. What worked was keeping preserves localized to key interfaces, checking interferences early, and making sure the starting shape enclosed everything before solve. I rebuilt the second study using the same logic, but I still could not fully figure out why the behavior changed so much between files until the final connectivity error appeared.

### Second Study (Setup Completed, Solve Failed at Generation)

In `Paris-V2 v2`, setup looked clean with preserves, obstacles, loads, and constraints all in place and no overlap warnings, but generation failed with **"Cannot solve. The starting shape body must be in contact with all preserve geometry bodies."** The issue was that the motor plate preserve was not physically touching the starting shape volume. With more time, I would fix this by adding connector geometry or using one fully connected starting volume that includes both hanger and motor plate regions.

---

## Material Comparison AlSi10Mg vs 17-4 PH

| Property | AlSi10Mg (selected) | 17-4 PH stainless |
|---|---|---|
| Density | 2.67 g/cm^3 | 7.80 g/cm^3 |
| Yield strength (typical additive values) | ~240 MPa | ~1100 MPa (H900 condition) |
| Final part mass | 0.207 kg | 3.332 kg |
| Minimum safety factor | 2.012 | 24.07 |
| Relative print cost | Lower | Higher |
| As-printed finish | Rougher, requires post-processing | Smoother |

I selected **AlSi10Mg** because it still meets SF >= 2 with much lower mass, lower expected print cost, and better handling response from reduced unsprung mass. The 17-4 PH outcome is structurally strong but heavily over-designed for this target.

---

## Commercial Generative Design Example

A widely cited GD case is the **General Motors seat bracket** developed with Autodesk. The redesign consolidated eight conventionally manufactured parts into one printed part, with lower mass and improved structural performance. This shows GD can do more than lightweighting and it can also reduce part count and assembly complexity.

---

## Critique of Generative Design Workflow

Generative design was really useful for cutting mass while still meeting the safety-factor target, and it helped me evaluate different materials quickly under the same load cases. At the same time, the setup is very sensitive, and small geometry or connectivity issues can stop the solver even when the model looks correct. I also found the process a bit black-box, since it is not always obvious why one setup converges and a similar one fails. In practice, I see GD as a strong design exploration tool, but it still needs manual review and engineering judgment before final manufacturing decisions.

---

## Project Visuals

**Original generated design**

![Original generated design]({{ '/assets/img/generative-design/generative-design-generated/Screenshot%202026-05-01%20at%202.04.16%E2%80%AFPM.png' | relative_url }})

**Second version**

![Second version model]({{ '/assets/img/generative-design/second-version-load/Screenshot%202026-05-01%20at%202.02.56%E2%80%AFPM.png' | relative_url }})

---

## Project Files

### Fusion Files

- Original generated design (Fusion 360) [https://a360.co/4eThAmj](https://a360.co/4eThAmj)
- Second version model (Fusion 360) [https://a360.co/4vUDfRc](https://a360.co/4vUDfRc)

### PDF

- [Discussion PDF]({{ '/assets/files/discussion.pdf' | relative_url }})

### Other Assets

- `gifs/turning.gif` hanger rotation about kingpin axis
- `gifs/motor_rotation.gif` motor and pulley rotation view
- `renders/longboard_full.png` full longboard render with GD trucks
- `prints/print_photos/` photos of SLS-printed hanger
