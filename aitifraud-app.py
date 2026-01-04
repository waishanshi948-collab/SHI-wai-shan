"""
S.A.F.E. WebGuard - 金融欺诈防御系统
商赛演示应用 - 完全测试版本
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random
import time

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="S.A.F.E. WebGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== 初始化会话状态 ====================
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 25
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# ==================== 自定义CSS ====================
st.markdown("""
<style>
    /* 主标题 */
    .main-title {
        text-align: center;
        color: #1E40AF;
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    /* 卡片样式 */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #3B82F6;
    }
    
    .card-red {
        border-left-color: #EF4444;
        background: #FEF2F2;
    }
    
    .card-yellow {
        border-left-color: #F59E0B;
        background: #FFFBEB;
    }
    
    .card-green {
        border-left-color: #10B981;
        background: #F0FDF4;
    }
    
    /* 区块链节点 */
    .node {
        display: inline-block;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin: 0 10px;
        text-align: center;
        line-height: 40px;
        font-weight: bold;
        color: white;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# ==================== 辅助函数 ====================
def create_risk_gauge(score):
    """创建风险评分仪表盘"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "风险评分", 'font': {'size': 20}},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#1E40AF"},
            'steps': [
                {'range': [0, 30], 'color': "#10B981"},
                {'range': [30, 70], 'color': "#F59E0B"},
                {'range': [70, 100], 'color': "#EF4444"}
            ]
        }
    ))
    fig.update_layout(height=300, margin=dict(t=50, b=20, l=20, r=20))
    return fig

def generate_transactions():
    """生成模拟交易数据"""
    data = []
    for i in range(10):
        risk = random.randint(10, 90)
        status = "✅ 通过" if risk < 30 else ("⚠️ 审核" if risk < 70 else "🚨 拦截")
        
        data.append({
            "时间": f"{random.randint(9,16)}:{random.randint(10,59):02d}",
            "类型": random.choice(["转账", "投资", "支付", "取款"]),
            "金额(HKD)": f"{random.randint(1000,500000):,}",
            "风险分": risk,
            "状态": status
        })
    return pd.DataFrame(data)

# ==================== 侧边栏 ====================
with st.sidebar:
    st.markdown('<div class="main-title"><h2>🛡️ S.A.F.E.</h2><p>WebGuard</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 导航按钮
    if st.button("🏠 首页", use_container_width=True):
        st.session_state.page = 'home'
    if st.button("💸 交易护航", use_container_width=True):
        st.session_state.page = 'transaction'
    if st.button("🧠 AI智能", use_container_width=True):
        st.session_state.page = 'ai'
    if st.button("🏢 机构面板", use_container_width=True):
        st.session_state.page = 'dashboard'
    if st.button("📚 解决方案", use_container_width=True):
        st.session_state.page = 'solution'
    
    st.markdown("---")
    
    # 系统状态
    st.markdown("### 📊 系统状态")
    st.metric("活跃银行", "8家", "+2")
    st.metric("今日防护", "1,428笔", "3.2%")
    st.progress(0.85, text="覆盖率 85%")

# ==================== 首页 ====================
if st.session_state.page == 'home':
    st.markdown('<div class="main-title"><h1>🛡️ S.A.F.E. WebGuard</h1><p>金融欺诈防御系统 - 商赛演示版</p></div>', unsafe_allow_html=True)
    
    # 核心创新点
    st.markdown("## 🚀 核心创新")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
        <h3>🔐 零知识证明</h3>
        <p>银行间无需共享数据即可协同风控，100%隐私保护</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <h3>🤖 联邦学习</h3>
        <p>去中心化AI训练，模型准确率提升至96%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
        <h3>⛓️ 区块链</h3>
        <p>不可篡改审计追踪，响应时间缩短99%</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 快速演示
    st.markdown("## 🎯 快速演示")
    
    demo_col1, demo_col2 = st.columns(2)
    
    with demo_col1:
        st.markdown("### 💰 风险检测模拟")
        
        scenario = st.selectbox(
            "选择场景",
            ["正常转账", "投资存款", "加密货币", "紧急支付"]
        )
        
        amount = st.slider("金额(HKD)", 1000, 1000000, 50000)
        
        if st.button("🔍 开始检测", type="primary"):
            with st.spinner("分析中..."):
                time.sleep(1)
                
                # 简单风险计算
                if "投资" in scenario or "加密" in scenario:
                    score = random.randint(70, 95)
                    card_class = "card-red"
                    icon = "🚨"
                elif "紧急" in scenario:
                    score = random.randint(40, 70)
                    card_class = "card-yellow"
                    icon = "⚠️"
                else:
                    score = random.randint(10, 40)
                    card_class = "card-green"
                    icon = "✅"
                
                st.session_state.risk_score = score
                
                st.markdown(f"""
                <div class="{card_class}">
                <h3>{icon} 风险评分: {score}/100</h3>
                <p>交易分析完成，建议根据风险等级采取措施</p>
                </div>
                """, unsafe_allow_html=True)
    
    with demo_col2:
        st.markdown("### 📈 实时指标")
        fig = create_risk_gauge(st.session_state.risk_score)
        st.plotly_chart(fig, use_container_width=True)

# ==================== 交易护航页面 ====================
elif st.session_state.page == 'transaction':
    st.title("💸 实时交易护航")
    st.markdown("#### 基于零知识证明的隐私保护交易风控")
    
    # 输入区域
    with st.form("transaction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            trans_type = st.selectbox(
                "交易类型",
                ["转账给朋友", "支付供应商", "投资理财", "购买加密货币", "紧急汇款"]
            )
            amount = st.number_input("金额(HKD)", 1000, 1000000, 50000)
        
        with col2:
            bank = st.selectbox(
                "收款银行",
                ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "虚拟银行"]
            )
            user_type = st.selectbox(
                "用户类型",
                ["普通用户", "企业客户", "老年用户", "新居民"]
            )
        
        submitted = st.form_submit_button("🚀 启动护航扫描")
    
    if submitted:
        # 显示处理过程
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            ("🔐 生成零知识证明", 20),
            ("🏦 查询联盟银行", 40),
            ("🤖 AI风险分析", 60),
            ("⛓️ 区块链验证", 80),
            ("✅ 完成评估", 100)
        ]
        
        for step, progress in steps:
            status_text.text(step)
            progress_bar.progress(progress)
            time.sleep(0.5)
        
        progress_bar.empty()
        status_text.empty()
        
        # 计算结果
        if "加密" in trans_type or amount > 100000:
            score = random.randint(75, 95)
        elif "投资" in trans_type or "紧急" in trans_type:
            score = random.randint(40, 75)
        else:
            score = random.randint(10, 40)
        
        # 显示结果
        st.markdown("## 📊 风险评估结果")
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = create_risk_gauge(score)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            if score > 70:
                st.markdown("""
                <div class="card-red">
                <h3>🚨 高风险警报</h3>
                <p>交易特征与诈骗模式高度匹配</p>
                <ul>
                <li>建议：立即暂停交易</li>
                <li>联系银行：+852 1234 5678</li>
                <li>报警热线：18222</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            elif score > 40:
                st.markdown("""
                <div class="card-yellow">
                <h3>⚠️ 中等风险</h3>
                <p>检测到可疑交易模式</p>
                <ul>
                <li>建议：验证收款方信息</li>
                <li>可延迟24小时处理</li>
                <li>联系客服确认</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="card-green">
                <h3>✅ 低风险</h3>
                <p>交易正常可继续</p>
                <ul>
                <li>建议：确认信息后继续</li>
                <li>启用双重验证</li>
                <li>保存交易记录</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
        
        # 区块链可视化
        st.markdown("### 🔗 区块链验证网络")
        
        nodes = ["汇丰", "中银", "恒生", "渣打", "金管局", "警方"]
        nodes_html = ""
        colors = ["#10B981", "#10B981", "#F59E0B", "#10B981", "#10B981", "#F59E0B"]
        
        for node, color in zip(nodes, colors):
            nodes_html += f'<div class="node" style="background:{color}">{node}</div>'
        
        st.markdown(f'<div style="text-align:center; margin:20px">{nodes_html}</div>', unsafe_allow_html=True)

# ==================== AI智能页面 ====================
elif st.session_state.page == 'ai':
    st.title("🧠 AI欺诈智能")
    st.markdown("#### 预测性分析与智能防御")
    
    # AI预测
    st.markdown("### 🔮 欺诈预测分析")
    
    predictions = pd.DataFrame({
        "欺诈类型": ["AI语音投资诈骗", "元宇宙投资骗局", "虚拟资产套利", "冒充政府支付", "供应链欺诈"],
        "概率": ["87%", "82%", "74%", "69%", "63%"],
        "目标群体": ["中年投资者", "科技爱好者", "年轻投资者", "新移民", "中小企业"],
        "防御策略": ["声纹验证+视频确认", "项目尽职调查", "平台白名单", "官方渠道验证", "区块链发票"]
    })
    
    st.dataframe(predictions, use_container_width=True)
    
    # 趋势分析
    st.markdown("### 📈 欺诈趋势分析")
    
    months = ['1月', '2月', '3月', '4月', '5月', '6月']
    df_trend = pd.DataFrame({
        '月份': months,
        '投资诈骗': [45, 48, 52, 55, 58, 62],
        '冒充诈骗': [32, 35, 38, 40, 42, 45],
        '电商诈骗': [28, 30, 32, 35, 38, 40]
    })
    
    fig = px.line(df_trend, x='月份', y=df_trend.columns[1:], 
                  title='2024年欺诈趋势变化',
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ==================== 机构面板页面 ====================
elif st.session_state.page == 'dashboard':
    st.title("🏢 机构协作面板")
    st.markdown("#### 银行联盟与执法机构协作平台")
    
    # 银行联盟
    st.markdown("## 🏦 银行联盟控制台")
    
    bank_metrics = st.columns(4)
    with bank_metrics[0]:
        st.metric("今日查询", "1,428", "+3.2%")
    with bank_metrics[1]:
        st.metric("响应时间", "0.8秒", "-12%")
    with bank_metrics[2]:
        st.metric("隐私保护", "100%", "0%")
    with bank_metrics[3]:
        st.metric("准确率", "96.2%", "+1.8%")
    
    # 银行排名
    st.markdown("### 🏆 银行安全排名")
    
    bank_data = pd.DataFrame({
        "银行": ["汇丰银行", "中银香港", "恒生银行", "渣打银行", "众安银行"],
        "安全评分": [925, 872, 821, 785, 642],
        "警报数": [142, 128, 98, 87, 45],
        "贡献度": ["35%", "28%", "18%", "12%", "7%"],
        "等级": ["金牌", "金牌", "银牌", "银牌", "铜牌"]
    })
    
    st.dataframe(bank_data, use_container_width=True, height=300)
    
    # 执法机构
    st.markdown("## 👮 执法协作中心")
    
    police_metrics = st.columns(4)
    with police_metrics[0]:
        st.metric("预防案件", "84起", "+18%")
    with police_metrics[1]:
        st.metric("保护资金", "3.12亿", "+22%")
    with police_metrics[2]:
        st.metric("响应时间", "42分钟", "-28%")
    with police_metrics[3]:
        st.metric("公众满意", "94.2%", "+3.5%")
    
    # 案件洞察
    st.markdown("### 🔍 案件洞察")
    
    case_data = pd.DataFrame({
        "案件类型": ["AI语音诈骗激增", "虚拟资产诈骗集群", "跨境洗钱网络", "发票欺诈趋势"],
        "严重程度": ["高", "高", "中", "中"],
        "目标群体": ["老年用户", "年轻投资者", "学生", "企业"],
        "应对行动": ["公众警报", "平台封锁", "调查中", "教育计划"]
    })
    
    st.dataframe(case_data, use_container_width=True)

# ==================== 解决方案页面 ====================
elif st.session_state.page == 'solution':
    st.title("📚 解决方案架构")
    st.markdown("#### 技术架构与商业模型")
    
    tab1, tab2, tab3 = st.tabs(["技术架构", "商业模型", "竞争优势"])
    
    with tab1:
        st.markdown("## 🏗️ 技术架构体系")
        
        st.markdown("""
        ### 三层防御框架
        
        **1. 用户层 (前端防护)**
        - 移动银行App集成
        - 实时风险提示
        - 紧急求助通道
        
        **2. 银行层 (核心处理)**
        - 零知识证明协议
        - 联邦学习AI引擎
        - 区块链共识网络
        
        **3. 执法层 (后端响应)**
        - 实时情报共享
        - 区块链取证系统
        - 协同响应机制
        
        ### 🔐 核心技术
        - **零知识证明**：银行间无需共享数据
        - **联邦学习**：去中心化AI训练
        - **联盟链**：不可篡改审计追踪
        - **生成式AI**：预测新型诈骗
        """)
    
    with tab2:
        st.markdown("## 💰 商业模型")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 收入来源")
            st.write("""
            - **SaaS授权费**：200-500万港币/年/大银行
            - **政府资助**：150-300万港币/年 (犯罪预防基金)
            - **保险合作**：100-200万港币/年 (风险降低分润)
            - **国际授权**：亚洲区域扩展
            """)
        
        with col2:
            st.markdown("### 关键指标")
            st.write("""
            - **欺诈检测率**：96% (提升41%)
            - **误报率**：3% (降低83%)
            - **响应时间**：3-5分钟 (缩短99%)
            - **跨行协作**：100%覆盖
            - **公众意识**：92% (提升104%)
            """)
    
    with tab3:
        st.markdown("## 🏆 竞争优势")
        
        comp_data = pd.DataFrame({
            "维度": ["技术方案", "商业模式", "生态系统", "监管支持"],
            "S.A.F.E.": [
                "零知识证明+联邦学习+区块链",
                "SaaS+政府+保险多收入",
                "用户-银行-警方三方网络",
                "金管局+警务处官方合作"
            ],
            "传统方案": [
                "单一AI或规则引擎",
                "一次性销售或维护费",
                "单点解决方案",
                "有限监管协作"
            ]
        })
        
        st.dataframe(comp_data, use_container_width=True)

# ==================== 页脚 ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 20px;">
    <p><strong>🛡️ S.A.F.E. WebGuard | 金融欺诈防御系统 v3.0</strong></p>
    <p>商赛演示应用 | 技术支持：零知识证明 + 联邦学习 + 联盟区块链</p>
    <p>© 2024 S.A.F.E. Technologies | All rights reserved</p>
</div>
""", unsafe_allow_html=True)

# ==================== 运行应用 ====================
if __name__ == "__main__":
    # 清除缓存确保新代码生效
    st.cache_data.clear()
    st.cache_resource.clear()