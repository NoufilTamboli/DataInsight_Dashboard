# DataInsight Dashboard

📊 **Automated CSV Analysis & Dashboard**

This project:
- Loads CSV data
- Cleans and analyzes it
- Generates KPI metrics
- Visualizes data interactively using Streamlit + Plotly
- Includes CI/CD via GitHub Actions

## Run Locally

```bash
pip install -r requirements.txt
streamlit run src/dashboard.py
```

## CI/CD

- Linting: flake8
- Unit Testing: pytest
- Workflow triggered on push or PR to `main`

## Folder Structure
```
data_insight_dashboard/
├── data/
│   └── sample_data.csv
├── src/
│   └── dashboard.py
├── tests/
│   └── test_data_loader.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── requirements.txt
└── README.md
```

---
Created by **Noufil Tamboli** 🚀
