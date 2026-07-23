# AI-Architecture-Research

AI-assisted workflow for architectural spatial optimization — turning pedestrian behavior data into ranked, evaluable design proposals.

> ⚠️ **Status: research prototype (partial).** Data ingestion and evaluation are functional; generative-AI inference is currently a stub (see honest notes below).

## What's implemented

- **`data_processing.py` — `BehaviorDataProcessor`**
  Loads and cleans pedestrian-flow CSV/JSON, handles NaN/clipping, and bins movement into a 10×10 gridded flow matrix.
- **`evaluation.py` — `DesignEvaluator`**
  Weighted proposal scoring + ranking (weights 30 / 25 / 25 / 20 across circulation, adjacency, daylight, program fit). Produces a ranked shortlist.
- **`research/`**
  Written statement, literature review, and an experimental log documenting the method.

## Honest notes (what is NOT yet real)

- **`ai_generation.py` is a stub.** It currently prints design prompts and returns placeholder filenames — it does **not** run Stable Diffusion / ControlNet inference. The intended SDXL + ControlNet generation pipeline is planned but not implemented.
- **`spatial_analysis.py`** implements only one metric (`compute_circulation`, entropy-based); other `SpatialMetrics` fields are declared but not yet computed.
- **BIM integration** (Revit / IFC export) is described in docs but not in code yet.
- **CI:** `.github/workflows/django.yml` was misconfigured (referenced Django, which this repo does not use) and has been removed.

## Intended pipeline

```
behavior CSV/JSON
      → BehaviorDataProcessor → flow matrix
      → DesignEvaluator → ranked proposals
      → [planned] ai_generation (SDXL + ControlNet)
      → [planned] BIM export
```

## Tech

Python · pandas · numpy · scipy · matplotlib
*(torch / diffusers / transformers are planned, currently commented out in requirements)*

## Run

```bash
pip install -r requirements.txt
python evaluation.py       # run the scoring / ranking demo
python data_processing.py  # process a behavior dataset
```

## License

MIT
