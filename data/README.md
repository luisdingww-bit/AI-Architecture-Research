# Data

## Datasets

| Dataset | Description | Size | Format |
|---|---|---|---|
| sample_behavior.csv | Sample pedestrian flow data (generated) | ~50KB | CSV |
| processed/ | Cleaned and feature-extracted data | - | JSON |

### Data Schema

sample_behavior.csv:
- `x`, `y` — Spatial coordinates (0-100)
- `timestamp` — Observation time
- `velocity` — Movement speed (optional)
- `direction` — Movement direction in degrees (optional)

### Notes
- Do not commit files larger than 100MB
- Use `.gitkeep` files for empty directories
