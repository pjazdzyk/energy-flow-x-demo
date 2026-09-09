"""Render the evidence figure from scene/engine-vs-closed-form.csv.

Two panels, because the case has two separate things to say:

  left   the shading curve itself. The closed form as a line, the ray tracer as points at the
         quality the product actually ships. Read this to see that the two describe the same
         physics, and that the ray-traced points sit on a staircase: the lit fraction is a mean
         over a finite grid of sub-samples, so it can only take a few discrete values.

  right  the disagreement against sub-sample count, on log axes, for a thick panel and a thin
         one. Read this to see WHY they differ. The thin curve falls toward zero, which is a
         quadrature error converging. The thick curve flattens out, and what it flattens onto
         is the panel's own 4 cm of thickness, which the closed form does not model and the
         ray tracer does.

Run:
    pip install -r requirements.txt
    python evidence_figure.py
"""

from __future__ import annotations

import csv
import pathlib
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
CSV_PATH = HERE.parent / "scene" / "engine-vs-closed-form.csv"
OUT_PATH = HERE.parent / "figures" / "row-shading-vs-closed-form.png"

INK = "#1f2933"
ACCENT = "#c2410c"
GRID = "#d7dde3"


def load(path: pathlib.Path) -> list[dict]:
    rows = []
    with path.open(newline="", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            reader = csv.DictReader([line] + fh.readlines())
            for r in reader:
                rows.append(
                    {
                        "thickness": float(r["panel_thickness_m"]),
                        "sub_n": int(r["sub_samples_per_axis"]),
                        "elevation": float(r["sun_elevation_deg"]),
                        "azimuth": float(r["sun_azimuth_deg"]),
                        "ray": float(r["ray_traced_shaded_fraction"]),
                        "closed": float(r["closed_form_shaded_fraction"]),
                        "diff": float(r["difference"]),
                    }
                )
            break
    return rows


def main() -> int:
    if not CSV_PATH.exists():
        sys.exit(f"missing {CSV_PATH}")
    rows = load(CSV_PATH)

    fig, (ax_curve, ax_conv) = plt.subplots(1, 2, figsize=(11.5, 4.4))

    # --- left: the curve itself, due south, at the quality the product ships
    south = sorted(
        (r for r in rows if r["azimuth"] == 180 and r["thickness"] == 0.04),
        key=lambda r: r["elevation"],
    )
    ref = [r for r in south if r["sub_n"] == 41]
    ax_curve.plot(
        [r["elevation"] for r in ref],
        [r["closed"] for r in ref],
        color=INK,
        lw=2,
        label="closed form (infinite thin rows)",
    )
    for sub_n, marker in ((7, "o"), (3, "s")):
        pts = [r for r in south if r["sub_n"] == sub_n]
        ax_curve.plot(
            [r["elevation"] for r in pts],
            [r["ray"] for r in pts],
            marker,
            ms=6,
            mfc="none",
            color=ACCENT if sub_n == 7 else "#6b7280",
            label=f"ray traced, {sub_n}x{sub_n} sub-samples",
        )
    ax_curve.set_xlabel("sun elevation, degrees (due south)")
    ax_curve.set_ylabel("shaded fraction of the collector slope")
    ax_curve.set_title("The same physics, sampled coarsely", loc="left", color=INK)
    ax_curve.grid(color=GRID, lw=0.8)
    ax_curve.legend(frameon=False, fontsize=9)

    # --- right: where the disagreement goes as the sampling is refined
    ax_conv.set_xscale("log")
    ax_conv.set_yscale("log")
    ax_conv.set_xticks([3, 5, 7, 21, 41, 81])
    ax_conv.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax_conv.get_xaxis().set_minor_formatter(matplotlib.ticker.NullFormatter())
    for thickness, colour, label in (
        (0.04, ACCENT, "4 cm panel (as built)"),
        (0.0004, INK, "0.4 mm panel (thickness removed)"),
    ):
        by_n: dict[int, float] = {}
        for r in rows:
            if r["thickness"] != thickness:
                continue
            by_n[r["sub_n"]] = max(by_n.get(r["sub_n"], 0.0), abs(r["diff"]))
        ns = sorted(by_n)
        ax_conv.plot(ns, [by_n[n] for n in ns], "o-", color=colour, lw=1.8, ms=5, label=label)
    ax_conv.axvspan(3, 7, color="#eef2f6", zorder=0)
    ax_conv.annotate(
        "what the\nproduct ships",
        xy=(4.6, 0.06),
        xycoords=("data", "axes fraction"),
        ha="center",
        fontsize=8,
        color="#6b7280",
    )
    ax_conv.set_xlabel("sub-samples per axis")
    ax_conv.set_ylabel("largest disagreement, shaded fraction")
    ax_conv.set_title("Sampling error converges, thickness does not", loc="left", color=INK)
    ax_conv.grid(color=GRID, lw=0.8, which="both")
    ax_conv.legend(frameon=False, fontsize=9)

    fig.tight_layout()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PATH, dpi=160)
    print(f"wrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
