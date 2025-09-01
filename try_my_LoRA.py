# Test the Lora That i made

# Make Yours in Train_Your_Lora/

# A 24 GB VRAM L4 GPU May Also Work for This
# You can use a lower VRAM GPU if you reduce RESOLUTION to 512 or 768


import os, glob
from diffusers import StableDiffusionXLPipeline
import torch

OUTPUT_DIR = r"/Lora/"
RESOLUTION = 1024

# find latest safetensors in output
lora_files = sorted([p for p in glob.glob(os.path.join(OUTPUT_DIR, "*.safetensors"))], key=os.path.getmtime)
assert lora_files, "No LoRA files found in OUTPUT_DIR. Check training output."
LORA_PATH = lora_files[-1]
print("Using LoRA:", LORA_PATH)

pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
).to("cuda")

# Load LoRA
pipe.load_lora_weights(os.path.dirname(LORA_PATH), weight_name=os.path.basename(LORA_PATH))

while True:
  print("Press Clt + C To Exit")
  # prompt = f"portrait of {TRIGGER}, professional lighting, ultra-detailed, 8k, sharp focus"
  prompt = input("Build Anything (Make sure to add your Trigger word): ")
  # neg = "low quality, blurry, lowres, bad hands, worst quality, jpeg artifacts"
  neg = input("Negative Prompt (leave blank if none): ")
  image = pipe(prompt, negative_prompt=neg, num_inference_steps=30, guidance_scale=7.5, height=RESOLUTION, width=RESOLUTION).images[0]

  image.save("/content/sample_lora_output.png")
  print("Saved /content/sample_lora_output.png")