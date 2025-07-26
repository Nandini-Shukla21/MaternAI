

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
* 🖥️ User friendly , clean and responsive UI using HTML , CSS and JS
* 💾 Backend uses `flask` for model and scaler serialization (`maternAI_rf_model.pkl`, `maternAI_scaler.pkl`).


**Overlook:**

 <img width="1900" height="887" alt="image" src="https://github.com/user-attachments/assets/8368f84b-0e70-462a-92ab-351123dd5c72" />
<img width="1830" height="895" alt="image" src="https://github.com/user-attachments/assets/5c68c208-49cd-46d2-8f6c-c380c97cadf2" />
<img width="1762" height="888" alt="image" src="https://github.com/user-attachments/assets/4e7dfab8-47d0-4878-97d8-5ba79a0dad94" />

**Tech Stack:**

* **Languages & Tools:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, JavaScript , Flask
* **Modeling:** Random Forest Classifier, XGBoost
* **UI:** HTML , CSS , JavaScript
* **Data Processing:** Feature scaling, synthetic feature generation, and correlation analysis

**Impact:**
By digitizing pregnancy risk assessment, MaternAI helps in early detection of potential complications, enabling proactive medical attention and improving maternal health outcomes.


