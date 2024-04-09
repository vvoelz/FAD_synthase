I concatenated receptor/conf.gro and FMN/FMN.amb2gmx/FMN_GMX_translated.gro into complex.gro

and renumbered with
gmx editconf -f complex.gro -o complex_renumbered.gro -resnr 1

