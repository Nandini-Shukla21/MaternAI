Here's a clean and professional **project description** for your MaternAI pregnancy risk prediction project — suitable for your resume, GitHub, LinkedIn, or portfolio:

---

## 🩺 MaternAI: Pregnancy Risk Level Prediction

**Overview:**
MaternAI is a Machine Learning-powered health application designed to predict the **pregnancy risk level** (high or low) based on clinical and demographic data. It aims to assist medical professionals and expecting mothers by offering a data-driven second opinion on potential pregnancy complications.

**Key Features:**

* ✅ Predicts **High Risk** or **Low Risk** pregnancy using ML classification models.
* 🧠 Built using **Random Forest Classifier** and **XGBoost**, with Random Forest achieving **97% accuracy** after hyperparameter tuning.
* 🔬 Uses a variety of features:
  `Age`, `SystolicBP`, `DiastolicBP`, `Blood Sugar`, `Body Temperature`, `Heart Rate`, `Number of Pregnancies`, `Previous Complications`, `Hemoglobin`, and `BMI`.
* 📊 Correlation heatmap analysis to understand the influence of clinical parameters on risk level.
* ⚖️ Applied **StandardScaler** for feature normalization.
* 🖥️ Deployed a user-friendly **Streamlit web app** that allows healthcare workers to input patient details and get real-time predictions.
* 💾 Backend uses `joblib` for model and scaler serialization (`maternAI_rf_model.pkl`, `maternAI_scaler.pkl`).

**Tech Stack:**

* **Languages & Tools:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit
* **Modeling:** Random Forest Classifier, XGBoost
* **Deployment:** Streamlit Web UI (local and deployable on cloud)
* **Data Processing:** Feature scaling, synthetic feature generation, and correlation analysis

**Impact:**
By digitizing pregnancy risk assessment, MaternAI helps in early detection of potential complications, enabling proactive medical attention and improving maternal health outcomes.


