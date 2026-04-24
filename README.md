📦 Optimizing Retail Stock Levels Through AI-Powered Demand Prediction

📌 Overview
This project focuses on improving retail inventory management by combining demand forecasting with intelligent optimization techniques. The system leverages historical sales data along with external factors to predict demand and dynamically adjust stock levels.
The goal is to address a common retail challenge: maintaining the right balance between product availability and inventory cost. By integrating machine learning, time-series forecasting, and reinforcement learning, the project provides a comprehensive solution for reducing stockouts and overstock situations.

🎯 Problem Statement
Retailers often struggle with:
•	Overstocking → increased holding costs and wastage
•	Stockouts → lost sales and poor customer experience
These issues are primarily caused by inaccurate demand forecasting and static inventory policies.

🚀 Solution Approach
This project builds an end-to-end AI-driven system that includes:
•	Demand forecasting using multiple models
•	Inventory simulation and optimization
•	Reinforcement learning for adaptive decisions
•	Interactive dashboard for business insights

🧠 Key Features
•	📊 Exploratory Data Analysis (EDA)
•	📅 Seasonality and cycle detection
•	📈 Forecasting models (ARIMA, Prophet, LSTM)
•	📦 Inventory optimization with reorder logic
•	🤖 Reinforcement learning for adaptive stock control
•	⚠️ Alert system for low stock
•	📊 Interactive Streamlit dashboard
•	📥 Forecast download (CSV)

📂 Dataset
The dataset is sourced from Kaggle (Walmart Retail Dataset) and includes:
•	Weekly sales data (Store, Department level)
•	Holiday indicators (IsHoliday)
•	Promotional markdowns (MarkDown1–5)
•	Economic indicators (CPI, Unemployment, Fuel Price)
•	Store attributes (Type, Size)

⚙️ Project Workflow
Week 1–2: Data Preparation
•	Data cleaning and preprocessing
•	Handling missing values
•	Feature engineering
Week 3–4: EDA
•	Sales trends
•	Seasonal patterns
•	Inventory inefficiencies
Week 5–6: Forecasting
•	ARIMA
•	Prophet
•	LSTM
•	Model comparison
Week 7–8: Optimization
•	Reorder point calculation
•	Cost optimization
•	Reinforcement learning
Week 9–10: Dashboard
•	Visualization modules
•	Alerts and monitoring
Week 11–12: Business Insights
•	Strategy recommendations
•	Operational improvements

🧪 Models Used
Model	Purpose
ARIMA	Baseline time-series forecasting
Prophet	Seasonality-aware forecasting
LSTM	Deep learning for complex patterns
PPO (RL)	Adaptive inventory control

📊 Dashboard Modules
The Streamlit dashboard includes:
•	🏠 Overview
•	📊 EDA
•	📅 Seasonality
•	🔁 Cycle & Trend
•	📈 Forecasting
•	🔮 Forecast View (Actual vs Predicted + Download)
•	📦 Inventory Optimization
•	⚠️ Alerts
•	🤖 Model Performance
•	💼 Business Insights

📁 Project Structure
├── data/
│   ├── train.csv
│   ├── features.csv
│   └── stores.csv
│
├── output/
│   ├── final_inventory_output.csv
│   ├── forecast_output.csv
│   ├── model_performance.csv
│   └── graphs/
│
├── app.py                # Streamlit dashboard
├── main_model.py        # Full pipeline code
├── requirements.txt
└── README.md

🛠️ Installation
pip install -r requirements.txt

▶️ Run the Project
Run Main Pipeline
python main_model.py
Run Dashboard
streamlit run app.py

📈 Key Results
•	Improved demand forecasting accuracy
•	Reduced stockouts during peak periods
•	Lower inventory holding costs
•	Better alignment between demand and supply

💼 Business Impact
Warehouse
•	Better space utilization
•	Reduced excess inventory
Procurement
•	Data-driven purchasing decisions
•	Improved supplier coordination
Strategy
•	Predictive planning
•	Improved customer satisfaction

⚠️ Limitations
•	Limited external variables (e.g., competitor pricing)
•	Simplified reinforcement learning environment
•	Static cost assumptions

🔮 Future Improvements
•	Real-time data integration
•	Advanced deep learning models
•	Multi-store optimization
•	Scenario simulation tools


