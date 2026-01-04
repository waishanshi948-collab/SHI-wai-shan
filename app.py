import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random
import time

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="S.A.F.E. WebGuard",
    page_icon="🛡️",
    layout="wide"
)

# ==================== 侧边栏 ====================
with st.sidebar:
    st.title("🛡️ S.A.F.E. WebGuard")
    st.caption("金融欺诈防御系统")
    
    st.markdown("---")
    
    # 使用radio进行导航
    page = st.radio(
        "导航菜单",
        ["首页", "实时交易", "AI智能", "机构面板", "解决方案"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.info("商赛演示应用 v3.0")

# ==================== 首页 ====================
if page == "首页":
    st.title("🛡️ S.A.F.E. WebGuard")
    st.subheader("金融欺诈防御系统 - 商赛演示版")
    
    # 核心功能展示
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔐 零知识证明")
        st.write("银行间无需共享数据即可协同风控")
    
    with col2:
        st.markdown("### 🤖 联邦学习")
        st.write("去中心化AI训练保护隐私")
    
    with col3:
        st.markdown("### ⛓️ 区块链")
        st.write("不可篡改的审计追踪")
    
    st.markdown("---")
    
    # 快速演示
    st.markdown("## 🚀 快速演示")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("### 💸 交易风险检测")
        
        # 简单输入
        amount = st.number_input("交易金额(HKD)", 1000, 1000000, 50000)
        scenario = st.selectbox("交易类型", ["正常转账", "投资存款", "加密货币"])
        
        if st.button("🔍 开始分析", type="primary"):
            with st.spinner("分析中..."):
                time.sleep(1)
                
                # 简单风险计算
                if "投资" in scenario or "加密" in scenario:
                    risk = random.randint(70, 95)
                    color = "red"
                else:
                    risk = random.randint(10, 40)
                    color = "green"
                
                # 显示结果
                st.markdown(f"### 风险评分: **{risk}/100**")
                if risk > 70:
                    st.error("🚨 高风险 - 建议暂停交易")
                elif risk > 40:
                    st.warning("⚠️ 中等风险 - 请确认信息")
                else:
                    st.success("✅ 低风险 - 可以继续")
    
    with demo_col2:
        st.markdown("### 📊 系统指标")
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("今日防护", "1,428笔", "+3.2%")
            st.metric("活跃银行", "8家", "+2")
        with col_b:
            st.metric("响应时间", "2.3秒", "-12%")
            st.metric("准确率", "96%", "+2%")

# ==================== 实时交易页面 ====================
elif page == "实时交易":
    st.title("💸 实时交易护航")
    st.write("基于零知识证明的隐私保护交易风控")
    
    # 交易信息输入
    with st.form("交易信息"):
        col1, col2 = st.columns(2)
        
        with col1:
            trans_type = st.selectbox(
                "交易类型",
                ["转账到已知账户", "支付给新供应商", "投资存款", "加密货币购买"]
            )
            amount = st.slider("金额(HKD)", 1000, 1000000, 50000, 1000)
        
        with col2:
            bank = st.selectbox(
                "收款银行",
                ["汇丰银行", "中银香港", "恒生银行", "渣打银行"]
            )
            user_type = st.selectbox(
                "用户类型",
                ["普通用户", "企业客户", "老年用户", "新居民"]
            )
        
        submitted = st.form_submit_button("🚀 开始风险扫描")
    
    if submitted:
        # 显示处理过程
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("🔐 生成零知识证明...")
            elif i < 60:
                status_text.text("🔄 查询联盟银行...")
            elif i < 90:
                status_text.text("📊 分析风险模式...")
            else:
                status_text.text("✅ 完成风险评估...")
            time.sleep(0.02)
        
        progress_bar.empty()
        status_text.empty()
        
        # 显示结果
        st.markdown("## 📊 风险评估结果")
        
        # 风险评分
        risk_score = random.randint(10, 95)
        
        # 创建仪表盘
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text': "风险评分"},
            gauge={
                'axis': {'range': [None, 100]},
                'steps': [
                    {'range': [0, 30], 'color': "green"},
                    {'range': [30, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "red"}
                ]
            }
        ))
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 建议
        if risk_score > 70:
            st.error("## 🚨 高风险警报")
            st.write("建议立即暂停交易并联系银行")
        elif risk_score > 40:
            st.warning("## ⚠️ 中等风险")
            st.write("建议验证收款方信息后再继续")
        else:
            st.success("## ✅ 低风险")
            st.write("交易安全，可以继续")

# ==================== AI智能页面 ====================
elif page == "AI智能":
    st.title("🧠 AI欺诈智能")
    st.write("基于机器学习的欺诈预测与防御")
    
    # AI预测表格
    st.markdown("### 🔮 AI欺诈预测")
    
    predictions = pd.DataFrame({
        "欺诈类型": [
            "AI合成投资骗局",
            "跨境虚拟资产诈骗",
            "政府支付冒充",
            "供应链发票欺诈"
        ],
        "概率": ["87%", "74%", "69%", "63%"],
        "目标群体": ["中年投资者", "年轻科技用户", "新移民", "中小企业"],
        "防御措施": ["实时交互验证", "平台白名单", "官方渠道确认", "区块链验证"]
    })
    
    st.dataframe(predictions, use_container_width=True)
    
    # 趋势图表
    st.markdown("### 📈 欺诈趋势")
    
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    investment_fraud = [45, 48, 52, 55, 58, 62]
    impersonation = [32, 35, 38, 40, 42, 45]
    
    trend_data = pd.DataFrame({
        '月份': months,
        '投资诈骗': investment_fraud,
        '冒充诈骗': impersonation
    })
    
    st.line_chart(trend_data.set_index('月份'))

# ==================== 机构面板页面 ====================
elif page == "机构面板":
    st.title("🏢 机构仪表板")
    st.write("银行与执法机构协作平台")
    
    # 银行联盟指标
    st.markdown("## 🏦 银行联盟")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("今日查询", "1,428", "+3.2%")
    
    with col2:
        st.metric("响应时间", "0.8秒", "-12%")
    
    with col3:
        st.metric("隐私保护", "100%", "0%")
    
    with col4:
        st.metric("误报率", "2.3%", "-15%")
    
    # 银行排名
    st.markdown("### 🏆 银行排名")
    
    bank_data = pd.DataFrame({
        "银行": ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "众安银行"],
        "安全评分": [925, 872, 821, 785, 642],
        "警报数": [142, 128, 98, 87, 45],
        "等级": ["金牌", "金牌", "银牌", "银牌", "铜牌"]
    })
    
    st.dataframe(bank_data, use_container_width=True)
    
    # 执法机构
    st.markdown("## 👮 执法协作")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("预防案件", "84起", "+18%")
    
    with col2:
        st.metric("保护资金", "3.12亿", "+22%")
    
    with col3:
        st.metric("响应时间", "42分钟", "-28%")
    
    with col4:
        st.metric("满意度", "94.2%", "+3.5%")
    
    # 案件数据
    st.markdown("### 📋 案件洞察")
    
    case_data = pd.DataFrame({
        "案件类型": ["AI语音诈骗", "虚拟资产诈骗", "跨境洗钱", "发票欺诈"],
        "严重程度": ["高", "高", "中", "中"],
        "目标群体": ["老年用户", "年轻投资者", "学生", "企业"],
        "状态": ["处理中", "已解决", "调查中", "监控中"]
    })
    
    st.dataframe(case_data, use_container_width=True)

# ==================== 解决方案页面 ====================
elif page == "解决方案":
    st.title("📚 解决方案")
    st.write("技术架构与商业模型")
    
    tab1, tab2, tab3 = st.tabs(["技术架构", "商业模型", "竞争优势"])
    
    with tab1:
        st.markdown("## 🏗️ 技术架构")
        st.markdown("""
        ### 三层防御体系
        
        1. **用户层**
           - 移动银行集成
           - 实时风险提示
           - 紧急援助通道
        
        2. **银行层**
           - 零知识证明协议
           - 联邦学习AI
           - 区块链验证
        
        3. **执法层**
           - 实时情报共享
           - 区块链取证
           - 协同响应
        """)
    
    with tab2:
        st.markdown("## 💰 商业模型")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 收入来源")
            st.write("- SaaS授权费：200-500万/年")
            st.write("- 政府资助：150-300万/年")
            st.write("- 保险合作：100-200万/年")
            st.write("- 国际授权：待拓展")
        
        with col2:
            st.markdown("### 关键指标")
            st.write("- 欺诈检测率：96% (+41%)")
            st.write("- 响应时间：3-5分钟 (快99%)")
            st.write("- 跨行协作：100%覆盖")
            st.write("- 公众意识：92% (+104%)")
    
    with tab3:
        st.markdown("## 🏆 竞争优势")
        
        advantage_data = pd.DataFrame({
            "维度": ["技术", "商业模式", "生态系统"],
            "S.A.F.E.方案": [
                "零知识证明+联邦学习",
                "SaaS+政府+保险",
                "三方协作网络"
            ],
            "传统方案": [
                "单一技术",
                "一次性收费",
                "单点解决方案"
            ]
        })
        
        st.dataframe(advantage_data, use_container_width=True)

# ==================== 页脚 ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>🛡️ S.A.F.E. WebGuard | 金融欺诈防御系统</p>
    <p>商赛演示应用 | © 2024</p>
</div>
""", unsafe_allow_html=True)
