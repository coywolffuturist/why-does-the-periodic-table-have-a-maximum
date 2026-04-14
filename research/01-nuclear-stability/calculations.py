#!/usr/bin/env python3
"""
Nuclear Stability Calculations

This module computes:
1. Semi-Empirical Mass Formula (SEMF) with shell corrections
2. Fission barrier heights as function of Z
3. Nuclear matter phase diagram (schematic)
4. Optimal N/Z ratios
5. Compressibility and equation of state
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional

# ============================================================================
# SEMF Parameters (MeV)
# ============================================================================

# Standard SEMF coefficients
a_V = 15.75      # Volume term
a_S = 17.8       # Surface term
a_C = 0.711      # Coulomb term
a_sym = 23.7     # Asymmetry (symmetry) term
delta_0 = 12.0   # Pairing term coefficient

# Nuclear matter properties
rho_0 = 0.16     # Saturation density (fm^-3)
K_0 = 230.0      # Incompressibility (MeV)
E_0 = -16.0      # Binding energy per nucleon at saturation (MeV)
E_sym_0 = 32.0   # Symmetry energy at saturation (MeV)
L_sym = 60.0     # Symmetry energy slope (MeV)


# ============================================================================
# SEMF Functions
# ============================================================================

def binding_energy_semf(Z: int, A: int) -> float:
    """
    Calculate binding energy using the Semi-Empirical Mass Formula.

    Parameters
    ----------
    Z : int
        Proton number
    A : int
        Mass number (Z + N)

    Returns
    -------
    float
        Binding energy in MeV
    """
    if A <= 0 or Z <= 0 or Z > A:
        return 0.0

    N = A - Z

    # Volume term
    B_V = a_V * A

    # Surface term
    B_S = -a_S * A**(2/3)

    # Coulomb term
    B_C = -a_C * Z**2 / A**(1/3)

    # Asymmetry term
    B_sym = -a_sym * (A - 2*Z)**2 / A

    # Pairing term
    if Z % 2 == 0 and N % 2 == 0:  # even-even
        delta = delta_0 / np.sqrt(A)
    elif Z % 2 == 1 and N % 2 == 1:  # odd-odd
        delta = -delta_0 / np.sqrt(A)
    else:  # odd A
        delta = 0.0

    return B_V + B_S + B_C + B_sym + delta


def shell_correction_strutinsky(Z: int, N: int) -> float:
    """
    Approximate shell correction using phenomenological magic number proximity.

    This is a simplified model - full Strutinsky calculation requires
    solving the single-particle Hamiltonian.

    Parameters
    ----------
    Z : int
        Proton number
    N : int
        Neutron number

    Returns
    -------
    float
        Shell correction energy in MeV
    """
    # Magic numbers
    magic_Z = [2, 8, 20, 28, 50, 82, 114, 126]
    magic_N = [2, 8, 20, 28, 50, 82, 126, 184]

    # Shell correction strength
    shell_strength = 4.0  # MeV per magic number closure
    width = 8  # Shell width for smooth falloff

    delta_E = 0.0

    # Proton shell correction
    for Zm in magic_Z:
        delta_E -= shell_strength * np.exp(-(Z - Zm)**2 / (2 * width**2))

    # Neutron shell correction
    for Nm in magic_N:
        delta_E -= shell_strength * np.exp(-(N - Nm)**2 / (2 * width**2))

    # Doubly magic enhancement
    for Zm in magic_Z:
        for Nm in magic_N:
            if abs(Z - Zm) < width and abs(N - Nm) < width:
                delta_E -= 2.0 * np.exp(-((Z - Zm)**2 + (N - Nm)**2) / (2 * width**2))

    return delta_E


def binding_energy_with_shell(Z: int, A: int) -> float:
    """
    Binding energy including shell corrections.
    """
    N = A - Z
    return binding_energy_semf(Z, A) + shell_correction_strutinsky(Z, N)


def optimal_A_for_Z(Z: int) -> int:
    """
    Find the optimal mass number A for a given Z.
    """
    # Analytical approximation from SEMF
    # Z_opt = A / (2 + a_C * A^(2/3) / (2 * a_sym))
    # Solving for A: A ≈ 2Z + 0.015 * Z^(5/3)

    A_approx = int(2 * Z + 0.015 * Z**(5/3))

    # Fine-tune by searching nearby
    best_A = A_approx
    best_B = binding_energy_with_shell(Z, A_approx)

    for dA in range(-10, 11):
        A_test = A_approx + dA
        if A_test > Z:
            B_test = binding_energy_with_shell(Z, A_test)
            if B_test > best_B:
                best_B = B_test
                best_A = A_test

    return best_A


# ============================================================================
# Fission Barrier Calculations
# ============================================================================

def fissility_parameter(Z: int, A: int) -> float:
    """
    Calculate the fissility parameter x = (Z²/A) / 50.

    x = 1 corresponds to zero fission barrier in liquid drop model.
    """
    return (Z**2 / A) / 50.0


def fission_barrier_ldm(Z: int, A: int) -> float:
    """
    Liquid drop model fission barrier height.

    E_B ≈ 0.73 * a_S * A^(2/3) * (1 - x)^3

    Returns
    -------
    float
        Barrier height in MeV
    """
    x = fissility_parameter(Z, A)

    if x >= 1.0:
        return 0.0

    E_surface = a_S * A**(2/3)
    return 0.73 * E_surface * (1 - x)**3


def shell_correction_at_saddle(Z: int, N: int) -> float:
    """
    Approximate shell correction at the saddle point.

    Generally smaller than ground state shell correction because
    deformed single-particle levels are more uniformly distributed.
    """
    # Saddle point shell corrections are typically 1/3 to 1/2 of ground state
    return 0.4 * shell_correction_strutinsky(Z, N)


def fission_barrier_total(Z: int, A: int) -> float:
    """
    Total fission barrier including shell corrections.

    E_B = E_B(LDM) + δE_shell(saddle) - δE_shell(ground)
    """
    N = A - Z

    E_ldm = fission_barrier_ldm(Z, A)
    delta_ground = shell_correction_strutinsky(Z, N)
    delta_saddle = shell_correction_at_saddle(Z, N)

    # Shell correction to barrier = (saddle correction) - (ground correction)
    # Since ground is more negative, this INCREASES the barrier
    delta_barrier = delta_saddle - delta_ground

    return max(0.0, E_ldm + delta_barrier)


# ============================================================================
# Nuclear Matter Equation of State
# ============================================================================

def nuclear_eos_energy(rho: float, alpha: float = 0.0) -> float:
    """
    Energy per nucleon as function of density.

    Parameters
    ----------
    rho : float
        Baryon density in fm^-3
    alpha : float
        Isospin asymmetry (N-Z)/A, default 0 (symmetric matter)

    Returns
    -------
    float
        Energy per nucleon in MeV
    """
    if rho <= 0:
        return 0.0

    u = rho / rho_0  # Reduced density

    # Symmetric matter: expansion around saturation
    # E(ρ) = E_0 + K_0/18 * (u-1)^2 + O((u-1)^3)
    E_symm = E_0 + K_0 / 18.0 * (u - 1)**2

    # Symmetry energy contribution
    # E_sym(ρ) ≈ E_sym_0 * (ρ/ρ_0)^γ where γ ≈ L/(3*E_sym_0)
    gamma = L_sym / (3 * E_sym_0)
    E_sym_rho = E_sym_0 * u**gamma

    return E_symm + E_sym_rho * alpha**2


def nuclear_pressure(rho: float, alpha: float = 0.0) -> float:
    """
    Pressure of nuclear matter.

    P = ρ² * d(E/A)/dρ

    Returns pressure in MeV/fm³
    """
    if rho <= 0:
        return 0.0

    # Numerical derivative
    delta = 0.001 * rho_0
    E_plus = nuclear_eos_energy(rho + delta, alpha)
    E_minus = nuclear_eos_energy(rho - delta, alpha)

    dE_drho = (E_plus - E_minus) / (2 * delta)

    return rho**2 * dE_drho


def compressibility_modulus(rho: float = None) -> float:
    """
    Calculate compression modulus at given density.

    K = 9 * ρ² * d²(E/A)/dρ²
    """
    if rho is None:
        rho = rho_0

    delta = 0.001 * rho_0
    E_plus = nuclear_eos_energy(rho + delta)
    E_0_val = nuclear_eos_energy(rho)
    E_minus = nuclear_eos_energy(rho - delta)

    d2E_drho2 = (E_plus - 2*E_0_val + E_minus) / delta**2

    return 9 * rho**2 * d2E_drho2


# ============================================================================
# Phase Diagram
# ============================================================================

def liquid_gas_coexistence_curve() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculate the liquid-gas coexistence curve for nuclear matter.

    Uses a simplified van der Waals-like model.

    Returns
    -------
    T : ndarray
        Temperature in MeV
    rho_liquid : ndarray
        Liquid branch density
    rho_gas : ndarray
        Gas branch density
    """
    T_c = 17.0  # Critical temperature in MeV
    rho_c = 0.06  # Critical density in fm^-3

    # Coexistence curve (parametric in reduced temperature)
    T = np.linspace(0.1, T_c - 0.1, 100)
    t = T / T_c  # Reduced temperature

    # Near critical point: (ρ - ρ_c) ∝ (T_c - T)^β with β ≈ 1/3
    beta = 0.33

    # Simple parametrization
    delta_rho = rho_c * (1 - t)**beta

    rho_liquid = rho_c + delta_rho * 2.5  # Asymmetric around critical
    rho_gas = rho_c - delta_rho * 0.9
    rho_gas = np.maximum(rho_gas, 0.001)  # Ensure positive

    return T, rho_liquid, rho_gas


# ============================================================================
# Plotting Functions
# ============================================================================

def plot_binding_energy_per_nucleon():
    """Plot B/A vs A for optimal isotopes."""
    fig, ax = plt.subplots(figsize=(10, 6))

    Z_range = range(1, 131)
    A_values = []
    B_over_A_semf = []
    B_over_A_shell = []

    for Z in Z_range:
        A = optimal_A_for_Z(Z)
        A_values.append(A)

        B_semf = binding_energy_semf(Z, A)
        B_shell = binding_energy_with_shell(Z, A)

        B_over_A_semf.append(B_semf / A if A > 0 else 0)
        B_over_A_shell.append(B_shell / A if A > 0 else 0)

    ax.plot(Z_range, B_over_A_semf, 'b-', label='SEMF (liquid drop)', linewidth=2)
    ax.plot(Z_range, B_over_A_shell, 'r-', label='SEMF + shell corrections', linewidth=2)

    ax.axhline(y=0, color='k', linestyle='--', alpha=0.5)
    ax.axvline(x=82, color='g', linestyle=':', alpha=0.7, label='Z=82 (Pb, last stable)')
    ax.axvline(x=114, color='orange', linestyle=':', alpha=0.7, label='Z=114 (Fl, island)')
    ax.axvline(x=126, color='purple', linestyle=':', alpha=0.7, label='Z=126 (predicted magic)')

    ax.set_xlabel('Proton Number Z', fontsize=12)
    ax.set_ylabel('Binding Energy per Nucleon (MeV)', fontsize=12)
    ax.set_title('Nuclear Stability: B/A vs Z', fontsize=14)
    ax.legend(loc='lower left')
    ax.set_xlim(0, 130)
    ax.set_ylim(-2, 10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/periodic-table-max/research/01-nuclear-stability/binding_energy.png', dpi=150)
    plt.close()

    print("Saved: binding_energy.png")


def plot_fission_barriers():
    """Plot fission barrier height vs Z."""
    fig, ax = plt.subplots(figsize=(10, 6))

    Z_range = range(80, 131)
    E_ldm = []
    E_total = []

    for Z in Z_range:
        A = optimal_A_for_Z(Z)
        E_ldm.append(fission_barrier_ldm(Z, A))
        E_total.append(fission_barrier_total(Z, A))

    ax.plot(Z_range, E_ldm, 'b--', label='Liquid Drop Model', linewidth=2)
    ax.plot(Z_range, E_total, 'r-', label='With Shell Corrections', linewidth=2)

    ax.axhline(y=0, color='k', linestyle='-', alpha=0.5)
    ax.axhline(y=1, color='gray', linestyle=':', alpha=0.7, label='~1 MeV (thermal fluctuation scale)')

    # Mark key elements
    ax.axvline(x=92, color='green', linestyle=':', alpha=0.5)
    ax.text(92.5, 5.5, 'U', fontsize=10)
    ax.axvline(x=114, color='orange', linestyle=':', alpha=0.5)
    ax.text(114.5, 3.5, 'Fl', fontsize=10)
    ax.axvline(x=120, color='purple', linestyle=':', alpha=0.5)
    ax.text(120.5, 4, 'Z=120', fontsize=10)

    ax.set_xlabel('Proton Number Z', fontsize=12)
    ax.set_ylabel('Fission Barrier Height (MeV)', fontsize=12)
    ax.set_title('Fission Barrier vs Z (for optimal A)', fontsize=14)
    ax.legend(loc='upper right')
    ax.set_xlim(80, 130)
    ax.set_ylim(-0.5, 8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/periodic-table-max/research/01-nuclear-stability/fission_barrier.png', dpi=150)
    plt.close()

    print("Saved: fission_barrier.png")


def plot_phase_diagram():
    """Plot nuclear matter phase diagram."""
    fig, ax = plt.subplots(figsize=(10, 8))

    # Coexistence curve
    T, rho_liq, rho_gas = liquid_gas_coexistence_curve()

    ax.fill_betweenx(T, rho_gas, rho_liq, alpha=0.3, color='blue', label='Two-phase region')
    ax.plot(rho_gas, T, 'b-', linewidth=2)
    ax.plot(rho_liq, T, 'b-', linewidth=2)

    # Critical point
    T_c = 17.0
    rho_c = 0.06
    ax.plot(rho_c, T_c, 'ro', markersize=10, label=f'Critical point\n(T={T_c} MeV, ρ={rho_c} fm⁻³)')

    # Saturation density line
    ax.axvline(x=rho_0, color='green', linestyle='--', alpha=0.7, label=f'Saturation density ρ₀={rho_0} fm⁻³')

    # Labels for phases
    ax.text(0.01, 12, 'Nuclear\nGas', fontsize=12, ha='center')
    ax.text(0.20, 8, 'Nuclear\nLiquid', fontsize=12, ha='center')
    ax.text(0.08, 3, 'Coexistence\nRegion', fontsize=10, ha='center', style='italic')

    # QGP transition (schematic)
    ax.axhline(y=150, color='red', linestyle='--', alpha=0.7)
    ax.text(0.12, 155, 'QGP transition ~156 MeV →', fontsize=10, color='red')

    ax.set_xlabel('Baryon Density (fm⁻³)', fontsize=12)
    ax.set_ylabel('Temperature (MeV)', fontsize=12)
    ax.set_title('Nuclear Matter Phase Diagram (Schematic)', fontsize=14)
    ax.legend(loc='upper right')
    ax.set_xlim(0, 0.25)
    ax.set_ylim(0, 25)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/periodic-table-max/research/01-nuclear-stability/phase_diagram.png', dpi=150)
    plt.close()

    print("Saved: phase_diagram.png")


def plot_eos():
    """Plot equation of state curves."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    rho = np.linspace(0.01, 0.4, 200)

    # Energy per nucleon
    E_sym = [nuclear_eos_energy(r, 0.0) for r in rho]  # Symmetric matter
    E_pnm = [nuclear_eos_energy(r, 1.0) for r in rho]  # Pure neutron matter

    axes[0].plot(rho/rho_0, E_sym, 'b-', linewidth=2, label='Symmetric matter (α=0)')
    axes[0].plot(rho/rho_0, E_pnm, 'r-', linewidth=2, label='Pure neutron matter (α=1)')
    axes[0].axhline(y=E_0, color='green', linestyle='--', alpha=0.7, label=f'E₀ = {E_0} MeV')
    axes[0].axvline(x=1.0, color='gray', linestyle=':', alpha=0.7)

    axes[0].set_xlabel('ρ/ρ₀', fontsize=12)
    axes[0].set_ylabel('E/A (MeV)', fontsize=12)
    axes[0].set_title('Energy per Nucleon', fontsize=14)
    axes[0].legend()
    axes[0].set_xlim(0, 2.5)
    axes[0].set_ylim(-20, 80)
    axes[0].grid(True, alpha=0.3)

    # Pressure
    P_sym = [nuclear_pressure(r, 0.0) for r in rho]
    P_pnm = [nuclear_pressure(r, 1.0) for r in rho]

    axes[1].plot(rho/rho_0, P_sym, 'b-', linewidth=2, label='Symmetric matter')
    axes[1].plot(rho/rho_0, P_pnm, 'r-', linewidth=2, label='Pure neutron matter')
    axes[1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
    axes[1].axvline(x=1.0, color='gray', linestyle=':', alpha=0.7)

    axes[1].set_xlabel('ρ/ρ₀', fontsize=12)
    axes[1].set_ylabel('Pressure (MeV/fm³)', fontsize=12)
    axes[1].set_title('Pressure vs Density', fontsize=14)
    axes[1].legend()
    axes[1].set_xlim(0, 2.5)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/periodic-table-max/research/01-nuclear-stability/eos.png', dpi=150)
    plt.close()

    print("Saved: eos.png")


def print_key_values():
    """Print key numerical results."""
    print("\n" + "="*60)
    print("KEY NUCLEAR STABILITY VALUES")
    print("="*60)

    print("\n--- Binding Energy at Optimal A ---")
    for Z in [26, 50, 82, 92, 100, 110, 114, 120, 126]:
        A = optimal_A_for_Z(Z)
        B = binding_energy_with_shell(Z, A)
        print(f"Z={Z:3d}: A_opt={A:3d}, B/A = {B/A:6.2f} MeV")

    print("\n--- Fission Barriers ---")
    for Z in [92, 100, 104, 110, 114, 120, 126]:
        A = optimal_A_for_Z(Z)
        E_ldm = fission_barrier_ldm(Z, A)
        E_tot = fission_barrier_total(Z, A)
        print(f"Z={Z:3d}: E_B(LDM)={E_ldm:5.2f} MeV, E_B(total)={E_tot:5.2f} MeV")

    print("\n--- Nuclear Matter Properties ---")
    print(f"Saturation density: ρ₀ = {rho_0} fm⁻³")
    print(f"Binding energy at saturation: E₀ = {E_0} MeV")
    print(f"Incompressibility: K₀ = {K_0} MeV")
    print(f"Symmetry energy: E_sym = {E_sym_0} MeV")
    print(f"Symmetry energy slope: L = {L_sym} MeV")
    print(f"Calculated K at saturation: {compressibility_modulus():.1f} MeV")

    print("\n--- Fissility Parameters ---")
    for Z in [92, 100, 104, 106, 110, 114, 120]:
        A = optimal_A_for_Z(Z)
        x = fissility_parameter(Z, A)
        print(f"Z={Z:3d}, A={A:3d}: x = {x:.3f} {'(barrier=0)' if x >= 1 else ''}")

    print("\n" + "="*60)


if __name__ == "__main__":
    print_key_values()

    # Generate plots
    plot_binding_energy_per_nucleon()
    plot_fission_barriers()
    plot_phase_diagram()
    plot_eos()

    print("\nAll calculations complete.")
