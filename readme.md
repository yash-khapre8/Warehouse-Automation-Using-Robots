# 📦 Warehouse Automation Using Robots – Analytics Dashboard

## 📖 Project Overview - https://colab.research.google.com/drive/1TcgVT52Go-EoR5z-bqwcNbMvgKW9C0d2?usp=sharing

This project analyzes the **business impact of implementing robotic warehouse automation** for SpeedLogistics Pvt. Ltd.

The company currently handles **15,000 orders per day manually**, which leads to:

* Slower order processing
* Higher labor costs
* Increased human errors
* Delivery delays during peak seasons

To solve this, the company plans to invest **₹3.5 Crores** in a **Warehouse Automation System** consisting of:

* Automated Guided Vehicles (AGVs)
* Robotic Picking Arms
* Barcode Scanners
* Central Control System for real-time tracking

The objective of this project is to perform:

* **Cost–Benefit Analysis**
* **Operational Data Simulation**
* **Interactive Dashboard Visualization**

---

# 📊 Business and Financial Analysis

### Current Annual Cost

₹6 Crores spent on:

* Warehouse labor
* Error corrections
* Delivery delays

### Expected Improvements After Automation

| Metric     | Reduction |
| ---------- | --------- |
| Labor Cost | 35%       |
| Error Loss | 40%       |

### Financial Calculations

Labor Savings
= 35% × ₹6 Cr
= **₹2.1 Crores**

Error Savings
= 40% × ₹6 Cr
= **₹2.4 Crores**

Total Annual Savings
= ₹2.1 Cr + ₹2.4 Cr
= **₹4.5 Crores**

Investment Cost
= **₹3.5 Crores**

Net Benefit
= ₹4.5 Cr − ₹3.5 Cr
= **₹1 Crore**

### 📈 Conclusion

The automation investment generates **₹1 Crore net benefit**, making it financially profitable.

---

# 🧠 Synthetic Data Generation

Real warehouse operational data may not always be available.
Therefore, **synthetic warehouse data** was generated using Python.

Using libraries such as:

* `pandas`
* `random`

We simulated realistic warehouse parameters:

| Column              | Description                          |
| ------------------- | ------------------------------------ |
| Order_ID            | Unique order number                  |
| Robot_Task_Time_sec | Time taken by robot to complete task |
| Picking_Accuracy_%  | Accuracy rate of robotic picking     |
| Daily_Order_Volume  | Number of orders processed daily     |

This simulated dataset helps analyze warehouse performance and visualize system efficiency.

---

# 📊 Interactive Streamlit Dashboard

An **interactive analytics dashboard** was built using **Streamlit** to visualize warehouse operations.

### Dashboard Features

✔ Financial KPI Metrics
✔ Synthetic Warehouse Data Table
✔ Robot Task Time Visualization
✔ Picking Accuracy Trends
✔ Operational Insights
✔ Business Recommendation System
✔ Downloadable Dataset

Users can also adjust **simulation parameters** from the sidebar.

---

# 🖥️ Dashboard Preview

The dashboard displays:

* Financial performance metrics
* Warehouse operational charts
* Real-time simulated warehouse data
* Business insights and recommendations

---

# ⚙️ Technologies Used

| Technology                    | Purpose                              |
| ----------------------------- | ------------------------------------ |
| Python                        | Data simulation and analysis         |
| Pandas                        | Data manipulation                    |
| Streamlit                     | Interactive dashboard                |
| Matplotlib / Streamlit Charts | Data visualization                   |
| Google Colab                  | Initial analysis and experimentation |

---

# 📂 Project Structure

```
warehouse-automation-dashboard
│
├── app.py                # Streamlit dashboard
├── notebook.ipynb       # Google Colab analysis
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

---

# ▶️ Running the Dashboard Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run app.py
```

The dashboard will open in your browser:

```
http://localhost:8501
```

---

# 🌐 Deployment

The dashboard can be deployed using **Streamlit Cloud**.

Steps:

1. Upload project to GitHub
2. Go to **Streamlit Cloud**
3. Connect repository
4. Deploy using `app.py`

The deployed app will generate a public link for access.

---

# 📌 Business Impact

Warehouse automation provides several operational advantages:

* Faster order processing
* Reduced human errors
* Lower labor costs
* Improved order accuracy
* Better customer satisfaction
* Real-time warehouse monitoring

---

# 🎯 Final Recommendation

Based on the **cost–benefit analysis and simulated operational data**, it is recommended that **SpeedLogistics Pvt. Ltd. should invest in warehouse automation**.

The automation system not only produces a **positive financial return**, but also significantly improves warehouse efficiency and scalability.

---

# 👨‍💻 Author

**Yash Khapre**
B.Tech CSE
ITM Skills University

Skills Used:

* Python
* Data Analysis
* Streamlit Dashboards
* Business Case Analysis
