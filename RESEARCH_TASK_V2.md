# Research Task V2: Periodic Table Limits — Full Systems Analysis
# Priority: HIGHEST | Duration: ~3 hours | Commit frequently

## Core Research Frame

This is NOT a literature review. This is a **systems engineering analysis** of limit conditions.

The central question: **Can a cascading dense reaction (electrons + neutrons, increasing density)
be engineered to overcome nuclear stability limits — and if so, where are the leverage points?**

Work methodically. Start from limit conditions. Work inward to activation energies.
Find every edge case. Flag unusual reagents. Look for step-function efficiency gains.

---

## PHASE 0: Master Limit Condition Map (`research/00-limit-conditions/`)

Before any thread, produce `research/00-limit-conditions/MASTER_MAP.md`:

A structured table of ALL limit conditions in the system, ordered from outermost (observable)
to innermost (fundamental). For each:

| Limit | Scale | Value | Governing Equation | Rate-Limiting Step | Leverage Point? |
|-------|-------|-------|-------------------|-------------------|-----------------|
| Spontaneous fission | Nuclear | Z > ~106 | Fission barrier height | Coulomb vs surface energy | Shell closures |
| ... | ... | ... | ... | ... | ... |

Include at minimum:
1. Spontaneous fission barrier collapse
2. Alpha decay chain stability
3. Optimal N/Z ratio ceiling
4. Neutron drip line
5. Proton drip line
6. Nuclear deformation / shape isomers
7. Fission isomers
8. Giant dipole resonances
9. Electron orbital relativistic limit (Z/137)
10. Vacuum polarization onset
11. Supercritical field / vacuum decay (Z~172)
12. QCD confinement pressure
13. Neutron degeneracy pressure
14. Quark degeneracy pressure
15. Schwarzschild radius / gravitational collapse
16. **CHARGE VACUUM CONDITIONS** (see Thread 7 below)

For each limit: what is the activation energy? What is the rate equation? What breaks first?

Also produce `research/00-limit-conditions/RELATED_RATES.md`:
A systems analysis of how rates at different scales couple. When you change one variable,
what does it do to every other rate? Build a dependency graph. Identify:
- Which rates are independent vs coupled
- Where positive feedback loops exist
- Where negative feedback (stabilizing) loops exist
- Where a small perturbation causes a discontinuous jump (step function)

---

## PHASE 1: Nuclear Stability — Materials Science Focus (`research/01-nuclear-stability/`)

### Existing notes.md — EXTEND with:

**Materials Science of Nuclear Matter:**
- Nuclear matter as a material: equation of state, compressibility, phase transitions
- Neutron-rich matter vs proton-rich matter — different material properties
- Nuclear pasta phases (in neutron star crusts): rods, slabs, tubes, bubbles
  - At what density do these form? What are their mechanical properties?
  - Can any analog be created in lab conditions?
- Skyrme interaction models: how nuclear matter behaves under compression
- The liquid-gas phase transition in nuclear matter (T ~ 10-20 MeV)

**Fission Barrier as Materials Property:**
- Fission barrier height as function of Z and A (calculate for Z=100 to Z=130)
- How shell corrections modify the liquid-drop barrier
- Fission barrier for superheavy elements: inner vs outer barrier
- Spontaneous fission half-life formula: `log(t₁/₂) ∝ a/√Eᵦ`
- Find the Z where fission barrier → 0 (no barrier = instant fission)

**calculations.py** — add:
- Full SEMF with shell corrections (Strutinsky method approximation)
- Fission barrier height as function of Z
- Phase diagram of nuclear matter (schematic, T vs density)
- Nuclear compressibility modulus K ~ 240 MeV

---

## PHASE 2: Island of Stability — Engineering Approach (`research/02-island-of-stability/`)

**Beyond standard notes — focus on:**

**Synthesis Engineering:**
- What projectile + target combinations could reach Z=120, Z=122, Z=126?
- Cross-section estimates for hot vs cold fusion at superheavy Z
- The "survival probability" problem: even if you make it, does it survive long enough to detect?
- Required beam intensities, target thicknesses, detector geometries
- Why JINR (Dubna), GSI (Darmstadt), RIKEN have different capabilities

**Predicted Properties of Island Elements:**
- Electron configuration predictions for Z=119, 120, 121 (relativistic effects dominate)
- Predicted chemistry: Z=119 behaves like... what? (relativistic contraction of s orbitals)
- Predicted physical state at room temperature
- Would Z=126 (if stable enough) be a useful material? What are its predicted properties?

**Shell Model Deep Dive:**
- Spherical shell model magic numbers vs deformed shell closures
- Why Z=114 (Fl) was predicted as magic but seems not to be
- Current debate: is N=184 a good magic number? What about N=172?
- Relativistic mean-field models vs non-relativistic predictions — where do they diverge?

**The Leverage Point:**
- If magic numbers are the stability leverage, what OTHER shell closures might exist beyond N=184?
- Are there any predicted "second island" at higher Z?

---

## PHASE 3: Fusion Cascades — Rate Engineering (`research/03-fusion-cascades/`)

**Reframe as systems engineering problem:**

**The Cascade Rate Equations:**
Write out the full coupled rate equations for:
1. D-T fusion: reaction rate R = nD · nT · ⟨σv⟩DT
2. Burn wave propagation: dE/dt = R · Q - dE_loss/dt
3. Compression dynamics: ρ/ρ₀ as function of time during implosion
4. Alpha particle energy deposition as a function of plasma density
5. The "gain cliff" — why Q goes from <1 to >1 discontinuously near ignition

**NIF Numbers — Actual Analysis:**
- Dec 2022: 2.05 MJ in (laser) → 3.15 MJ out (fusion). Net gain = 1.54
- But wall-plug efficiency of NIF lasers: ~1%. So real gain vs electricity: ~0.01
- What needs to happen for wall-plug Q > 1? Work through the numbers.
- SPARC (Commonwealth Fusion): 20T magnet, Q > 2 target — what's different?

**Cascade → Dense Matter Connection:**
- At what compression ratio does D-T fusion plasma approach nuclear density?
- ICF peak compression: ~1000× solid density = ~2.3×10²⁰ kg/m³ (nuclear density: 2.3×10¹⁷)
- So ICF reaches ~0.1% of nuclear density. Gap is 3 orders of magnitude.
- What would it take to bridge that gap? Is there a plausible path?
- Could a staged cascade (fission trigger → fusion → further compression) get closer?

**Unusual Reagents / Edge Cases:**
- Muon-catalyzed fusion: muons replace electrons, shrink Bohr radius by 207×, enable fusion at room temperature
  - Why doesn't it scale? (muon sticking problem) — calculate the sticking fraction
  - What would it take to make it work? Any recent progress?
- Metallic hydrogen as fusion fuel/catalyst — pressures required, current synthesis status
- Spin-polarized fusion fuel: aligned nuclear spins increase cross-section by ~50% for some reactions
- Laser-induced nuclear reactions: can photonuclear reactions be used as cascade triggers?
- Heavy ion beams as compression drivers (alternative to lasers)
- **Antimatter-triggered fusion**: p̄ + nucleus → mesons + energy → compression wave. Analyzed by ICAN project.

---

## PHASE 4: Ultra-Dense Matter — Phase Transitions as Leverage (`research/04-ultra-dense-matter/`)

**Focus on phase transitions as discontinuous leverage points:**

**Nuclear → Quark Matter Transition:**
- At what density does nuclear matter transition to quark-gluon plasma? (~5-10× nuclear density)
- Is this transition first-order (discontinuous) or crossover?
- If first-order: there's a latent heat — energy stored/released discontinuously. This IS a step function.
- Strange quark matter hypothesis (Witten-Bodmer): could strange quark matter be the TRUE ground state?
  - If so: a seed of strange quark matter contacting normal matter would convert it (strangelet hypothesis)
  - Is this dangerous? (CERN safety reviews)
  - Is this a leverage point? Could you USE the conversion energy?

**Color Superconductivity:**
- At extreme density, quarks form Cooper pairs → color superconductor
- Different phases: 2SC, CFL (color-flavor locked), crystalline CFL
- Each phase has different properties — some conduct, some don't, some are superfluid
- Could any of these phases be metastable at lower densities?

**Neutron Star Merger Data (GW170817 + AT2017gfo):**
- What did the gravitational wave signal tell us about the nuclear EOS?
- Tidal deformability constraints: Λ < 800 for 1.4 M☉ neutron stars
- Radius constraints: R ~ 11-13 km
- Does the merger data support or rule out quark matter cores?

**Lab Analogs:**
- Ultracold Fermi gases as nuclear matter analogs (unitarity limit)
- BCS-BEC crossover in cold atoms: same physics as nuclear pairing
- Can desktop experiments tell us about nuclear matter?

---

## PHASE 5: QED Limits — The Charge Vacuum (`research/05-qed-limits/`)

### THIS IS THE KEY THREAD — RESEARCH EXTENSIVELY

**Proton Charge: What Is It, Really?**

Start from first principles:
- A proton's charge is not a point charge — it has a finite charge distribution
- Proton charge radius: rp = 0.8409 ± 0.0004 fm (2019 CODATA — the "proton radius puzzle")
- The charge distribution is described by the proton electromagnetic form factors F₁(q²), F₂(q²)
- At short distances, the charge is actually carried by quarks (2 up quarks + 1 down quark)
- Quark charge distribution: u quarks carry +2/3e, d quark carries -1/3e

**The Proton Radius Puzzle:**
- Muonic hydrogen measurements give rp = 0.84087 fm
- Electronic hydrogen measurements historically gave rp = 0.8775 fm
- The 4% discrepancy was resolved in 2019 but the deeper question remains:
  DOES CHARGE BEHAVE DIFFERENTLY AT DIFFERENT SCALES?

**Vacuum Polarization — This Is the "Charge Vacuum":**
- In QED, the vacuum is NOT empty. Virtual electron-positron pairs constantly pop in and out.
- A charge placed in vacuum POLARIZES it — virtual pairs align with the charge.
- This screening effect means the "bare" charge of a proton is actually INFINITE at a point.
- What we measure (e = 1.602×10⁻¹⁹ C) is the SCREENED charge at low energy.
- At higher energies (shorter distances), we see MORE of the bare charge → running coupling constant
- α(mZ) ≈ 1/128 vs α(0) ≈ 1/137 — the charge is measurably different at Z boson mass scale

**The Running Coupling Constant:**
```
α(Q²) = α(0) / (1 - (α(0)/3π) · ln(Q²/m²e))
```
Calculate α as function of energy scale from 0.511 MeV (electron mass) to 91.2 GeV (Z mass).

**Vacuum Polarization as Charge Displacement:**
- The virtual pairs BETWEEN two charges partially cancel the field
- This IS a form of "charge vacuum" — the charges act on the virtual medium, not directly on each other
- At the Schwinger limit (E = m²c³/eℏ ≈ 1.3×10¹⁸ V/m), the vacuum breaks down
- Above this field strength, pair production is spontaneous and exponential
- This is the QED equivalent of "dielectric breakdown"

**Vacuum as Dielectric:**
Treat the QED vacuum as a dielectric medium:
- Vacuum permittivity ε₀ = 8.854×10⁻¹² F/m
- QED correction to vacuum permittivity (Euler-Heisenberg effective Lagrangian)
- The vacuum has a nonlinear response at high fields
- Calculate: at what proton number Z does the field at the nuclear surface approach the Schwinger limit?
```
E_nuclear_surface ≈ Ze / (4πε₀ · r²_nucleus)
For r_nucleus ≈ 1.2 · A^(1/3) fm
```

**Supercritical Fields and Vacuum Decay:**
- For Z > Z_cr ≈ 172, the 1s electron energy dives below -mec²
- The vacuum becomes unstable: spontaneous e⁺e⁻ pair production
- The e⁻ is bound to the nucleus, the e⁺ is emitted as real radiation
- This is the vacuum DISCHARGING the nuclear charge — nature's own charge relief mechanism
- **Key question: Could this process be exploited BEFORE Z=172?**

**Quasi-Atoms and Charge Screening:**
- In U+U (Z+Z=184) collisions at GSI, quasi-atoms briefly form with Z_eff > 172
- Observed: enhanced positron emission consistent with vacuum decay
- Duration: ~10⁻²¹ seconds — but the effect is real
- **Leverage point: Could you SUSTAIN a supercritical field configuration?**

**Exotic Charge Displacement Mechanisms:**
Research each of these — find actual papers, current status, viability:

1. **Muonic atoms as charge concentrators**: Replace electrons with muons (207× heavier).
   Muon orbital radius: a_μ = a₀/207 ≈ 253 fm for hydrogen.
   For heavy atoms, muon 1s orbital overlaps significantly WITH THE NUCLEUS.
   This CHANGES the nuclear charge distribution seen by outer electrons.
   - Has this been used to probe nuclear structure? (YES — muonic X-ray spectroscopy)
   - Could a muonic atom with Z > 137 survive long enough to study vacuum decay?
   - What happens to the nuclear stability of a muonic heavy atom?

2. **Pionic atoms and hadronic atoms**: Replace electrons with pions (π⁻), kaons (K⁻), antiprotons (p̄).
   These are absorbed by the nucleus — but en route, they modify the charge distribution.
   - Kaonic atoms: K⁻ orbital overlaps nucleus, creates exotic nuclear states
   - Could a kaonic nucleus have DIFFERENT stability properties?

3. **Nuclear charge redistribution via shape oscillations:**
   - Nuclei are not spherical — they oscillate (Giant Dipole Resonance, quadrupole modes)
   - During oscillation, the charge distribution changes
   - Could resonant shape oscillations REDUCE the effective Coulomb repulsion during a reaction?

4. **Plasma screening in stellar environments:**
   - In stellar cores, free electrons partially screen nuclear charges
   - This INCREASES fusion reaction rates (Salpeter enhancement factor)
   - Enhancement: `exp(0.188 · Z₁Z₂ · (ρ/A)^(1/2) / T₆^(3/2))`
   - Could artificially dense electron plasmas enhance heavy element synthesis?

5. **Casimir-Polder effect as charge vacuum:**
   - Between conducting plates, the QED vacuum is MODIFIED
   - The virtual photon spectrum is altered — this changes vacuum polarization
   - Could a structured electromagnetic environment modify the effective charge?

6. **Laser-induced vacuum birefringence:**
   - At ELI-NP (Romania) and LUXE (DESY), experiments to observe vacuum nonlinearity
   - Two laser beams → light-by-light scattering via virtual pairs
   - This is direct manipulation of the QED vacuum
   - Could extreme laser fields near a heavy nucleus alter its effective charge?

---

## PHASE 6: Artificial Black Holes — Actual Frontier (`research/06-artificial-black-holes/`)

**Focus on what's actually being done, not sci-fi:**

**Analog Gravity Systems:**
- Acoustic black holes (Unruh 1981): sonic horizon in flowing fluid
- Optical analogs: slow light in BEC
- Steinhauer 2019: observed stimulated Hawking radiation in BEC analog
- What do these tell us about real black holes?
- Can analog systems be used to study quantum gravity effects at lab scales?

**Gravitational Analogs in Condensed Matter:**
- Type-II Weyl semimetals as spacetime analogs
- Artificial event horizons in 2D materials
- Tilted Dirac cones → analog spacetime geometry

**Micro Black Hole Non-Detection — What It Means:**
- LHC Run 2: no micro BH events found at √s = 13 TeV
- Constraints on extra dimensions: n=2 (large extra dimensions): Mpl > 11 TeV
- TeV-scale gravity models now heavily constrained
- But: quantum gravity at Planck scale (10¹⁹ GeV) remains entirely untested

**The Holographic Connection:**
- AdS/CFT correspondence: strongly coupled matter in 3D ↔ gravity in 4D
- QGP at RHIC/LHC has properties EXPLAINED by black hole physics (holographic duality)
- The QGP viscosity/entropy ratio η/s ≈ 1/4π matches the black hole prediction
- **This is not metaphor — it's a quantitative match**
- Could QGP experiments be considered "analog black hole" experiments?

---

## PHASE 7: Proton Charge Deep Dive (`research/07-proton-charge/`) — NEW THREAD

**This thread is specifically about proton charge as an engineering variable.**

### What IS proton charge?

**From QCD first principles:**
- Proton = uud quarks bound by gluons
- Electric charge emerges from quark content: (2/3 + 2/3 - 1/3)e = +e
- But the charge distribution is NOT uniform — it's a smeared quantum object
- Proton electromagnetic form factors:
  - Dirac form factor F₁(q²): charge distribution
  - Pauli form factor F₂(q²): magnetic moment distribution
  - Sachs form factors: GE(q²) = F₁ - τF₂, GM(q²) = F₁ + F₂
  - GE(0) = 1 (charge), GM(0) = μp = 2.793 nuclear magnetons

**Charge Radius and Its Implications:**
- rp² = -6 · dGE/dq² |q²=0
- rp = 0.8409 fm (current best value)
- This means the charge is spread over a sphere of radius ~0.84 fm
- At distances << 0.84 fm, you start resolving the quark structure
- The quarks themselves have charge radii (or are they pointlike?)

**Running of the Coupling — Charge at Different Scales:**
Calculate and plot α_EM(Q) from Q = 1 MeV to Q = 1 TeV:
- At Q ~ 1 MeV: α ≈ 1/137.036 (fine structure constant)
- At Q ~ 91 GeV (Z mass): α ≈ 1/128.9
- Extrapolating: at what energy does α → 1? (Landau pole — QED breaks down)
- Above this scale, need full electroweak theory

**Proton Self-Energy and the Hierarchy Problem:**
- Why is the proton mass 1836× the electron mass?
- The proton mass comes MOSTLY from QCD binding energy, not quark masses
- Quark masses: u ~ 2.3 MeV, d ~ 4.8 MeV. Proton mass: 938.3 MeV.
- So ~99% of proton mass is gluon field / quark kinetic energy
- Implication: the proton charge (+e) and proton mass (938 MeV) are almost independent properties

**Charge Displacement Mechanisms — Engineering Viability:**

For each mechanism, provide:
- Physical basis
- Current experimental status
- Activation energy / required conditions
- Theoretical maximum effect size
- Viability rating (1-5)
- Key papers

1. **Vacuum polarization screening** (natural, always present)
   - Effect: ~1% charge modification at nuclear distances
   - Exploitability: LOW — it's a fixed QED effect

2. **Dense electron plasma screening (Salpeter)**
   - Effect: exponential fusion rate enhancement
   - Required: ρ > 10⁷ g/cm³, T < 10⁷ K (degenerate)
   - Exploitability: MEDIUM — requires stellar densities

3. **Muon replacement (muonic atoms)**
   - Effect: muon 1s overlaps nucleus directly
   - Required: muon beam, cold target
   - Duration: muon lifetime 2.2 μs (long enough for spectroscopy)
   - Exploitability: MEDIUM — exotic but achievable

4. **Laser field dressing of nuclear charge**
   - Extreme UV/X-ray laser fields can modify electron screening transiently
   - Required: ELI-level fields (10²³ W/cm²)
   - Effect on nuclear Coulomb: small but nonzero
   - Exploitability: LOW-MEDIUM — frontier research

5. **Structured nuclear environment (crystalline matter)**
   - Nuclei in crystal lattice have coherent electron environment
   - Channeling effects: ions traveling along crystal axes experience very different fields
   - Planar channeling: nuclear reactions enhanced in aligned crystals
   - Exploitability: MEDIUM — actually used in some accelerator targets

6. **Nuclear excitation by electron transition (NEET / NEEC)**
   - Nuclear Excitation by Electron Capture: electron captured by nucleus, triggers nuclear transition
   - The TIME-REVERSE of internal conversion
   - Could be used to selectively populate nuclear isomers
   - Exploitability: HIGH (narrow, but real) — NEEC observed in 2018

7. **Coherent nuclear excitation via laser (NIXEN / XFEL)**
   - X-ray free electron lasers can now address nuclear transitions directly
   - LCLS-II, European XFEL: photon energies approaching nuclear transition energies
   - Nuclear clock transition in Th-229: ~8.4 eV (optical!) — unique accessible nuclear state
   - Exploitability: HIGH for Th-229 specifically

8. **Hypernuclei — strange quark substitution:**
   - Replace a neutron with a Lambda hyperon (contains a strange quark)
   - Hypernuclei are real and studied: He, Li, C hypernuclei created at CERN, J-PARC
   - The Lambda changes the nuclear structure, potentially modifying stability
   - Double-strange nuclei (H-dibaryon): possibly bound, being searched for
   - Exploitability: MEDIUM — changes nuclear structure in potentially useful ways

9. **Isospin symmetry breaking as leverage:**
   - Up and down quarks have different masses (mu ≠ md)
   - This breaks isospin symmetry — makes proton and neutron slightly different
   - In extreme isospin asymmetric matter, new phases may appear
   - Exploitability: THEORETICAL

10. **Charge conjugation asymmetry (CP violation)**
    - Matter and antimatter nuclei have identical but opposite charges
    - In matter-antimatter interfaces: annihilation + energy release
    - ALPHA experiment at CERN: trapped antihydrogen, measured its spectrum
    - Is the antiproton charge exactly -e? (Testing CPT symmetry)
    - Exploitability: VERY LOW — antimatter production rate is 10⁻¹² of proton rate

---

## PHASE 8: Step-Function Leverage Analysis (`research/08-leverage-analysis/`)

This is the synthesis thread. After completing all other threads, produce:

### `research/08-leverage-analysis/LEVERAGE_MAP.md`

For each identified leverage point:
```
## Leverage Point N: [Name]

**System:** [which scale/domain]
**Mechanism:** [what happens physically]
**Current State:** [where we are now]
**Activation Threshold:** [what you need to trigger it]
**Amplification Factor:** [how much does effect scale with input?]
**Coupling to Other Leverage Points:** [what else does this trigger?]
**Step Function Potential:** [YES/NO/MAYBE + explanation]
**Required Enabling Technologies:** [what needs to be built]
**Timeline to Viability:** [honest estimate]
**Key Papers:** [1-3 most important references]
```

Include at minimum:
1. Shell closures (magic numbers) — stability step functions
2. Ignition threshold (Lawson criterion) — fusion Q step function
3. Fission barrier collapse — spontaneous cascade trigger
4. Vacuum decay onset (Z~172) — charge discharge step function
5. QCD phase transition (nuclear → quark matter) — density step function
6. Nuclear pasta phases — mechanical property discontinuity
7. Muon catalysis scaling — if sticking solved, exponential gain
8. NEEC/NEET nuclear clock transitions — coherent nuclear control
9. Salpeter enhancement in dense plasma — reaction rate amplification
10. Hypernuclear stability modification
11. Color superconductivity onset — condensed quark matter phase
12. Holographic duality (QGP ↔ black hole) — theoretical unification

### `research/08-leverage-analysis/UNUSUAL_REAGENTS.md`

List every unusual/unexpected reagent or condition identified:
- What it is
- Why it's unexpected
- What it does to the system
- Viability and sourcing
- Whether it could be a cascade amplifier

Candidates to research:
- Muons (natural in cosmic rays — ~10,000/m²/min at sea level)
- Antiprotons (CERN ALPHA/BASE)
- Kaons and pions as nuclear reagents
- Metallic hydrogen
- Strangelet seeds
- Nuclear isomers (hafnium-178m2: 2.45 MeV stored in metastable nuclear state)
- Thorium-229 nuclear clock state
- Spin-polarized nuclei
- Aligned crystal targets
- Degenerate electron plasma
- Photon-photon scattering (laser-laser)
- Ultracold neutrons
- Neutron stars as "natural laboratories" — what can we learn from their properties?

---

## FINAL REPORT (`report/FINAL_REPORT.md`)

Structure:
1. **Executive Summary** — The answer in 500 words. What can be done. What can't. Where the leverage is.
2. **Master Limit Condition Table** — All limits, sorted by scale
3. **The Cascade System** — How the limits connect as a system
4. **Materials Science at Each Limit** — What matter IS at each phase boundary
5. **Charge Vacuum Analysis** — Proton charge as engineering variable — full analysis
6. **Step-Function Opportunities** — Where discontinuous gains are possible
7. **Unusual Reagents Summary** — The unexpected candidates and why they matter
8. **Related Rates at Scale** — The coupled differential equations governing the system
9. **Viability Matrix** — Honest assessment of every edge case (5-point scale)
10. **Open Questions** — What we don't know and why it matters
11. **Recommended Research Directions** — If you had $1B and 10 years, where would you put it?
12. **Appendix: All Key Equations**

---

## Commit Strategy
- Commit after EACH thread: `git commit -m "Thread N complete: [topic]"`
- Push after every commit
- Final commit: `git commit -m "COMPLETE: All 8 threads + final report"`
- Then: `clawdbot gateway wake --text "DONE: Periodic table research complete. 8 threads, final report at https://github.com/coywolffuturist/why-does-the-periodic-table-have-a-maximum" --mode now`

## Tools Available
- Python (numpy, scipy, matplotlib) for calculations
- web_search / web_fetch for literature
- Read existing research/01-nuclear-stability/notes.md as starting point
