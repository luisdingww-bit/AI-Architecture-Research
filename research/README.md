# Research Notes

## AI-assisted Campus Spatial Optimization

### Research Questions

1. How can human behavior data inform AI-generated architectural layouts?
2. What is the optimal workflow integrating Stable Diffusion with BIM tools?
3. How do different prompt strategies affect the quality of generated designs?

### Methodology

| Phase | Method | Output |
|---|---|---|
| Data Collection | Site observation, Wi-Fi tracking | Behavior dataset |
| Analysis | Python (Pandas, NumPy) | Flow patterns, heatmaps |
| Generation | Stable Diffusion + ControlNet | Design concepts |
| Evaluation | Spatial metrics + expert review | Design scores |

### Literature

- *Space Syntax* — Hillier & Hanson (1984)
- *Attention Is All You Need* — Vaswani et al. (2017)
- *Denoising Diffusion Probabilistic Models* — Ho et al. (2020)
- *LoRA: Low-Rank Adaptation* — Hu et al. (2021)

### Experimental Log

| Date | Experiment | Result |
|---|---|---|
| 2026-06 | LoRA fine-tune on architectural dataset | Good concept variety |
| 2026-07 | ControlNet plan-to-rendering | Promising spatial accuracy |
