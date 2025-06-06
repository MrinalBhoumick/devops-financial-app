import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("DevOps Career & Financial Tracker")
st.subheader("For Mrinal Bhoumick | Starting June 2025")

# 1. Monthly Financial Snapshot
st.header("1. Monthly Financial Snapshot")
financial_data = {
    "Item": [
        "Net In-Hand Salary", "Rent (Kolkata)", "Fuel", "Education Loan EMI",
        "Food", "Misc + Home Support", "Monthly SIP", "Remaining Monthly Disposable"
    ],
    "Amount (₹)": [34570, 3000, 1500, 2877, 2000, 10000, 3500, 11693]
}
df_financial = pd.DataFrame(financial_data)
st.dataframe(df_financial)

# Pie chart (excluding Remaining Disposable and Net Salary)
fig1, ax1 = plt.subplots()
labels = df_financial["Item"][1:-1]  # exclude Net Salary and Remaining
sizes = df_financial["Amount (₹)"][1:-1]
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# 2. Savings & Investment Plan
st.header("2. Savings & Investment Plan")
invest_data = {
    "Bucket": [
        "Emergency Fund", "DevOps Certification", "Mutual Funds SIP",
        "Technology Upskilling", "Personal Goals", "Travel & Wellness", "Laptop Upgrade"
    ],
    "Monthly (₹)": [3000, 2000, 3500, 1000, 2000, 1000, 1500],
    "Annual (₹)": [36000, 2000, 42000, 12000, 24000, 12000, 18000]
}
df_invest = pd.DataFrame(invest_data)
st.dataframe(df_invest)

# Bar chart for monthly investments
st.subheader("Monthly Investment Allocation")
st.bar_chart(df_invest.set_index("Bucket")["Monthly (₹)"])

# 3. Milestone Plan
st.header("3. Milestone Plan (June 2025 - May 2026)")
milestones = pd.DataFrame({
    "Month": ["June", "July–Sept", "Oct", "Nov–Dec", "Jan–Mar", "Apr–May"],
    "Goal": [
        "AWS DevOps Pro Certification", 
        "GenAI Automation Portfolio",
        "Update Resume + Start Applying",
        "Try for Promotion / Job Switch",
        "Focus on SIP & Corpus", 
        "Consider Asset Upgrade"
    ]
})
st.dataframe(milestones)

# 4. Investment Platform Suggestions
st.header("4. Investment Platform Suggestions")
platforms = pd.DataFrame({
    "Type": ["Mutual Funds SIP", "Emergency Fund", "Cert Learning", "GenAI Tools", "Budget Tracker"],
    "Platform": ["Groww, Kuvera", "Jupiter, Fi Money", "ACG, Whizlabs", "Claude 4, Zoho", "Notion, Excel"]
})
st.table(platforms)

# 5. Career Plan Integration
st.header("5. Career Plan Integration")
career_plan = pd.DataFrame({
    "Action": [
        "DevOps Certification (Jun–Jul)",
        "GenAI Project (Jun–Aug)",
        "Resume Update (Aug)",
        "GitHub Portfolio", 
        "Switch / Promotion (Oct–Dec)"
    ],
    "Benefit": [
        "Reach ₹8–10 LPA", 
        "Unique Profile", 
        "Add Latest Tools", 
        "Visible Skills", 
        "Up to 2x CTC"
    ]
})
st.dataframe(career_plan)

# 6. Final Strategy Summary
st.header("6. Final Strategy Summary")
strategy_points = [
    "Stay in Workmates unless 2x offer",
    "Invest monthly in SIPs and corpus",
    "After certification, actively job hunt",
    "Mock interviews post-August",
    "Target 10 LPA by mid-2026"
]
st.write("\n".join([f"✅ {point}" for point in strategy_points]))

st.success("This app helps you track finances + career & make informed decisions. Good luck, Mrinal!")
