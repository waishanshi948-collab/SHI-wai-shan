import streamlit as st
import time
import random
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Seadria Antifraud System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    .risk-high {
        color: #DC2626;
        font-weight: bold;
        padding: 8px 15px;
        background-color: #FEE2E2;
        border-radius: 8px;
        border-left: 4px solid #DC2626;
    }
    .risk-medium {
        color: #D97706;
        font-weight: bold;
        padding: 8px 15px;
        background-color: #FEF3C7;
        border-radius: 8px;
        border-left: 4px solid #D97706;
    }
    .risk-low {
        color: #059669;
        font-weight: bold;
        padding: 8px 15px;
        background-color: #D1FAE5;
        border-radius: 8px;
        border-left: 4px solid #059669;
    }
    .block-card {
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 20px;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .feature-card {
        background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #BAE6FD;
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
st.sidebar.markdown("""
<div style='text-align: center; margin-bottom: 30px;'>
    <h2 style='color: #2563EB;'>🛡️ Seadria</h2>
    <h3 style='color: #1E3A8A; font-size: 1.1rem;'>Antifraud Intelligence</h3>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    ["📊 Overview Dashboard", "💸 Transaction Simulator", "🔗 Alliance Monitor", "📈 Analytics & Reports"]
)

# ==================== DATA GENERATION ====================
def generate_transaction_data():
    """Generate mock transaction data"""
    fraud_patterns = ["Normal Purchase", "Task Fraud", "Fake Investment", "Authority Impersonation", "Money Laundering"]
    data = []
    
    for i in range(100):  # 减少数据量确保性能
        pattern = random.choice(fraud_patterns)
        amount = random.randint(50, 50000)
        
        if pattern == "Task Fraud":
            risk = random.randint(75, 95)
            status = "Blocked" if risk > 85 else "Under Review"
        elif pattern == "Fake Investment":
            risk = random.randint(80, 98)
            status = "Blocked" if risk > 80 else "Under Review"
        elif pattern == "Authority Impersonation":
            risk = random.randint(85, 99)
            status = "Blocked"
        elif pattern == "Money Laundering":
            risk = random.randint(70, 90)
            status = "Under Review"
        else:
            risk = random.randint(5, 30)
            status = "Completed"
        
        days_ago = random.randint(0, 30)
        timestamp = datetime.now() - timedelta(days=days_ago)
        
        data.append({
            "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M"),
            "Pattern": pattern,
            "Amount": f"${amount:,}",
            "Risk Score": risk,
            "Status": status,
            "Bank": random.choice(["Bank A", "Bank B", "Bank C", "Bank D"])
        })
    
    return pd.DataFrame(data)

# ==================== PAGES ====================
if page == "📊 Overview Dashboard":
    st.markdown('<h1 class="main-header">🛡️ Seadria Antifraud Intelligence Platform</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #4B5563; margin-bottom: 40px;">Federated Learning & Blockchain-Powered Defense Network</h3>', unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Alliance Members", "12 Institutions", "+2")
    with col2:
        st.metric("Transactions/Day", "2.4M", "+18.2%")
    with col3:
        st.metric("Detection Accuracy", "96.7%", "▲ 2.1%")
    with col4:
        st.metric("Losses Prevented", "$520M", "+$42M")
    
    st.markdown("---")
    
    # Technology Features
    st.markdown("### 🚀 Core Technology Advantages")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🤝 Federated Learning
        **Privacy-Preserving AI**
        - Data never leaves local banks
        - Collaborative model training
        - GDPR/CCPA compliant
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🔗 Blockchain Consortium
        **Transparent & Auditable**
        - Immutable audit trail
        - Smart contract automation
        - Cross-institution trust
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        st.markdown("""
        ### 🎯 Context-Aware Protection
        **Real-time Intervention**
        - Behavioral pattern recognition
        - Family protection network
        - Instant risk neutralization
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Fraud Trends Chart
    st.markdown("---")
    st.markdown("### 📊 Fraud Pattern Trends (Last 30 Days)")
    
    dates = pd.date_range(start="2024-10-01", periods=30, freq="D")
    chart_data = pd.DataFrame({
        "Date": dates,
        "Investment Fraud": [random.randint(40, 65) for _ in range(30)],
        "Task Scams": [random.randint(30, 55) for _ in range(30)],
        "Impersonation": [random.randint(15, 35) for _ in range(30)]
    })
    
    chart_data_melted = chart_data.melt(id_vars=["Date"], var_name="Fraud Type", value_name="Cases")
    fig = px.line(chart_data_melted, x="Date", y="Cases", color="Fraud Type", markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif page == "💸 Transaction Simulator":
    st.title("💸 Transaction Risk Simulator")
    st.markdown("*Experience real-time fraud detection in action*")
    
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.markdown("### 1. Transaction Details")
        
        scenario = st.radio(
            "Select Transaction Scenario:",
            ["💰 Normal Transfer to Friend", 
             "📱 Task Commission Payment", 
             "📈 High-Return Investment", 
             "⚖️ 'Legal Fee' Payment"],
            horizontal=False
        )
        
        scenarios = {
            "💰 Normal Transfer to Friend": {
                "account": "•••• 4832", "name": "Michael Chen", 
                "institution": "Chase Bank", "risk": "low"
            },
            "📱 Task Commission Payment": {
                "account": "0x8f3a...c7e9", "name": "QuickTask Platform", 
                "institution": "Cryptocurrency Wallet", "risk": "high"
            },
            "📈 High-Return Investment": {
                "account": "invest-secure.com", "name": "WealthGrow Fund", 
                "institution": "Investment Platform", "risk": "high"
            },
            "⚖️ 'Legal Fee' Payment": {
                "account": "•••• 6712", "name": "Federal Court", 
                "institution": "Bank of America", "risk": "high"
            }
        }
        
        selected = scenarios[scenario]
        
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Amount (USD)", min_value=1, max_value=200000, value=1000)
        with col2:
            st.text_input("Recipient Account", value=selected["account"], disabled=True)
        
        st.text_input("Recipient Name", value=selected["name"], disabled=True)
        st.text_input("Financial Institution", value=selected["institution"], disabled=True)
        
        if st.button("🚀 Process Transaction", type="primary", use_container_width=True):
            with st.spinner("Connecting to Seadria Alliance Network..."):
                time.sleep(2)
                
                risk_profiles = {
                    "💰 Normal Transfer to Friend": {
                        "score": 8, "level": "low",
                        "message": "✅ Transaction appears legitimate"
                    },
                    "📱 Task Commission Payment": {
                        "score": 94, "level": "high",
                        "message": "🚨 Task Fraud Pattern Detected"
                    },
                    "📈 High-Return Investment": {
                        "score": 89, "level": "high",
                        "message": "🚨 Suspected Investment Scam"
                    },
                    "⚖️ 'Legal Fee' Payment": {
                        "score": 97, "level": "high",
                        "message": "🚨 Authority Impersonation Detected"
                    }
                }
                
                result = risk_profiles[scenario]
                
                st.markdown("---")
                st.markdown("### 2. Real-time Risk Analysis")
                
                if result["level"] == "high":
                    st.markdown(f'<div class="risk-high">CRITICAL RISK ALERT! Score: {result["score"]}/100</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="risk-low">LOW RISK! Score: {result["score"]}/100</div>', unsafe_allow_html=True)
                
                st.info(f"**Analysis:** {result['message']}")
                
                if result["level"] == "high":
                    st.error("**🛡️ Protection System Activated:** Transaction suspended for verification.")
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("⚠️ Override & Proceed", use_container_width=True):
                            st.error(f"Transaction forced. ${amount:,} transferred.")
                    with col_b:
                        if st.button("✅ Cancel Transaction", type="primary", use_container_width=True):
                            st.success(f"Transaction canceled. ${amount:,} remains secure.")
                else:
                    if st.button("✅ Confirm Transaction", type="primary", use_container_width=True):
                        st.success(f"Transaction completed! ${amount:,} transferred successfully.")
    
    with right_col:
        st.markdown("### 📱 Mobile Interface")
        
        # FIXED: 修正了HTML字符串中的引号问题
        risk_color = "#92400E" if selected["risk"] == "high" else "#065F46"
        risk_text = "⚠️ Risk Assessment Pending" if selected["risk"] == "high" else "✅ Secured Transaction"
        
        mobile_html = f"""
        <div style="border: 2px solid #CBD5E1; border-radius: 24px; padding: 20px; width: 280px; margin: 0 auto; background: #F8FAFC;">
            <div style="text-align: center; margin-bottom: 15px;">
                <div style="font-size: 1.1em; font-weight: 600; color: #1E293B;">Seadria Shield</div>
            </div>
            
            <div style="background: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <div style="text-align: center; margin-bottom: 10px;">
                    <div style="font-size: 1.8em; font-weight: 700; color: #1E293B;">${amount:,}</div>
                </div>
                
                <div style="margin: 10px 0;">
                    <div style="font-size: 0.8em; color: #94A3B8;">TO ACCOUNT</div>
                    <div style="font-weight: 600; color: #1E293B;">{selected['account']}</div>
                </div>
                
                <div style="background: {'#FEF3C7' if selected['risk'] == 'high' else '#D1FAE5'}; padding: 8px; border-radius: 6px; margin-top: 10px;">
                    <div style="font-size: 0.8em; color: {risk_color};">
                        {risk_text}
                    </div>
                </div>
            </div>
        </div>
        """
        
        st.markdown(mobile_html, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 👨‍👩‍👧 Guardian Network")
        st.success("""
        **Active Guardians:**
        • Michael Chen (Father)
        • Sarah Wilson (Spouse)
        
        **Status:** Online
        """)

elif page == "🔗 Alliance Monitor":
    st.title("🔗 Real-time Alliance Monitor")
    
    st.markdown('<div class="block-card">', unsafe_allow_html=True)
    st.markdown("""
    <h4>⛓️ Consortium Blockchain Activity</h4>
    <p style="color: #6B7280;">Synchronizing threat intelligence across 12 financial institutions...</p>
    <div style="background: #F3F4F6; padding: 10px; border-radius: 6px; font-family: monospace;">
        <div style="color: #059669;">✓ Block #84291: Bank C → Fraud pattern uploaded</div>
        <div style="color: #2563EB;">⏳ Block #84292: Model update aggregating</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 🚨 Live Threat Alerts")
    
    alerts = [
        {"time": "14:28:03", "source": "Bank B", "type": "Investment Scam", "score": 96},
        {"time": "14:27:45", "source": "Platform C", "type": "Money Mule", "score": 88},
        {"time": "14:27:22", "source": "Bank A", "type": "Phishing", "score": 91},
    ]
    
    for alert in alerts:
        cols = st.columns([1, 2, 1, 1])
        cols[0].code(alert["time"])
        cols[1].write(f"**{alert['type']}**")
        cols[2].write(f"🏦 {alert['source']}")
        if alert["score"] > 90:
            cols[3].markdown(f'<span class="risk-high">{alert["score"]}</span>', unsafe_allow_html=True)
        else:
            cols[3].markdown(f'<span class="risk-medium">{alert["score"]}</span>', unsafe_allow_html=True)
        st.divider()
    
    st.markdown("---")
    st.markdown("### 🤖 Federated Learning Status")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Training Round", "#48")
        st.progress(0.82)
    with col2:
        st.metric("Active Nodes", "12/12")
        st.progress(1.0)

elif page == "📈 Analytics & Reports":
    st.title("📈 Analytics & Impact Reports")
    
    df = generate_transaction_data()
    
    st.markdown("### 📊 Executive Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Transactions", len(df))
    with col2:
        blocked = len(df[df['Status'] == 'Blocked'])
        st.metric("Fraud Blocked", blocked)
    with col3:
        st.metric("Block Rate", f"{(blocked/len(df)*100):.1f}%")
    
    st.markdown("---")
    st.markdown("### 🔍 Data Explorer")
    
    tab1, tab2 = st.tabs(["Data Table", "Charts"])
    
    with tab1:
        st.dataframe(df, use_container_width=True, height=300)
    
    with tab2:
        # Risk Distribution
        fig1 = px.histogram(df, x='Risk Score', nbins=20, title='Risk Score Distribution')
        st.plotly_chart(fig1, use_container_width=True)
        
        # Pattern Distribution
        pattern_counts = df['Pattern'].value_counts().reset_index()
        pattern_counts.columns = ['Pattern', 'Count']
        fig2 = px.pie(pattern_counts, values='Count', names='Pattern', title='Fraud Pattern Distribution')
        st.plotly_chart(fig2, use_container_width=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.9em; padding: 20px;">
    <p><strong>🛡️ Seadria Antifraud Intelligence Platform</strong></p>
    <p>Federated Learning & Blockchain Consortium | Demo Version</p>
</div>
""", unsafe_allow_html=True)

# Auto-refresh
if st.sidebar.checkbox("🔄 Enable Live Updates", False):
    st.rerun()

# Sidebar info
st.sidebar.markdown("---")
st.sidebar.info("""
**Demo Instructions:**
1. Try different transaction scenarios
2. Observe risk assessment results
3. Experience protection mechanisms
""")
