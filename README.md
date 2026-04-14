# Why Does the Periodic Table Have a Maximum?

> *"The universe has opinions about its own periodic table, and they're fairly non-negotiable."*

This repository explores the fundamental physics question: **why can't we just keep adding protons to atoms?**

What starts as a simple chemistry question unravels into some of the most profound physics at the edge of human knowledge — nuclear stability limits, the island of stability, ultra-dense matter, fusion ignition, quark-gluon plasma, and the point where spacetime itself refuses to cooperate.

---

## The Question That Started It All

When you look at the periodic table, it ends. Currently at element 118 (Oganesson). But *why*?

- Can't we just add more protons?
- What if we add more neutrons to stabilize?
- What if we balance the charge with more electrons?
- How does this connect to fusion research and attempts to create ultra-dense matter?

These questions, asked in sequence, lead somewhere surprising.

---

## Threads Being Explored

### 🔬 Thread 1: Nuclear Stability Limits
*The Bethe-Weizsäcker semi-empirical mass formula and why Coulomb repulsion always wins eventually*

→ [`research/01-nuclear-stability/`](research/01-nuclear-stability/)

### ⚛️ Thread 2: The Island of Stability
*Theoretical superheavy nuclei around Z=120, N=184 — magic numbers and predicted half-lives*

→ [`research/02-island-of-stability/`](research/02-island-of-stability/)

### 🌊 Thread 3: Fusion Ignition & Cascading Reactions
*How inertial confinement fusion uses exactly the cascade-density mechanism — and where it hits its ceiling*

→ [`research/03-fusion-cascades/`](research/03-fusion-cascades/)

### 💫 Thread 4: Ultra-Dense Matter & Quark-Gluon Plasma
*From neutron star densities to CERN's QGP experiments — what happens when you compress matter past nuclear density*

→ [`research/04-ultra-dense-matter/`](research/04-ultra-dense-matter/)

### ⚡ Thread 5: The Feynman Limit & QED Breakdown
*Why Z=137 is special, how relativistic electrons constrain atomic structure, and the vacuum instability at Z≈172*

→ [`research/05-qed-limits/`](research/05-qed-limits/)

### 🕳️ Thread 6: Artificial Black Holes & Lab-Scale Gravity
*What it would actually take, current CERN constraints, Hawking radiation at micro scales*

→ [`research/06-artificial-black-holes/`](research/06-artificial-black-holes/)

---

## How to Navigate This Repo

Each research thread contains:
- `notes.md` — Key findings, equations, and analysis
- `calculations.py` — Numerical explorations (Python, runnable)
- `references.md` — Papers, sources, and further reading

The [`report/`](report/) folder contains the synthesized final report across all threads.

---

## Origin

This research emerged from a conversation exploring what stops us from adding more protons to atoms — and whether cascading electron/neutron reactions at increasing density connect to fusion research and artificial black holes.

The short answer: yes, they're deeply connected. The long answer is this repository.

---

## Running the Calculations

```bash
pip install numpy matplotlib scipy
python research/01-nuclear-stability/calculations.py
python research/03-fusion-cascades/calculations.py
```

---

*Research conducted April 2026. All calculations are theoretical/educational.*
