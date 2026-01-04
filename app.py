import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random
import time

# 简单配置
st.set_page_config(page_title="S.A.F.E. WebGuard", page_icon="🛡️", layout="wide")

# 导航
st.sidebar.title("🛡️ S.A.F.E. WebGuard")
page = st.sidebar.radio("选择页面", ["首页", "实时交易", "AI智能", "仪表板"])

if page == "首页":
    st.title("🛡️ S.A.F.E. WebGuard")
    st.subheader("金融欺诈防御系统")
    
    # 简单演示
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💸 风险检测演示")
        risk_score = st.slider("设置风险分数", 0, 100, 50)
        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=risk_score,
            title={'text': "风险评分"},
            gauge={'axis': {'range': [None, 100]}}
        ))
        st.plotly_chart(fig)
    
    with col2:
        st.markdown("### 📊 今日数据")
        st.metric("防护交易数", "1,428", "+3.2%")
        st.metric("阻止诈骗", "84", "+18%")
        st.metric("响应时间", "2.3秒", "-12%")

elif page == "实时交易":
    st.title("💸 实时交易护航")
    
    # 简单表单
    with st.form("交易表单"):
        amount = st.number_input("金额(HKD)", 1000, 1000000, 50000)
        bank = st.selectbox("收款银行", ["汇丰", "中银", "恒生", "渣打"])
        
        if st.form_submit_button("🔍 开始分析"):
            with st.spinner("分析中..."):
                time.sleep(2)
                risk = random.randint(20, 90)
                
                if risk > 70:
                    st.error(f"🚨 高风险 ({risk}/100) - 建议暂停交易")
                elif risk > 40:
                    st.warning(f"⚠️ 中等风险 ({risk}/100) - 请确认信息")
                else:
                    st.success(f"✅ 低风险 ({risk}/100) - 可以继续")

elif page == "AI智能":
    st.title("🧠 AI欺诈智能")
    
    # 简单数据表
    data = pd.DataFrame({
        "预测类型": ["AI语音诈骗", "虚拟资产诈骗", "冒充诈骗", "发票诈骗"],
        "概率": ["87%", "74%", "69%", "63%"],
        "目标群体": ["中年投资者", "年轻用户", "新移民", "企业"]
    })
    
    st.dataframe(data)

elif page == "仪表板":
    st.title("🏢 机构仪表板")
    
    # 简单指标
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("银行联盟", "8家", "+2")
    with col2:
        st.metric("今日查询", "1,428", "3.2%")
    with col3:
        st.metric("隐私保护", "100%", "0%")
    
    # 简单表格
    st.markdown("### 📋 银行排名")
    banks = pd.DataFrame({
        "银行": ["汇丰", "中银", "恒生", "渣打"],
        "评分": [925, 872, 821, 785],
        "等级": ["金牌", "金牌", "银牌", "银牌"]
    })
    st.dataframe(banks)
