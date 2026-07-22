# Experimental Log

## Experiment 001: LoRA Fine-tuning

**Date:** 2026-06-15  
**Model:** Stable Diffusion XL 1.0  
**Dataset:** 200 architectural reference images (campus buildings, public spaces)

### Parameters
- LoRA Rank: 16
- Learning Rate: 1e-4
- Training Steps: 1500
- Batch Size: 2

### Results
- Concept variety: Good
- Architectural consistency: Moderate
- Prompt adherence: High

### Samples
See `../images/generations/exp001/`

---

## Experiment 002: ControlNet Plan Generation

**Date:** 2026-07-01  
**Model:** SDXL + ControlNet (Canny)  
**Condition:** Site plan sketches

### Parameters
- ControlNet Weight: 0.8
- Guidance Scale: 7.5
- Steps: 50

### Results
- Spatial accuracy: Promising
- Need more conditioning data

---

## Experiment 003: Text-to-Architecture Comparison

**Date:** 2026-07-15  
**Comparison:** Baseline SDXL vs. Fine-tuned LoRA

### Metrics
| Metric | Baseline | LoRA FT | Improvement |
|---|---|---|---|
| Architectural Correctness | 6.2/10 | 8.1/10 | +31% |
| Prompt Alignment | 7.5/10 | 8.3/10 | +11% |
| Visual Quality | 7.8/10 | 8.5/10 | +9% |
