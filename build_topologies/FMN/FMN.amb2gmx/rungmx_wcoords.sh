echo "a 1-31\nq\n" | gmx make_ndx -f FMN_GMX_translated.gro
echo "3\n" | gmx genrestr -f FMN_GMX_translated.gro -n index.ndx -o FMN_GMX_posre.itp
# The I put the line `#include "FMN_GMX_posre.itp"` before [ system ] in the FMN_GMX.top file

gmx grompp -f em.mdp -c FMN_GMX_translated.gro -r FMN_GMX_translated.gro -p FMN_GMX.top -o em.tpr -v -maxwarn 2
gmx mdrun -ntmpi 1 -v -s em.tpr -c FMN_GMX_translated_minimized.gro
