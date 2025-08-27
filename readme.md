# 🔧 LoRA Training — Stable Diffusion 1.5 (Google Colab)

This repository contains a **Google Colab notebook** to train **LoRA models** on **Stable Diffusion 1.5**.  
It is designed for creators who want to fine-tune SD1.5 on custom datasets (faces, characters, styles, etc.).  

---

## 🚀 Features
- ✅ Automatic environment setup (Python 3.10, CUDA 12.1, Torch 2.2.2)  
- ✅ Tested with **kohya-ss sd-scripts**  
- ✅ Drive integration for dataset, cache, outputs, and logs  
- ✅ Custom **trigger token** for your LoRA  
- ✅ Configurable hyperparameters (resolution, batch size, steps, etc.)  
- ✅ Optimized with **xformers** and **bitsandbytes**  

---

## 📂 Notebook Sections
1. **Environment Setup** — GPU check, Drive mount, Python 3.10 upgrade  
2. **Dependency Installation** — Torch + CUDA, Hugging Face stack, utilities  
3. **Dataset Preparation** — Split into close-ups, medium, full-body  
4. **Project Config** — Define project name, trigger word, training parameters  
5. **Training** — Launch kohya-ss script with your settings  
6. **Export & Inference** — Save LoRA to Drive, test with prompt  

---

## ⚙️ Project Config (STEP 4)
When configuring your project in the notebook, set:

- **Project Name** → folder for datasets, outputs, logs  
- **Trigger Word** → unique keyword (e.g. `akashawriter`)  
- **Resolution** → `512` (lighter/faster) or `768` (better detail, heavy VRAM)  
- **Batch Size** → `1` for T4 GPU, `2+` if you have higher VRAM  
- **Max Steps** → start with `3000–5000` for decent results  
- **Network Dim / Alpha** → `16` or `32` (higher = more capacity, heavier model)  
- **Learning Rate** → Default `1e-4` works for most cases  

👉 If unsure, stick to defaults.  

---

## 🔥 Best Settings for Maximum Quality
If you want **the best possible output**, even if it consumes more GPU memory or takes longer:  

- **Resolution** → `768`  
- **Batch Size** → `2` (if VRAM allows)  
- **Max Steps** → `8000–12000` (longer training = sharper features, but risk of overfit)  
- **Network Dim** → `32` (more detail capacity)  
- **Learning Rate** → keep defaults; don’t go too high or it overfits  
- **Dataset** →  
  - 60–70% close-up faces  
  - 20–30% medium shots  
  - 10–20% full body  
  - Use **high-res, diverse images** with consistent labeling  
  - Avoid duplicates and blurred/noisy images  

⚠️ Note: On Colab T4 GPUs, training with these settings may take several hours. For faster results, reduce steps.  

---

## 📊 Tips for Best Results
- Clean your dataset manually before training (blurred/duplicate images kill quality).  
- Use **unique, uncommon trigger tokens** (avoid generic words).  
- Save intermediate checkpoints (e.g., at 3k, 6k, 10k steps).  
- Test LoRA at multiple checkpoints — sometimes earlier ones perform better.  

---

## 📜 License
This notebook is based on [kohya-ss sd-scripts](https://github.com/kohya-ss/sd-scripts).  
Follow the license of that repository when redistributing.  

---

## 🙌 Credits
- Stable Diffusion 1.5 by [CompVis & StabilityAI](https://github.com/CompVis/stable-diffusion)  
- LoRA training scripts from [kohya-ss](https://github.com/kohya-ss/sd-scripts)  
- Colab adaptation by Akash  
