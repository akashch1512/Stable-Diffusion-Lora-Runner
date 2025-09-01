# 🔧 LoRA Training — Stable Diffusion XL (v0.2.0)

This repository contains tools and scripts to train and test **LoRA models** on **Stable Diffusion XL (SDXL)**, the latest major upgrade from SD1.5. It is designed for creators aiming to fine-tune SDXL on custom datasets (faces, characters, styles, etc.).

***

Example Output:

![Sample Output](Example_Outputs/Image4.jpg)

## ⚠️ Major Update Notice

- **Switched from Stable Diffusion 1.5 to Stable Diffusion XL (SDXL)** for improved image quality and model capabilities.
- **Important:** SDXL requires higher hardware specs.  
  If running on a low-end PC or limited GPU, it is recommended to use **v0.1.0** with SD1.5 for better performance and stability.

***

## 🚀 New Features in v0.2.0

- Migrated codebase to support SDXL instead of SD1.5.
- Optimized code for better performance and efficiency.
- Added test script: `try_my_LoRA.py` to easily test trained LoRA models using a standalone Python file.
- Simplified folder structure with dedicated locations for LoRA safetensors and training notebooks.

***

## 📂 Updated Folder Structure

```
Lora/                   # LoRA safetensors placed here
Train_Your_Lora/        # Jupyter notebooks to train your LoRA models
readme.md               # This readme file
requirements.txt        # Required Python dependencies
try_my_LoRA.py          # Test script to run inference with your trained LoRA
```

***

## 🛠️ How to Use

### Training

1. Use the notebook(s) in `Train_Your_Lora/` to prepare datasets and train your LoRA on SDXL.
2. Training requires hardware capable of running SDXL smoothly (high VRAM GPUs recommended).

### Testing

- Run `try_my_LoRA.py` to test your trained LoRA with sample prompts and evaluate results immediately.

***

## 💡 Disclaimer

- SDXL models are **more demanding** and may not run smoothly on low-end or older GPUs.
- For users with limited hardware, please continue to use **v0.1.0** which supports Stable Diffusion 1.5, consuming less VRAM.

***

## 📋 Requirements

- See `requirements.txt` for all necessary Python packages and versions.

***

## 🙌 Credits

- Stable Diffusion XL by Stability AI and collaborators.
- LoRA training scripts adapted and optimized from [kohya-ss sd-scripts].
- v0.1.0 legacy support for Stable Diffusion 1.5 by Akash.

***

This update unleashes the power of SDXL with LoRA training and testing in one streamlined repo!