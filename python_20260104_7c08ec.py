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
    .company-name {
        color: #2563EB;
        font-weight: 800;
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
        margin-bottom: 15px;
    }
    .feature-card {
        background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #BAE6FD;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR NAVIGATION ====================
st.sidebar.markdown(f"""
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
    
    for i in range(150):
        pattern = random.choice(fraud_patterns)
        amount = random.randint(50, 50000)
        
        # Set base risk score based on pattern
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
        
        # Generate timestamp
        days_ago = random.randint(0, 30)
        hours_ago = random.randint(0, 23)
        timestamp = datetime.now() - timedelta(days=days_ago, hours=hours_ago)
        
        data.append({
            "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M"),
            "Pattern": pattern,
            "Amount (USD)": f"${amount:,}",
            "Risk Score": risk,
            "Status": status,
            "Bank": random.choice(["Bank A", "Bank B", "Bank C", "Bank D"])
        })
    
    return pd.DataFrame(data)

# ==================== PAGES ====================
if page == "📊 Overview Dashboard":
    # HEADER
    st.markdown('<h1 class="main-header">🛡️ Seadria Antifraud Intelligence Platform</h1>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; color: #4B5563; margin-bottom: 40px;">Federated Learning & Blockchain-Powered Defense Network</h3>', unsafe_allow_html=True)
    
    # KEY METRICS
    st.markdown("### 📈 Real-time System Metrics")
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
    
    # TECHNOLOGY FEATURES
    st.markdown("### 🚀 Core Technology Advantages")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("""
            ### 🤝 Federated Learning
            **Privacy-Preserving AI**
            - Data never leaves local banks
            - Collaborative model training
            - GDPR/CCPA compliant
            - Zero raw data sharing
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("""
            ### 🔗 Blockchain Consortium
            **Transparent & Auditable**
            - Immutable audit trail
            - Contribution tokenization
            - Smart contract automation
            - Cross-institution trust
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown('<div class="feature-card">', unsafe_allow_html=True)
            st.markdown("""
            ### 🎯 Context-Aware Protection
            **Real-time Intervention**
            - Behavioral pattern recognition
            - Multi-layered defense
            - Family protection network
            - Instant risk neutralization
            """)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # FRAUD TRENDS
    st.markdown("---")
    st.markdown("### 📊 Fraud Pattern Trends (Last 30 Days)")
    
    trends_data = pd.DataFrame({
        "Date": pd.date_range(start="2024-10-01", periods=30, freq="D"),
        "Investment Fraud": [random.randint(40, 65) for _ in range(30)],
        "Task Scams": [random.randint(30, 55) for _ in range(30)],
        "Impersonation": [random.randint(15, 35) for _ in range(30)],
        "Money Laundering": [random.randint(10, 30) for _ in range(30)]
    })
    
    fig = px.line(trends_data.melt(id_vars=["Date"], var_name="Fraud Type", value_name="Cases"),
                  x="Date", y="Cases", color="Fraud Type",
                  title="Daily Fraud Case Distribution",
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

elif page == "💸 Transaction Simulator":
    st.title("💸 Transaction Risk Simulator")
    st.markdown("*Experience real-time fraud detection in action*")
    
    # TWO-COLUMN LAYOUT
    sim_col, demo_col = st.columns([2, 1])
    
    with sim_col:
        st.markdown("### 1. Transaction Details")
        
        # SCENARIO SELECTION
        scenario = st.radio(
            "Select Transaction Scenario:",
            ["💰 Normal Transfer to Friend", 
             "📱 Task Commission Payment", 
             "📈 High-Return Investment", 
             "⚖️ 'Legal Fee' Payment"],
            horizontal=True
        )
        
        # SCENARIO PRESETS
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
        
        # TRANSACTION FORM
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Amount (USD)", min_value=1, max_value=200000, 
                                    value=1000 if scenario == "💰 Normal Transfer to Friend" else 25000)
        with col2:
            st.text_input("Recipient Account", value=selected["account"], disabled=True)
        
        st.text_input("Recipient Name", value=selected["name"], disabled=True)
        st.text_input("Financial Institution", value=selected["institution"], disabled=True)
        
        # INITIATE TRANSACTION
        if st.button("🚀 Process Transaction", type="primary", use_container_width=True):
            with st.spinner("Connecting to Seadria Alliance Network..."):
                time.sleep(2.5)
                
                # RISK ANALYSIS
                risk_profiles = {
                    "💰 Normal Transfer to Friend": {
                        "score": 8, "level": "low",
                        "message": "✅ Transaction appears legitimate",
                        "details": "• Recipient is in your contacts\n• Normal transaction pattern\n• Low-risk amount"
                    },
                    "📱 Task Commission Payment": {
                        "score": 94, "level": "high",
                        "message": "🚨 Task Fraud Pattern Detected",
                        "details": "• Platform associated with 142 scam reports\n• Irregular payment pattern\n• High victim concentration"
                    },
                    "📈 High-Return Investment": {
                        "score": 89, "level": "high",
                        "message": "🚨 Suspected Investment Scam",
                        "details": "• Unregistered investment platform\n• Promises unrealistic returns\n• 8 alliance members flagged similar patterns"
                    },
                    "⚖️ 'Legal Fee' Payment": {
                        "score": 97, "level": "high",
                        "message": "🚨 Authority Impersonation Detected",
                        "details": "• Fake government agency account\n• Urgency pressure tactics\n• Exact match with known fraud template"
                    }
                }
                
                result = risk_profiles[scenario]
                
                # DISPLAY RESULTS
                st.markdown("---")
                st.markdown("### 2. Real-time Risk Analysis")
                
                # RISK INDICATOR
                if result["level"] == "high":
                    st.markdown(f'<div class="risk-high">CRITICAL RISK ALERT! Score: {result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                elif result["level"] == "medium":
                    st.markdown(f'<div class="risk-medium">MODERATE RISK! Score: {result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="risk-low">LOW RISK! Score: {result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                
                st.info(f"**Analysis:** {result['message']}")
                st.warning(f"**Key Findings:**\n{result['details']}")
                
                # PROTECTION MECHANISMS
                if result["level"] == "high":
                    st.error("""
                    **🛡️ Protection System Activated:**
                    1. **Transaction suspended** - Requires manual override
                    2. **Guardian notified** - Family protection network alerted
                    3. **Law enforcement API** - Report generated for authorities
                    4. **Alliance warning** - Pattern shared with 12 partner institutions
                    """)
                    
                    # ACTION BUTTONS
                    action_col1, action_col2, action_col3 = st.columns(3)
                    with action_col1:
                        if st.button("⚠️ Override & Proceed", type="secondary"):
                            st.error("Transaction forced. **$" + f"{amount:,}" + " transferred.** High risk acknowledged.")
                    with action_col2:
                        if st.button("📞 Verify Recipient", type="secondary"):
                            st.info("Simulating verification call...")
                            time.sleep(1)
                            st.success("Verification failed - number disconnected.")
                    with action_col3:
                        if st.button("✅ Cancel Transaction", type="primary"):
                            st.success(f"Transaction canceled. ${amount:,} remains secure.")
                else:
                    if st.button("✅ Confirm Transaction", type="primary"):
                        st.balloons()
                        st.success(f"Transaction completed! ${amount:,} transferred successfully.")
    
    with demo_col:
        st.markdown("### 📱 Mobile Interface Demo")
        
        # MOBILE APP MOCKUP
        st.markdown(f"""
        <div style="border: 2px solid #CBD5E1; border-radius: 24px; padding: 25px; 
                    width: 300px; margin: 0 auto; background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%); 
                    box-shadow: 0 10px 25px rgba(0,0,0,0.08); position: relative;">
            
            <!-- Status Bar -->
            <div style="display: flex; justify-content: space-between; margin-bottom: 20px; font-size: 0.8em; color: #64748B;">
                <span>9:41</span>
                <span>🛡️ Seadria Secure</span>
            </div>
            
            <!-- App Content -->
            <div style="text-align: center; margin-bottom: 10px;">
                <div style="font-size: 1.2em; font-weight: 600; color: #1E293B;">Seadria Shield</div>
                <div style="font-size: 0.9em; color: #475569;">Active Protection</div>
            </div>
            
            <!-- Transaction Card -->
            <div style="background: white; padding: 20px; border-radius: 16px; 
                        box-shadow: 0 4px 12px rgba(0,0,0,0.05); margin: 15px 0;">
                <div style="text-align: center; margin-bottom: 15px;">
                    <div style="font-size: 2em; font-weight: 700; color: #1E293B;">${amount:,}</div>
                    <div style="font-size: 0.9em; color: #64748B;">Transfer Amount</div>
                </div>
                
                <div style="margin: 15px 0;">
                    <div style="font-size: 0.8em; color: #94A3B8;">TO ACCOUNT</div>
                    <div style="font-weight: 600; color: #1E293B;">{selected['account']}</div>
                </div>
                
                <div style="margin: 15px 0;">
                    <div style="font-size: 0.8em; color: #94A3B8;">RECIPIENT</div>
                    <div style="font-weight: 600; color: #1E293B;">{selected['name']}</div>
                </div>
                
                <div style="background: {'#FEF3C7' if selected['risk'] == 'high' else '#D1FAE5'}; 
                            padding: 8px; border-radius: 8px; margin-top: 15px;">
                    <div style="font-size: 0.8em; color: #92400E if selected['risk'] == 'high' else #065F46;">
                        {'⚠️ Risk Assessment Pending' if selected['risk'] == 'high' else '✅ Secured Transaction'}
                    </div>
                </div>
            </div>
            
            <!-- Protection Badge -->
            <div style="text-align: center; margin-top: 15px;">
                <div style="display: inline-flex; align-items: center; background: #DBEAFE; 
                            padding: 6px 12px; border-radius: 20px; font-size: 0.8em;">
                    <span style="margin-right: 5px;">🔒</span> Seadria Protected
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # GUARDIAN NETWORK STATUS
        st.markdown("---")
        st.markdown("### 👨‍👩‍👧 Guardian Network")
        st.success("""
        **Active Guardians:**
        • 👨 Michael Chen (Father) - **Online**
        • 👩 Sarah Wilson (Spouse) - **Online 5m ago**
        
        **Last Alert:** 2 days ago
        """)

elif page == "🔗 Alliance Monitor":
    st.title("🔗 Real-time Alliance Monitor")
    st.markdown("*Live cross-institution threat intelligence dashboard*")
    
    # BLOCKCHAIN VISUALIZATION
    st.markdown("""
    <div class="block-card">
        <h4>⛓️ Consortium Blockchain Activity</h4>
        <p style="color: #6B7280;">Synchronizing threat intelligence across 12 financial institutions...</p>
        <div style="background: #F3F4F6; padding: 15px; border-radius: 8px; font-family: monospace; margin-top: 10px;">
            <div style="color: #059669;">✓ Block #84291: Bank C → Fraud pattern uploaded</div>
            <div style="color: #059669;">✓ Block #84292: Payment Platform B → Risk proof verified</div>
            <div style="color: #2563EB;">⏳ Block #84293: Bank A → Model update aggregating (78%)</div>
            <div style="color: #6B7280;">◻ Block #84294: Bank D → Pending contribution</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # LIVE ALERT STREAM
    st.markdown("### 🚨 Live Threat Intelligence Stream")
    
    # SAMPLE ALERTS
    alerts = [
        {"time": "14:28:03", "source": "Bank B", "type": "Investment Scam", "severity": "Critical", "score": 96},
        {"time": "14:27:45", "source": "Platform C", "type": "Money Mule", "severity": "High", "score": 88},
        {"time": "14:27:22", "source": "Bank A", "type": "Phishing Attack", "severity": "High", "score": 91},
        {"time": "14:26:58", "source": "Bank D", "type": "Account Takeover", "severity": "Medium", "score": 74},
        {"time": "14:26:30", "source": "Bank F", "type": "Synthetic Identity", "severity": "High", "score": 86}
    ]
    
    for alert in alerts:
        with st.container():
            cols = st.columns([1, 2, 1, 1, 1])
            cols[0].code(alert["time"])
            cols[1].write(f"**{alert['type']}**")
            cols[2].write(f"🏦 {alert['source']}")
            
            if alert["severity"] == "Critical":
                cols[3].markdown(f"<span class='risk-high'>{alert['score']}</span>", unsafe_allow_html=True)
                cols[4].markdown("🔴 **Critical**")
            elif alert["severity"] == "High":
                cols[3].markdown(f"<span class='risk-high'>{alert['score']}</span>", unsafe_allow_html=True)
                cols[4].markdown("🟠 **High**")
            else:
                cols[3].markdown(f"<span class='risk-medium'>{alert['score']}</span>", unsafe_allow_html=True)
                cols[4].markdown("🟡 **Medium**")
            
            st.divider()
    
    # FEDERATED LEARNING STATUS
    st.markdown("---")
    st.markdown("### 🤖 Federated Learning Engine")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Training Round", "#48", "+1")
        st.progress(0.82, text="Global Model Aggregation")
    with col2:
        st.metric("Active Nodes", "12/12", "100%")
        st.progress(1.0, text="Data Synchronization")
    with col3:
        st.metric("Pattern Library", "8,421", "+142")
        st.progress(0.65, text="Feature Extraction")
    
    # PERFORMANCE COMPARISON
    st.markdown("#### 🏆 Performance Improvement")
    
    comparison_data = pd.DataFrame({
        "Metric": ["Detection Accuracy", "False Positive Rate", "Response Time", "Pattern Coverage"],
        "Traditional System": [78.3, 22.5, "4.2s", "64%"],
        "Seadria Alliance": [96.7, 5.3, "0.8s", "92%"],
        "Improvement": ["+18.4%", "-17.2%", "-3.4s", "+28%"]
    })
    
    st.dataframe(comparison_data, use_container_width=True, hide_index=True)

elif page == "📈 Analytics & Reports":
    st.title("📈 Analytics & Impact Reports")
    
    # GENERATE SAMPLE DATA
    df = generate_transaction_data()
    
    # EXECUTIVE SUMMARY
    st.markdown("### 📊 Executive Summary")
    
    total_tx = len(df)
    blocked = len(df[df['Status'] == 'Blocked'])
    prevented_amount = blocked * random.randint(5000, 50000)
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Transactions", f"{total_tx:,}")
    kpi2.metric("Fraud Attempts Blocked", f"{blocked}")
    kpi3.metric("Block Rate", f"{(blocked/total_tx*100):.1f}%")
    kpi4.metric("Estimated Losses Prevented", f"${prevented_amount:,}")
    
    # INTERACTIVE DATA EXPLORER
    st.markdown("---")
    st.markdown("### 🔍 Transaction Data Explorer")
    
    # FILTERS
    filter_col1, filter_col2, filter_col3 = st.columns(3)
    with filter_col1:
        min_risk = st.slider("Minimum Risk Score", 0, 100, 50)
    with filter_col2:
        selected_patterns = st.multiselect(
            "Fraud Patterns",
            df['Pattern'].unique(),
            default=df['Pattern'].unique()[:3]
        )
    with filter_col3:
        selected_banks = st.multiselect(
            "Financial Institutions",
            df['Bank'].unique(),
            default=df['Bank'].unique()
        )
    
    # APPLY FILTERS
    filtered_df = df[
        (df['Risk Score'] >= min_risk) &
        (df['Pattern'].isin(selected_patterns)) &
        (df['Bank'].isin(selected_banks))
    ]
    
    # DATA DISPLAY
    tab1, tab2, tab3 = st.tabs(["📋 Data Table", "📈 Visual Analytics", "📊 Institution Breakdown"])
    
    with tab1:
        st.dataframe(filtered_df, use_container_width=True, height=400)
        
        # EXPORT OPTION
        if st.button("📥 Export to CSV"):
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="seadria_transaction_data.csv",
                mime="text/csv"
            )
    
    with tab2:
        st.markdown("##### Risk Score Distribution")
        fig1 = px.histogram(filtered_df, x='Risk Score', nbins=20,
                           title='Risk Score Frequency Distribution')
        st.plotly_chart(fig1, use_container_width=True)
        
        st.markdown("##### Fraud Pattern Analysis")
        pattern_counts = filtered_df['Pattern'].value_counts().reset_index()
        pattern_counts.columns = ['Fraud Pattern', 'Cases']
        fig2 = px.pie(pattern_counts, values='Cases', names='Fraud Pattern',
                     title='Fraud Pattern Distribution')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        st.markdown("##### Performance by Institution")
        bank_performance = filtered_df.groupby('Bank').agg({
            'Risk Score': 'mean',
            'Pattern': 'count'
        }).reset_index()
        bank_performance.columns = ['Institution', 'Avg Risk Score', 'Cases Detected']
        
        fig3 = px.bar(bank_performance, x='Institution', y=['Avg Risk Score', 'Cases Detected'],
                     title='Institution Performance Comparison',
                     barmode='group')
        st.plotly_chart(fig3, use_container_width=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; font-size: 0.9em;">
    <p><strong>🛡️ Seadria Antifraud Intelligence Platform</strong></p>
    <p>Federated Learning & Blockchain Consortium | Version 2.1.4</p>
    <p>© 2024 Seadria Technologies. For demonstration purposes only.</p>
</div>
""", unsafe_allow_html=True)

# AUTO-REFRESH OPTION
if st.sidebar.checkbox("🔄 Enable Live Updates"):
    st.rerun()

# ADDITIONAL SIDEBAR INFO
st.sidebar.markdown("---")
st.sidebar.info("""
**Demo Instructions:**
1. Try different transaction scenarios
2. Observe real-time risk assessment
3. Experience multi-layered protection
""")
