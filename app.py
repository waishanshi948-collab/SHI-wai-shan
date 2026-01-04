import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random
import time

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="S.A.F.E. WebGuard - 金融欺诈防御系统",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== 自定义CSS样式 ====================
st.markdown("""
<style>
    .main-header {
        color: #1E3A8A;
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    
    .risk-high {
        border-left: 5px solid #EF4444;
        background: linear-gradient(90deg, #FEE2E2, #FECACA);
    }
    
    .risk-medium {
        border-left: 5px solid #F59E0B;
        background: linear-gradient(90deg, #FEF3C7, #FDE68A);
    }
    
    .risk-low {
        border-left: 5px solid #10B981;
        background: linear-gradient(90deg, #D1FAE5, #A7F3D0);
    }
    
    .tech-highlight {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 5px solid #3B82F6;
    }
    
    .blockchain-node {
        display: inline-block;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        margin: 0 8px;
        text-align: center;
        line-height: 35px;
        font-weight: bold;
        color: white;
        font-size: 14px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# ==================== 数据生成函数 ====================
def generate_transaction_data():
    scenarios = [
        {"type": "正常转账", "risk": "low", "icon": "✅", "category": "转账"},
        {"type": "可疑模式", "risk": "medium", "icon": "⚠️", "category": "投资"},
        {"type": "投资骗局", "risk": "high", "icon": "🚨", "category": "投资"},
        {"type": "冒充诈骗", "risk": "high", "icon": "🎭", "category": "诈骗"}
    ]
    
    transactions = []
    for i in range(20):
        scenario = random.choice(scenarios)
        amount = random.randint(1000, 500000)
        risk_score = random.randint(10, 30) if scenario["risk"] == "low" else (
            random.randint(40, 70) if scenario["risk"] == "medium" else random.randint(75, 99)
        )
        
        transactions.append({
            "时间": f"{random.randint(9, 16)}:{random.randint(10, 59):02d}",
            "类型": f"{scenario['icon']} {scenario['type']}",
            "金额": f"HK${amount:,}",
            "风险评分": risk_score,
            "银行": random.choice(["汇丰银行", "中银香港", "恒生银行", "渣打银行"]),
            "状态": "已完成" if risk_score < 50 else ("已拦截" if risk_score > 75 else "待审核")
        })
    
    return pd.DataFrame(transactions)

def create_risk_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "实时风险评分", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(height=400, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def create_fraud_trend_chart():
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months,
        y=[45, 48, 52, 55, 58, 62, 60, 57, 53, 50, 48, 45],
        mode='lines+markers',
        name='投资诈骗',
        line=dict(color='#EF4444', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=months,
        y=[32, 35, 38, 40, 42, 45, 43, 41, 38, 36, 34, 32],
        mode='lines+markers',
        name='冒充诈骗',
        line=dict(color='#F59E0B', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=months,
        y=[28, 30, 32, 35, 38, 40, 39, 37, 34, 32, 30, 28],
        mode='lines+markers',
        name='电商诈骗',
        line=dict(color='#3B82F6', width=3)
    ))
    
    fig.update_layout(
        title={'text': "📈 香港2024年诈骗趋势分析", 'font': {'size': 20}},
        xaxis_title="月份",
        yaxis_title="报告案件数量",
        height=400,
        template="plotly_white"
    )
    
    return fig

def simulate_ai_analysis(transaction_type, amount):
    if "投资" in transaction_type or "虚拟" in transaction_type:
        risk_level = "high_risk"
        color = "#EF4444"
        icon = "🚨"
        score = 85
    elif "新收款方" in transaction_type or "紧急" in transaction_type:
        risk_level = "suspicious"
        color = "#F59E0B"
        icon = "⚠️"
        score = 65
    else:
        risk_level = "normal"
        color = "#10B981"
        icon = "✅"
        score = 15
    
    if amount > 100000:
        score = min(99, score + 20)
    elif amount > 50000:
        score = min(95, score + 10)
    
    return {
        "score": score,
        "level": risk_level,
        "color": color,
        "icon": icon
    }

# ==================== 侧边栏 ====================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center;">
        <h2 style="color: #1E3A8A;">🛡️ S.A.F.E. WebGuard</h2>
        <p style="color: #6B7280;">金融安全生态系统联盟</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 导航菜单
    page = st.radio(
        "导航菜单",
        ["🏠 首页", "💸 实时交易护航", "🧠 AI欺诈智能", "🏢 机构仪表板", "📚 解决方案", "⚙️ 创新技术"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # 创新技术亮点
    st.markdown("### 🚀 创新技术")
    st.markdown("""
    <div style="background: #F0F9FF; padding: 15px; border-radius: 10px;">
    <p><strong>🎯 核心技术：</strong></p>
    <ul style="margin-left: 20px;">
    <li>🔐 零知识证明</li>
    <li>🤖 联邦学习</li>
    <li>⛓️ 联盟区块链</li>
    <li>🧠 生成式AI</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 实时状态
    st.markdown("### 📊 系统状态")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("活跃银行", "8家", "+2")
    with col2:
        st.metric("今日防护", "1,428笔", "3.2%")
    
    st.progress(0.85, text="系统防护覆盖率 85%")

# ==================== 首页 ====================
if page == "🏠 首页":
    st.markdown("""
    <div class="main-header">
        <h1>🛡️ S.A.F.E. WebGuard</h1>
        <h3>金融欺诈防御系统 - 商赛演示版</h3>
        <p>连接用户、银行、执法机构的三方防护网络</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 创新亮点
    st.markdown("## 🎯 创新亮点")
    
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="metric-card">
            <h3>🔐 隐私保护协作</h3>
            <p>零知识证明技术让银行无需共享数据即可协同风控</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="metric-card">
            <h3>🤖 联邦学习AI</h3>
            <p>去中心化AI训练，保护数据隐私的同时提升检测能力</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="metric-card">
            <h3>⚡ 实时风险拦截</h3>
            <p>毫秒级风险识别，平均响应时间2.1秒</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 快速演示
    st.markdown("## 🚀 快速演示")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("### 💸 模拟交易风险检测")
        
        scenario = st.selectbox(
            "选择交易场景",
            ["向已知联系人转账", "支付给新供应商", "高回报投资存款", "紧急商务转账", "加密货币购买"]
        )
        
        amount = st.slider("金额 (HKD)", 1000, 1000000, 50000, 1000)
        
        if st.button("🚀 开始风险扫描", type="primary"):
            with st.spinner("正在分析交易风险..."):
                time.sleep(1.5)
                analysis = simulate_ai_analysis(scenario, amount)
                
                if analysis["level"] == "high_risk":
                    risk_class = "risk-high"
                elif analysis["level"] == "suspicious":
                    risk_class = "risk-medium"
                else:
                    risk_class = "risk-low"
                
                st.markdown(f"""
                <div class="{risk_class}">
                    <h3>{analysis['icon']} 风险评分: {analysis['score']}/100</h3>
                    <p><strong>分析结果：</strong>交易已通过S.A.F.E.系统验证</p>
                </div>
                """, unsafe_allow_html=True)
    
    with demo_col2:
        st.markdown("### 📈 欺诈趋势预览")
        fig = create_fraud_trend_chart()
        st.plotly_chart(fig, use_container_width=True)

# ==================== 实时交易护航页面 ====================
elif page == "💸 实时交易护航":
    st.markdown("# 💸 实时交易护航")
    st.markdown("### 基于零知识证明的隐私保护交易风控")
    
    # 交易输入区域
    col1, col2 = st.columns(2)
    
    with col1:
        transaction_type = st.selectbox(
            "交易类型",
            ["向已知联系人转账", "支付给新供应商", "高回报投资存款", "紧急商务转账", "加密货币购买"]
        )
        
        amount = st.number_input(
            "金额 (HKD)",
            min_value=1000,
            max_value=1000000,
            value=50000,
            step=1000
        )
        
        recipient_bank = st.selectbox(
            "收款银行",
            ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "虚拟银行", "海外银行"]
        )
    
    with col2:
        user_profile = st.selectbox(
            "用户画像",
            ["普通用户", "企业主", "老年用户", "新居民", "金融从业者"]
        )
        
        urgency = st.select_slider(
            "紧急程度",
            options=["低", "中", "高", "非常紧急"]
        )
    
    # 区块链验证可视化
    st.markdown("### 🔗 联盟区块链验证")
    
    # 创建区块链节点
    nodes = ["汇丰", "中银", "恒生", "渣打", "金管局", "警方"]
    nodes_html = ""
    for node in nodes:
        color = "#10B981" if random.random() > 0.3 else "#F59E0B"
        nodes_html += f'<div class="blockchain-node" style="background-color: {color};">{node}</div>'
    
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        {nodes_html}
    </div>
    """, unsafe_allow_html=True)
    
    # 开始分析按钮
    if st.button("🚀 启动S.A.F.E.护航扫描", type="primary", use_container_width=True):
        with st.spinner("正在调用零知识证明协议..."):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(100):
                progress_bar.progress(i + 1)
                if i < 25:
                    status_text.text("⚡ 生成零知识证明...")
                elif i < 50:
                    status_text.text("🔄 向联盟银行查询...")
                elif i < 75:
                    status_text.text("🔐 验证隐私数据...")
                else:
                    status_text.text("✅ 完成风险评估...")
                time.sleep(0.02)
            
            progress_bar.empty()
            status_text.empty()
            
            # 显示分析结果
            analysis = simulate_ai_analysis(transaction_type, amount)
            fig = create_risk_gauge(analysis["score"])
            st.plotly_chart(fig, use_container_width=True)
            
            # 详细分析
            if analysis["level"] == "high_risk":
                risk_class = "risk-high"
                message = "🚨 高风险警报：交易特征与已知诈骗模式匹配"
            elif analysis["level"] == "suspicious":
                risk_class = "risk-medium"
                message = "⚠️ 检测到可疑模式：金额超出用户常规范围"
            else:
                risk_class = "risk-low"
                message = "✅ 交易模式正常，风险评估通过"
            
            st.markdown(f"""
            <div class="{risk_class}">
                <h3>{analysis['icon']} {message}</h3>
                <p><strong>⚡ 响应时间:</strong> 2.3秒</p>
                <p><strong>🏦 咨询银行:</strong> 4家联盟银行</p>
                <p><strong>🔗 区块链确认:</strong> 6个节点</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 显示交易数据
            st.markdown("### 📋 实时交易监控")
            transactions = generate_transaction_data()
            st.dataframe(transactions, use_container_width=True)

# ==================== AI欺诈智能页面 ====================
elif page == "🧠 AI欺诈智能":
    st.markdown("# 🧠 AI欺诈智能")
    st.markdown("### 基于生成式AI的欺诈预测与防御")
    
    # AI预测展示
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🔮 AI欺诈预测")
        
        predictions = pd.DataFrame({
            "预测类型": [
                "AI合成投资讲座骗局",
                "跨境虚拟资产套利诈骗",
                "政府电子支付冒充",
                "供应链发票欺诈"
            ],
            "概率": ["87%", "74%", "69%", "63%"],
            "目标群体": ["中年投资者", "年轻科技投资者", "新移民/学生", "中小企业财务"],
            "应对措施": ["验证API + 实时交互检查", "教育计划 + 平台白名单", "官方渠道验证", "区块链发票验证"]
        })
        
        st.dataframe(predictions, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 实时风险热点")
        
        risk_data = [
            {"地区": "九龙东", "风险": 85, "趋势": "📈"},
            {"地区": "港岛", "风险": 72, "趋势": "📉"},
            {"地区": "新界西", "风险": 65, "趋势": "➡️"},
            {"地区": "九龙西", "风险": 78, "趋势": "📈"},
            {"地区": "新界东", "风险": 70, "趋势": "➡️"}
        ]
        
        for data in risk_data:
            bg_color = "#FEE2E2" if data["风险"] > 75 else "#FEF3C7" if data["风险"] > 60 else "#D1FAE5"
            st.markdown(f"""
            <div style="padding: 10px; border-radius: 8px; background: {bg_color}; margin: 5px 0;">
                <strong>{data['地区']}</strong><br>
                风险指数: {data['风险']} {data['趋势']}
            </div>
            """, unsafe_allow_html=True)
    
    # 欺诈趋势分析
    st.markdown("### 📈 欺诈趋势分析")
    trend_fig = create_fraud_trend_chart()
    st.plotly_chart(trend_fig, use_container_width=True)

# ==================== 机构仪表板页面 ====================
elif page == "🏢 机构仪表板":
    st.markdown("# 🏢 机构仪表板")
    st.markdown("### 银行联盟与执法机构协作平台")
    
    # 银行联盟部分
    st.markdown("## 🏦 银行联盟控制台")
    
    bank_cols = st.columns(4)
    
    with bank_cols[0]:
        st.metric("今日查询", "1,428", "+3.2%")
    
    with bank_cols[1]:
        st.metric("证明生成时间", "0.8秒", "-12%")
    
    with bank_cols[2]:
        st.metric("隐私保护率", "100%", "0%")
    
    with bank_cols[3]:
        st.metric("误报率", "2.3%", "-15%")
    
    # 银行排名
    st.markdown("#### 🏆 银行安全排名")
    
    bank_ranking = pd.DataFrame({
        "银行": ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "众安银行"],
        "安全评分": [925, 872, 821, 785, 642],
        "生成警报": [142, 128, 98, 87, 45],
        "联盟等级": ["金牌", "金牌", "银牌", "银牌", "铜牌"],
        "贡献度": ["35%", "28%", "18%", "12%", "7%"]
    })
    
    st.dataframe(bank_ranking, use_container_width=True)
    
    # 执法机构部分
    st.markdown("## 👮 警务处协作中心")
    
    police_cols = st.columns(4)
    
    with police_cols[0]:
        st.metric("本月预防案件", "84", "+18%")
    
    with police_cols[1]:
        st.metric("保护资金", "3.12亿", "+22%")
    
    with police_cols[2]:
        st.metric("平均响应时间", "42分钟", "-28%")
    
    with police_cols[3]:
        st.metric("公众满意度", "94.2%", "+3.5%")
    
    # 案件洞察
    st.markdown("#### 🔍 案件洞察")
    
    case_data = pd.DataFrame({
        "洞察": ["新AI语音诈骗激增", "虚拟资产诈骗集群", "跨境洗钱网络", "中小企业发票诈骗趋势"],
        "严重程度": ["高", "高", "中", "中"],
        "受影响群体": ["老年用户", "年轻投资者", "学生", "企业"],
        "应对行动": ["公众警报", "平台封锁", "调查中", "教育计划"],
        "状态": ["进行中", "已解决", "调查中", "监控中"]
    })
    
    st.dataframe(case_data, use_container_width=True)
    
    # 创新技术展示
    st.markdown("---")
    st.markdown("## 🚀 创新技术应用展示")
    
    tech_cols = st.columns(3)
    
    with tech_cols[0]:
        st.markdown("""
        <div class="tech-highlight">
        <h4>🔐 零知识证明技术</h4>
        <p><strong>商赛创新点：</strong></p>
        <ul>
        <li>银行间无需共享敏感数据</li>
        <li>仅验证风险证明的真实性</li>
        <li>完全保护用户隐私</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_cols[1]:
        st.markdown("""
        <div class="tech-highlight">
        <h4>🤖 联邦学习AI</h4>
        <p><strong>商赛创新点：</strong></p>
        <ul>
        <li>去中心化AI训练</li>
        <li>各银行本地训练模型</li>
        <li>全局模型聚合更新</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_cols[2]:
        st.markdown("""
        <div class="tech-highlight">
        <h4>⛓️ 联盟区块链</h4>
        <p><strong>商赛创新点：</strong></p>
        <ul>
        <li>多方参与共识机制</li>
        <li>不可篡改审计追踪</li>
        <li>透明化协作平台</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== 解决方案页面 ====================
elif page == "📚 解决方案":
    st.markdown("# 📚 S.A.F.E. WebGuard 解决方案")
    st.markdown("### 完整的技术架构与商业模型")
    
    # 创建选项卡
    tab1, tab2, tab3 = st.tabs(["技术架构", "商业模型", "竞争优势"])
    
    with tab1:
        st.markdown("## 🏗️ 技术架构体系")
        
        st.markdown("""
        ### 🎯 三层防御框架
        
        | 角色 | 传统挑战 | S.A.F.E.创新方案 |
        |------|---------|-----------------|
        | **用户端** | 通用警告，保护有限 | 情境感知警报 + 紧急援助 |
        | **银行端** | 数据孤岛，责任担忧 | 零知识证明 + 声誉激励 |
        | **执法端** | 被动调查，响应缓慢 | 主动情报 + 实时区块链取证 |
        
        ### 🔐 核心技术栈
        
        **1. 联邦学习人工智能**
        - 银行本地训练模型 → 无需共享数据
        - 全局智能无需隐私妥协
        - 自改进检测算法
        
        **2. 零知识证明协议**
        - 银行A证明："账户X为高风险"
        - 银行B验证证明 → 不泄露敏感数据
        - 密码学真实性保证
        
        **3. 联盟区块链**
        - 所有风险评估的不可变审计追踪
        - 透明贡献度跟踪
        - 防篡改调查证据
        """)
    
    with tab2:
        st.markdown("## 💰 商业模型")
        
        st.markdown("### 📊 关键绩效指标")
        
        kpi_data = pd.DataFrame({
            "指标": ["欺诈检测率", "误报率", "响应时间", "跨行协作", "公众意识"],
            "实施前": ["68%", "18%", "3-7天", "有限", "45%"],
            "实施后": ["96%", "3%", "3-5分钟", "完整生态", "92%"],
            "改善幅度": ["+41%", "-83%", "快99%", "100%覆盖", "+104%"]
        })
        
        st.dataframe(kpi_data, use_container_width=True)
        
        st.markdown("### 💸 收入来源")
        
        revenue_cols = st.columns(4)
        
        with revenue_cols[0]:
            st.metric("SaaS授权费", "200-500万/年", "主要收入")
        
        with revenue_cols[1]:
            st.metric("政府资助", "150-300万/年", "犯罪预防")
        
        with revenue_cols[2]:
            st.metric("保险合作", "100
