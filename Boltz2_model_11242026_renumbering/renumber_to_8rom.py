#!/usr/bin/env python3
"""Renumber the two Boltz-2 models to match the deposited 8ROM chain A."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
MODEL_DIR = HERE.parent / "Boltz2_model"
MODEL_NAMES = ("HsFS_ATP", "HsFS_2AP-TP")
CHAIN = "A"


def read_pdb(path):
    """Read fixed-width records while preserving their line endings."""
    return path.read_bytes().decode("ascii").splitlines(keepends=True)


def atom_residues(lines):
    """Return chain A residue names keyed by (residue number, insertion code)."""
    return {
        (int(line[22:26]), line[26]): line[17:20]
        for line in lines
        if line.startswith("ATOM  ") and line[21] == CHAIN
    }


def reference_residues(lines):
    residues = atom_residues(lines)
    for line in lines:
        # REMARK 465 supplies author IDs for residues without coordinates.
        if line.startswith("REMARK 465") and line[19] == CHAIN:
            number = line[21:26].strip()
            if number.lstrip("-").isdigit():
                residues[(int(number), line[26])] = line[15:18]

    ordered = sorted(residues.items())
    seqres = [
        name
        for line in lines
        if line.startswith("SEQRES") and line[11] == CHAIN
        for name in line[19:70].split()
    ]
    if not seqres or [name for _, name in ordered] != seqres:
        raise ValueError("8ROM chain A residue IDs do not reproduce its SEQRES records")
    return ordered


def renumber_model(lines, reference, source):
    model = list(atom_residues(lines).items())
    if [name for _, name in model] != [name for _, name in reference]:
        raise ValueError(f"{source.name} chain A does not match the full 8ROM sequence")

    # Equal sequences give a one-to-one alignment in polymer order.
    mapping = {old_id: new_id for (old_id, _), (new_id, _) in zip(model, reference)}
    output = []
    for line in lines:
        if line[:6] in ("ATOM  ", "ANISOU", "TER   ") and line[21] == CHAIN:
            body = line.rstrip("\r\n")
            ending = line[len(body):]
            old_id = (int(body[22:26]), body[26:27] or " ")
            number, insertion = mapping[old_id]
            # The model TER records end at column 26, before the blank code.
            code = insertion if len(body) > 26 or insertion != " " else ""
            line = f"{body[:22]}{number:4d}{code}{body[27:]}{ending}"
        output.append(line)
    return "".join(output).encode("ascii")


def main():
    reference = reference_residues(read_pdb(HERE / "8ROM.pdb"))
    outputs = {}
    for name in MODEL_NAMES:
        source = MODEL_DIR / f"{name}.pdb"
        outputs[HERE / f"{name}_8ROM.pdb"] = renumber_model(
            read_pdb(source), reference, source
        )

    for path, content in outputs.items():
        path.write_bytes(content)
        print(f"{path.name}: renumbered {len(reference)} residues in chain {CHAIN}")


if __name__ == "__main__":
    main()
