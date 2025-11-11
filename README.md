

```markdown
# 🌞 Solar Energy Data Profiling, Cleaning, and EDA (Benin, Sierra Leone, Togo)

This project focuses on **Exploratory Data Analysis (EDA)** of solar energy datasets from **Benin, Sierra Leone, and Togo**.  
It was developed as part of the **TenX Academy Week 0 Data Science Challenge**, combining professional data workflows with reproducible analytics.

---

## 🎯 Project Overview

The goal of this project is to **analyze, clean, and visualize solar energy datasets** to uncover meaningful patterns in solar irradiance and environmental conditions across three African countries.

Each dataset includes readings of:
- Solar radiation metrics: **GHI**, **DNI**, **DHI**
- Module temperatures: **TModA**, **TModB**
- Environmental variables: **Temperature**, **Humidity**, **Wind Speed**

The analysis was performed individually per country and later combined for comparative insights.

---

## 🧑‍💻 My Contribution

I completed the entire workflow independently, covering both technical setup and analytical execution:

### 🪜 Setup & Version Control
- Initialized a **Git repository** for version control.
- Created **country-specific branches**:
  - `eda-benin`
  - `eda-togo`
  - `eda-sierraleone`
  - `compare-countries`
- Configured **remote repository** on GitHub for collaboration and CI integration.
- Used **descriptive commit messages** to document progress.
- Added `.gitignore` to exclude unnecessary files and maintain clean commits.

### 🧠 Environment Management
- Created a **Python virtual environment (.venv)** for dependency isolation.
- Installed core data science libraries:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `statsmodels`, `jupyter`
- Configured **VS Code** with:
  - Python and Jupyter extensions.
  - Correct interpreter selection for the virtual environment.
- Verified installations and created `requirements.txt` for reproducibility.

### 🔍 Data Profiling & Cleaning
- Performed **data profiling** to understand dataset structure:
  - Checked column types, missing values, duplicates, and cardinality.
- Executed **data cleaning**:
  - Removed empty or redundant columns.
  - Handled missing values and outliers using Z-score techniques.
  - Converted timestamps to datetime format.
  - Created derived columns for month/day-based analyses.

### 📊 Exploratory Data Analysis (EDA)
- Conducted **univariate**, **bivariate**, and **multivariate** analyses:
  - Histograms, boxplots, scatter plots, and correlation heatmaps.
  - Wind rose plots to visualize directional data.
- Explored relationships between:
  - Solar irradiance and temperature.
  - Humidity, wind speed, and solar potential.
- Performed **comparative analysis** across all three countries.

### 🧪 Statistical Testing
- Validated findings using formal tests:
  - Shapiro-Wilk (normality)
  - Levene’s (variance homogeneity)
  - Kruskal-Wallis and Tukey’s HSD (for significance testing)
- Confirmed statistically significant differences in **GHI** among countries.

### 📈 Streamlit Dashboard Implementation
- Built an **interactive Streamlit app** — _Solar Data EDA Dashboard_.
- Enabled users to:
  - Upload cleaned CSV files.
  - Choose visualization types: **Line Chart**, **Box Plot**, or **Scatter Plot**.
  - Explore time-series and distribution patterns interactively.

---

## 🧩 Project Structure

```

solar-eda-project/
│
├── data/                    # Raw and cleaned datasets
├── notebooks/               # EDA notebooks (Benin, Togo, Sierra Leone)
├── app/
│   └── streamlit_app.py     # Streamlit dashboard code
├── .venv/                   # Python virtual environment
├── requirements.txt          # Project dependencies
├── README.md                 # Documentation file
└── .gitignore                # Ignored files and folders

````

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Deregit2025/solar-challenge-week0.git
cd solar-challenge-week0
````

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

### 5️⃣ Open Notebooks

Use VS Code or Jupyter Notebook to explore:

* `notebooks/EDA_Benin.ipynb`
* `notebooks/EDA_SierraLeone.ipynb`
* `notebooks/EDA_Togo.ipynb`
* `notebooks/Compare_Countries.ipynb`

---

## 📊 Key Findings

* **Benin** had the highest and most consistent median GHI values.
* **Sierra Leone** showed high variability in DHI and DNI, indicating unstable solar potential.
* **Togo** exhibited moderate and steady readings, suitable for reliable solar generation.
* Statistical tests confirmed significant differences in solar irradiance among the three countries.

---

## 🧠 Lessons Learned

* Importance of **data cleaning** for reliable EDA.
* How **branching strategies** support parallel analyses and reproducibility.
* Application of **statistical testing** in validating insights.
* Building interactive tools using **Streamlit** to communicate data stories.
* Collaboration through **Git, Slack, and CI pipelines** for professional workflow management.

---

## 🪪 Author

**Dereje Derib**
Data Science Trainee — TenX Academy
🔗 [GitHub Profile](https://github.com/Deregit2025)

---

## 📚 License

This project is shared for academic and educational purposes under the MIT License.

````

---

