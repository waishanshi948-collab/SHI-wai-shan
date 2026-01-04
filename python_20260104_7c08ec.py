import streamlit as st
import time
import random
import pandas as pd
import plotly.express as px
from datetime import datetime

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="智盾金融反诈系统",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== 自定义CSS美化 ====================
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .risk-high {
        color: #DC2626;
        font-weight: bold;
        padding: 5px 10px;
        background-color: #FEE2E2;
        border-radius: 5px;
    }
    .risk-medium {
        color: #D97706;
        font-weight: bold;
        padding: 5px 10px;
        background-color: #FEF3C7;
        border-radius: 5px;
    }
    .risk-low {
        color: #059669;
        font-weight: bold;
        padding: 5px 10px;
        background-color: #D1FAE5;
        border-radius: 5px;
    }
    .blockchain-animation {
        border-left: 3px solid #3B82F6;
        padding-left: 1rem;
        background: linear-gradient(90deg, #F0F9FF, white);
        margin: 1rem 0;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ==================== 侧边栏导航 ====================
st.sidebar.title("🛡️ 智盾导航")
page = st.sidebar.radio(
    "选择演示模块",
    ["🏠 总览看板", "💸 模拟转账体验", "🔗 联盟链监控", "📊 数据与成效"]
)

# ==================== 模拟数据生成 ====================
def generate_transaction_data():
    """生成模拟交易数据"""
    transactions = []
    patterns = ["正常消费", "刷单返利", "虚假投资", "冒充公检法", "虚拟货币洗钱"]
    
    for i in range(100):
        trans_type = random.choice(patterns)
        amount = random.randint(100, 50000)
        risk_score = random.randint(1, 100)
        
        # 根据类型调整风险
        if trans_type in ["刷单返利", "虚假投资"]:
            risk_score = random.randint(70, 95)
        elif trans_type == "冒充公检法":
            risk_score = random.randint(85, 99)
        elif trans_type == "正常消费":
            risk_score = random.randint(1, 30)
            
        transactions.append({
            "时间": f"2024-{random.randint(1,12):02d}-{random.randint(1,28):02d} {random.randint(10,20):02d}:{random.randint(0,59):02d}",
            "类型": trans_type,
            "金额(元)": amount,
            "风险评分": risk_score,
            "状态": "成功" if risk_score < 50 else ("已拦截" if risk_score > 70 else "人工审核")
        })
    
    return pd.DataFrame(transactions)

# ==================== 各页面内容 ====================
if page == "🏠 总览看板":
    # 标题和介绍
    st.markdown('<h1 class="main-header">🛡️ 智盾金融反诈系统演示平台</h1>', unsafe_allow_html=True)
    st.markdown("### 基于联邦学习与区块链的协同防御网络")
    
    # 关键指标展示
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("联盟成员", "8 家机构", "+3")
    with col2:
        st.metric("日均监测交易", "1.2M 笔", "+15%")
    with col3:
        st.metric("诈骗识别准确率", "94.3%", "+8.2%")
    with col4:
        st.metric("累计挽回损失", "¥4.2亿", "+¥0.8亿")
    
    # 图表展示
    st.markdown("---")
    st.subheader("📈 近7天诈骗类型分布")
    
    # 生成图表数据
    fraud_types = ["虚拟投资理财", "刷单返利", "冒充客服", "贷款诈骗", "其他"]
    daily_counts = [
        [45, 32, 18, 12, 8],
        [48, 35, 16, 10, 7],
        [52, 38, 20, 15, 9],
        [47, 33, 17, 13, 8],
        [50, 36, 19, 14, 10],
        [55, 40, 22, 16, 11],
        [53, 39, 21, 15, 10]
    ]
    
    df_chart = pd.DataFrame({
        '日期': ['11-01', '11-02', '11-03', '11-04', '11-05', '11-06', '11-07'] * 5,
        '类型': fraud_types * 7,
        '数量': [item for sublist in daily_counts for item in sublist]
    })
    
    fig = px.line(df_chart, x='日期', y='数量', color='类型', 
                  title='各类诈骗趋势监控', markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # 系统架构图示意
    st.markdown("---")
    st.subheader("🏗️ 系统架构核心优势")
    
    cols = st.columns(3)
    with cols[0]:
        st.info("""
        **🤝 联邦学习协作**
        - 数据不出本地
        - 联合训练AI模型
        - 保护隐私合规
        """)
    with cols[1]:
        st.warning("""
        **🔗 区块链审计**
        - 操作全程可追溯
        - 贡献度量化激励
        - 不可篡改存证
        """)
    with cols[2]:
        st.success("""
        **🎯 精准干预**
        - 情景化预警
        - 家庭守护联动
        - 实时风险阻断
        """)

elif page == "💸 模拟转账体验":
    st.title("💸 模拟转账风险拦截演示")
    
    # 创建两列布局
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.subheader("1. 转账信息填写")
        
        # 账户选择
        account_type = st.radio(
            "选择转账场景",
            ["正常朋友转账", "兼职刷单佣金", "高收益投资", "缴纳'安全保证金'"],
            horizontal=True
        )
        
        # 根据场景预设信息
        preset_info = {
            "正常朋友转账": {"account": "6217********1234", "name": "李明", "bank": "招商银行"},
            "兼职刷单佣金": {"account": "0x8a7f...e5c9", "name": "XX刷单平台", "bank": "虚拟货币地址"},
            "高收益投资": {"account": "http://fake-invest.com", "name": "稳赚理财", "bank": "虚假平台"},
            "缴纳'安全保证金'": {"account": "6216********5678", "name": "XX公安局", "bank": "中国银行"}
        }
        
        selected = preset_info[account_type]
        
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("转账金额 (元)", min_value=1, max_value=500000, 
                                    value=5000 if account_type == "正常朋友转账" else 50000)
        with col2:
            st.text_input("收款账号", value=selected["account"], disabled=True)
        
        st.text_input("收款人姓名", value=selected["name"], disabled=True)
        st.text_input("收款银行", value=selected["bank"], disabled=True)
        
        # 转账按钮
        if st.button("🚀 发起转账", type="primary", use_container_width=True):
            with st.spinner("正在连接联盟链进行实时风险分析..."):
                # 模拟分析过程
                time.sleep(2)
                
                # 根据场景生成不同的风险结果
                risk_profiles = {
                    "正常朋友转账": {"score": 15, "level": "low", "msg": "✅ 交易环境安全"},
                    "兼职刷单佣金": {"score": 92, "level": "high", "msg": "🚨 检测到刷单诈骗模式"},
                    "高收益投资": {"score": 87, "level": "high", "msg": "🚨 疑似虚假投资平台"},
                    "缴纳'安全保证金'": {"score": 96, "level": "high", "msg": "🚨 符合冒充公检法诈骗特征"}
                }
                
                result = risk_profiles[account_type]
                
                # 显示风险结果
                st.markdown("---")
                st.subheader("2. 实时风险分析结果")
                
                # 风险评分展示
                if result["level"] == "high":
                    st.markdown(f'<div class="risk-high">高风险警报！评分：{result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                elif result["level"] == "medium":
                    st.markdown(f'<div class="risk-medium">中度风险！评分：{result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="risk-low">低风险！评分：{result["score"]}/100</div>', 
                               unsafe_allow_html=True)
                
                st.info(f"**分析依据：** {result['msg']}")
                
                # 具体风险点
                st.warning("""
                **🔍 检测到以下风险特征：**
                - 对方账户近期收到多笔小额测试转账
                - 交易模式符合已知诈骗模板
                - 3家联盟银行曾报告类似风险
                """)
                
                # 干预措施
                if result["level"] == "high":
                    st.error("""
                    **🛡️ 系统已自动采取保护措施：**
                    1. 交易已暂停，需人工确认
                    2. 已通知您绑定的守护人（张伟）
                    3. 建议拨打110或96110咨询
                    """)
                    
                    # 操作按钮
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        if st.button("✅ 确认安全，继续转账", type="secondary"):
                            st.error("⚠️ 强制转账成功，请注意资金安全！")
                    with col_b:
                        if st.button("📞 联系收款人核实"):
                            st.info("正在模拟通话...")
                            time.sleep(1)
                            st.success("已确认对方身份可疑，建议取消交易")
                    with col_c:
                        if st.button("🚫 取消交易"):
                            st.success("交易已取消，资金安全")
                else:
                    if st.button("✅ 确认转账", type="primary"):
                        st.balloons()
                        st.success(f"转账成功！{amount}元已汇出。")
    
    with right_col:
        st.subheader("📱 模拟手机银行界面")
        
        # 模拟手机界面
        st.markdown("""
        <div style="border: 2px solid #ccc; border-radius: 20px; padding: 20px; 
                    width: 300px; margin: 0 auto; background: #f8f9fa;">
            <div style="text-align: center; margin-bottom: 20px;">
                <strong>智盾安全检测</strong>
            </div>
            <div style="background: white; padding: 15px; border-radius: 10px; 
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <p style="margin: 5px 0;"><small>收款人</small><br><strong>{name}</strong></p>
                <p style="margin: 5px 0;"><small>账号</small><br><strong>{account}</strong></p>
                <p style="margin: 5px 0;"><small>金额</small><br><strong>¥{amount}</strong></p>
                <hr>
                <p style="color: #666; font-size: 0.9em;">🔒 交易受智盾保护</p>
            </div>
        </div>
        """.format(name=selected["name"], account=selected["account"][:10]+"...", 
                  amount=format(amount, ",")), unsafe_allow_html=True)
        
        # 家庭守护状态
        st.markdown("---")
        st.subheader("👨‍👩‍👧 家庭守护状态")
        st.success("""
        **已绑定守护人：**
        - 👨 张伟（父亲）
        - 👩 李芳（配偶）
        
        **最后在线：** 5分钟前
        """)

elif page == "🔗 联盟链监控":
    st.title("🔗 联盟链实时监控面板")
    
    # 区块链动画效果
    st.markdown("""
    <div class="blockchain-animation">
        <h4>⛓️ 联盟链实时数据流</h4>
        <p>正在同步8个节点的风险情报...</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 模拟实时数据流
    st.subheader("实时风险警报流")
    
    # 创建数据流显示
    alert_data = []
    alerts = [
        {"node": "银行A", "type": "虚拟投资诈骗", "score": 95, "time": "14:23:01"},
        {"node": "银行C", "type": "刷单返利", "score": 88, "time": "14:22:45"},
        {"node": "支付平台B", "type": "冒充客服", "score": 92, "time": "14:22:30"},
        {"node": "银行F", "type": "贷款诈骗", "score": 76, "time": "14:22:15"},
        {"node": "银行A", "type": "杀猪盘", "score": 96, "time": "14:22:00"},
    ]
    
    for alert in alerts:
        with st.container():
            cols = st.columns([1, 2, 1, 1])
            cols[0].write(f"🏦 {alert['node']}")
            cols[1].write(f"{alert['type']}")
            cols[2].markdown(f"<span class='risk-high'>{alert['score']}</span>", unsafe_allow_html=True)
            cols[3].write(f"`{alert['time']}`")
            st.divider()
    
    # 联邦学习训练状态
    st.markdown("---")
    st.subheader("🤖 联邦学习训练状态")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("当前训练轮次", "第42轮", "+1")
        st.progress(0.78, text="模型聚合进度")
    with col2:
        st.metric("参与节点", "8/8", "100%")
        st.progress(1.0, text="数据同步进度")
    
    # 模型效果指标
    st.markdown("""
    | 指标 | 单独训练 | 联邦学习 | 提升 |
    |------|---------|---------|------|
    | 准确率 | 86.2% | 94.3% | +8.1% |
    | 召回率 | 78.5% | 89.7% | +11.2% |
    | 误报率 | 15.3% | 6.8% | -8.5% |
    """)

elif page == "📊 数据与成效":
    st.title("📊 数据分析与成效展示")
    
    # 生成模拟数据
    df = generate_transaction_data()
    
    # 数据摘要
    st.subheader("数据摘要")
    total_tx = len(df)
    intercepted = len(df[df['状态'] == '已拦截'])
    success_rate = (intercepted / total_tx * 100) if total_tx > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    col1.metric("总交易数", f"{total_tx:,}")
    col2.metric("成功拦截数", f"{intercepted}")
    col3.metric("拦截成功率", f"{success_rate:.1f}%")
    
    # 交互式数据表格
    st.subheader("交易数据明细")
    st.dataframe(df, use_container_width=True, height=300)
    
    # 图表分析
    st.subheader("风险分布分析")
    
    tab1, tab2, tab3 = st.tabs(["📈 风险评分分布", "🎯 诈骗类型统计", "📅 时间趋势"])
    
    with tab1:
        fig1 = px.histogram(df, x='风险评分', nbins=20, 
                           title='风险评分分布直方图')
        st.plotly_chart(fig1, use_container_width=True)
    
    with tab2:
        type_counts = df['类型'].value_counts().reset_index()
        type_counts.columns = ['诈骗类型', '数量']
        fig2 = px.pie(type_counts, values='数量', names='诈骗类型',
                     title='诈骗类型分布')
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        # 按状态分组
        status_counts = df.groupby(['时间', '状态']).size().unstack().fillna(0)
        fig3 = px.area(status_counts, title='交易状态趋势')
        st.plotly_chart(fig3, use_container_width=True)

# ==================== 页脚 ====================
st.markdown("---")
st.caption("""
**演示说明：** 本系统为"智盾金融反诈平台"概念演示，所有数据均为模拟生成，用于展示基于联邦学习与区块链的协同反诈技术架构。
""")

# 添加自动刷新（可选）
if st.sidebar.checkbox("🔄 开启实时更新"):
    st.rerun()