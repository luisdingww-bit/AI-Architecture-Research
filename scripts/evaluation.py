\"\"\"
AI-Architecture-Research - Design Evaluation Module
=====================================================
Evaluates and compares generated design proposals.
\"\"\"

from dataclasses import dataclass, asdict
from typing import List
import json
from datetime import datetime


@dataclass
class EvaluationResult:
    proposal_name: str
    spatial_score: float
    circulation_score: float
    aesthetics_score: float
    feasibility_score: float
    
    @property
    def overall_score(self):
        weights = {\"spatial_score\": 0.30, \"circulation_score\": 0.25,
                    \"aesthetics_score\": 0.25, \"feasibility_score\": 0.20}
        return round(sum(getattr(self, k) * v for k, v in weights.items()), 3)


class DesignEvaluator:
    \"\"\"Evaluate and compare architectural design proposals.\"\"\"
    
    def __init__(self):
        self.history: List[EvaluationResult] = []
    
    def evaluate(self, result: EvaluationResult):
        self.history.append(result)
        return {\"proposal\": result.proposal_name, \"overall\": result.overall_score}
    
    def compare(self) -> List[dict]:
        ranked = sorted(self.history, key=lambda r: r.overall_score, reverse=True)
        return [{\"rank\": i+1, \"name\": r.proposal_name, \"score\": r.overall_score}
                for i, r in enumerate(ranked)]


if __name__ == \"__main__\":
    evaluator = DesignEvaluator()
    for p in [
        EvaluationResult(\"方案A-中央庭院\", 0.85, 0.72, 0.90, 0.78),
        EvaluationResult(\"方案B-线性布局\", 0.78, 0.88, 0.75, 0.85),
    ]:
        r = evaluator.evaluate(p)
        print(f\"{r['proposal']}: {r['overall']}\")
    print(\"\\n排名:\")
    for r in evaluator.compare():
        print(f\"  #{r['rank']} {r['name']} ({r['score']})\")
