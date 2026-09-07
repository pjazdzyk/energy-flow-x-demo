/**
 * PVGIS reference: annual clear-sky global horizontal irradiation, kWh/m2.
 *
 * Fetches the REFERENCE side of the clear-sky cross-check documented in ../README.md, from PVGIS
 * (the EU Joint Research Centre tool), whose clear-sky irradiance comes from the McClear model.
 *
 * THIS SCRIPT PRODUCES THE REFERENCE ONLY, deliberately. The EnergyFlowX side is not recomputed
 * here: it is integrated live, in the browser, on the Validation page, and pinned in the product's
 * own test suite (see "Reproduce it" in ../README.md). A comparison script that computes both
 * columns proves only that it agrees with itself, and the moment it is committed alongside its own
 * output it stops being able to fail. So this fetches one column, and the product computes the
 * other independently.
 *
 * Requires network access and nothing else: plain Node 18+, no dependencies.
 *
 *   node pvgis_reference.mjs
 *
 * The output includes ../scene/pvgis-reference.csv in its exact committed form, so a re-run can be
 * diffed against the recorded reference rather than read off by eye.
 */

/** The three sites, chosen to span latitude, altitude and climate rather than to flatter a model. */
const SITES = [
  { name: 'Warsaw', lat: 52.23, lon: 21.01, elevationM: 119 },
  { name: 'Madrid', lat: 40.42, lon: -3.7, elevationM: 667 },
  { name: 'Rome', lat: 41.9, lon: 12.5, elevationM: 21 },
]

const DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
const sum = (a) => a.reduce((x, y) => x + y, 0)

/**
 * PVGIS annual clear-sky GHI (kWh/m2) on the horizontal.
 *
 * DRcalc returns, per month, the average-day hourly clear-sky global irradiance Gcs(i) in W/m2.
 * Summed over the 24 hourly steps that is Wh/m2 for the average day; times the days in the month,
 * summed over the year and divided by 1000, kWh/m2.
 */
async function pvgisAnnualClearSkyKWh(site) {
  const monthlyKWh = []
  for (let m = 1; m <= 12; m += 1) {
    const url =
      `https://re.jrc.ec.europa.eu/api/v5_2/DRcalc?lat=${site.lat}&lon=${site.lon}` +
      `&month=${m}&global=1&clearsky=1&outputformat=json`
    const res = await fetch(url)
    if (!res.ok) throw new Error(`PVGIS DRcalc ${site.name} month ${m}: HTTP ${res.status}`)
    const json = await res.json()
    const rows = json.outputs.daily_profile
    /* A SHAPE CHECK, not politeness. DRcalc's average day is 24 hourly steps; if the endpoint ever
       returns a half-hourly profile the sum below silently doubles, and a 100% error would arrive
       looking like a plausible number. */
    if (rows.length !== 24) {
      throw new Error(
        `PVGIS returned ${rows.length} steps for ${site.name} month ${m}, expected 24 hourly ` +
          `steps. The integration below assumes hourly and would be wrong.`
      )
    }
    monthlyKWh.push((sum(rows.map((r) => r['Gcs(i)'])) * DAYS_IN_MONTH[m - 1]) / 1000)
  }
  return { annualKWh: sum(monthlyKWh), monthlyKWh }
}

async function main() {
  console.log('PVGIS v5.2 DRcalc, clear-sky (McClear) - annual GLOBAL HORIZONTAL irradiation\n')
  const results = []
  for (const site of SITES) {
    const { annualKWh, monthlyKWh } = await pvgisAnnualClearSkyKWh(site)
    results.push({ site, annualKWh, monthlyKWh })
    console.log(`${site.name} (${site.lat}, ${site.lon}, ${site.elevationM} m)`)
    console.log(`  annual clear-sky GHI : ${annualKWh.toFixed(1)} kWh/m2`)
    console.log(`  by month (kWh/m2)    : ${monthlyKWh.map((v) => v.toFixed(1)).join(', ')}\n`)
  }

  console.log('--- ../scene/pvgis-reference.csv form ---')
  console.log('site,lat,lon,elevation_m,annual_clear_sky_ghi_kwh_m2')
  for (const { site, annualKWh } of results) {
    console.log(`${site.name},${site.lat},${site.lon},${site.elevationM},${annualKWh.toFixed(1)}`)
  }
}

main().catch((e) => {
  console.error('PVGIS reference failed:', e.message)
  process.exit(1)
})
