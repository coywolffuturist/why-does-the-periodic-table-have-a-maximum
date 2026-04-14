# Research Task: Why Does the Periodic Table Have a Maximum?

You are a research agent conducting deep scientific exploration across 6 interconnected threads.
Work for approximately 3 hours. Be thorough. Commit frequently. Produce real calculations.

## Repository
/home/ubuntu/periodic-table-max
GitHub: https://github.com/coywolffuturist/why-does-the-periodic-table-have-a-maximum

## Git Setup (already configured)
Remote already set. Just `git add`, `git commit`, `git push` as you go.

---

## Your Mission

Research and produce substantive content across all 6 threads below.
Each thread should have:
1. `notes.md` — deep analysis, key equations, findings
2. `calculations.py` — working Python code with real numerical results
3. `references.md` — actual papers, Wikipedia articles, CERN/NIF/ITER sources

After all threads, produce `report/FINAL_REPORT.md` — a synthesized, well-structured report
that connects all threads and answers: "What stops us from adding more protons, and how does
a cascading dense reaction connect to fusion and artificial black holes?"

---

## Thread 1: Nuclear Stability Limits (`research/01-nuclear-stability/`)

Topics to cover:
- Bethe-Weizsäcker semi-empirical mass formula in full detail
- How each term (volume, surface, Coulomb, asymmetry, pairing) behaves with Z
- Calculate binding energy per nucleon for Z=1 to Z=130
- Find the optimal N/Z ratio as a function of Z
- Plot/tabulate where binding energy goes negative
- Why Coulomb repulsion scales as Z² while strong force saturates
- The concept of "fission barrier" and how it shrinks with Z
- Spontaneous fission limit (around Z~106 without magic numbers)

Key equations to implement:
```
B(Z,A) = aᵥA − aₛA^(2/3) − aC·Z²/A^(1/3) − aₐ(A−2Z)²/A ± δ
aᵥ=15.75, aₛ=17.8, aC=0.711, aₐ=23.7 MeV
```

---

## Thread 2: Island of Stability (`research/02-island-of-stability/`)

Topics to cover:
- Nuclear shell model — magic numbers (2,8,20,28,50,82,126,184)
- Why magic numbers create extra stability (filled shells)
- Predicted island around Z=114-126, N=184
- Current experimental status: elements 113-118 synthesized
- Half-life predictions for Z=120 (element 120), Z=126
- The role of deformed shell closures (Z=114 debate vs Z=120)
- Superheavy element synthesis methods (cold fusion vs hot fusion)
- GSI, RIKEN, JINR experimental programs
- What "doubly magic" Z=114, N=184 means
- Calculate predicted alpha-decay chains for Z=120

---

## Thread 3: Fusion Cascades (`research/03-fusion-cascades/`)

Topics to cover:
- Lawson criterion in full: n·τ·T ≥ 3×10²¹ keV·s/m³
- How inertial confinement fusion IS the cascading density reaction described
- NIF December 2022 ignition: numbers, what it means, what it doesn't
- Fuel compression ratios (ICF compresses D-T to ~1000× solid density)
- The "burn wave" propagation — exactly the cascade mechanism
- ITER design parameters and Q=10 target
- Private fusion: Commonwealth Fusion (SPARC), Helion, TAE Technologies
- The gap between fusion ignition and "useful cascade" for element synthesis
- Could a fusion cascade ever reach densities relevant to superheavy element formation?
- Calculate ignition conditions and compare to stellar core conditions

---

## Thread 4: Ultra-Dense Matter & QGP (`research/04-ultra-dense-matter/`)

Topics to cover:
- Nuclear density: ~2.3×10¹⁷ kg/m³ — what this means
- Neutron star structure: crust → outer core → inner core → (hypothetical) quark core
- Tolman-Oppenheimer-Volkoff equation (conceptual + simplified form)
- Quark-gluon plasma: what it is, when it exists (T > 150 MeV, ~10¹² K)
- CERN ALICE experiment: Pb+Pb collisions, QGP evidence
- The QCD phase diagram: temperature vs baryon chemical potential
- Color superconductivity at extreme densities
- Strange quark matter / strangelets hypothesis
- Could lab-created QGP ever be sustained? Current record durations.
- How neutron star mergers (GW170817) constrain the equation of state

---

## Thread 5: QED Limits & Feynman Limit (`research/05-qed-limits/`)

Topics to cover:
- Why Z=137 is special: α = e²/ℏc ≈ 1/137 (fine structure constant)
- Electron orbital velocity: v/c ≈ Z/137 for 1s electrons
- Dirac equation breakdown: for Z > 137, 1s energy becomes imaginary
- Extended Dirac with finite nuclear radius: limit pushed to Z≈173
- "Diving into the Dirac sea" — what vacuum decay means physically
- Spontaneous electron-positron pair production from vacuum at Z≥173
- Implications: the vacuum IS the limit, not just nuclear instability
- Relativistic effects already observable: gold's yellow color (Au Z=79), mercury liquid at room temp
- Calculate 1s binding energy as function of Z through relativistic correction
- The supercritical field threshold

---

## Thread 6: Artificial Black Holes (`research/06-artificial-black-holes/`)

Topics to cover:
- Schwarzschild radius: rₛ = 2GM/c² — calculate for various masses
- What it would take to form a micro black hole in a lab
- LHC safety review: why micro BHs, if formed, are harmless
- Hawking radiation: T = ℏc³/(8πGMkB) — calculate for micro BHs
- ADD model (extra dimensions) and why it predicted LHC micro BHs (that didn't appear)
- What the non-detection tells us about extra dimensions
- Cosmic ray argument: Earth has been bombarded by far more energetic particles
- The gap between current lab energies and gravitational collapse energies (orders of magnitude)
- Analog black holes: acoustic black holes (dumb holes), optical analogs
- Hawking radiation experimentally detected in analog systems (2019 Steinhauer)
- What "artificial black hole" research actually means today vs sci-fi version

---

## Final Report (`report/FINAL_REPORT.md`)

Structure:
1. Executive Summary (the answer in 300 words)
2. The Core Physics: Why the Periodic Table Ends
3. Thread Summaries with Key Numbers
4. The Connection: Cascading Dense Reactions → Fusion → Dense Matter → Black Holes
5. What's Possible vs What's Not (honest frontier table)
6. Open Questions & Future Research Directions
7. Appendix: Key Equations Reference

---

## Commit Strategy
- Commit after each thread is complete
- Final commit: "Complete: all 6 threads + final report"
- Push to GitHub after every commit

## Notification
When completely finished with all threads and the final report, run:
clawdbot gateway wake --text "Research complete: periodic table limits repo. All 6 threads + final report pushed to GitHub." --mode now

