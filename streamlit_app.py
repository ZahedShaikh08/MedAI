import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1) Caching heavy loads
@st.cache_resource
def load_model(path="models/svc.pkl"):
    try:
        return pickle.load(open(path, 'rb'))
    except FileNotFoundError:
        st.error(f"Model file not found at {path}")
        st.stop()

@st.cache_data
def load_datasets():
    files = {
        'sym_des': "datasets/symtoms_df.csv",
        'precautions': "datasets/precautions_df.csv",
        'workout': "datasets/workout_df.csv",
        'description': "datasets/description.csv",
        'medications': "datasets/medications.csv",
        'diets': "datasets/diets.csv"
    }
    data = {}
    for name, path in files.items():
        try:
            data[name] = pd.read_csv(path)
        except FileNotFoundError:
            st.error(f"Dataset missing: {path}")
            st.stop()
    return data

svc = load_model()
data = load_datasets()

# 2) Helper & mappings
symptoms_dict = {
    'itching': 0, 'skin_rash': 1, # … your full mapping …
}
diseases_list = {
    15: 'Fungal infection', 4: 'Allergy', # … your full mapping …
}

def helper(dis):
    desc = data['description'].loc[data['description']['Disease']==dis, 'Description'].squeeze()
    # Precautions
    row = data['precautions'].loc[data['precautions']['Disease']==dis]
    pre = [row[f'Precaution_{i}'].values[0] for i in range(1,5) if row[f'Precaution_{i}'].notna().bool()]
    # Medications / Diets / Workouts (split on commas if needed)
    def split_field(df, key, col):
        val = df.loc[df[key]==dis, col].squeeze()
        return [v.strip() for v in str(val).split(',')] if isinstance(val, str) else [val]
    med  = split_field(data, 'Disease', 'Medication')
    die  = split_field(data, 'Disease', 'Diet')
    wrk  = split_field(data['workout'], 'disease', 'workout')
    return desc, pre, med, die, wrk

def predict(symptoms_list):
    vec = np.zeros(len(symptoms_dict))
    valid = []
    for s in symptoms_list:
        key = s.strip().lower().replace(' ', '_')
        idx = symptoms_dict.get(key)
        if idx is not None:
            vec[idx] = 1
            valid.append(key)
    if not valid:
        return None, []
    try:
        label = svc.predict([vec])[0]
        return diseases_list.get(label, "Unknown"), valid
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        return None, valid

# 3) Streamlit UI
st.set_page_config("MediAI Health Diagnosis", page_icon="🩺", layout="centered")

# Custom CSS
st.markdown("""
<style>
  .result-card { padding:1rem; margin:1rem 0; box-shadow:0 4px 8px rgba(0,0,0,0.1); border-radius:10px; }
  .disease-title { color:#2a4d69; border-bottom:2px solid #4CAF50; padding-bottom:0.5rem; }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1,3])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2785/2785523.png", width=64)
with col2:
    st.title("MediAI Health Diagnosis")
    st.caption("AI‑powered symptom analysis & disease prediction")

st.divider()

# Input Form
with st.form("symp_form"):
    st.subheader("🔍 Enter Your Symptoms")
    symp_input = st.text_area("", placeholder="e.g. headache, fever, nausea...", height=100)
    submitted = st.form_submit_button("Analyze Symptoms")

# Prediction Logic
if submitted:
    if not symp_input.strip():
        st.warning("Please enter at least one symptom.")
    else:
        with st.spinner("Analyzing..."):
            syms = [s.strip() for s in symp_input.split(',')]
            disease, valid = predict(syms)

        if not disease:
            st.error("No valid symptoms detected. Check your spelling?")
        else:
            st.success("Analysis complete!")
            desc, pre, med, die, wrk = helper(disease)

            # Results Card
            st.markdown(f"<div class='result-card'>", unsafe_allow_html=True)
            st.markdown(f"<h3 class='disease-title'>{disease}</h3>", unsafe_allow_html=True)
            st.write(desc)
            st.subheader("✅ Symptoms Detected")
            st.write(", ".join(valid))
            st.subheader("🛡️ Precautions")
            for p in pre: st.write(f"- {p}")
            st.subheader("💊 Medications")
            for m in med: st.write(f"- {m}")
            st.subheader("🥗 Diets")
            for d in die: st.write(f"- {d}")
            st.subheader("💪 Workouts")
            for w in wrk: st.write(f"- {w}")
            st.markdown("</div>", unsafe_allow_html=True)

st.divider()
st.subheader("ℹ️ About This Tool")
st.write("This AI‑powered tool provides preliminary insights based on symptoms. Always consult a healthcare professional for medical advice.")

st.markdown("---")
st.caption("© 2025 MediAI Health | Educational purposes only")
