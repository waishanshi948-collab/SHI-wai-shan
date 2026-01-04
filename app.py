import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import random
import time
from streamlit_option_menu import option_menu
import json

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="S.A.F.E. WebGuard - 金融欺诈防御系统",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/your-repo',
        'Report a bug': None,
        'About': "S.A.F.E. WebGuard - 商赛演示应用"
    }
)

# ==================== 自定义CSS样式 ====================
st.markdown("""
<style>
    /* 主标题样式 */
    .main-header {
        color: #1E3A8A;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    /* 指标卡片样式 */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    
    .metric-card.high-risk {
        border-left: 5px solid #EF4444;
        background: linear-gradient(90deg, #FEE2E2, #FECACA);
    }
    
    .metric-card.medium-risk {
        border-left: 5px solid #F59E0B;
        background: linear-gradient(90deg, #FEF3C7, #FDE68A);
    }
    
    .metric-card.low-risk {
        border-left: 5px solid #10B981;
        background: linear-gradient(90deg, #D1FAE5, #A7F3D0);
    }
    
    /* 动画效果 */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    /* 区块链节点样式 */
    .blockchain-node {
        display: inline-block;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        margin: 0 5px;
        text-align: center;
        line-height: 30px;
        font-weight: bold;
        color: white;
        font-size: 12px;
    }
    
    /* 创新技术高亮 */
    .tech-highlight {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 5px solid #3B82F6;
    }
    
    /* 时间线样式 */
    .timeline-container {
        position: relative;
        padding-left: 2rem;
    }
    
    .timeline-item {
        position: relative;
        margin-bottom: 1.5rem;
        padding-left: 1.5rem;
    }
    
    .timeline-item:before {
        content: '';
        position: absolute;
        left: 0;
        top: 0.5rem;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #3B82F6;
    }
</style>
""", unsafe_allow_html=True)

# ==================== 数据生成函数 ====================
def generate_transaction_data():
    """生成模拟交易数据"""
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
            "状态": "已完成" if risk_score < 50 else ("已拦截" if risk_score > 75 else "待审核"),
            "类别": scenario["category"]
        })
    
    return pd.DataFrame(transactions)

def create_risk_gauge(score):
    """创建风险评分仪表盘"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "实时风险评分", 'font': {'size': 24, 'color': '#1E3A8A'}},
        delta={'reference': 50, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
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
    
    fig.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def create_fraud_trend_chart():
    """创建欺诈趋势图表"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    
    fig = go.Figure()
    
    # 投资诈骗趋势
    fig.add_trace(go.Scatter(
        x=months,
        y=[45, 48, 52, 55, 58, 62, 60, 57, 53, 50, 48, 45],
        mode='lines+markers',
        name='投资诈骗',
        line=dict(color='#EF4444', width=3, dash='solid'),
        marker=dict(size=8)
    ))
    
    # 冒充诈骗趋势
    fig.add_trace(go.Scatter(
        x=months,
        y=[32, 35, 38, 40, 42, 45, 43, 41, 38, 36, 34, 32],
        mode='lines+markers',
        name='冒充诈骗',
        line=dict(color='#F59E0B', width=3, dash='dash'),
        marker=dict(size=8)
    ))
    
    # 电商诈骗趋势
    fig.add_trace(go.Scatter(
        x=months,
        y=[28, 30, 32, 35, 38, 40, 39, 37, 34, 32, 30, 28],
        mode='lines+markers',
        name='电商诈骗',
        line=dict(color='#3B82F6', width=3, dash='dot'),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title={
            'text': "📈 香港2024年诈骗趋势分析",
            'font': {'size': 24, 'color': '#1E3A8A'}
        },
        xaxis_title="月份",
        yaxis_title="报告案件数量",
        height=500,
        template="plotly_white",
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def generate_blockchain_log():
    """生成区块链验证日志"""
    current_time = datetime.now()
    logs = []
    
    nodes = [
        {"name": "汇丰银行", "status": "✅ 已验证", "time": 0.8},
        {"name": "中银香港", "status": "⏳ 处理中", "time": 1.2},
        {"name": "恒生银行", "status": "✅ 已验证", "time": 0.9},
        {"name": "金管局", "status": "✅ 已验证", "time": 1.5},
        {"name": "警务处", "status": "⏳ 同步中", "time": 2.1}
    ]
    
    for i, node in enumerate(nodes):
        log_time = current_time - timedelta(seconds=random.randint(1, 5))
        logs.append({
            "时间戳": log_time.strftime("%H:%M:%S.%f")[:-3],
            "节点": node["name"],
            "操作": "零知识证明验证",
            "状态": node["status"],
            "响应时间": f"{node['time']}秒",
            "区块高度": f"#{random.randint(1000, 9999)}"
        })
    
    return pd.DataFrame(logs)

def simulate_ai_analysis(transaction_type, amount):
    """模拟AI风险分析"""
    base_scores = {
        "normal": 15,
        "suspicious": 65,
        "high_risk": 85
    }
    
    if "投资" in transaction_type or "虚拟" in transaction_type:
        risk_level = "high_risk"
        color = "#EF4444"
        icon = "🚨"
    elif "新收款方" in transaction_type or "紧急" in transaction_type:
        risk_level = "suspicious"
        color = "#F59E0B"
        icon = "⚠️"
    else:
        risk_level = "normal"
        color = "#10B981"
        icon = "✅"
    
    # 根据金额调整
    if amount > 100000:
        score = min(99, base_scores[risk_level] + 20)
    elif amount > 50000:
        score = min(95, base_scores[risk_level] + 10)
    else:
        score = base_scores[risk_level]
    
    return {
        "score": score,
        "level": risk_level,
        "color": color,
        "icon": icon,
        "message": get_risk_message(risk_level, amount),
        "recommendations": get_recommendations(risk_level)
    }

def get_risk_message(level, amount):
    messages = {
        "normal": f"✅ 交易模式正常，金额 HK${amount:,} 在合理范围内",
        "suspicious": f"⚠️ 检测到可疑模式：金额 HK${amount:,} 超出用户常规范围",
        "high_risk": f"🚨 高风险警报：交易特征与已知诈骗模式匹配度达87%"
    }
    return messages.get(level, "")

def get_recommendations(level):
    recommendations = {
        "normal": [
            "✅ 验证收款方信息后继续",
            "📱 通过双重认证确认",
            "💾 保存交易记录"
        ],
        "suspicious": [
            "📞 联系收款方确认身份",
            "⏸️ 延迟24小时处理",
            "🏦 咨询银行客服"
        ],
        "high_risk": [
            "🚨 立即暂停交易",
            "📱 联系反诈骗协调中心 (ADCC: 18222)",
            "🏦 前往银行分行核实",
            "🔒 冻结相关账户"
        ]
    }
    return recommendations.get(level, [])

# ==================== 侧边栏导航 ====================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/shield--v1.png", width=80)
    
    st.markdown("""
    <div style="text-align: center;">
        <h2 style="color: #1E3A8A;">🛡️ S.A.F.E. WebGuard</h2>
        <p style="color: #6B7280;">金融安全生态系统联盟</p>
    </div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title=None,
        options=["🏠 首页", "💸 实时交易护航", "🧠 AI欺诈智能", "🏢 机构仪表板", "📚 解决方案", "⚙️ 创新技术"],
        icons=["house", "currency-exchange", "cpu", "building", "book", "gear"],
        default_index=0,
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "#3B82F6", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px"},
            "nav-link-selected": {"background-color": "#3B82F6"},
        }
    )
    
    st.markdown("---")
    
    # 创新技术亮点
    st.markdown("### 🚀 创新技术应用")
    st.markdown("""
    <div class="tech-highlight">
    <p><strong>🎯 核心技术：</strong></p>
    <ul>
    <li>🔐 零知识证明 (Zero-Knowledge Proof)</li>
    <li>🤖 联邦学习 (Federated Learning)</li>
    <li>⛓️ 联盟区块链 (Consortium Blockchain)</li>
    <li>🧠 生成式AI预测</li>
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

# ==================== 主页内容 ====================
if selected == "🏠 首页":
    # 英雄区域
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
    innovations = [
        {
            "title": "🔐 隐私保护协作",
            "desc": "零知识证明技术让银行无需共享数据即可协同风控",
            "icon": "🔐"
        },
        {
            "title": "🤖 联邦学习AI",
            "desc": "去中心化AI训练，保护数据隐私的同时提升检测能力",
            "icon": "🤖"
        },
        {
            "title": "⚡ 实时风险拦截",
            "desc": "毫秒级风险识别，平均响应时间2.1秒",
            "icon": "⚡"
        }
    ]
    
    for idx, innov in enumerate(innovations):
        with cols[idx]:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{innov['icon']} {innov['title']}</h3>
                <p>{innov['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # 快速演示
    st.markdown("## 🚀 快速演示")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("### 💸 模拟高风险交易")
        
        with st.form("quick_demo_form"):
            scenario = st.selectbox(
                "选择交易场景",
                ["向已知联系人转账", "支付给新供应商", "高回报投资存款", "紧急商务转账", "加密货币购买"]
            )
            
            amount = st.slider("金额 (HKD)", 1000, 1000000, 50000, 1000)
            
            submitted = st.form_submit_button("🚀 开始风险扫描", type="primary")
            
            if submitted:
                with st.spinner("正在分析交易风险..."):
                    time.sleep(1.5)
                    analysis = simulate_ai_analysis(scenario, amount)
                    
                    risk_class = f"metric-card {analysis['level']}-risk"
                    st.markdown(f"""
                    <div class="{risk_class}">
                        <h3>{analysis['icon']} 风险评分: {analysis['score']}/100</h3>
                        <p>{analysis['message']}</p>
                        <p><strong>建议操作:</strong></p>
                        <ul>
                        {''.join([f'<li>{rec}</li>' for rec in analysis['recommendations'][:2]])}
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
    
    with demo_col2:
        st.markdown("### 📈 欺诈趋势预览")
        fig = create_fraud_trend_chart()
        st.plotly_chart(fig, use_container_width=True)
    
    # 技术架构图
    st.markdown("## 🏗️ 技术架构")
    
    st.image("https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1VzZXJdIC0tPiBCW01vYmlsZSBCYW5raW5nIEFwcF1cbiAgICBCIC0tPiBDW1MuQS5GLkUuIFdlYkd1YXJkXVxuICAgIEMgLS0-IEVbWmVyby1Lbm93bGVkZ2UgUHJvb2ZdXG4gICAgRSAtLT4gRltGZWRlcmF0ZWQgTGVhcm5pbmcgQUldXG4gICAgRiAtLT4gR1tDb25zb3J0aXVtIEJsb2NrY2hhaW5dXG4gICAgRyAtLT4gSFtCYW5rIEFdXG4gICAgRyAtLT4gSVtCYW5rIEJdXG4gICAgRyAtLT4gSltCYW5rIENdXG4gICAgRyAtLT4gS1tBRENDXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9", 
             caption="S.A.F.E. WebGuard 技术架构图 - 基于零知识证明的隐私保护协作网络")

# ==================== 实时交易护航页面 ====================
elif selected == "💸 实时交易护航":
    st.markdown("# 💸 实时交易护航")
    st.markdown("### 基于零知识证明的隐私保护交易风控")
    
    # 交易输入区域
    with st.container():
        st.markdown("### 📝 交易详情")
        
        col1, col2 = st.columns(2)
        
        with col1:
            transaction_type = st.selectbox(
                "交易类型",
                ["向已知联系人转账", "支付给新供应商", "高回报投资存款", 
                 "紧急商务转账", "加密货币购买", "虚拟资产交易"]
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
            
            recipient_type = st.selectbox(
                "收款方类型",
                ["个人账户", "企业账户", "投资平台", "电商平台", "政府机构"]
            )
            
            urgency = st.select_slider(
                "紧急程度",
                options=["低", "中", "高", "非常紧急"]
            )
    
    # 区块链验证可视化
    st.markdown("### 🔗 联盟区块链验证")
    
    blockchain_log = generate_blockchain_log()
    
    # 创建区块链节点可视化
    st.markdown("#### 🌐 实时节点验证状态")
    
    nodes_html = ""
    for _, row in blockchain_log.iterrows():
        status_color = "#10B981" if "✅" in row["状态"] else "#F59E0B"
        nodes_html += f"""
        <div class="blockchain-node" style="background-color: {status_color};" 
             title="{row['节点']}: {row['状态']}">
            {row['节点'][:1]}
        </div>
        """
    
    st.markdown(f"""
    <div style="text-align: center; margin: 20px 0;">
        {nodes_html}
    </div>
    """, unsafe_allow_html=True)
    
    # 开始分析按钮
    if st.button("🚀 启动S.A.F.E.护航扫描", type="primary", use_container_width=True):
        with st.spinner("正在调用零知识证明协议..."):
            # 模拟处理过程
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
            st.markdown("### 📊 风险评估结果")
            
            # 风险评分仪表盘
            analysis = simulate_ai_analysis(transaction_type, amount)
            fig = create_risk_gauge(analysis["score"])
            st.plotly_chart(fig, use_container_width=True)
            
            # 详细分析
            risk_class = f"metric-card {analysis['level']}-risk"
            st.markdown(f"""
            <div class="{risk_class}">
                <h3>{analysis['icon']} {analysis['message']}</h3>
                <p><strong>⚡ 响应时间:</strong> 2.3秒</p>
                <p><strong>🏦 咨询银行:</strong> 4家联盟银行</p>
                <p><strong>🔗 区块链确认:</strong> 7个节点</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 建议操作
            st.markdown("### 🎯 建议操作")
            
            cols = st.columns(len(analysis["recommendations"]))
            for idx, rec in enumerate(analysis["recommendations"]):
                with cols[idx]:
                    if "暂停" in rec or "冻结" in rec:
                        st.button(rec, type="secondary", use_container_width=True)
                    elif "确认" in rec:
                        st.button(rec, type="primary", use_container_width=True)
                    else:
                        st.button(rec, use_container_width=True)
            
            # 显示详细的区块链日志
            with st.expander("📋 查看详细区块链日志"):
                st.dataframe(
                    blockchain_log,
                    column_config={
                        "时间戳": "时间戳",
                        "节点": "验证节点",
                        "操作": "操作类型",
                        "状态": "状态",
                        "响应时间": "响应时间",
                        "区块高度": "区块高度"
                    },
                    use_container_width=True
                )

# ==================== AI欺诈智能页面 ====================
elif selected == "🧠 AI欺诈智能":
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
        
        st.dataframe(
            predictions,
            column_config={
                "预测类型": st.column_config.TextColumn("预测欺诈类型", width="medium"),
                "概率": st.column_config.ProgressColumn(
                    "发生概率",
                    help="AI预测的发生概率",
                    format="%f",
                    min_value=0,
                    max_value=100,
                ),
                "目标群体": st.column_config.TextColumn("主要目标群体"),
                "应对措施": st.column_config.TextColumn("推荐应对措施")
            },
            use_container_width=True
        )
    
    with col2:
        st.markdown("### 🎯 实时风险热点")
        
        # 风险地图数据
        risk_data = pd.DataFrame({
            "地区": ["九龙东", "港岛", "新界西", "九龙西", "新界东"],
            "风险指数": [85, 72, 65, 78, 70],
            "趋势": ["上升", "下降", "稳定", "上升", "稳定"]
        })
        
        for _, row in risk_data.iterrows():
            with st.container():
                st.markdown(f"""
                <div style="padding: 10px; border-radius: 8px; background: {'#FEE2E2' if row['风险指数'] > 75 else '#FEF3C7' if row['风险指数'] > 60 else '#D1FAE5'}; margin: 5px 0;">
                    <strong>{row['地区']}</strong><br>
                    风险指数: {row['风险指数']} {'📈' if row['趋势'] == '上升' else '📉' if row['趋势'] == '下降' else '➡️'}
                </div>
                """, unsafe_allow_html=True)
    
    # 欺诈趋势分析
    st.markdown("### 📈 欺诈趋势分析")
    trend_fig = create_fraud_trend_chart()
    st.plotly_chart(trend_fig, use_container_width=True)
    
    # AI训练模拟
    st.markdown("### 🎮 AI防御训练")
    
    with st.expander("🤖 开始AI欺诈识别训练", expanded=True):
        training_scenario = st.selectbox(
            "选择训练场景",
            ["AI语音诈骗识别", "虚假投资平台检测", "冒充诈骗应对", "虚拟货币诈骗预防"]
        )
        
        if training_scenario == "AI语音诈骗识别":
            st.markdown("""
            #### 🎭 训练场景：AI语音诈骗识别
            
            **情境模拟：**
            你收到"儿子"的紧急语音信息："爸爸，我手机丢了，急需8000港币交房租..."
            
            **❓ 决策点：你会如何应对？**
            
            1. 💸 立即转账（高风险）
            2. 🎥 要求视频通话验证（推荐）
            3. 📞 拨打他常用号码（推荐）
            4. 🤔 提问个人验证问题（推荐）
            
            **✅ S.A.F.E.指导：** AI可以模仿声音，但难以处理实时视频交互和个人知识验证。
            """)
            
            user_choice = st.radio("你的选择：", 
                ["立即转账", "要求视频通话", "拨打常用号码", "提问验证问题"], 
                index=None)
            
            if user_choice:
                if user_choice == "立即转账":
                    st.error("❌ 高风险选择！AI语音诈骗的典型手法。得分：0/100")
                else:
                    st.success("✅ 优秀选择！有效防范AI语音诈骗。得分：100/100")
        
        elif training_scenario == "虚假投资平台检测":
            st.markdown("""
            #### 💰 训练场景：虚假投资平台识别
            
            **平台特征检查清单：**
            - ✅ 是否有金融牌照号码？
            - ✅ 是否在证监会注册？
            - ✅ 回报率是否异常高（>30%）？
            - ✅ 是否要求加密货币支付？
            - ✅ 是否有实体办公地址？
            
            **检测结果：** 平台未在证监会注册 + 承诺50%回报率 = 高风险平台
            """)

# ==================== 机构仪表板页面 ====================
elif selected == "🏢 机构仪表板":
    st.markdown("# 🏢 机构仪表板")
    st.markdown("### 银行联盟与执法机构协作平台")
    
    # 银行联盟部分
    st.markdown("## 🏦 银行联盟控制台")
    
    bank_cols = st.columns(4)
    bank_metrics = [
        {"label": "今日查询", "value": "1,428", "change": "+3.2%", "icon": "📊"},
        {"label": "证明生成时间", "value": "0.8秒", "change": "-12%", "icon": "⚡"},
        {"label": "隐私保护率", "value": "100%", "change": "0%", "icon": "🔐"},
        {"label": "误报率", "value": "2.3%", "change": "-15%", "icon": "📉"}
    ]
    
    for idx, metric in enumerate(bank_metrics):
        with bank_cols[idx]:
            st.metric(
                label=f"{metric['icon']} {metric['label']}",
                value=metric['value'],
                delta=metric['change']
            )
    
    # 银行排名
    st.markdown("#### 🏆 银行安全排名")
    
    bank_ranking = pd.DataFrame({
        "银行": ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "众安银行"],
        "安全评分": [925, 872, 821, 785, 642],
        "生成警报": [142, 128, 98, 87, 45],
        "联盟等级": ["金牌", "金牌", "银牌", "银牌", "铜牌"],
        "贡献度": ["35%", "28%", "18%", "12%", "7%"]
    })
    
    st.dataframe(
        bank_ranking,
        column_config={
            "银行": "银行名称",
            "安全评分": st.column_config.ProgressColumn(
                "安全评分",
                min_value=0,
                max_value=1000,
                format="%d"
            ),
            "生成警报": "生成警报数",
            "联盟等级": st.column_config.SelectboxColumn(
                "联盟等级",
                options=["铜牌", "银牌", "金牌", "白金"]
            ),
            "贡献度": "数据贡献度"
        },
        use_container_width=True,
        hide_index=True
    )
    
    # 执法机构部分
    st.markdown("## 👮 警务处协作中心")
    
    police_cols = st.columns(4)
    police_metrics = [
        {"label": "本月预防案件", "value": "84", "change": "+18%", "icon": "🛡️"},
        {"label": "保护资金", "value": "3.12亿", "change": "+22%", "icon": "💰"},
        {"label": "平均响应时间", "value": "42分钟", "change": "-28%", "icon": "⚡"},
        {"label": "公众满意度", "value": "94.2%", "change": "+3.5%", "icon": "😊"}
    ]
    
    for idx, metric in enumerate(police_metrics):
        with police_cols[idx]:
            st.metric(
                label=f"{metric['icon']} {metric['label']}",
                value=metric['value'],
                delta=metric['change']
            )
    
    # 案件洞察
    st.markdown("#### 🔍 案件洞察")
    
    case_data = pd.DataFrame({
        "洞察": ["新AI语音诈骗激增", "虚拟资产诈骗集群", "跨境洗钱网络", "中小企业发票诈骗趋势"],
        "严重程度": ["高", "高", "中", "中"],
        "受影响群体": ["老年用户", "年轻投资者", "学生", "企业"],
        "应对行动": ["公众警报", "平台封锁", "调查中", "教育计划"],
        "状态": ["进行中", "已解决", "调查中", "监控中"]
    })
    
    st.dataframe(
        case_data,
        column_config={
            "洞察": st.column_config.TextColumn("关键洞察", width="large"),
            "严重程度": st.column_config.SelectboxColumn(
                "严重程度",
                options=["低", "中", "高", "严重"]
            ),
            "受影响群体": "主要受影响群体",
            "应对行动": "推荐应对行动",
            "状态": st.column_config.SelectboxColumn(
                "处理状态",
                options=["待处理", "进行中", "已解决", "监控中"]
           
