<h1 align="center">BCG X Gen AI Job Simulation - Forage</h1>
<h2 align="center">Financial Trend Analysis • Ratio Calculation • Chatbot Logic Implementation</h2>

A comprehensive project demonstrating an end-to-end financial data workflow, from manual extraction of corporate filings to programmatic analysis and a prototype AI chatbot interface for delivering insights.

---

## 💡 Overview

This project simulates a complete financial data pipeline:

1. **Financial Data Extraction** – Manual collection of key figures from 10-K filings of Microsoft, Tesla, and Apple.  
2. **Programmatic Analysis** – Calculation of growth rates, profitability, and debt ratios using Python and Pandas.  
3. **AI Chatbot Prototype** – A command-line interface (CLI) chatbot that maps predefined financial queries to analytical insights.

---

## 📁 Project Deliverables

| Task | Focus Area | Files |
|------|------------|-------|
| Task 1 | Data Extraction & Financial Trend Analysis | `Task 1 - BCG.ipynb`, `10-K Filings.xlsx`, |
| Task 2 | AI Chatbot Prototype Development | `Financial_Chatbot.py` |

---

## ✅ Task 1: Data Extraction and Financial Trend Analysis

### Methodology
- **Data Source:** 10-K filings from SEC EDGAR  
- **Key Metrics:** Total Revenue, Net Income, Total Assets, Total Liabilities, Cash Flow from Operating Activities  
- **Calculations:**  
  - Year-over-Year (YoY) percentage changes for Revenue and Net Income  
  - Profit Margin (%) and Debt Ratio (Total Liabilities / Total Assets)

### Key Analytical Outputs

The following key ratios and growth figures were calculated using `pandas` and form the basis of the analysis.

| Company | Profit Margin (%) (2024) | Debt Ratio (2024) | Net Income Growth (%) (2023) |
| :--- | :--- | :--- | :--- |
| **Microsoft** | 35.95 | 0.47 | -17.89 |
| **Tesla** | 7.32 | 0.39 | 109.34 |
| **Apple** | 23.97 | 0.84 | 3.48 |

**Comparative Financial Health**

* **Scale Dominance:** Apple and Microsoft demonstrate significantly higher absolute figures for Revenue and Net Income compared to Tesla.
* **Profitability Highlight:** Microsoft exhibits the highest Profit Margin in 2024 at 35.95%, indicating strong operational efficiency.
* **Growth Volatility:** Tesla showed the most significant year-over-year Net Income growth for 2023 at 109.34%, highlighting its rapid, albeit volatile, growth trajectory.

---

## 🤖 Task 2: AI-Powered Financial Chatbot Prototype

### Implementation
- **Technology:** Python CLI script (`Financial_Chatbot.py`)  
- **Logic:** Simple dictionary mapping or if/else structure for predefined queries  
- **Focus:** Structured financial data retrieval (not NLP-based)

### Chatbot Capabilities
The prototype responds to queries such as:
- “What is the total revenue?”  
- “How has net income changed over the last year?”  
- “What are the total assets and liabilities?”  
- “What is the operating cash flow trend?”  
- “Which company is the most profitable?”

---

## 📂 Repository Structure
| File / Folder                  | Description                             |
|--------------------------------|-----------------------------------------|
| 10-K Filings.xlsx  | Extracted financial data               |
| Financial_Chatbot.py           | Chatbot prototype script                |
| Task 1 - BCG.ipynb             | Jupyter Notebook for analysis           |
| GenAI Certificate - BCG X.pdf            | Completion Certificate           |
| README.md                       | Project documentation                   |

---

## 🙋‍♂️ About Me

👤 **Satyam Kumar**  
📧 **satyamkv123@gmail.com**  
🌐 [LinkedIn](https://www.linkedin.com/in/satyam-kumar-5a229222b)

---


