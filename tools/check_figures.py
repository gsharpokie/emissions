"""Recompute the figures used on the page from Our World in Data's CO2 dataset.

Usage: download owid-co2-data.csv (https://github.com/owid/co2-data or the newer
catalog file linked from that repository's README), then run:
    python3 tools/check_figures.py path/to/owid-co2-data.csv
Compare the printed numbers with the values in `const Q` and `const SERIES` in index.html.
"""
import csv, json, sys

D = {(r["country"], int(r["year"])): r for r in csv.DictReader(open(sys.argv[1]))}
def g(c, y, k):
    v = D.get((c, y), {}).get(k, "")
    return float(v) if v else None

LAST = max(y for (c, y), r in D.items() if c == "World" and r["co2"])
print("Latest year:", LAST)
for c in ["China", "United States", "India", "European Union (27)"]:
    print(f"Share of world CO2, {c}: 2005 {g(c,2005,'co2')/g('World',2005,'co2')*100:.1f}%  {LAST} {g(c,LAST,'share_global_co2'):.1f}%")
for c in ["United States", "China", "European Union (27)", "World", "India", "Low-income countries", "United Kingdom"]:
    print(f"Per person {LAST}, {c}: {g(c,LAST,'co2_per_capita'):.2f} t")
for c in ["United States", "European Union (27)", "China", "Russia", "United Kingdom", "India", "Africa"]:
    print(f"Share of cumulative CO2 since 1750, {c}: {g(c,LAST,'share_global_cumulative_co2'):.1f}%")
for c in ["United States", "United Kingdom"]:
    s = [(y, g(c, y, "co2_per_capita")) for y in range(1750, LAST + 1) if g(c, y, "co2_per_capita") is not None]
    print(f"{c} per-person peak: {max(s, key=lambda t: t[1])}")
# Decoupling, 2005 to the last year with GDP data
GY = max(y for (c, y), r in D.items() if c == "United States" and r["gdp"])
print("Last GDP year:", GY)
print(f"U.S. GDP 2005-{GY}: {(g('United States',GY,'gdp')/g('United States',2005,'gdp')-1)*100:+.0f}%, CO2: {(g('United States',GY,'co2')/g('United States',2005,'co2')-1)*100:+.0f}%")
res = []
for c in {c for (c, y), r in D.items() if r["iso_code"] and len(r["iso_code"]) == 3}:
    v = [g(c, 2005, "gdp"), g(c, GY, "gdp"), g(c, 2005, "co2"), g(c, GY, "co2"),
         g(c, 2005, "consumption_co2"), g(c, GY, "consumption_co2"), g(c, GY, "population")]
    if None in v: continue
    ga, gb, ca, cb, ka, kb, p = v
    if gb > ga and cb <= ca * .95 and kb <= ka * .95 and p > 1e6: res.append(c)
print(f"Countries (pop > 1M) with GDP up and production and consumption CO2 both down 5%+ (2005-{GY}): {len(res)}")
print(", ".join(sorted(res)))
CY = max(y for (c, y), r in D.items() if c == "United Kingdom" and r["consumption_co2_per_capita"])
print(f"U.K. {CY}: produced {g('United Kingdom',CY,'co2_per_capita'):.2f} t, consumed {g('United Kingdom',CY,'consumption_co2_per_capita'):.2f} t; consumed 2005 {g('United Kingdom',2005,'consumption_co2_per_capita'):.2f} t")
w = lambda y: g("World", y, "co2")
print(f"World growth 2005-2015: {(w(2015)/w(2005)-1)*100:.1f}%; {LAST-10}-{LAST}: {(w(LAST)/w(LAST-10)-1)*100:.1f}%")
print(f"Low-income countries {LAST}: {g('Low-income countries',LAST,'population')/g('World',LAST,'population')*100:.1f}% of people, {g('Low-income countries',LAST,'share_global_co2'):.2f}% of CO2")
series = {c: [round(g(c, y, "co2_per_capita"), 1) for y in range(1950, LAST + 1)]
          for c in ["United States", "United Kingdom", "China", "India", "European Union (27)", "World"]}
print("SERIES (paste into index.html; the chart assumes the series start in 1950 and end in", LAST, "):")
print(json.dumps(series, separators=(",", ":")))
