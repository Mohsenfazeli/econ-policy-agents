"""Reproducible pipeline for the CPI fee-indexing worked example.

Downloads Statistics Canada Table 18-10-0005-01 (Consumer Price Index, annual
average, not seasonally adjusted), extracts All-items CPI for Canada and
British Columbia, and computes the figures used in the walkthrough.

Usage:
    python fetch_cpi.py            # prints tables, writes outputs/ (gitignored)
    python fetch_cpi.py --chart    # also draws outputs/cpi_bc_canada.png (needs matplotlib)

Standard library only, except the optional chart.
"""

import argparse
import csv
import io
import json
import sys
import urllib.request
import zipfile
from datetime import date
from pathlib import Path

TABLE_ID = "18100005"
WDS_URL = f"https://www150.statcan.gc.ca/t1/wds/rest/getFullTableDownloadCSV/{TABLE_ID}/en"
GEOS = ("Canada", "British Columbia")
PRODUCT = "All-items"
START, END = 2015, 2025
HYPOTHETICAL_FEE = 100.0
OUT = Path(__file__).parent / "outputs"


def download_table() -> list[dict]:
    with urllib.request.urlopen(WDS_URL, timeout=60) as r:
        meta = json.load(r)
    if meta.get("status") != "SUCCESS":
        sys.exit(f"WDS did not return a download link: {meta}")
    with urllib.request.urlopen(meta["object"], timeout=120) as r:
        archive = zipfile.ZipFile(io.BytesIO(r.read()))
    with archive.open(f"{TABLE_ID}.csv") as f:
        return list(csv.DictReader(io.TextIOWrapper(f, encoding="utf-8-sig")))


def extract(rows: list[dict]) -> dict:
    series = {g: {} for g in GEOS}
    vectors = {}
    for row in rows:
        if row["GEO"] in GEOS and row["Products and product groups"] == PRODUCT:
            year = int(row["REF_DATE"])
            if START - 1 <= year <= END and row["VALUE"]:
                series[row["GEO"]][year] = float(row["VALUE"])
                vectors[row["GEO"]] = row["VECTOR"]
                if row["UOM"] != "2002=100":
                    sys.exit(f"Unexpected unit of measure: {row['UOM']}")
    for g in GEOS:
        missing = [y for y in range(START, END + 1) if y not in series[g]]
        if missing:
            sys.exit(f"Missing years for {g}: {missing}")
    return {"series": series, "vectors": vectors}


def pct(a: float, b: float) -> float:
    return 100.0 * (a / b - 1.0)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chart", action="store_true")
    args = parser.parse_args()

    data = extract(download_table())
    s, v = data["series"], data["vectors"]
    retrieved = date.today().isoformat()

    print(f"Source: Statistics Canada Table 18-10-0005-01, retrieved {retrieved}")
    print(f"Vectors: Canada {v['Canada']}, British Columbia {v['British Columbia']}\n")

    print("| Year | CPI Canada | CPI BC | Change Canada (%) | Change BC (%) |")
    print("| --- | --- | --- | --- | --- |")
    for y in range(START, END + 1):
        c, b = s["Canada"][y], s["British Columbia"][y]
        print(f"| {y} | {c:.1f} | {b:.1f} | {pct(c, s['Canada'][y-1]):.1f} | {pct(b, s['British Columbia'][y-1]):.1f} |")

    print(f"\nCumulative change {START} to {END}:")
    for g in GEOS:
        print(f"  {g}: {pct(s[g][END], s[g][START]):.1f}%")

    print(f"\nHypothetical ${HYPOTHETICAL_FEE:.2f} fee set in {START}, indexed annually:")
    print("| Year | Indexed to Canada CPI ($) | Indexed to BC CPI ($) | Real value of an unindexed fee, BC ({}$) |".format(START))
    print("| --- | --- | --- | --- |")
    for y in range(START, END + 1):
        ic = HYPOTHETICAL_FEE * s["Canada"][y] / s["Canada"][START]
        ib = HYPOTHETICAL_FEE * s["British Columbia"][y] / s["British Columbia"][START]
        real = HYPOTHETICAL_FEE * s["British Columbia"][START] / s["British Columbia"][y]
        print(f"| {y} | {ic:.2f} | {ib:.2f} | {real:.2f} |")

    OUT.mkdir(exist_ok=True)
    with open(OUT / "cpi_bc_canada.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "cpi_canada", "cpi_bc", "retrieved"])
        for y in range(START - 1, END + 1):
            w.writerow([y, s["Canada"][y], s["British Columbia"][y], retrieved])

    if args.chart:
        import matplotlib.pyplot as plt

        years = list(range(START, END + 1))
        fig, ax = plt.subplots(figsize=(8, 4.5))
        for g, style, dy in (("British Columbia", "-", 7), ("Canada", "--", -7)):
            vals = [pct(s[g][y], s[g][y - 1]) for y in years]
            ax.plot(years, vals, style, color="#1f3b73" if g == "British Columbia" else "#7a7a7a", linewidth=2)
            ax.annotate(g, (years[-1], vals[-1]), xytext=(6, dy), textcoords="offset points", va="center")
        ax.set_title("BC and Canada inflation moved closely together, 2015 to 2025", loc="left")
        ax.set_ylabel("Annual change in All-items CPI (%)")
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_xticks(years[::2])
        ax.set_xlim(years[0], years[-1] + 2)
        ax.set_ylim(0, None)
        fig.text(0.01, 0.01, f"Source: Statistics Canada, Table 18-10-0005-01. Annual averages, 2014 to 2025. "
                 f"Changes computed from published index values. Retrieved {retrieved}.", fontsize=7)
        fig.tight_layout(rect=(0, 0.04, 1, 1))
        fig.savefig(OUT / "cpi_bc_canada.png", dpi=150)
        print(f"\nChart written to {OUT / 'cpi_bc_canada.png'}")


if __name__ == "__main__":
    main()
