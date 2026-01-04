# ==================== 机构仪表板页面（修复版本）====================
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
                value=metric['value"],
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
    
    # 修复这里的括号问题
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
            )
        },  # 这里添加了闭合的大括号
        use_container_width=True,
        hide_index=True
    )
    
    # 添加更多内容以完善页面
    st.markdown("---")
    
    # 实时交易监控
    st.markdown("#### 📈 实时交易监控")
    
    # 生成实时交易数据
    realtime_data = pd.DataFrame({
        "时间": [f"{i}:{random.randint(10, 59):02d}" for i in range(9, 18)],
        "交易类型": random.choices(["转账", "投资", "支付", "取款"], k=9),
        "金额": [random.randint(1000, 100000) for _ in range(9)],
        "风险等级": random.choices(["低", "中", "高"], k=9),
        "处理状态": random.choices(["已拦截", "已放行", "待审核"], k=9)
    })
    
    st.dataframe(realtime_data, use_container_width=True)
    
    # 添加创新技术展示
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
        <p><strong>技术优势：</strong></p>
        <p>采用ZK-SNARKs协议，证明生成时间<1秒</p>
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
        <p><strong>技术优势：</strong></p>
        <p>欺诈检测准确率提升至96%</p>
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
        <p><strong>技术优势：</strong></p>
        <p>响应时间从3天缩短至5分钟</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== 解决方案页面 ====================
elif selected == "📚 解决方案":
    st.markdown("# 📚 S.A.F.E. WebGuard 解决方案")
    st.markdown("### 完整的技术架构与商业模型")
    
    # 创建选项卡
    tab1, tab2, tab3, tab4 = st.tabs(["技术架构", "商业模型", "实施路线", "竞争优势"])
    
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
        
        **4. 生成式AI预测器**
        - 分析多数据源模式
        - 预测新兴欺诈手法
        - 生成个性化培训场景
        """)
        
        # 技术架构图
        st.markdown("### 🖼️ 系统架构图")
        st.image("https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1VzZXJdIC0tPiBCW01vYmlsZSBCYW5raW5nIEFwcF1cbiAgICBCIC0tPiBDW1MuQS5GLkUuIFdlYkd1YXJkXVxuICAgIEMgLS0-IEVbWmVyby1Lbm93bGVkZ2UgUHJvb2ZdXG4gICAgRSAtLT4gRltGZWRlcmF0ZWQgTGVhcm5pbmcgQUldXG4gICAgRiAtLT4gR1tDb25zb3J0aXVtIEJsb2NrY2hhaW5dXG4gICAgRyAtLT4gSFtCYW5rIEFdXG4gICAgRyAtLT4gSVtCYW5rIEJdXG4gICAgRyAtLT4gSltCYW5rIENdXG4gICAgRyAtLT4gS1tBRENDXSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9", 
                 caption="S.A.F.E. WebGuard 技术架构图")
    
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
            st.metric("保险合作", "100-200万/年", "风险降低")
        
        with revenue_cols[3]:
            st.metric("国际授权", "待拓展", "区域扩张")
    
    with tab3:
        st.markdown("## 🗺️ 实施路线图")
        
        st.markdown("""
        <div class="timeline-container">
        <div class="timeline-item">
        <h4>第一阶段：基础建设（1-6个月）</h4>
        <p>• 核心银行联盟（3大银行）</p>
        <p>• 基础ZKP基础设施</p>
        <p>• MVP移动端集成</p>
        </div>
        
        <div class="timeline-item">
        <h4>第二阶段：扩展（7-18个月）</h4>
        <p>• 完整银行生态系统（10+机构）</p>
        <p>• ADCC整合</p>
        <p>• AI预测引擎上线</p>
        </div>
        
        <div class="timeline-item">
        <h4>第三阶段：成熟（19-36个月）</h4>
        <p>• 80%市场覆盖率</p>
        <p>• 国际扩张</p>
        <p>• 高级AI能力</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("## 🏆 竞争优势")
        
        advantage_data = pd.DataFrame({
            "维度": ["技术优势", "商业模式", "生态系统", "监管支持"],
            "S.A.F.E.方案": [
                "零知识证明+联邦学习+区块链",
                "SaaS+政府+保险多收入流",
                "用户-银行-警方三方网络",
                "金管局+警务处合作"
            ],
            "传统方案": [
                "单一AI或规则引擎",
                "一次性销售或维护费",
                "单点解决方案",
                "有限监管协作"
            ],
            "优势程度": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐"]
        })
        
        st.dataframe(advantage_data, use_container_width=True)

# ==================== 创新技术页面 ====================
elif selected == "⚙️ 创新技术":
    st.markdown("# ⚙️ 创新技术详解")
    st.markdown("### 商赛核心技术亮点展示")
    
    tech_tabs = st.tabs(["零知识证明", "联邦学习", "联盟区块链", "生成式AI"])
    
    with tech_tabs[0]:
        st.markdown("## 🔐 零知识证明技术")
        
        st.markdown("""
        ### 🎯 商赛创新应用
        
        **传统问题：**
        - 银行间不敢共享敏感数据
        - 数据隐私法规限制
        - 信息孤岛效应
        
        **S.A.F.E.解决方案：**
        - 银行A：生成"账户X高风险"的零知识证明
        - 银行B：验证证明的真实性，无需看到原始数据
        - 结果：协同风控，隐私保护
        
        ### ⚡ 技术实现
        """)
        
        # ZKP演示
        if st.button("🔍 演示零知识证明过程", type="primary"):
            with st.expander("查看详细过程", expanded=True):
                st.markdown("""
                **步骤1：证明生成**
                ```
                银行A输入：{账户X，交易模式，风险评分}
                ZKP算法 → 生成加密证明
                输出：π (证明)，无原始数据泄露
                ```
                
                **步骤2：证明验证**
                ```
                银行B输入：π (证明)
                验证算法 → 返回：true/false
                输出：验证结果，不学习任何额外信息
                ```
                
                **步骤3：协同决策**
                ```
                多个银行验证同一证明
                达成共识：账户X确实高风险
                采取协同防护措施
                ```
                """)
                
                # 模拟证明过程
                st.markdown("### 📊 模拟演示")
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                steps = [
                    ("🔐 加密原始数据", 25),
                    ("🧮 生成零知识证明", 50),
                    ("🔍 发送证明给联盟银行", 75),
                    ("✅ 验证通过，达成共识", 100)
                ]
                
                for step_text, progress in steps:
                    status_text.text(f"正在执行: {step_text}")
                    progress_bar.progress(progress)
                    time.sleep(1)
                
                st.success("✅ 零知识证明验证成功！隐私数据全程保护。")
    
    with tech_tabs[1]:
        st.markdown("## 🤖 联邦学习技术")
        
        st.markdown("""
        ### 🎯 商赛创新应用
        
        **传统AI困境：**
        - 需要集中训练数据
        - 隐私泄露风险
        - 数据合规挑战
        
        **联邦学习优势：**
        - 数据留在本地银行
        - 仅交换模型参数
        - 全局模型协同进化
        
        ### 🏗️ 架构设计
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔵 本地训练阶段**
            1. 各银行本地训练AI模型
            2. 使用自身客户数据
            3. 生成模型更新参数
            
            **🟢 参数聚合阶段**
            1. 上传加密的模型参数
            2. 中央服务器安全聚合
            3. 生成全局模型
            """)
        
        with col2:
            st.markdown("""
            **🟡 模型分发阶段**
            1. 分发更新后的全局模型
            2. 各银行接收并验证
            3. 替换本地模型
            
            **🔴 效果评估**
            - 欺诈检测准确率：+28%
            - 数据隐私保护：100%
            - 模型更新频率：每小时
            """)
    
    with tech_tabs[2]:
        st.markdown("## ⛓️ 联盟区块链")
        
        st.markdown("""
        ### 🎯 商赛创新应用
        
        **传统审计问题：**
        - 中心化记录易被篡改
        - 多方协作缺乏信任
        - 调查取证困难
        
        **区块链解决方案：**
        - 分布式账本不可篡改
        - 智能合约自动化执行
        - 透明化协作信任
        
        ### 🔗 区块链网络结构
        """)
        
        # 区块链节点可视化
        st.markdown("#### 🌐 联盟节点分布")
        
        nodes = [
            {"name": "汇丰银行", "type": "验证节点", "status": "在线"},
            {"name": "中银香港", "type": "验证节点", "status": "在线"},
            {"name": "恒生银行", "type": "验证节点", "status": "在线"},
            {"name": "金管局", "type": "监管节点", "status": "在线"},
            {"name": "警务处", "type": "执法节点", "status": "在线"},
            {"name": "证监会", "type": "监管节点", "status": "离线"}
        ]
        
        for node in nodes:
            status_icon = "🟢" if node["status"] == "在线" else "🔴"
            node_type_color = "#3B82F6" if "银行" in node["type"] else "#10B981" if "监管" in node["type"] else "#EF4444"
            
            st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 10px; margin: 5px 0; background: #F8FAFC; border-radius: 8px; border-left: 4px solid {node_type_color};">
                <div style="flex: 1;">
                    <strong>{node['name']}</strong><br>
                    <small style="color: #6B7280;">{node['type']}</small>
                </div>
                <div style="margin-left: auto;">
                    {status_icon} {node['status']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tech_tabs[3]:
        st.markdown("## 🧠 生成式AI技术")
        
        st.markdown("""
        ### 🎯 商赛创新应用
        
        **传统风控局限：**
        - 基于历史模式的检测
        - 难以预测新型诈骗
        - 缺乏个性化教育
        
        **生成式AI优势：**
        - 模拟未来诈骗场景
        - 生成个性化培训内容
        - 预测新兴风险模式
        
        ### 🎭 AI生成演示
        """)
        
        if st.button("🤖 生成新型诈骗场景预测", type="primary"):
            with st.spinner("AI正在分析趋势并生成预测..."):
                time.sleep(2)
                
                st.markdown("""
                ### 🔮 AI生成预测结果
                
                **新型诈骗类型：** 元宇宙投资诈骗
                
                **预测特征：**
                - 利用元宇宙概念包装
                - 承诺虚拟地产高回报
                - 目标：年轻科技投资者
                - 预计发生率：2024年增长300%
                
                **AI推荐防御策略：**
                1. 建立虚拟资产交易白名单
                2. 元宇宙项目尽职调查指南
                3. 投资者教育：区分真实项目与骗局
                4. 实时监控虚拟资产异常流动
                
                **技术实现：**
                - 使用GPT-4分析网络趋势
                - 结合历史诈骗模式识别
                - 生成针对性防御方案
                """)

# ==================== 页脚 ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 20px;">
    <p><strong>🛡️ S.A.F.E. WebGuard | 金融欺诈防御系统 v2.0</strong></p>
    <p>商赛演示应用 | 非生产环境使用</p>
    <p>技术支持：联邦学习 + 零知识证明 + 联盟区块链 + 生成式AI</p>
    <p>© 2024 S.A.F.E. Technologies | 保留所有权利</p>
</div>
""", unsafe_allow_html=True)

# ==================== 运行说明 ====================
if __name__ == "__main__":
    # 在Streamlit Cloud上自动运行
    pass
