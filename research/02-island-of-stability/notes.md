# Thread 2: Island of Stability — Engineering Approach

## Overview

The "island of stability" refers to a predicted region of superheavy nuclei with enhanced stability due to nuclear shell effects. This thread analyzes the island from an **engineering perspective**: What does it take to synthesize these nuclei? What are their predicted properties? Where are the leverage points for extending nuclear stability?

---

## Part 1: Synthesis Engineering

### Current Synthesis Methods

**Hot Fusion:**
- Uses actinide targets (U, Pu, Cm, Cf, etc.) + lighter projectiles (Ca-48)
- Higher excitation energy: E* ~ 30-50 MeV
- Multiple neutrons evaporated (3-5n channels)
- Access to more neutron-rich isotopes
- Used for Z=113-118 (Dubna)

**Cold Fusion:**
- Uses Pb/Bi targets + heavier projectiles (Cr, Fe, Ni, etc.)
- Lower excitation energy: E* ~ 10-15 MeV
- Fewer neutrons evaporated (1-2n channels)
- Higher survival probability but lower production cross-section
- Used for Z=107-113 (GSI, RIKEN)

### Cross-Section Estimates for Z=119, 120, 126

Production cross-section σ depends on three factors:
$$\sigma = \sigma_{capture} \times P_{fusion} \times P_{survival}$$

| Target | Projectile | Z_CN | E* (MeV) | σ_max (pb) | Method |
|--------|------------|------|----------|------------|--------|
| Cf-249 | Ca-48 | 119 | ~35 | 0.3-0.5 | Hot fusion |
| Bk-249 | Ti-50 | 119 | ~40 | 0.05-0.1 | Hot fusion |
| Cf-249 | Sc-45 | 119 | ~35 | ~0.29 | Hot fusion |
| Cm-246 | V-50 | 119 | ~35 | ~0.24 | Hot fusion |
| Cf-249 | Ti-46 | 120 | ~40 | ~0.04 | Hot fusion |
| Cf-252 | Ti-50 | 120 | ~40 | 0.01-0.05 | Hot fusion |
| Cm-248 | Cr-54 | 120 | ~45 | 0.01-0.03 | Hot fusion |

**Key insight:** Cross-sections for Z=119 are ~10× smaller than Z=118. For Z=120, another factor of ~10 smaller. This is the "cross-section cliff."

### The Survival Probability Problem

Even if a compound nucleus is formed, it must survive:
1. **Fission during de-excitation** — dominant loss mechanism
2. **Particle emission** — neutrons evaporated (desired), protons (loss)

Survival probability for superheavy nuclei:
$$P_{survival} \approx \left(\frac{\Gamma_n}{\Gamma_n + \Gamma_f}\right)^n$$

where n = number of neutrons evaporated.

For Z=120: P_survival ~ 10^-4 to 10^-5
For Z=126: P_survival ~ 10^-6 to 10^-8 (estimated)

### Required Experimental Parameters

**Beam intensity:**
- Current Ca-48 beams: 2-10 pμA (particle microamperes)
- 1 pμA = 6.25 × 10^12 particles/second
- Needed for Z=120: >10 pμA sustained

**Target considerations:**
- Actinide targets (Cf, Bk, Cm) have limited availability
- Cf-252 production: ~mg/year at ORNL
- Target lifetimes: weeks to months under beam
- Rotating targets to distribute heat load

**Detection requirements:**
- 1 event per month = successful detection threshold
- Need position-sensitive Si detectors for α-decay chains
- Recoil separators (SHIP, TASCA, GARIS, DGFRS)

### Facility Capabilities

| Facility | Location | Accelerator | Max Ca-48 Intensity | Key Achievements |
|----------|----------|-------------|---------------------|------------------|
| JINR/FLNR | Dubna, Russia | U-400 | 10 pμA | Z=113-118 (Og) |
| GSI | Darmstadt, Germany | UNILAC | 2 pμA | Z=107-112 |
| RIKEN | Tokyo, Japan | RILAC | 5-10 pμA | Z=113 (Nh) |
| LBNL | Berkeley, USA | 88-inch | 1-2 pμA | Z=104-106 |
| FRIB | Michigan, USA | SC linac | High (future) | Under development |

**JINR SHE Factory (2019+):** World's most intense superheavy facility
- DC-280 cyclotron: designed for 10 pμA Ca-48
- Target: new automated systems
- Goal: Z=119, 120 synthesis

### Reactions for Reaching Z=119, 120, 126

**Best candidates for Z=119:**
1. ⁴⁸Ca + ²⁴⁹Bk → ²⁹⁷119* (most likely to succeed)
2. ⁴⁵Sc + ²⁴⁹Cf → ²⁹⁴119*
3. ⁵¹V + ²⁴³Am → ²⁹⁴119*

**Best candidates for Z=120:**
1. ⁵⁰Ti + ²⁴⁹Cf → ²⁹⁹120*
2. ⁵⁴Cr + ²⁴⁸Cm → ³⁰²120*
3. ⁵⁸Fe + ²⁴⁴Pu → ³⁰²120*

**Reaching Z=126 — Major challenges:**
- No single reaction provides sufficient cross-section
- Would need: ⁶⁴Ni + ²⁵⁴Es → ³¹⁸126* (Es extremely rare)
- Or multi-nucleon transfer reactions (very low yield)
- Effectively requires new synthesis paradigms

---

## Part 2: Predicted Properties of Island Elements

### Electron Configurations (Relativistic Effects)

Relativistic effects dominate superheavy element chemistry:
- **Relativistic contraction:** s and p₁/₂ orbitals contract toward nucleus
- **Spin-orbit splitting:** p, d, f orbitals split into j = l±1/2 subshells
- **Relativistic expansion:** d and f orbitals expand due to reduced screening

**Predicted ground state configurations:**

| Z | Symbol | Conventional | Relativistic Prediction |
|---|--------|--------------|------------------------|
| 119 | Uue | [Og]8s¹ | [Og]8s¹ (or 8s²7p₃/₂⁻¹ mixed) |
| 120 | Ubn | [Og]8s² | [Og]8s² (but p-block character) |
| 121 | Ubu | [Og]8s²8p¹ | [Og]8s²8p₁/₂¹ (not s²d¹!) |
| 122-138 | — | 5g filling | 5g/6f/7d mixed |
| 126 | Ubh | [Og]5g⁶8s²8p₁/₂² | Complex mixed configuration |

**Key relativistic anomalies:**
- Z=119: NOT a simple alkali metal. 7p₃/₂ and 8s nearly degenerate.
- Z=120: NOT a simple alkaline earth. Significant p-character.
- Z=121: Expected s²p configuration instead of s²d (unlike La, Ac)
- Z=126: Potentially stable with proton magic number effects

### Predicted Chemistry

**Element 119 (Eka-francium):**
- Ionization potential: ~4.8 eV (lower than Fr at 4.07 eV? — uncertain)
- Most common oxidation state: +1, but +3 and +5 possible
- Expected to form Uue⁺ cation readily
- Relativistic effects make it behave as "new type of p-block metalloid"

**Element 120 (Eka-radium):**
- Ionization potentials: IP₁ ~ 5.8 eV, IP₂ ~ 12 eV
- Oxidation states: +2 (primary), +4, +6 possible
- Not a typical alkaline earth — p-block character
- May exhibit noble gas character under some conditions

**Element 126 (Eka-plutonium):**
- Part of predicted "superactinide" series (5g-filling)
- Strong coupling between 5g, 6f, 7d, 8s, 8p orbitals
- Multiple oxidation states likely: +2, +4, +6
- Predicted to form stable UbhF₂ diatomic molecule
- Chemistry dominated by relativistic spin-orbit effects

### Predicted Physical Properties

| Property | Z=119 | Z=120 | Z=126 |
|----------|-------|-------|-------|
| Melting point | ~27°C (liquid at RT?) | ~700°C | Unknown |
| Density | ~3 g/cm³ | ~7 g/cm³ | ~25-30 g/cm³? |
| Crystal structure | BCC (predicted) | FCC/BCC | Unknown |
| Metallic radius | ~3.0 Å | ~2.0 Å | ~1.7 Å |
| Electronegativity | ~0.9 (Pauling) | ~1.0 | ~1.5 |

**Uncertainties:** These predictions are highly uncertain. Relativistic effects are difficult to calculate accurately, and no experimental data exists.

---

## Part 3: Shell Model Deep Dive

### Magic Numbers: Spherical vs Deformed

**Traditional magic numbers (spherical shell closures):**
- Protons: 2, 8, 20, 28, 50, 82
- Neutrons: 2, 8, 20, 28, 50, 82, 126

**Predicted superheavy magic numbers:**
- Protons: 114, 120, 126 (models disagree)
- Neutrons: 172, 184 (184 more favored)

**Current understanding:**

| Model | Predicted Z_magic | Predicted N_magic | Notes |
|-------|-------------------|-------------------|-------|
| Woods-Saxon | 114 | 184 | Classical prediction |
| Relativistic mean field | 120 | 172, 184 | Z=120 stronger than 114 |
| Hartree-Fock-Bogoliubov | 126 | 184 | Z=126 as traditional doubly-magic |
| Modern Skyrme | 114, 120 | 184 | Multiple islands |

### Why Z=114 Was Expected But May Not Be "Magic"

The original predictions (1960s) used Woods-Saxon potentials suggesting Z=114 as the next proton magic number after 82.

**Problems discovered:**
1. Flerovium (Z=114) isotopes discovered at JINR don't show dramatically enhanced stability
2. Half-lives are milliseconds, not the predicted seconds/minutes
3. No clear shell closure signature in binding energies

**Possible explanations:**
- Shell gap smaller than predicted
- Deformation reduces spherical shell effects
- The "magic" may be at Z=120 or Z=126 instead

### Deformed Shell Closures

At high Z, nuclei are often deformed (prolate or oblate), creating DIFFERENT shell closures:

**Deformed magic numbers (at β₂ ~ 0.3):**
- N = 152, 162 (deformed sub-shells)
- These explain enhanced stability of some Cf, Fm isotopes

**Shape coexistence:** Some nuclei have nearly degenerate spherical and deformed minima
- Could allow "switching" between configurations
- Potential leverage point for engineering stability?

### The N=184 Question

N=184 remains the most robust prediction for neutron magic number in superheavy region.

**Evidence supporting N=184:**
- Consistent across multiple theoretical models
- α-decay chains from Z=118 suggest increasing stability toward N=184
- Shell correction energy calculations show clear gap

**Current status:**
- No isotope with N=184 has been synthesized
- Closest: Og-294 (Z=118, N=176) — 8 neutrons short
- Reaching N=184 requires more neutron-rich reactions or multi-neutron transfer

---

## Part 4: Leverage Points for Extended Stability

### Shell Closures as Leverage

**Mechanism:** At magic numbers, there's a gap in single-particle energy levels
- Nuclei "resist" excitation across the gap
- Fission barrier enhanced by 2-4 MeV
- Half-lives extended by 10⁶ or more

**Engineering approach:**
1. Target isotopes closest to N=184
2. Use reactions that deposit minimum excitation energy
3. Use cooling mechanisms (neutron evaporation) efficiently

### Neutron-Rich Synthesis Paths

**The problem:** Current reactions produce neutron-deficient superheavy isotopes
- Ca-48 + Cf-249 → (Z=118, N~176) — 8 neutrons short of N=184
- Need N/Z ~ 1.55 for optimal stability; typically achieve N/Z ~ 1.45-1.50

**Potential solutions:**
1. **Radioactive beams:** Use neutron-rich projectiles (e.g., Ni-68)
   - FRIB could produce such beams
   - Cross-sections unknown, likely very small

2. **Multi-nucleon transfer (MNT):**
   - Reactions like U+U can transfer many nucleons
   - Could reach more neutron-rich regions
   - Very low yield, products hard to identify

3. **Neutron capture chains (r-process):**
   - Successive neutron captures build to heavy nuclei
   - Requires extremely high neutron flux (supernovae/mergers)
   - Not achievable in laboratory

### Isomeric States as Stability Enhancement

**K-isomers:** High-K states where angular momentum is aligned with symmetry axis
- Decay suppressed by angular momentum selection rules
- Can have half-lives of years (e.g., Ta-180m: t½ > 10¹⁵ years)

**Potential in superheavy region:**
- Some deformed superheavy nuclei should have K-isomers
- Could extend effective half-lives
- Excitation energy stored in nuclear deformation

---

## Part 5: Second Island of Stability?

### Beyond N=184

Some theoretical models predict additional shell closures beyond the first island:

**Predicted second island:**
- Z ~ 164 (closed proton shell?)
- N ~ 228 or 308 (various predictions)

**Challenges:**
- Requires synthesizing 100+ new elements
- No viable synthesis path known
- Fission barriers may not support such heavy nuclei
- QED vacuum decay limit (Z~172) intervenes

### The "Peninsula of Stability" Concept

Rather than discrete islands, some models suggest a connected region of enhanced stability:
- Peninsula extending from Pb-208 toward superheavy region
- Shell effects create continuous (but uneven) stabilization
- No sharp "end" to the periodic table, just declining half-lives

---

## Part 6: Key Open Questions

1. **Where exactly are the proton magic numbers?** Z=114, 120, or 126?
   - Experiments at Z=119, 120 will provide crucial data

2. **How robust is N=184?** Can we reach isotopes with N>180?
   - Multi-nucleon transfer may be the key

3. **Do deformed magic numbers matter?** Can deformed shell closures be exploited?
   - Shape isomers could provide additional stability

4. **Is there chemistry on the island?** Can superheavy atoms form compounds?
   - Single-atom chemistry experiments at GSI/RIKEN addressing this

5. **Can we predict half-lives accurately?** Current theory uncertain by orders of magnitude
   - Machine learning approaches being developed

---

## Summary: Engineering Assessment

### Current State of Art
- Z=118 (Oganesson) synthesized (2002-2006, confirmed)
- Z=119, 120 actively pursued (Dubna, GSI, RIKEN)
- Expected discovery: 1-5 years if facilities reach required sensitivity

### Key Challenges
1. **Cross-section cliff:** Each Z costs factor of ~10 in production rate
2. **Target limitations:** Cf, Bk availability constrains hot fusion
3. **Neutron deficit:** Current reactions don't reach N=184
4. **Half-life cliff:** Beyond Z~120, even with shell effects, t½ < seconds

### Viable Near-Term Goals
- Synthesis of Z=119 (likely within ~5 years)
- Synthesis of Z=120 (challenging but possible)
- First chemical studies of Z=119-120

### Likely Impossible with Current Methods
- Synthesis of Z>126
- Production of gram quantities of any superheavy
- Reaching true "stability" (t½ > years)

---

## References

- Superheavy element synthesis reviews: https://link.springer.com/article/10.1007/s41365-025-01781-6
- Element 119/120 cross-section predictions: https://arxiv.org/abs/2210.16821
- Relativistic effects in superheavy elements: https://arxiv.org/abs/2103.15886
- Island of stability: https://en.wikipedia.org/wiki/Island_of_stability
- JINR SHE Factory: https://www.jinr.ru/posts/superheavy-elements-scientific-programme-and-infrastructure/
- Element 126 chemistry: https://cen.acs.org/articles/84/i10/Element-126.html
