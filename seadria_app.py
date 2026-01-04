import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ========== 页面配置 ==========
st.set_page_config(
    page_title="金融反诈演示系统",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== 自定义CSS样式 ==========
st.markdown("""
<style>
    /* 主标题样式 */
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    /* 风险等级卡片 */
    .risk-high {
        background: linear-gradient(90deg, #FEE2E2, #FECACA);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #DC2626;
        margin: 10px 0;
    }
    
    .risk-medium {
        background: linear-gradient(90deg, #FEF3C7, #FDE68A);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D97706;
        margin: 10px 0;
    }
    
    .risk-low {
        background: linear-gradient(90deg, #D1FAE5, #A7F3D0);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #059669;
        margin: 10px 0;
    }
    
    /* 指标卡片 */
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* 按钮样式 */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# ========== 侧边栏导航 ==========
st.sidebar.title("🛡️ 导航菜单")
page = st.sidebar.radio(
    "选择页面",
    ["🏠 首页仪表板", "💸 交易风险模拟", "📊 数据分析", "🛠️ 系统说明"]
)

# ========== 数据生成函数 ==========
def generate_transaction_data():
    """生成模拟交易数据"""
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    
    data = []
    for i in range(100):
        amount = np.random.randint(1000, 500000)
        risk_score = np.random.randint(1, 100)
        
        # 根据金额调整风险
        if amount > 200000:
            risk_score = min(100, risk_score + 30)
        elif amount > 50000:
            risk_score = min(100, risk_score + 15)
            
        # 确定状态
        if risk_score > 80:
            status = "已拦截"
        elif risk_score > 50:
            status = "人工审核"
        else:
            status = "已完成"
            
        data.append({
            "日期": dates[i].strftime("%Y-%m-%d"),
            "交易类型": np.random.choice(["转账", "投资", "充值", "提现", "支付"]),
            "金额": f"¥{amount:,}",
            "风险评分": risk_score,
            "状态": status,
            "银行": np.random.choice(["银行A", "银行B", "银行C", "银行D"])
        })
    
    return pd.DataFrame(data)

# ========== 页面内容 ==========
if page == "🏠 首页仪表板":
    # 标题
    st.markdown('<h1 class="main-title">🛡️ 金融反诈智能系统</h1>', unsafe_allow_html=True)
    st.markdown("### 基于联邦学习与区块链的协同防御网络")
    
    # 关键指标
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("系统准确率", "96.3%", "+2.1%")
    with col2:
        st.metric("预警交易数", "1,428", "+15%")
    with col3:
        st.metric("挽回损失", "¥4.2亿", "+¥0.8亿")
    with col4:
        st.metric("合作机构", "12家", "+3")
    
    st.markdown("---")
    
    # 图表展示
    st.subheader("📈 风险趋势分析")
    
    # 生成图表数据
    dates = pd.date_range('2024-01-01', periods=30, freq='D')
    chart_data = pd.DataFrame({
        "日期": dates,
        "高风险": np.random.randint(20, 50, 30),
        "中风险": np.random.randint(30, 70, 30),
        "低风险": np.random.randint(100, 200, 30)
    })
    
    # 使用Plotly创建交互式图表
    fig = px.line(chart_data, x="日期", y=["高风险", "中风险", "低风险"],
                  title="每日风险交易分布", markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # 系统状态
    st.subheader("🔄 系统运行状态")
    col1, col2 = st.columns(2)
    with col1:
        st.progress(0.85, text="模型训练进度")
        st.progress(0.95, text="数据同步进度")
    with col2:
        st.progress(1.0, text="节点连接状态")
        st.progress(0.78, text="风险库更新")

elif page == "💸 交易风险模拟":
    st.title("💸 交易风险实时模拟")
    
    with st.container():
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("1. 交易信息填写")
            
            # 交易场景选择
            scenario = st.selectbox(
                "选择交易场景",
                ["普通转账", "投资理财", "刷单返利", "虚拟货币交易", "跨境汇款"]
            )
            
            # 金额输入
            amount = st.number_input(
                "转账金额 (¥)",
                min_value=100,
                max_value=1000000,
                value=50000,
                step=1000
            )
            
            # 收款账户
            recipient = st.text_input("收款账户", placeholder="输入账户号码")
            
            # 风险评估按钮
            if st.button("🚀 开始风险评估", type="primary"):
                with st.spinner("正在连接联盟网络进行风险评估..."):
                    # 模拟处理时间
                    import time
                    time.sleep(1.5)
                    
                    # 根据场景确定风险
                    if scenario in ["刷单返利", "虚拟货币交易"]:
                        risk_score = min(95, 70 + amount // 10000)
                        risk_level = "high"
                        risk_color = "#DC2626"
                        risk_message = "🚨 高风险！检测到可疑交易模式"
                    elif scenario == "投资理财" and amount > 100000:
                        risk_score = min(85, 60 + amount // 20000)
                        risk_level = "medium"
                        risk_color = "#D97706"
                        risk_message = "⚠️ 中风险！大额投资需谨慎"
                    else:
                        risk_score = max(5, 20 - amount // 50000)
                        risk_level = "low"
                        risk_color = "#059669"
                        risk_message = "✅ 低风险！交易环境安全"
                    
                    # 显示结果
                    st.markdown("---")
                    st.subheader("2. 风险评估结果")
                    
                    # 风险仪表盘
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=risk_score,
                        title={'text': "风险评分"},
                        gauge={
                            'axis': {'range': [None, 100]},
                            'bar': {'color': risk_color},
                            'steps': [
                                {'range': [0, 30], 'color': "green"},
                                {'range': [30, 70], 'color': "yellow"},
                                {'range': [70, 100], 'color': "red"}
                            ],
                            'threshold': {
                                'line': {'color': "black", 'width': 4},
                                'thickness': 0.75,
                                'value': risk_score
                            }
                        }
                    ))
                    fig.update_layout(height=300)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # 详细分析
                    if risk_level == "high":
                        st.markdown(f'<div class="risk-high"><h3>{risk_message}</h3>'
                                   f'<p>评分：{risk_score}/100</p>'
                                   f'<p>建议：立即暂停交易，拨打反诈热线 96110 咨询</p></div>', 
                                   unsafe_allow_html=True)
                    elif risk_level == "medium":
                        st.markdown(f'<div class="risk-medium"><h3>{risk_message}</h3>'
                                   f'<p>评分：{risk_score}/100</p>'
                                   f'<p>建议：通过官方渠道核实对方身份</p></div>', 
                                   unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="risk-low"><h3>{risk_message}</h3>'
                                   f'<p>评分：{risk_score}/100</p>'
                                   f'<p>建议：确认信息无误后可继续操作</p></div>', 
                                   unsafe_allow_html=True)
        
        with col2:
            st.subheader("📱 手机界面预览")
            
            # 模拟手机界面
            st.markdown(f"""
            <div style="border: 2px solid #ccc; border-radius: 20px; padding: 20px; 
                        width: 280px; margin: 0 auto; background: #f8f9fa;">
                <div style="text-align: center; margin-bottom: 15px;">
                    <strong>手机银行</strong>
                </div>
                <div style="background: white; padding: 15px; border-radius: 10px;">
                    <p style="margin: 5px 0;"><small>收款账户</small><br><strong>{recipient or '待输入'}</strong></p>
                    <p style="margin: 5px 0;"><small>转账金额</small><br><strong>¥{amount:,}</strong></p>
                    <p style="margin: 5px 0;"><small>交易类型</small><br><strong>{scenario}</strong></p>
                    <hr>
                    <p style="color: #666; font-size: 0.9em;">🔒 受反诈系统保护</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

elif page == "📊 数据分析":
    st.title("📊 数据分析中心")
    
    # 生成数据
    df = generate_transaction_data()
    
    # 数据筛选
    st.subheader("数据筛选")
    col1, col2, col3 = st.columns(3)
    with col1:
        min_risk = st.slider("最低风险评分", 0, 100, 50)
    with col2:
        selected_banks = st.multiselect(
            "选择银行",
            df["银行"].unique(),
            default=df["银行"].unique()
        )
    with col3:
        selected_status = st.multiselect(
            "选择状态",
            df["状态"].unique(),
            default=df["状态"].unique()
        )
    
    # 应用筛选
    filtered_df = df[
        (df["风险评分"] >= min_risk) &
        (df["银行"].isin(selected_banks)) &
        (df["状态"].isin(selected_status))
    ]
    
    # 显示数据
    st.dataframe(filtered_df, use_container_width=True, height=300)
    
    # 分析图表
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("风险分布")
        risk_dist = filtered_df["风险评分"].value_counts().sort_index()
        fig1 = px.histogram(filtered_df, x="风险评分", nbins=20)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.subheader("银行对比")
        bank_stats = filtered_df.groupby("银行")["风险评分"].mean().reset_index()
        fig2 = px.bar(bank_stats, x="银行", y="风险评分", color="风险评分")
        st.plotly_chart(fig2, use_container_width=True)

elif page == "🛠️ 系统说明":
    st.title("🛠️ 系统技术说明")
    
    st.markdown("""
    ## 🎯 系统架构
    
    ### 核心技术
    
    1. **联邦学习 (Federated Learning)**
    - 各银行在本地训练模型
    - 仅共享模型参数，不共享原始数据
    - 保护用户隐私和商业机密
    
    2. **区块链 (Blockchain)**
    - 交易记录不可篡改
    - 多方共识验证
    - 透明可审计
    
    3. **人工智能 (AI)**
    - 实时风险识别
    - 模式学习与预测
    - 自适应优化
    
    ### 工作流程
    
    ```
    用户发起交易 → 本地银行初步评估 → 联邦学习网络协同分析 → 
    区块链记录验证 → 实时风险预警 → 用户决策辅助
    ```
    
    ## 📈 预期效果
    
    | 指标 | 当前 | 目标 | 提升 |
    |------|------|------|------|
    | 诈骗识别率 | 65% | 95% | +30% |
    | 响应时间 | 24小时 | 3分钟 | 99.8% |
    | 误报率 | 25% | 5% | -80% |
    | 用户满意度 | 60% | 90% | +50% |
    
    ## 🚀 实施路线
    
    1. **第一阶段** (1-3个月): 原型开发，2家银行测试
    2. **第二阶段** (4-9个月): 5家银行接入，功能完善
    3. **第三阶段** (10-18个月): 全面推广，生态系统建设
    """)

# ========== 页脚 ==========
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p>金融反诈智能系统演示版 | 仅供教学演示使用</p>
    <p>© 2024 Fintech Innovation Lab</p>
</div>
""", unsafe_allow_html=True)
