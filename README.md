# marketing-mix-modeling-mini
# Marketing Mix Modeling (MMM) – Budget Optimization Project

## Project Overview
This project implements a **Marketing Mix Model (MMM)** using a regression-based approach to estimate the contribution of different marketing channels to sales.  
The goal is to support **data-driven budget allocation decisions** by analyzing channel effectiveness, simulating what-if scenarios, and optimizing spend under real-world constraints.

The project is designed as a **lightweight, interpretable baseline MMM**, suitable for business and marketing decision-making.

---

## Business Problem
Marketing teams often face the question:

> *How should we allocate a limited marketing budget across channels to maximize sales?*

This project addresses that question by:
- Estimating channel-level impact on sales
- Comparing ROI across channels
- Simulating budget reallocation scenarios
- Optimizing budget allocation under constraints

---

## Data Description
- **Granularity:** Weekly aggregated data  
- **Channels:**  
  - TV advertising  
  - Search (paid search)  
  - Social media  
  - Email marketing  
- **Target variable:** Sales

The dataset is **semi-synthetic**, designed to reflect realistic marketing behavior, including noise, different ROI levels, and diminishing returns.

**Columns:**
- `tv_spend`
- `search_spend`
- `social_spend`
- `email_spend`
- `sales`

---

## Modeling Approach
### Marketing Mix Model
A linear regression model is used as a baseline MMM:

Sales = β₀ + β₁·TV + β₂·Search + β₃·Social + β₄·Email + ε


This approach provides:
- High interpretability
- Clear marginal effects per channel
- Strong alignment with business decision-making needs

---

## Exploratory Data Analysis (EDA)
EDA focuses on:
- Validating spend ranges
- Checking for missing values
- Inspecting weekly trends and variability

The data shows realistic spend distributions and sales variability, making it suitable for regression-based modeling.

---

## ROI Analysis
Channel ROI is estimated by comparing regression coefficients to average channel spend:

ROI ≈ Marginal Contribution / Average Spend

This highlights:
- High-ROI digital channels
- Lower marginal returns for saturated channels (e.g., TV)

---

## What-if Scenario Analysis
To support managerial decision-making, the project includes **what-if simulations**, such as:

- Reducing TV spend by 20%
- Reallocating the freed budget to digital channels
- Estimating the resulting change in sales

These scenarios allow stakeholders to explore trade-offs before executing budget changes.

---

## Budget Optimization
### Objective
Maximize expected sales subject to real-world constraints.

### Constraints
- Total budget is fixed
- Each channel has minimum and maximum spend limits
- Spend must be non-negative

### Optimization Method
- Implemented using **SciPy constrained optimization**
- Objective function derived directly from the MMM coefficients
- Optimization logic implemented in a separate module (`optimization.py`) for clean code separation

---

## Results & Insights
Key insights from the optimized allocation:
- Budget is shifted away from saturated TV spend
- Higher allocation to high-ROI digital channels
- Total spend remains constant while expected sales increase

This demonstrates how MMM can directly inform **strategic budget decisions**.

---

## Project Structure
marketing-mix-modeling-mini/

│
├── mmm_model.ipynb # End-to-end MMM analysis

├── optimization.py # Budget optimization logic


├── data/
│ └── marketing_data.csv

├── requirements.txt

└── README.md


---

## How to Run
1. Install dependencies:

pip install -r requirements.txt
2.Run the notebook:
jupyter notebook mmm_model.ipynb

Key Takeaways
Built an interpretable Marketing Mix Model from end to end

Evaluated channel ROI and marginal returns

Simulated what-if budget scenarios

Optimized marketing budget under realistic constraints

Bridged analytics with real business decision-making

Future Improvements
Add saturation curves (log or Hill functions)

Incorporate lag/adstock effects

Validate results with controlled experiments (A/B testing)
