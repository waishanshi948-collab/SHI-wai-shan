import streamlit as st
import time

st.set_page_config(page_title="智盾反诈系统", layout="centered")
st.title("🛡️ 智盾金融反诈演示系统")
st.subheader("基于联邦学习与区块链的协同防御网络")

st.markdown("---")

# 演示模块
tab1, tab2, tab3 = st.tabs(["风险拦截", "联盟监控", "数据看板"])

with tab1:
    st.header("💸 模拟转账风险拦截")
    account_type = st.selectbox("选择场景", ["正常转账", "刷单诈骗", "虚假投资"])
    amount = st.number_input("金额（元）", 1000, 100000, 50000)
    
    if st.button("检测风险"):
        with st.spinner("连接联盟链分析中..."):
            time.sleep(2)
            if account_type != "正常转账":
                st.error("🚨 高风险警报！检测到诈骗模式")
                st.info("**系统已自动拦截**")
            else:
                st.success("✅ 交易安全")

with tab2:
    st.header("🔗 联盟链实时监控")
    st.metric("活跃节点", "8 家机构")
    st.metric("实时警报", "24 条/小时")
    st.progress(0.75, "模型训练进度")

with tab3:
    st.header("📊 成效数据")
    col1, col2 = st.columns(2)
    col1.metric("识别准确率", "94.3%")
    col2.metric("挽回损失", "¥4.2亿")

st.caption("金融反诈技术演示系统 | 商赛专用")
