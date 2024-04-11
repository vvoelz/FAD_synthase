# Molecular simulation model of *C. ammoniagenes* FAD synthase in complex with ATP/Mg<sup>2+</sup> and FMN

Briefly, the protocol was:
* Minimization of solvent+ions receptor:ATP:Mg2+:FMN with position restraints (on AMP portion of ATP and FMN)
* 100 ps of NVT md with restraints
* Re-minimize without restraints
* 100 ps of NVT md without restraints
* 200 ps of NPT md without restraints
* Final minimization without restraints

## Files

* `em_final.gro` - final minimized configuration GROMACS *.gro format
* `em_final.pdb` - final minimized configuration PDB format
* `em_final_noSOL_noIONS.gro` - solvent and ions removed GROMACS *.gro format
* `em_final_noSOL_noIONS.pdb` - solvent and ions removed PDB format


#### System preparation

* `build_topologies` - contains work to build AMBER topologies for use with the GROMACS simulation package
* `solvation_equilibration` - steps to add Mg2+, add solvent and ions, minimize and equilibrate

## Methods

All structural models were mimimized and equilibrated using the GROMACS simulation software, version 2020.4 (Abraham 2015).  Input coordinates were taken from the molecular docking model of *C. ammoniagenes* FAD synthase in complex with adenosine monophosphate (AMP) and flavin mononucleotide (FMN), based on the  published by ??????.  The GROMACS tool *pdb2gmx* was used to protonate the receptor at pH 7.0 and prepare its topology using the AMBER ff99SB force field ().  AMBER-compatible simulation parameters for adenosine triphosphate (ATP) and FMN (fully oxidized) were taken from Meager et al. (2003) and Schneider et al (1999), respectively.  


# References

Lans, Isaias, Juan Seco, Ana Serrano, Ricardo Burbano, Pilar Cossio, Martha C. Daza, and Milagros Medina. “The Dimer-of-Trimers Assembly Prevents Catalysis at the Transferase Site of Prokaryotic FAD Synthase.” Biophysical Journal 115, no. 6 (September 2018): 988–95. https://doi.org/10.1016/j.bpj.2018.08.011.

Abraham, Mark James, Teemu Murtola, Roland Schulz, Szilárd Páll, Jeremy C. Smith, Berk Hess, and Erik Lindahl. “GROMACS: High Performance Molecular Simulations through Multi-Level Parallelism from Laptops to Supercomputers.” SoftwareX 1–2 (September 2015): 19–25. https://doi.org/10.1016/j.softx.2015.06.001.

Meagher, Kristin L., Luke T. Redman, and Heather A. Carlson. “Development of Polyphosphate Parameters for Use with the AMBER Force Field.” Journal of Computational Chemistry 24, no. 9 (July 15, 2003): 1016–25. https://doi.org/10.1002/jcc.10262.

Schneider, C., and J. Sühnel. “A Molecular Dynamics Simulation of the Flavin Mononucleotide-RNA Aptamer Complex.” Biopolymers 50, no. 3 (September 1999): 287–302. https://doi.org/10.1002/(SICI)1097-0282(199909)50:3<287::AID-BIP5>3.0.CO;2-G.



