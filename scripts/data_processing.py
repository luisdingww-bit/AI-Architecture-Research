"""
AI-Architecture-Research - Data Processing Module
==================================================
Processes human behavior data for spatial optimization analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime


class BehaviorDataProcessor:
    """Process pedestrian flow and space usage data."""
    
    def __init__(self, data_dir="../data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
    
    def load_raw_data(self, filepath):
        path = Path(filepath)
        if path.suffix == ".csv":
            return pd.read_csv(path)
        elif path.suffix == ".json":
            return pd.read_json(path)
        raise ValueError(f"Unsupported format: {path.suffix}")
    
    def clean_data(self, df):
        df = df.dropna(subset=["x", "y"])
        df["x"] = df["x"].clip(0, 100)
        df["y"] = df["y"].clip(0, 100)
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            df = df.sort_values("timestamp")
        return df
    
    def extract_flow_features(self, df, grid_size=10):
        x_bins = np.linspace(0, 100, grid_size + 1)
        y_bins = np.linspace(0, 100, grid_size + 1)
        df["cell_x"] = np.digitize(df["x"], x_bins) - 1
        df["cell_y"] = np.digitize(df["y"], y_bins) - 1
        flow_matrix = df.groupby(["cell_x", "cell_y"]).size().unstack(fill_value=0)
        return flow_matrix
    
    def export_for_ai(self, df, output_path="../data/processed"):
        output_dir = Path(output_path)
        output_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = output_dir / f"processed_data_{timestamp}.json"
        data = {"metadata": {"generated_at": timestamp, "total_observations": len(df)}, "data": json.loads(df.to_json(orient="records"))}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return str(filename)


if __name__ == "__main__":
    processor = BehaviorDataProcessor()
    np.random.seed(42)
    sample = pd.DataFrame({
        "x": np.random.uniform(0, 100, 1000),
        "y": np.random.uniform(0, 100, 1000),
        "timestamp": pd.date_range("2026-01-01", periods=1000, freq="5min"),
    })
    sample.to_csv("../data/sample_behavior.csv", index=False)
    cleaned = processor.clean_data(sample)
    flow = processor.extract_flow_features(cleaned)
    print(f"Processed {len(cleaned)} observations, flow matrix: {flow.shape}")
