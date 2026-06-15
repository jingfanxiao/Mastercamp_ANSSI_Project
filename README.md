# Mastercamp ANSSI Project

A cybersecurity analysis pipeline that collects vulnerability bulletins from [CERT-FR (ANSSI)](https://www.cert.ssi.gouv.fr/), enriches them with CVE/CVSS/EPSS data, applies machine learning models, and generates automated security alert emails.

## Features

- **RSS feed collection** from CERT-FR (avis & alertes)
- **CVE extraction** from local JSON bulletin files
- **CVSS / EPSS enrichment** via NVD and FIRST APIs
- **ML analysis**: Random Forest (classifier & regressor), KMeans clustering, Isolation Forest anomaly detection
- **Alert generation** with email notification (Gmail SMTP)
- **Django web dashboard** to visualize results

---

## Project Structure

```
Mastercamp_ANSSI_Project/
├── data/
│   ├── raw/              # Raw JSON bulletins + RSS cache (CSV, tracked by Git LFS)
│   └── processed/        # Consolidated CVE data (CSV, tracked by Git LFS)
├── django_app/           # Django web dashboard
├── notebooks/            # Jupyter analysis notebooks
├── outputs/              # Generated plots and alert CSV
├── scripts/              # Utility scripts
├── video/                # Demo videos
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.9+
- Git LFS (for large CSV files)
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords) (for email alerts)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jingfanxiao/Mastercamp_ANSSI_Project.git
cd Mastercamp_ANSSI_Project
```

### 2. Create and activate a virtual environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Jupyter Notebook

Make sure Jupyter is installed (it is included in `requirements.txt`), then launch:

```bash
jupyter notebook notebooks/anssi_analysis.ipynb
```

Run cells sequentially. The notebook will:
1. Fetch RSS bulletins from CERT-FR
2. Extract CVEs from local JSON files in `data/raw/`
3. Enrich with CVSS & EPSS scores
4. Train ML models and export plots to `outputs/plots/`
5. Generate security alerts and export to `outputs/generated_alerts.csv`
6. Optionally send alert emails via Gmail SMTP

### Email configuration (optional)

In the notebook, locate **Step 7** and set:

```python
EMAIL_ENABLED = True
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"   # Gmail App Password, not your regular password
RECIPIENT_EMAIL = "recipient@example.com"
```

---

## Running the Django Dashboard

```bash
cd django_app

# Apply database migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

Then open your browser at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Outputs

| File | Description |
|------|-------------|
| `outputs/generated_alerts.csv` | All triggered security alerts |
| `outputs/plots/` | ML visualizations (clustering, anomaly detection, feature importance, etc.) |
| `data/processed/consolidated_cve_data.csv` | Enriched CVE dataset |

---

## Notes

- `data/` and `outputs/` CSV files are tracked via **Git LFS**.
- The `venv/` folder is not versioned (listed in `.gitignore`).
- API calls to NVD and FIRST include mandatory delays to respect rate limits.
