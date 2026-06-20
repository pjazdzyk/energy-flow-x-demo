"""
Ladybug Tools reference: direct sun-hours on the comparison test box.

Computes the reference values for the IFC Lens vs Ladybug comparison
(see ladybug-comparison-protocol.md), using the Ladybug Tools Python library
(`ladybug`) for the sun positions — the same Sunpath / NREL-based engine the
Grasshopper "Direct Sun Hours" component uses. Opaque-box shadowing is a
ray / axis-aligned-box intersection (the Direct Sun Hours method = sun vectors
from Sunpath + geometric occlusion).

Run (after `pip install ladybug-core ladybug-geometry`):
    python ladybug_reference.py

Scene (metres, +X east, +Y north, +Z up):
    box  X[-10,10]  Y[-5,5]  Z[0,15]  (opaque, no glazing)
    site Warsaw 52.23N 21.01E, date 20 March (equinox), whole day, 5-min step.
"""

from ladybug.sunpath import Sunpath

LAT, LON, TZ = 52.23, 21.01, 1  # Warsaw, standard time (whole-day total is TZ-independent)
MONTH, DAY = 3, 20
STEP_MIN = 5

# Axis-aligned opaque box.
BOX_MIN = (-10.0, -5.0, 0.0)
BOX_MAX = (10.0, 5.0, 15.0)

# Ground sample points (X, Y, Z) — north of the box is where the shadow falls.
POINTS = {
    "G (0,6)  1m N of face": (0.0, 6.0, 0.0),
    "A (0,8)  3m N": (0.0, 8.0, 0.0),
    "B (0,12) 7m N": (0.0, 12.0, 0.0),
    "C (0,20) 15m N": (0.0, 20.0, 0.0),
    "D (0,35) 30m N": (0.0, 35.0, 0.0),
    "E (30,0) 25m E": (30.0, 0.0, 0.0),
    "F (0,-10) S side": (0.0, -10.0, 0.0),
    "OPEN ref (no box)": (200.0, 200.0, 0.0),  # far away → unobstructed daylight
}

EPS = 1e-9


def ray_hits_box(origin, direction):
    """Slab-method ray vs axis-aligned box. Returns True if the forward ray from
    `origin` along unit `direction` pierces the box (t > 0)."""
    tmin, tmax = -float("inf"), float("inf")
    for i in range(3):
        o, d = origin[i], direction[i]
        lo, hi = BOX_MIN[i], BOX_MAX[i]
        if abs(d) < EPS:
            if o < lo - EPS or o > hi + EPS:
                return False  # parallel and outside this slab
        else:
            t1, t2 = (lo - o) / d, (hi - o) / d
            if t1 > t2:
                t1, t2 = t2, t1
            tmin = max(tmin, t1)
            tmax = min(tmax, t2)
            if tmin > tmax:
                return False
    return tmax > EPS and tmax >= tmin


def main():
    sp = Sunpath(LAT, LON, time_zone=TZ)
    weight_h = STEP_MIN / 60.0

    # Collect daylight sun vectors (toward the sun) across the calendar day.
    suns = []
    minute = 0
    while minute < 24 * 60:
        sun = sp.calculate_sun(MONTH, DAY, minute / 60.0)
        if sun.altitude > 0:
            v = sun.sun_vector_reversed  # points TOWARD the sun
            suns.append((v.x, v.y, v.z, sun.altitude, sun.azimuth))
        minute += STEP_MIN

    daylight_h = len(suns) * weight_h
    alts = [s[3] for s in suns]
    print(f"Ladybug Sunpath: {len(suns)} daylight samples @ {STEP_MIN} min "
          f"= {daylight_h:.2f} h daylight; max alt {max(alts):.2f} deg")

    print(f"\n{'point':<22}{'sun-hours':>10}{'% daylight':>12}")
    print("-" * 44)
    for name, p in POINTS.items():
        lit_h = 0.0
        for (vx, vy, vz, _alt, _az) in suns:
            if vz <= 0:
                continue
            if not ray_hits_box(p, (vx, vy, vz)):
                lit_h += weight_h
        pct = 100.0 * lit_h / daylight_h if daylight_h else 0.0
        print(f"{name:<22}{lit_h:>10.3f}{pct:>11.1f}%")


if __name__ == "__main__":
    main()
