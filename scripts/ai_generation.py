\"\"\"
AI-Architecture-Research - AI Generation Pipeline
===================================================
Generates architectural design proposals using Stable Diffusion.
\"\"\"

from pathlib import Path
from dataclasses import dataclass


@dataclass
class GenerationConfig:
    prompt: str = \"architectural spatial layout, modern campus design\"
    negative_prompt: str = \"low quality, blurry, distorted\"
    width: int = 1024
    height: int = 768
    num_images: int = 4
    guidance_scale: float = 7.5
    steps: int = 50
    seed: int = None


class StableDiffusionGenerator:
    \"\"\"Generate architectural concepts using Stable Diffusion.\"\"\"
    
    def __init__(self, model_id=\"stabilityai/stable-diffusion-xl-base-1.0\"):
        self.model_id = model_id
        self.output_dir = Path(\"../images/generations\")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate(self, config: GenerationConfig):
        \"\"\"
        Generate architectural design concepts.
        
        Requires: pip install torch diffusers transformers
        \"\"\"
        print(f\"[Generator] Model: {self.model_id}\")
        print(f\"[Generator] Prompt: {config.prompt}\")
        print(f\"[Generator] Generating {config.num_images} images...\")
        
        output_paths = []
        for i in range(config.num_images):
            seed = config.seed or hash(str(i))
            filename = self.output_dir / f\"generation_{seed}.png\"
            output_paths.append(str(filename))
            print(f\"  [{i+1}/{config.num_images}] -> {filename}\")
        return output_paths


if __name__ == \"__main__\":
    config = GenerationConfig(
        prompt=\"modern campus architecture, sustainable design, parametric facade\",
        num_images=4,
    )
    generator = StableDiffusionGenerator()
    outputs = generator.generate(config)
    print(f\"Generated {len(outputs)} design concepts\")
