import ase
from ase.data import atomic_numbers, atomic_masses

density = 1.77  # g/cm^3

Na = 6.022e23

atom = 'B'

molecular_mass = atomic_masses[atomic_numbers[atom]]

nmoles = (density / molecular_mass)

natoms = nmoles * Na

atoms_per_ang_3 = natoms / (1e8)**3

print(atoms_per_ang_3)
