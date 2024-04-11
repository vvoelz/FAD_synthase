# Molecular simulation model of *C. ammoniagenes* FAD synthase in complex with ATP/Mg<sup>2+</sup> and FMN

* `build_topologies` - contains work to build AMBER topologies for use with the GROMACS simulation package
* `solvation_equilibration` - steps to add Mg2+, add solvent and ions, minimize and equilibrate

## Methods

All structural models were mimimized and equilibrated using the GROMACS simulation software, version 2020.4 (Abraham 2015).  Input coordinates were taken from the molecular docking model of *C. ammoniagenes* FAD synthase in complex with ATP/Mg<sup>2+</sup> published by Lars et al. (2018).  The GROMACS tool *pdb2gmx* was used to protonate the  receptor at physiological pH and prepare its topology using the AMBER ff99SB force field ().  AMBER-compatible simulation parameters for adenosine triphosphate (ATP) and were taken from XXX.  AMBER-comp


# References

Lans, Isaias, Juan Seco, Ana Serrano, Ricardo Burbano, Pilar Cossio, Martha C. Daza, and Milagros Medina. “The Dimer-of-Trimers Assembly Prevents Catalysis at the Transferase Site of Prokaryotic FAD Synthase.” Biophysical Journal 115, no. 6 (September 2018): 988–95. https://doi.org/10.1016/j.bpj.2018.08.011.

Abraham, Mark James, Teemu Murtola, Roland Schulz, Szilárd Páll, Jeremy C. Smith, Berk Hess, and Erik Lindahl. “GROMACS: High Performance Molecular Simulations through Multi-Level Parallelism from Laptops to Supercomputers.” SoftwareX 1–2 (September 2015): 19–25. https://doi.org/10.1016/j.softx.2015.06.001.


