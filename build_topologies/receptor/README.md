I prcessed the  ModMonoLigMiliNterminal.pdb model with the H++ server:
[http://newbiophysics.cs.vt.edu/H++/](http://newbiophysics.cs.vt.edu/H++/)

The resulting PDB (PQR) structure in the predicted protonation state:
`0.15_80_10_pH6.5_ModMonoLigMiliNterminal.result.pdb`

RETRY

The ADP caused a break in the chain, so I removed it (see: ../../ModMonoLigMiliNterminal_noADP.pdb )

There were some missing atoms and fractional occupancy, which were repaired using ChimeraX Dock Prep, to
create: `receptor_prepped.pdb`

```
gmx pdb2gmx -f receptor_prepped.pdb -o receptor.gro -p receptor.top -i receptor.itp -ignh
```

Chose AMBERff99sb and TIP3P water




  



