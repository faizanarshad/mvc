from diffusers import StableDiffusionPipeline
import torch

# Load the model once at module level for efficiency
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float32
)
pipe = pipe.to("cpu")

def generate_image(prompt: str):
    image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
    return image 