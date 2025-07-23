# 🚀 Creative Story Generator with Illustrations

Turn your ideas into magical illustrated stories—powered by AI, running 100% locally on your machine!

---

## ✨ Features
- **AI-Powered Storytelling:** Generate creative, multi-segment stories from any prompt using Hugging Face Transformers (GPT-2).
- **Unique Illustrations:** Each story segment gets its own AI-generated image (Stable Diffusion via Diffusers).
- **Modern Web App:** Clean, interactive UI built with Streamlit.
- **Runs Locally:** No cloud, no data sharing—your stories and images stay on your computer.

---

## 🖥️ Demo
> _Add a GIF or screenshot here to show off your app!_

---

## 🚦 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mvc
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install accelerate  # (Recommended for faster model loading)
   ```
3. **Run the app:**
   ```bash
   streamlit run src/app.py
   ```
4. **Open your browser:**
   - Go to the local URL shown in your terminal (usually [http://localhost:8501](http://localhost:8501))

---

## 📝 How to Use
1. Enter a story prompt (e.g., _"A robot discovers a hidden garden"_)
2. Choose the number of story segments (1–10)
3. Click **Generate Story & Illustrations**
4. Read your story and see each segment illustrated by AI
5. Download any illustration you like!

---

## 📁 Project Structure
```
src/
  story_generator.py      # Story generation logic
  image_generator.py      # Illustration generation logic
  app.py                 # Streamlit app
```

---

## 🛠️ Troubleshooting & Tips
- **First run is slow:** Models are downloaded the first time (can take several minutes).
- **Stuck on image generation?**
  - Make sure you have a stable internet connection for the first run.
  - Try installing `accelerate` for better performance: `pip install accelerate`
  - If you see errors, try updating dependencies:
    ```bash
    pip install --upgrade diffusers huggingface_hub
    ```
- **Low memory?**
  - Reduce the number of segments or use a smaller model (ask for recommendations!)
- **Firewall/Proxy issues?**
  - Try a different network if model downloads fail.

---

## 💡 Customization Ideas
- Swap in different text or image models
- Add story export (PDF, ePub)
- Let users edit or continue stories interactively
- Add themes or style options for illustrations

---

## 🧑‍💻 Requirements
- Python 3.8+
- MacBook Pro 2018 or newer recommended

---

## 📜 License
MIT

---

> Made with ❤️ using Hugging Face, Diffusers, and Streamlit