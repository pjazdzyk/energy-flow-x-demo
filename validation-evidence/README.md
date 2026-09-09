# Validation evidence

Documented, reproducible validation evidence for EnergyFlowX tools. Each folder holds a
controlled test case, the result of an independent reference, the EnergyFlowX result on the same
case, and everything needed to reproduce both (scene files, scripts, dependencies, and step by
step instructions).

The goal is that any engineer can take a folder, run the same check, and confirm the numbers
rather than trust a claim.

## Index

| Area | Module | What it shows | Automated |
| --- | --- | --- | --- |
| [ifc_lens](ifc_lens/solar_module) | Solar, geometry | Direct sun hours match Ladybug Tools on a controlled box scene | yes, re-run on every commit |
| [ifc_lens](ifc_lens/solar_module/clear_sky_irradiation) | Solar, irradiation | Annual clear sky irradiation agrees with PVGIS, an independent clear sky model, and our clarity band brackets it | yes, re-run on every commit |
| [ifc_lens](ifc_lens/solar_module/row_shading) | PV, shading | Ray-traced inter-row shading converges onto a closed form for the one geometry that has one, and the residual is the panel's own thickness | yes, re-run on every commit |

More modules and tools will be added here as they mature.

## A note on what "validated" means here

A case in this folder is only evidence if someone else can re-run it and get the same answer, so
each one records the reference in a form that cannot drift: exact counts rather than rounded
figures, with the script and pinned dependencies that produced them. Where the EnergyFlowX side can
be recomputed without a browser, it is also wired into the product's own test suite, so the
comparison fails loudly if the engine moves rather than sitting here going stale.

**Both sides get re-run, not just ours.** A reference nobody ever re-executes is a number, not a
reference: it can be a transcription slip, or a figure from a version of a tool that no longer
behaves that way, and the comparison against it would look immaculate either way. Each case records
when its reference was last regenerated from the original source, and against which version.

**The reference scripts here compute the reference only.** A comparison script that computes both
columns and is committed beside its own output can no longer fail, so the EnergyFlowX column always
comes from the product, independently, by a route each case documents.

Cases carry their tolerance and the reason for it. "Agrees to within one sampling step" is a claim
about what the comparison can resolve; "agrees closely" is not a claim at all.

## How each case is structured

- `figures/` the reference result and the EnergyFlowX result, side by side.
- `scene/` the input geometry and any read points.
- `scripts/` the code and dependencies to reproduce the reference and rebuild the scene.
- `README.md` the method, the result table, and reproduction steps.

See the [repository root README](../README.md) for the project, licensing, and citation terms.
</content>
