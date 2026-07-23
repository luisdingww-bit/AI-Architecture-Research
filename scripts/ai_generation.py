"""
AI-Architecture-Research - Design Generation Module
====================================================
AI-assisted concept generation using Stable Diffusion XL (+ ControlNet).

STATUS: reference stub.
This module documents the intended generation pipeline and provides a
clean interface, but does NOT ship a working inference backend yet.
`DesignGenerator.generate()` raises NotImplementedError instead of
fabricating output files. Wire up `torch` + `diffusers` and implement
`_generate_real()` to enable real generation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class GeneratorConfig:
    """Configuration for design-concept generation."""

    prompt: str = "architectural spatial layout, modern campus design"
    negative_prompt: str = "low quality, blurry, distorted"
    model_id: str = "stabilityai/stable-diffusion-xl-base-1.0"
    num_images: int = 4
    seed: int = 42
    output_dir: str = "../images/generations"


class DesignGenerator:
    """Generates architectural design concepts with SDXL.

    The inference backend is not implemented in this repository. Call
    `generate()` only after wiring up `_generate_real()` (see scaffold).
    """

    def __init__(self, config: GeneratorConfig | None = None):
        self.config = config or GeneratorConfig()
        self.output_dir = Path(self.config.output_dir)

    def generate(self) -> List[Path]:
        """Generate design concepts and return saved image paths.

        Raises:
            NotImplementedError: the SDXL inference backend is not wired up.
        """
        raise NotImplementedError(
            "Real SDXL inference is not wired up in this repo. "
            "Install torch+diffusers and implement DesignGenerator._generate_real()."
        )

    def _generate_real(self) -> List[Path]:
        """Reference scaffold for real SDXL generation (not active).

        Enable by installing dependencies and uncommenting:
            from diffusers import StableDiffusionXLPipeline
            pipe = StableDiffusionXLPipeline.from_pretrained(self.config.model_id)
            images = pipe(
                self.config.prompt,
                negative_prompt=self.config.negative_prompt,
                num_images_per_prompt=self.config.num_images,
                seed=self.config.seed,
            ).images
            self.output_dir.mkdir(parents=True, exist_ok=True)
            paths = []
            for i, img in enumerate(images):
                p = self.output_dir / f"generation_{i}.png"
                img.save(p)
                paths.append(p)
            return paths
        """
        raise NotImplementedError


if __name__ == "__main__":
    config = GeneratorConfig(
        prompt="modern campus architecture, sustainable design, parametric facade"
    )
    generator = DesignGenerator(config)
    try:
        outputs = generator.generate()
        print(f"Generated {len(outputs)} design concepts")
        for p in outputs:
            print(f"  -> {p}")
    except NotImplementedError as e:
        print("[stub] AI generation is not implemented yet.")
        print(f"[stub] {e}")
        print("[stub] No images were produced.")
"""
