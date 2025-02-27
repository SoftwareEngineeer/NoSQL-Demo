import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import seaborn as sns

st.title("NoSQL Banking Dashboard")
st.markdown("### Unlocking Big Data in Banking with NoSQL")
st.markdown("#### A Strategic Approach for VietinBank")

st.header("1. Real-Time Data Growth and Scalability")
data = pd.DataFrame({
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],
    "Traditional RDBMS": [1, 1.2, 1.4, 1.5, 1.6, 1.7],
    "NoSQL": [1, 1.4, 2.0, 2.7, 3.5, 4.5]
})
st.line_chart(data.set_index("Year"))
st.markdown("**Insight:** NoSQL scales horizontally with ease, unlike RDBMS limited by hardware.")

st.header("2. NoSQL vs. RDBMS Cost Efficiency")
st.markdown("### Cost Efficiency Analysis Tool")
data_volume = st.slider("Select Data Volume (in TB):", min_value=1, max_value=100, value=10, step=1)
rdbms_cost = data_volume * 200  
nosql_cost = data_volume * 120  

cost_data = pd.DataFrame({
    "Storage Type": ["RDBMS", "NoSQL"],
    "Cost ($)": [rdbms_cost, nosql_cost]
})
st.bar_chart(cost_data.set_index("Storage Type"))
st.markdown(f"**Total Cost for {data_volume} TB:** RDBMS = ${rdbms_cost}, NoSQL = ${nosql_cost}")

st.header("3. Fraud Detection Simulation")
st.markdown("### Real-Time Anomaly Detection using AI-Driven NoSQL Models")

np.random.seed(42)
transactions = np.random.normal(1000, 250, 100)
transactions[95:] = np.random.normal(10000, 3000, 5)  # Anomalies

df = pd.DataFrame(transactions, columns=["Transaction Amount"])
st.line_chart(df)

model = IsolationForest(contamination=0.05)
df['Anomaly'] = model.fit_predict(df)
anomalies = df[df['Anomaly'] == -1]

st.markdown("#### Anomalous Transactions Detected:")
st.write(anomalies)

st.header("4. Hybrid NoSQL-SQL Integration Demo")
st.markdown("### Unifying Structured and Unstructured Data")
st.markdown("""
This demo showcases how a hybrid NoSQL-SQL model can be used to:
- Efficiently store unstructured data (e.g., social media interactions) using NoSQL.
- Leverage SQL for complex transactional queries.
""")
st.markdown("""
**Example:** Combining customer transaction history (SQL) with social media feedback (NoSQL) for a 360-degree view.
""")

st.header("5. AI-Driven Database Optimization")
st.markdown("### How AI Dynamically Optimizes Query Execution")
st.markdown("""
- **Self-Tuning:** AI adjusts indexes and execution plans in real-time.
- **Predictive Query Optimization:** ML analyzes query patterns for enhanced performance.
- **Anomaly Detection:** AI detects security threats and performance bottlenecks.
""")
st.markdown("""
**Example:** Real-time scaling during peak transaction hours.
""")

st.header("6. Customer Insights & Recommendations")
st.markdown("Using NoSQL Document Stores for Personalized Banking")

customers = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Purchase History": ["Loan, Credit Card", "Savings, Loan", "Credit Card, Investments", "Savings, Insurance", "Insurance, Investments"],
    "Recommended Product": ["Investments", "Credit Card", "Insurance", "Savings", "Loan"]
})

st.table(customers)
st.markdown("### Powered by NoSQL Document Stores (MongoDB-like)")

st.header("7. Future Trends & Recommendations")
st.markdown("""
- **AI-Driven Databases:** Self-optimizing for performance.
- **NoSQL-SQL Hybrids:** Combining flexibility and complex query power.
- **Automated Scaling:** Reducing costs and improving efficiency.
- **Security & Compliance:** Proactive threat detection and automated compliance.
""")
st.markdown("### Recommendations for VietinBank")
st.markdown("""
1. Start with hybrid NoSQL-SQL integration for enhanced scalability.
2. Implement AI-driven databases for real-time optimization.
3. Invest in automated scaling solutions for cost efficiency.
""")
