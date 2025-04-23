# 🏥 DataPulse - Health Tracker Dashboard

**DataPulse** is a beginner-friendly yet production-grade health analytics dashboard built using **Streamlit**, **Pandas**, and **Plotly**. It allows users to explore, visualize, and track their daily health metrics such as **steps taken**, **calories burned**, and **sleep hours** – all from a clean, interactive web interface.

> This is Project 1 in my mission to build 15 full-stack data science projects by June.

---

## 🚀 Features

- 📊 Interactive line, bar, and pie charts using Plotly
- 🧮 Real-time metric display: total steps, average sleep, peak calorie burn
- 🗂️ Raw data table with expand/collapse toggle
- 📥 Download processed data as CSV
- 🧠 Insight generation using simple stats
- 🎯 Fully deployable with zero backend setup

---


## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core logic and data wrangling |
| `Pandas` | Data analysis |
| `Streamlit` | Web app framework |
| `Plotly` | Beautiful interactive charts |
| `CSV` | Input data source |

---

## 📂 Folder Structure
📁 datapulse/ ├── health_data.csv ├── app.py └── README.md

---

## 🧪 How to Run It Locally

1. Clone this repo:
    ```bash
    git clone https://github.com/yourusername/datapulse.git
    cd datapulse
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
pandas
plotly
