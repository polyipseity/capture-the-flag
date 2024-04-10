from json import loads
from pathlib import Path

if __name__ == "__main__":
    cmap = loads(Path("cmap.json").read_text())
    cmap_reverse = {v: int(k) for k, v in cmap.items()}
    gsub = loads(Path("GSUB.json").read_text())
    for lig_sets in gsub["subtables"][0]["ligatureSets"][0]:
        if lig_sets["ligGlyph"] != 98:
            continue
        comps = lig_sets["components"]
        print("".join(chr(cmap_reverse[char]) for char in comps))
