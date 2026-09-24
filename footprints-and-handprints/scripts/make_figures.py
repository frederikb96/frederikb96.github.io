"""Generate all figures for the footprint white paper.

Every figure is built from the CSV files in ../data (primary-source downloads)
or from constants that carry their source in the comment above them.
"""

from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)

# Okabe-Ito derived categorical order, validated for CVD separation
# (validate_palette.js: all checks pass, contrast WARN answered by direct labels).
C = {
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "green": "#009E73",
    "orange": "#E69F00",
    "sky": "#56B4E9",
    "purple": "#CC79A7",
    "grey": "#6E6E6E",
    "ink": "#1A1A1A",
    "muted": "#767676",
    "grid": "#DCDCDC",
    "surface": "#FFFFFF",
}
ORDER = [C["blue"], C["vermillion"], C["green"], C["orange"], C["sky"], C["purple"]]

mpl.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.edgecolor": C["grid"],
        "axes.labelcolor": C["muted"],
        "axes.titlesize": 10,
        "axes.titleweight": "bold",
        "axes.titlecolor": C["ink"],
        "axes.grid": True,
        "grid.color": C["grid"],
        "grid.linewidth": 0.6,
        "xtick.color": C["muted"],
        "ytick.color": C["muted"],
        "legend.frameon": False,
        "legend.fontsize": 8,
        "lines.linewidth": 2.0,
    }
)


def clean(ax, spines=("top", "right")):
    for s in spines:
        ax.spines[s].set_visible(False)
    ax.set_axisbelow(True)


def save(fig, name):
    fig.savefig(FIG / f"{name}.pdf")
    plt.close(fig)
    print("wrote", name)


def owid(fname):
    out = {}
    with open(DATA / fname) as fh:
        for row in csv.reader(fh):
            if row[0] == "Entity" or len(row) < 4:
                continue
            try:
                out.setdefault(row[0], {})[int(row[2])] = float(row[3])
            except ValueError:
                continue
    return out


def gfn():
    out = {}
    with open(DATA / "gfn_series.csv") as fh:
        for r in csv.DictReader(fh):
            out.setdefault((r["entity"], r["record"]), {})[int(r["year"])] = r
    return out


# --- F1: the German consumer-calculator breakdown -------------------------
# UBA CO2-Rechner averages as published by BMUKN / Kompetenzzentrum
# Nachhaltiger Konsum, status 2025; reproduced via greenpeace.de.
def fig_breakdown():
    items = [
        ("Other consumption", 2.9, "clothing, electronics, furniture,\nservices, capital investment"),
        ("Housing", 2.2, "space heating, hot water,\nrent, construction"),
        ("Mobility", 2.0, "car, rail, flights\n(private travel only)"),
        ("Food", 1.6, "incl. restaurants,\nexcl. pet food"),
        ("Public infrastructure", 1.2, "state, health, education,\nwater, waste, civil engineering"),
        ("Electricity", 0.5, "household electricity\nonly"),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ys = range(len(items))
    vals = [v for _, v, _ in items]
    bars = ax.barh(list(ys), vals, height=0.62, color=ORDER, zorder=3)
    ax.set_yticks(list(ys), [n for n, _, _ in items])
    for bar, (_, v, note) in zip(bars, items):
        ax.text(v + 0.08, bar.get_y() + bar.get_height() / 2, f"{v:.1f} t",
                va="center", ha="left", fontsize=9, color=C["ink"], fontweight="bold")
        ax.text(v + 0.62, bar.get_y() + bar.get_height() / 2, note,
                va="center", ha="left", fontsize=6.5, color=C["muted"])
    ax.axvline(1.0, color=C["ink"], lw=1.2, ls=(0, (4, 3)), zorder=4)
    ax.text(1.08, -0.5, "long-run target: well below 1 t CO$_2$e", fontsize=7.5,
            color=C["ink"], va="center", linespacing=1.4)
    ax.set_xlim(0, 5.6)
    ax.set_ylim(6.1, -0.6)
    ax.set_xlabel("t CO$_2$e per person and year")
    ax.set_title("Germany: 10.4 t CO$_2$e per person, as a consumer calculator splits it")
    ax.grid(axis="y", visible=False)
    clean(ax)
    save(fig, "f1-breakdown")


# --- F2: one country, four legitimate numbers -----------------------------
def fig_four_numbers():
    bars = [
        ("Territorial\nCO$_2$ only\n(2024)", 6.77, C["sky"],
         "produced inside the border,\nCO$_2$ alone"),
        ("Territorial\nall GHG\n(2025)", 7.77, C["blue"],
         "649 Mt CO$_2$e / 83.5 m people,\nexcl. LULUCF"),
        ("Consumption-\nbased CO$_2$\n(2023)", 9.09, C["green"],
         "trade-adjusted,\nCO$_2$ alone"),
        ("Consumer\ncalculator\n(2025)", 10.4, C["vermillion"],
         "trade-adjusted, all GHG,\n+ aviation non-CO$_2$"),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 3.3))
    xs = range(len(bars))
    rects = ax.bar(list(xs), [b[1] for b in bars], width=0.56,
                   color=[b[2] for b in bars], zorder=3)
    for r, b in zip(rects, bars):
        ax.text(r.get_x() + r.get_width() / 2, b[1] + 0.15, f"{b[1]:.2f}", ha="center",
                fontsize=10, fontweight="bold", color=C["ink"])
        ax.text(r.get_x() + r.get_width() / 2, -2.55, b[3], ha="center", fontsize=6.4,
                color=C["muted"], linespacing=1.5, va="top")
    ax.set_xticks(list(xs), [b[0] for b in bars], fontsize=8)
    ax.axhline(1.0, color=C["ink"], lw=1.2, ls=(0, (4, 3)), zorder=4)
    ax.text(3.42, 1.2, "well below 1 t", fontsize=7.5, color=C["ink"], ha="right")
    ax.set_ylabel("t per person and year")
    ax.set_ylim(0, 12)
    ax.set_title("Four defensible per-capita numbers for the same country")
    ax.grid(axis="x", visible=False)
    clean(ax)
    save(fig, "f2-four-numbers")


# --- F3: territorial vs consumption-based, Germany and the world ----------
def fig_trade_gap():
    terr, cons = owid("owid-co2pc.csv"), owid("owid-cons-co2pc.csv")
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    series = [
        ("Germany, consumption-based", cons["Germany"], C["vermillion"], "-"),
        ("Germany, territorial", terr["Germany"], C["blue"], "-"),
        ("World average", terr["World"], C["grey"], (0, (5, 2))),
    ]
    for label, d, color, ls in series:
        ys = sorted(y for y in d if 1990 <= y <= 2024)
        ax.plot(ys, [d[y] for y in ys], color=color, ls=ls, label=label, zorder=3)
        last = ys[-1]
        ax.annotate(f"{d[last]:.1f}", (last, d[last]), xytext=(5, -3),
                    textcoords="offset points", fontsize=8, color=color, fontweight="bold")
    g_years = sorted(y for y in cons["Germany"] if 1990 <= y <= 2023)
    ax.fill_between(g_years, [terr["Germany"][y] for y in g_years],
                    [cons["Germany"][y] for y in g_years], color=C["vermillion"],
                    alpha=0.12, zorder=2, label="emissions embodied in net imports")
    ax.set_ylabel("t CO$_2$ per person and year")
    ax.set_xlim(1990, 2027)
    ax.set_ylim(0, 16)
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.set_title("The trade gap: what Germany emits vs. what Germany consumes")
    ax.legend(loc="upper right")
    clean(ax)
    save(fig, "f3-trade-gap")


# --- F4: country comparison, both accounting bases ------------------------
def fig_countries():
    terr, cons = owid("owid-co2pc.csv"), owid("owid-cons-co2pc.csv")
    names = ["Qatar", "United States", "Germany", "China", "France", "World", "India"]
    year = 2023
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    xs = range(len(names))
    w = 0.38
    t_vals = [terr[n][year] for n in names]
    c_vals = [cons[n][year] for n in names]
    b1 = ax.bar([x - w / 2 for x in xs], t_vals, w, color=C["blue"],
                label="territorial (produced here)", zorder=3)
    b2 = ax.bar([x + w / 2 for x in xs], c_vals, w, color=C["vermillion"],
                label="consumption-based (consumed here)", zorder=3)
    for rects, vals in ((b1, t_vals), (b2, c_vals)):
        for r, v in zip(rects, vals):
            ax.text(r.get_x() + r.get_width() / 2, v + 0.4, f"{v:.1f}", ha="center",
                    fontsize=7, color=C["ink"])
    ax.set_xticks(list(xs), names, fontsize=8)
    ax.set_ylabel(f"t CO$_2$ per person, {year}")
    ax.set_ylim(0, 45)
    ax.set_title("Rich countries import emissions; workshop countries export them")
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper right")
    clean(ax)
    save(fig, "f4-countries")


# --- F5: carbon inequality (Chancel 2022, Nature Sustainability) ----------
def fig_inequality():
    # Shares from Chancel (2022). The per-person figures are the shares divided
    # by each group's population share, i.e. multiples of the world average.
    groups = [
        ("Bottom 50%", 12, 0.24, C["sky"]),
        ("Middle 40%", 40, 1.0, C["blue"]),
        ("Top 10%", 48, 4.8, C["vermillion"]),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 1.9))
    left = 0.0
    for name, share, percap, color in groups:
        ax.barh([0], [share], left=left, height=0.5, color=color, zorder=3,
                edgecolor="white", linewidth=2)
        txt = f"{name}\n{share:.0f}% of emissions\n{percap}$\\times$ the world average"
        if share < 20:
            ax.annotate(txt, (left + share / 2, 0.28), xytext=(left + share / 2, 0.62),
                        ha="center", va="bottom", fontsize=7.6, color=color,
                        fontweight="bold", linespacing=1.5,
                        arrowprops=dict(arrowstyle="-", color=color, lw=1))
        else:
            ax.text(left + share / 2, 0, txt, ha="center", va="center", fontsize=7.6,
                    color="white", fontweight="bold", linespacing=1.5)
        left += share
    ax.set_xlim(0, 100)
    ax.set_ylim(-0.42, 1.35)
    ax.set_yticks([])
    ax.set_xlabel("share of global greenhouse gas emissions, 2019 (%)")
    ax.set_title("Income, not nationality, is the strongest predictor of a footprint")
    ax.grid(visible=False)
    clean(ax, ("top", "right", "left"))
    save(fig, "f5-inequality")


# --- F6: Germany's Ecological Footprint by land type ----------------------
def fig_ef_germany():
    g = gfn()
    ef = g[("Germany", "EFConsPerCap")]
    bc = g[("Germany", "BiocapPerCap")]
    years = [y for y in sorted(ef) if y <= 2023]
    comps = [("carbon", "Carbon (forest area to absorb CO$_2$)", C["blue"]),
             ("cropland", "Cropland", C["orange"]),
             ("forest", "Forest products", C["green"]),
             ("grazing", "Grazing land", C["purple"]),
             ("builtup", "Built-up land", C["grey"]),
             ("fishing", "Fishing grounds", C["sky"])]
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    stacks = [[float(ef[y][k]) for y in years] for k, _, _ in comps]
    ax.stackplot(years, *stacks, labels=[lab for _, lab, _ in comps],
                 colors=[c for _, _, c in comps], zorder=3, edgecolor="white", linewidth=0.4)
    ax.plot(years, [float(bc[y]["total"]) for y in years], color=C["vermillion"], lw=2.2,
            zorder=5, label="Germany's own biocapacity")
    ax.set_ylabel("global hectares per person")
    ax.set_xlim(1961, 2023)
    ax.set_ylim(0, 7.5)
    ax.set_title("Germany's Ecological Footprint is mostly a carbon number in disguise")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=4, fontsize=7)
    clean(ax)
    save(fig, "f6-ef-germany")


# --- F7: world footprint vs biocapacity, in Earths ------------------------
def fig_earths():
    g = gfn()
    ef = g[("World", "EFConsPerCap")]
    bc = g[("World", "BiocapPerCap")]
    years = sorted(ef)
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    ax.plot(years, [float(ef[y]["total"]) for y in years], color=C["vermillion"],
            label="humanity's Ecological Footprint", zorder=4)
    ax.plot(years, [float(bc[y]["total"]) for y in years], color=C["green"],
            label="Earth's biocapacity", zorder=4)
    cross = [y for y in years if float(ef[y]["total"]) > float(bc[y]["total"])][0]
    ax.axvline(cross, color=C["ink"], lw=1.0, ls=(0, (3, 3)), zorder=3)
    ax.annotate(f"overshoot begins\n({cross})", (cross, 3.3), xytext=(6, 0),
                textcoords="offset points", fontsize=7.5, color=C["ink"])
    last = years[-1]
    ratio = float(ef[last]["total"]) / float(bc[last]["total"])
    ax.annotate(f"{ratio:.2f} Earths ({last})", (last, float(ef[last]["total"])),
                xytext=(-10, 12), textcoords="offset points", fontsize=8,
                color=C["vermillion"], fontweight="bold", ha="right")
    ax.set_ylabel("global hectares per person")
    ax.set_xlim(1961, last)
    ax.set_ylim(0, 4.2)
    ax.set_title("Demand crossed supply around 1970 and never came back")
    ax.legend(loc="upper right")
    clean(ax)
    save(fig, "f7-earths")


# --- F8: Earth Overshoot Day, recalculated series -------------------------
# Global Footprint Network, recalculated with the 2026 edition of the accounts.
EOD = {
    1972: "12-31", 1975: "12-12", 1980: "11-29", 1985: "11-17", 1990: "10-23",
    1995: "10-17", 2000: "09-23", 2005: "09-01", 2010: "08-15", 2015: "08-12",
    2019: "08-06", 2020: "08-18", 2021: "08-05", 2022: "08-02", 2023: "08-02",
    2024: "08-01", 2025: "08-01", 2026: "07-30",
}


def fig_overshoot():
    years = sorted(EOD)
    doys = [dt.date(y, *map(int, EOD[y].split("-"))).timetuple().tm_yday for y in years]
    fig, ax = plt.subplots(figsize=(6.6, 2.8))
    ax.plot(years, doys, color=C["vermillion"], marker="o", markersize=4, zorder=4)
    ax.axhline(365, color=C["green"], lw=1.2, ls=(0, (4, 3)), zorder=3)
    ax.text(1974, 352, "one planet's worth of regeneration", fontsize=7.5, color=C["green"])
    ax.annotate("30 July 2026", (2026, doys[-1]), xytext=(-8, -14),
                textcoords="offset points", fontsize=8, color=C["vermillion"],
                fontweight="bold", ha="right")
    month_starts = [dt.date(2025, m, 1).timetuple().tm_yday for m in (8, 9, 10, 11, 12)]
    ax.set_yticks(month_starts + [365], ["1 Aug", "1 Sep", "1 Oct", "1 Nov", "1 Dec", "31 Dec"])
    ax.set_ylim(200, 375)
    ax.set_xlim(1970, 2029)
    ax.set_title("Earth Overshoot Day, recalculated on one consistent method")
    clean(ax)
    save(fig, "f8-overshoot")


# --- F9: what a personal reduction can and cannot reach -------------------
def fig_levers():
    # Ivanova et al. 2020 medians; Wynes & Nicholas 2017 for the flight figure.
    levers = [
        ("Live car-free", 2.4, C["blue"]),
        ("Avoid one transatlantic return flight", 1.6, C["blue"]),
        ("Switch to renewable electricity", 1.6, C["blue"]),
        ("Refurbish / renovate the home", 0.9, C["blue"]),
        ("Adopt a plant-based diet", 0.8, C["blue"]),
        ("Comprehensive recycling", 0.2, C["grey"]),
        ("Change lightbulbs", 0.1, C["grey"]),
    ]
    fig, ax = plt.subplots(figsize=(6.6, 2.9))
    ys = range(len(levers))
    ax.barh(list(ys), [v for _, v, _ in levers], height=0.6,
            color=[c for _, _, c in levers], zorder=3)
    for y, (_, v, _) in zip(ys, levers):
        ax.text(v + 0.05, y, f"{v:.1f} t", va="center", fontsize=8, color=C["ink"],
                fontweight="bold")
    ax.set_yticks(list(ys), [n for n, _, _ in levers])
    ax.set_ylim(6.6, -1.15)
    ax.set_xlim(0, 3.0)
    ax.set_xlabel("annual saving, t CO$_2$e per person")
    ax.set_title("What the largest private actions are each worth per year")
    ax.grid(axis="y", visible=False)
    clean(ax)
    save(fig, "f9-levers")


if __name__ == "__main__":
    fig_breakdown()
    fig_four_numbers()
    fig_trade_gap()
    fig_countries()
    fig_inequality()
    fig_ef_germany()
    fig_earths()
    fig_overshoot()
    fig_levers()
