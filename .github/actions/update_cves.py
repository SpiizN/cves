#!/usr/bin/env python3

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
START = "<!-- cves-table:start -->"
END = "<!-- cves-table:end -->"

rows = []

for advisory in sorted(ROOT.glob("CVE-*/README.md")):
    cve = advisory.parent.name
    lines = advisory.read_text(encoding="utf-8").splitlines()

    title = lines[0]
    product = title.split(":", 1)[1].strip() if ":" in title else "-"

    meta = next((line for line in lines if "**Severity:**" in line), "")
    fields = dict(re.findall(r"\*\*([A-Za-z ]+):\*\*\s*([^·|\n]+)", meta))

    poc = advisory.parent / "poc"
    has_poc = poc.is_dir() and any(not f.name.startswith(".") for f in poc.iterdir())

    rows.append(
        f"| [{cve}]({cve}/README.md) | {product} "
        f"| {fields.get('Class', '-').strip()} "
        f"| {fields.get('Severity', '-').strip()} "
        f"| {f'[poc]({cve}/poc)' if has_poc else '-'} |"
    )

table = "\n".join([
    "| CVE | Product | Class | Severity | PoC |",
    "|-----|---------|-------|----------|-----|",
    *(rows or ["| _none yet_ | | | | |"]),
])

readme = ROOT / "README.md"
readme.write_text(
    re.sub(
        re.escape(START) + ".*?" + re.escape(END),
        lambda _: f"{START}\n{table}\n{END}",
        readme.read_text(encoding="utf-8"),
        flags=re.DOTALL,
    ),
    encoding="utf-8",
)

print(f"README.md updated: {len(rows)} advisories")
