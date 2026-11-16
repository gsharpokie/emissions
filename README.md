# Who Emits the Carbon?

An interactive guess-first activity about carbon dioxide emissions: which countries emit the most in total, per person, and over history; whether any countries have cut emissions while their economies grew; and where world emissions are heading. Students make nine guesses, then see the answers from the Global Carbon Budget. By Gwen Sharp.

**Live site:** https://gsharpokie.github.io/emissions/

## What it does

- **Nine guesses** (sliders and multiple choice), each followed by bars showing the answer.
- **An interactive line chart** for the U.S., U.K., EU, China, India, and the world, with four views students can switch between: emissions **per person**, **total per year**, **total since 1750** (a running total), and **per dollar of GDP** (1950–2022). Move across the chart or drag the “Pick a year” slider, and the boxes under the chart show each figure for that year. In the two “total” views and the GDP view the world line isn’t drawn (too large for the scale, or too few years of data), but its value appears in the boxes.
- **All nine answers** in one place.
- **The fuller picture:** three ways of counting (total, per person, historical), how emissions can fall while economies grow, the 22 countries that did it, progress and how far there is to go, the unequal footprint, and connections to economics, political science, and geography.
- **Discussion questions.**

## For instructors

To skip the guesses and show the chart and all the answers, add `#answers` (or `#charts`) to the link: https://gsharpokie.github.io/emissions/#answers

## Data

- **Emissions:** Global Carbon Project, Global Carbon Budget 2026, as compiled by Our World in Data (`owid-co2-data.csv` from https://github.com/owid/co2-data, downloaded November 14, 2026; CC BY 4.0). Fossil fuel and industry CO₂ only (no other greenhouse gases, no land-use change). Production-based unless noted; consumption-based figures run 1990–2024. Per-person figures are in metric tons (t; about 2,200 pounds), written as “metric tons” on the page because most U.S. readers haven’t seen “tonnes.”
- **GDP:** Maddison Project Database 2023 (Bolt and van Zanden), via the same Our World in Data file. Ends in 2022, so the growth comparisons run 2005–2022.
- **2026 projection and clean-energy offset:** Hausfather and Friedlingstein, “Analysis: Fossil-Fuel CO₂ Emissions Set to Dip in 2026 as Iran Conflict Hits Oil Use,” *Carbon Brief*, Nov. 10, 2026; University of Exeter news release, “Fossil CO₂ Emissions Decrease in 2026,” Nov. 10, 2026.

Key figures used:

| Figure | Value |
|---|---|
| Share of world CO₂, 2005 → 2025 | China 20.0% → 31.8%; U.S. 20.7% → 12.9%; India 8.2% and EU 6.2% (2025) |
| Per person, 2025 | U.S. 14.5 t; China 8.8; EU 5.4; world 4.7; India 2.2; low-income countries 0.3 (EU 8.6 and China 4.5 in 2005) |
| Share of cumulative CO₂ since 1750 | U.S. 23.3%; EU 16.1%; China 15.8%; Russia 6.5%; U.K. 4.3%; India 3.7%; Africa 3.0% |
| U.S. per person | peak 21.5 t (1973); 20.7 (2005); 14.5 (2025) |
| U.K. per person | peak 12.0 t (1971); 9.4 (2005); 4.6 (2025) |
| U.S. 2005–2022 | GDP +33%; CO₂ −17% |
| Countries (pop. > 1 million) with GDP up and both production- and consumption-based CO₂ down at least 5%, 2005–2022 | 22 |
| U.K. 2024 | produced 4.6 t per person; consumed 7.1 t (12.6 in 2005) |
| World fossil CO₂ growth | 2005–2015 +20%; 2015–2025 +10%; 2025 a record |
| Low-income countries, 2025 | 9.3% of people; 0.55% of CO₂ |

Claims on the page that come from general knowledge rather than this dataset: China passing the U.S. in the mid-2000s (the dataset shows 2006); the U.K. closing its last coal power plant in 2024; coal-to-gas switching and renewables as the main driver of the U.S. drop; the general explanations for decoupling; and the environmental Kuznets curve.

## Updating

The Global Carbon Budget comes out each November. To update:

1. Download the latest `owid-co2-data.csv` (see the README at https://github.com/owid/co2-data for the current download link).
2. Run `python3 tools/check_figures.py path/to/owid-co2-data.csv`. It prints every figure the page uses, the list of decoupling countries, and a new `DATA` line for the chart.
3. Update the numbers in `const Q` and `const DATA` in `index.html`, and the matching sentences in “The fuller picture.” If the latest year changes, update the chart’s end year (`CH.y1` and each `end` and title in `const VIEWS`) and the years in the question text.

## Turning on the site (one time)

Go to **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the **main** branch and the **/ (root)** folder, and select **Save**. Keep Issues turned on so the “Suggest a correction” link works.

## Accessibility

This site aims to meet [WCAG 2.1](https://www.w3.org/TR/WCAG21/) Level AA, so it works for people who use screen readers, keyboards, or screen magnification.

- All buttons, sliders, and links can be reached and used with a keyboard, and show a visible outline when selected.
- Charts have text descriptions, and many also have a data table or a slider that reads out each value.
- Text meets WCAG AA color contrast standards.
- Pages fit narrow phone screens without sideways scrolling.

I checked it in November 2026 with automated accessibility testing (axe-core) plus keyboard and small-screen checks. It hasn’t yet been tested by people who use screen readers every day, so there may be problems I haven’t caught. If something doesn’t work for you, please [let me know](https://github.com/gsharpokie/emissions/issues/new).

## Author

Created by Gwen Sharp ([@gsharpokie](https://x.com/gsharpokie)).

## License

© 2026 Gwen Sharp. Licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): you may share and adapt it for noncommercial purposes with credit. See [LICENSE](LICENSE). Emissions data are from the Global Carbon Project via Our World in Data (CC BY 4.0); this license covers the page’s design, text, and code.
