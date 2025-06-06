import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("DevOps Career & Financial Tracker")
st.subheader("For Mrinal Bhoumick | Starting June 2025")

# Section 1: Monthly Financial Snapshot
st.header("1. Monthly Financial Snapshot")

# Categorize fixed and variable expenses
fixed_items = ["Rent (Kolkata)", "Education Loan EMI", "Misc + Home Support", "Monthly SIP", "Brother School Fees"]
variable_items = ["Fuel", "Home Wifi", "Phone Recharge", "Food & Drinks"]

# Data
financial_data = {
    "Item": [
        "Net In-Hand Salary", "Rent (Kolkata)", "Fuel", "Education Loan EMI",
        "Misc + Home Support", "Monthly SIP", "Home Wifi", "Phone Recharge",
        "Food & Drinks", "Brother School Fees", "Remaining Monthly Disposable"
    ],
    "Amount (₹)": [34570, 3000, 1500, 2877, 10000, 3500, 600, 450, 3000, 500, 9143]
}
df_financial = pd.DataFrame(financial_data)

# Show financial data with styling
def highlight_expense(row):
    if row["Item"] in fixed_items:
        return ["background-color: #ffdddd"] * len(row)
    elif row["Item"] in variable_items:
        return ["background-color: #ddffdd"] * len(row)
    else:
        return [""] * len(row)

st.dataframe(df_financial.style.apply(highlight_expense, axis=1))

# Pie chart
fig1, ax1 = plt.subplots()
labels = df_financial["Item"][1:-1]  # exclude Net Salary and Remaining
sizes = df_financial["Amount (₹)"][1:-1]
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Section 2: Savings & Investment Plan
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

# Monthly investment chart
st.subheader("Monthly Investment Allocation")
st.bar_chart(df_invest.set_index("Bucket")["Monthly (₹)"])

# Projected Remaining Balance Trend (if SIP increases ₹250 every 3 months)
st.subheader("Remaining Disposable Trend (12 Months)")
months = ["Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May"]
sip_series = [3500 + (i//3)*250 for i in range(12)]
expenses_fixed = 25427 - 3500  # all fixed except SIP
remaining_series = [34570 - (expenses_fixed + sip) for sip in sip_series]
trend_df = pd.DataFrame({"Month": months, "Remaining ₹": remaining_series})
st.line_chart(trend_df.set_index("Month"))

# Section 3: Milestone Plan
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

# Section 4: Investment Platforms
st.header("4. Investment Platform Suggestions")
platforms = pd.DataFrame({
    "Type": ["Mutual Funds SIP", "Emergency Fund", "Cert Learning", "GenAI Tools", "Budget Tracker"],
    "Platform": ["Groww, Kuvera", "Jupiter, Fi Money", "ACG, Whizlabs", "Claude 4, Zoho", "Notion, Excel"]
})
st.table(platforms)

# Section 5: Career Plan Integration
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

# Section 6: Monthly Goal Tracker (Interactive)
st.header("6. Monthly Goal Tracker ✅")
goals = [
    "Complete AWS DevOps Certification",
    "Build GenAI Automation Projects",
    "Update Resume & LinkedIn",
    "Apply to 10+ Job Roles",
    "Mock Interviews Scheduled",
    "Save Emergency Fund ₹30K",
    "Maintain SIP Consistency",
    "Laptop Upgrade Plan Initiated"
]

for goal in goals:
    st.checkbox(goal)

# Final Strategy Summary
st.header("7. Final Strategy Summary")
strategy_points = [
    "Stay in Workmates unless 2x offer",
    "Invest monthly in SIPs and corpus",
    "After certification, actively job hunt",
    "Mock interviews post-August",
    "Target 10 LPA by mid-2026"
]
st.write("\n".join([f"✅ {point}" for point in strategy_points]))

st.success("You’re building a smart roadmap. Stay focused and consistent. Good luck, Mrinal!")
