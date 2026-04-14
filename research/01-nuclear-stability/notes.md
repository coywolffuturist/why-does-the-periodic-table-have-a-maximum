# Thread 1: Nuclear Stability Limits

## Overview

The periodic table has a maximum because atomic nuclei become fundamentally unstable at high proton numbers. This instability arises from the competition between:
1. **Strong nuclear force** - short-range attraction (~1-2 fm), saturates with increasing nucleons
2. **Coulomb repulsion** - long-range repulsion between protons, grows as Z²

This thread explores the quantitative physics of nuclear binding and why nuclei inevitably become unbound.

---

## The Bethe-Weizsäcker Semi-Empirical Mass Formula (SEMF)

### Historical Context

Developed in 1935 by Carl Friedrich von Weizsäcker (building on Hans Bethe's work), this formula treats the nucleus as a charged liquid drop. Despite its simplicity, it captures the essential physics of nuclear binding with remarkable accuracy.

### The Complete Formula

The binding energy B(Z, A) is given by:

$$B(Z, A) = a_V A - a_S A^{2/3} - a_C \frac{Z^2}{A^{1/3}} - a_{sym} \frac{(A - 2Z)^2}{A} + \delta(A, Z)$$

Where:
- **Z** = number of protons (atomic number)
- **N** = number of neutrons
- **A** = Z + N (mass number)

### Standard Parameter Values (in MeV)

| Parameter | Symbol | Value (MeV) | Physical Origin |
|-----------|--------|-------------|-----------------|
| Volume    | aᵥ     | 15.75       | Strong force saturation |
| Surface   | aₛ     | 17.8        | Missing neighbors at surface |
| Coulomb   | aC     | 0.711       | Electrostatic repulsion |
| Asymmetry | aₐ     | 23.7        | Pauli exclusion principle |
| Pairing   | δ      | ±12/√A      | Spin pairing energy |

---

## Term-by-Term Analysis

### 1. Volume Term: +aᵥA

**Physical meaning:** Each nucleon contributes roughly the same binding energy due to strong force saturation.

The strong nuclear force has a range of ~1.4 fm (about the size of a nucleon). Each nucleon only "sees" its immediate neighbors. In the nuclear interior, each nucleon has roughly the same number of neighbors, so binding energy scales linearly with A.

**Key insight:** This term represents the idealized binding if all nucleons were surrounded by the same number of neighbors.

**Behavior with Z:** Linear growth. For fixed N/Z ratio, this scales as A = Z(1 + N/Z).

### 2. Surface Term: -aₛA^(2/3)

**Physical meaning:** Nucleons at the surface have fewer neighbors → less binding.

The nuclear surface area scales as R² ∝ A^(2/3) (since R ∝ A^(1/3)). The correction is negative because surface nucleons contribute less binding than the volume term assumes.

**Behavior with Z:** For spherical nuclei, surface area grows as A^(2/3). This term becomes relatively less important for larger nuclei (scales slower than volume).

### 3. Coulomb Term: -aC·Z²/A^(1/3)

**Physical meaning:** Electrostatic repulsion between protons destabilizes the nucleus.

Derivation:
- Coulomb energy of uniformly charged sphere: E = (3/5)(Q²/4πε₀R)
- Q = Ze, R = r₀A^(1/3) where r₀ ≈ 1.25 fm
- This gives: E ∝ Z²/A^(1/3)

**THE CRITICAL TERM FOR SUPERHEAVY ELEMENTS**

**Behavior with Z:** This term grows as Z². For large Z, it eventually dominates all positive terms. This is the fundamental reason the periodic table must end.

| Z   | Z² | Comment |
|-----|-----|---------|
| 10  | 100 | Light elements - Coulomb manageable |
| 50  | 2,500 | Tin - still stable |
| 82  | 6,724 | Lead - heaviest stable element |
| 100 | 10,000 | Fermium - highly unstable |
| 120 | 14,400 | Unbinilium - predicted island of stability |
| 137 | 18,769 | Feynman limit - QED breakdown |
| 173 | 29,929 | Extended Dirac limit |

### 4. Asymmetry Term: -aₐ(A-2Z)²/A

**Physical meaning:** Nuclei prefer equal numbers of protons and neutrons (for light nuclei).

This arises from the Pauli exclusion principle:
- Protons and neutrons fill separate quantum levels
- If N >> Z or Z >> N, particles must occupy higher energy levels
- Symmetric nuclei (N ≈ Z) are more tightly bound

However, for heavy nuclei, the Coulomb repulsion shifts the optimum toward neutron-rich configurations.

**Optimal N/Z ratio:** For light nuclei, N/Z ≈ 1. For heavy nuclei, N/Z → ~1.5 to compensate for Coulomb repulsion.

### 5. Pairing Term: ±δ(A,Z)

**Physical meaning:** Nucleons prefer to pair up with opposite spins.

$$\delta = \begin{cases} +\delta_0/\sqrt{A} & \text{even-even (Z, N both even)} \\ 0 & \text{odd A} \\ -\delta_0/\sqrt{A} & \text{odd-odd (Z, N both odd)} \end{cases}$$

With δ₀ ≈ 12 MeV.

**Effect:** Even-even nuclei are most stable. This is why most heavy elements decay through alpha emission (⁴He is doubly magic and even-even).

---

## The Mathematics of Nuclear Instability

### Binding Energy Per Nucleon

The binding energy per nucleon, B/A, is the key stability metric:

$$\frac{B}{A} = a_V - a_S A^{-1/3} - a_C \frac{Z^2}{A^{4/3}} - a_{sym} \frac{(A - 2Z)^2}{A^2} + \frac{\delta}{A}$$

**Maximum B/A occurs around A ≈ 56 (Iron-56)**

This is why:
- Fusion releases energy for A < 56 (moving toward iron)
- Fission releases energy for A > 56 (moving toward iron)

### Finding the Optimal N/Z Ratio

For a given A, minimize -B(Z,A) with respect to Z:

$$\frac{\partial B}{\partial Z} = 0$$

$$-2a_C \frac{Z}{A^{1/3}} + 4a_{sym} \frac{(A - 2Z)}{A} = 0$$

Solving:

$$Z_{optimal} = \frac{A}{2 + \frac{a_C A^{2/3}}{2a_{sym}}}$$

For small A: Z ≈ A/2 (symmetric nuclei)
For large A: Z/A decreases (more neutrons needed)

**Numerical examples:**
- A = 20: Z_opt ≈ 10 (observed: ²⁰Ne)
- A = 100: Z_opt ≈ 44 (observed: stable isotopes around Z=44-46)
- A = 238: Z_opt ≈ 92 (uranium)
- A = 298: Z_opt ≈ 114 (predicted island of stability)

---

## The Fission Barrier

### What is the Fission Barrier?

The fission barrier is the activation energy a nucleus must overcome to split apart. Even if fission is energetically favorable (releases energy), there's a potential barrier preventing spontaneous fission.

### Liquid Drop Model of Fission

Consider a nucleus deforming from a sphere to an elongated ellipsoid:
- Surface energy increases (surface area grows)
- Coulomb energy decreases (charges farther apart)

The fission barrier exists because for small deformations:
- Surface energy increase > Coulomb energy decrease

### The Fissility Parameter

$$x = \frac{E_C}{2E_S} = \frac{a_C Z^2 / A^{1/3}}{2 a_S A^{2/3}} = \frac{a_C}{2a_S} \cdot \frac{Z^2}{A}$$

With standard parameters: x ≈ 0.020 × Z²/A

**Critical values:**
- x < 1: Fission barrier exists (nucleus can be metastable)
- x = 1: Fission barrier vanishes (spontaneous fission instantaneous)

**Condition for zero barrier:** Z²/A > 2aₛ/aC ≈ 50

This gives the **spontaneous fission limit** around Z ~ 104-106 for nuclei along the beta-stability line.

### Barrier Heights

For nuclei with x < 1, the barrier height is approximately:

$$E_B ≈ 0.73 E_S (1 - x)^3$$

**Examples:**
- ²³⁸U (Z=92, A=238): x ≈ 0.71, E_B ≈ 6 MeV
- ²⁵²Cf (Z=98, A=252): x ≈ 0.76, E_B ≈ 4 MeV
- Z=110, A=280: x ≈ 0.87, E_B < 1 MeV

As Z increases, the barrier shrinks, and eventually nuclei fission spontaneously.

---

## Why Coulomb Repulsion Always Wins

### The Scaling Argument

| Force | Scaling | Range |
|-------|---------|-------|
| Strong nuclear | ~A (saturates) | ~1-2 fm |
| Coulomb | ~Z² | Infinite |

For a nucleus with N/Z ≈ 1.5 (heavy elements):
- A ≈ 2.5Z
- Volume term: ~15.75 × 2.5Z = 39.4Z
- Coulomb term: ~0.711 × Z²/(2.5Z)^(1/3) = 0.52Z^(5/3)

At large Z, the Z^(5/3) or higher power scaling of the Coulomb term overcomes the linear growth of the volume term.

### Numerical Crossover

Setting B(Z,A) = 0 for optimal A:

The binding energy goes negative around Z ≈ 120-130, depending on the assumed N/Z ratio and whether shell effects are included.

**Without shell corrections:** Nuclei become unbound around Z ≈ 104-110
**With shell corrections (island of stability):** Extended to Z ≈ 114-126

---

## The Drip Lines

### Neutron Drip Line

Where adding one more neutron gives negative binding (neutron unbound):

$$S_n = B(Z, N) - B(Z, N-1) < 0$$

For superheavy elements, the neutron drip line limits how many neutrons can stabilize against Coulomb repulsion.

### Proton Drip Line

Where adding one more proton gives negative binding:

$$S_p = B(Z, N) - B(Z-1, N) < 0$$

Heavy elements are neutron-rich precisely because they're far from the proton drip line.

---

## Alpha Decay and Spontaneous Fission

### Competition at High Z

For superheavy elements, two decay modes dominate:

1. **Alpha decay:** Nucleus emits ⁴He (very stable, doubly magic)
   - Half-lives: microseconds to milliseconds for Z > 100

2. **Spontaneous fission:** Nucleus splits into two fragments
   - Dominates when fission barrier < alpha decay Q-value

### The Geiger-Nuttall Law

For alpha decay, half-life depends exponentially on Q-value:

$$\log_{10}(t_{1/2}) = a - b \frac{Z}{\sqrt{Q_\alpha}}$$

Higher Q-values → faster decay → shorter half-lives

### Why Elements Beyond ~118 Don't Stick Around

At Z > 118:
- Fission barriers ≈ 1-2 MeV (comparable to zero-point motion)
- Alpha decay Q-values ≈ 10-12 MeV
- Half-lives: 10⁻⁶ to 10⁻³ seconds (without shell effects)

Shell effects near Z=114, N=184 extend half-lives significantly, creating the "island of stability."

---

## Key Conclusions

1. **The periodic table ends because Coulomb repulsion scales as Z² while nuclear binding saturates**

2. **The fission barrier shrinks with increasing Z and vanishes around Z²/A ≈ 50**

3. **Without quantum shell effects, nuclei become unbound around Z ≈ 104-110**

4. **Shell effects create the island of stability, potentially extending to Z ≈ 120-126**

5. **Even on the island of stability, half-lives are at most seconds to minutes—no superheavy element can exist indefinitely**

6. **The fundamental limit is not a sharp cutoff but a gradual transition from metastable to instantaneously unstable**

---

## Numerical Results Preview

The calculations.py file computes:
- Binding energy per nucleon for Z = 1 to 130
- Optimal N/Z ratio as function of Z
- Fission barrier heights
- Predicted half-lives (simplified model)
- The Z value where B/A goes negative

Key findings:
- B/A maximum at A ≈ 62 (near ⁶²Ni, most tightly bound)
- B/A → 0 around Z ≈ 125-130 (without shell corrections)
- Fission barrier < 1 MeV for Z > 110
- Spontaneous fission half-lives < 1 ms for Z > 115 (without shell effects)

---

## Connection to Other Threads

- **Thread 2 (Island of Stability):** Shell effects modify these predictions significantly
- **Thread 3 (Fusion):** Fusion releases energy because B/A increases toward iron
- **Thread 4 (Dense Matter):** At extreme densities, nuclear binding is overwhelmed by gravitational compression
- **Thread 5 (QED Limits):** Even if nuclei were stable, electrons can't orbit beyond Z ≈ 173
- **Thread 6 (Black Holes):** Ultimate compression exceeds nuclear binding—matter collapses to singularity
