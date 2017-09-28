import ase
from ase.data import atomic_numbers, atomic_masses

density = 1.73  # g/cm^3

Na = 6.022e23

atom = 'B'
thickness = 4.5 #nm

molecular_mass = atomic_masses[atomic_numbers[atom]]

nmoles = (density / molecular_mass)

natoms = nmoles * Na

atoms_per_ang_3 = natoms / (1e8)**3

atoms_per_cm_3 = natoms

thickness_cm = thickness * 1e-9 * 1e2

tfu = atoms_per_cm_3 * thickness_cm
tfu = tfu / 1e15

print(atoms_per_ang_3)
print(atoms_per_cm_3)
print(tfu)
