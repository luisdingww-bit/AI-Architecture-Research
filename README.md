# AI-Architecture-Research 🏗️🤖

> **AI-assisted design workflow for architectural spatial optimization.**
> 
> *基于人类行为数据的 AI 辅助建筑设计工作流*

---

## 📋 Project Overview

**Objective:** Develop an AI-assisted workflow for campus spatial optimization by integrating human behavior analysis, generative AI, and BIM modeling.

### Research Pipeline

```
┌──────────────────────────────────────────────────────────────┐
│                   1. Data Collection                          │
│   Sensor Data · Video Tracking · Survey · Wi-Fi Positioning   │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   2. Behavior Analysis                         │
│   Python · Pandas · NumPy · Spatial Statistics               │
│   → Flow patterns · Occupancy rates · Hotspot mapping        │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   3. AI Generation                             │
│   Stable Diffusion · ControlNet · ComfyUI                    │
│   → Design concepts · Spatial layouts · Facade variations    │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   4. BIM Integration                           │
│   Rhino · Grasshopper · Revit                                │
│   → Parametric models · BIM components · Documentation       │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   5. Evaluation & Optimization                 │
│   Circulation analysis · Daylight simulation · Design scoring│
└──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tools & Technologies

| Category | Tools |
|---|---|
| 🏗 **Architecture** | Rhino 7, Grasshopper, Revit, Blender |
| 💻 **Programming** | Python, C++ |
| 🤖 **AI/ML** | Stable Diffusion XL, ComfyUI, PyTorch, ControlNet |
| 📊 **Analysis** | Pandas, NumPy, SciPy, Matplotlib, Seaborn |
| 🖨 **Fabrication** | 3D Printing, CNC, Robotic Arm |

---

## 📂 Repository Structure

```
AI-Architecture-Research/
│
├── 📁 research/          ← Research papers, notes, literature review
│   └── README.md
│
├── 📁 images/            ← Diagrams, AI generations, site photos
│   └── README.md
│
├── 📁 data/              ← Datasets: behavior data, processed files
│   └── README.md
│
├── 📁 models/            ← Trained LoRAs, model weights, configs
│   └── README.md
│
├── 📁 scripts/           ← Python analysis & generation scripts
│   ├── data_processing.py    # 行为数据清洗与特征提取
│   ├── ai_generation.py      # Stable Diffusion 生成管线
│   ├── spatial_analysis.py   # 空间分析工具
│   ├── evaluation.py         # 设计方案评估
│   └── requirements.txt      # Python 依赖
│
└── README.md             ← This file
```

---

## 📊 Script Overview

### `scripts/data_processing.py`
Load, clean, and process human behavior data. Extracts flow features and exports for AI pipeline.

```python
from scripts.data_processing import BehaviorDataProcessor
processor = BehaviorDataProcessor()
flow_matrix = processor.extract_flow_features(cleaned_data)
```

### `scripts/ai_generation.py`
Generate architectural concepts using Stable Diffusion XL with ControlNet conditioning.

```python
from scripts.ai_generation import StableDiffusionGenerator, GenerationConfig
gen = StableDiffusionGenerator()
outputs = gen.generate(GenerationConfig(prompt="campus plaza with green space"))
```

### `scripts/spatial_analysis.py`
Compute spatial metrics: circulation efficiency, connectivity, diversity.

### `scripts/evaluation.py`
Score and compare design proposals with weighted evaluation criteria.

---

## 🚀 Getting Started

```bash
# Clone
git clone https://github.com/luisdingww-bit/AI-Architecture-Research.git
cd AI-Architecture-Research

# Install Python dependencies
pip install -r scripts/requirements.txt

# Run data processing example
python scripts/data_processing.py

# Generate design concepts (requires PyTorch + Diffusers)
python scripts/ai_generation.py
```

---

## 📈 Research Directions

### 1️⃣ Spatial Behavior Analysis
- Pedestrian flow prediction using LSTM networks
- Space syntax analysis integrated with AI
- Environmental behavior mapping with computer vision

### 2️⃣ AI-assisted Generative Design
- Stable Diffusion for architectural concept generation
- ControlNet-based site plan generation
- Multi-modal design space exploration

### 3️⃣ BIM Automation
- Automated Revit model generation from AI output
- Parametric family creation with Python
- Data-driven design optimization

---

## 📄 License

MIT

---

## 📬 Contact

**Louis** — [luisdingww@gmail.com](mailto:luisdingww@gmail.com)

---

<p align="center"><i>Architecture · AI · Digital Fabrication</i></p>
