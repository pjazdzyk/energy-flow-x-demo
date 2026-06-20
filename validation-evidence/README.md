# Validation evidence

Documented, reproducible validation evidence for EnergyFlowX tools. Each folder holds a
controlled test case, the result of an independent reference, the EnergyFlowX result on the same
case, and everything needed to reproduce both (scene files, scripts, dependencies, and step by
step instructions).

The goal is that any engineer can take a folder, run the same check, and confirm the numbers
rather than trust a claim.

## Index

| Area | Module | What it shows |
| --- | --- | --- |
| [ifc_lens](ifc_lens/solar_module) | Solar | Direct sun hours match Ladybug Tools on a controlled box scene |

More modules and tools will be added here as they mature.

## How each case is structured

- `figures/` the reference result and the EnergyFlowX result, side by side.
- `scene/` the input geometry and any read points.
- `scripts/` the code and dependencies to reproduce the reference and rebuild the scene.
- `README.md` the method, the result table, and reproduction steps.

See the [repository root README](../README.md) for the project, licensing, and citation terms.
</content>
