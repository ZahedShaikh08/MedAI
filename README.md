# 🧠 MediAI – AI‑Powered Health Diagnosis

**MediAI** is an intuitive web app that leverages machine learning to provide preliminary health diagnostics based on user‑entered symptoms. Built with **Flask** (backend) and optionally deployable in **Streamlit**, MediAI combines predictive insights with lifestyle guidance—description, precautions, medications, diet, and workouts.

---

## 🚀 Features

- 🎯 **Symptom-based disease prediction** using a trained SVC model.
- 📚 Displays *descriptions*, *precautions*, *medications*, *dietary advice*, and *workout tips*.
- 🗣️ Supports speech-to-text symptom input in the web version.
- ✨ Clean UI: Bootstrap + custom gradients and glass/card effects.
- ✅ Optional: Daily deploy via Streamlit for rapid prototyping.

---

## 🧩 Project Structure

```
MediAI/
├── datasets/
│   ├── symtoms_df.csv
│   ├── precautions_df.csv
│   ├── workout_df.csv
│   ├── description.csv
│   ├── medications.csv
│   └── diets.csv
├── models/
│   └── svc.pkl
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── developer.html
│   └── blog.html
├── static/
│   ├── css/
│   └── medi_logo.png
├── main.py             # Flask backend
├── app_streamlit.py    # Optional Streamlit version
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/ZahedShaikh08/MediAI.git
   cd MediAI
   ```

2. **Create virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Flask version**  
   ```bash
   python main.py
   ```  
   Visit: `http://127.0.0.1:5000/index`

5. **[Optional] Run Streamlit version**  
   ```bash
   streamlit run app_streamlit.py
   ```

---

## 🧠 How It Works

- **Input processing:** User enters symptoms (comma-separated or via voice).  
- **Symptom vector:** Text parsed & converted into binary feature vector.  
- **Model prediction:** SVC outputs a disease label.  
- **Retrieve details:** Helper function fetches related details from CSVs.  
- **Display:** Info rendered in responsive cards or expandable sections.

---

## 📂 Folder Descriptions

- `main.py`: Flask API and routes handling web app behavior.  
- `app_streamlit.py`: An alternate UI built using Streamlit.  
- `datasets/`: CSV lookup files for symptom–disease relationships and descriptions.  
- `models/`: Trained SVC model file (`svc.pkl`).  
- `templates/`, `static/`: Frontend assets & HTML templates.  
- `requirements.txt`: Project dependencies.

---

## 🎉 Contributions

Contributions and suggestions are welcome! Feel free to open an issue or submit a PR. Here's how:

1. Fork & clone the repo.  
2. Create a branch: `git checkout -b feature/my-change`  
3. Commit & push: `git commit -m "Add my feature"` / `git push origin feature/my-change`  
4. Open a PR and describe your changes.

---

## ⚠️ Disclaimer

MediAI is a _research & educational_ tool. It's **not** a substitute for professional medical evaluation or diagnosis.

---

## 🧍‍♂️ About Me

Developed by **Shaikh Zahed** — an AI/ML Engineer passionate about building health‑tech solutions.  
Connect: [GitHub](https://github.com/ZahedShaikh08) | [LinkedIn](https://www.linkedin.com/in/zahed-shaikh-1ab916337/) | Portfolio

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.
