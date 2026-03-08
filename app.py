import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Jason Lai | Interactive Resume",
    page_icon="📊",
    layout="wide",
)

# ---------- Data ----------
profile = {
    "name": "Bokai (Jason) Lai",
    "title": "Data Scientist | ML Engineer | Analytics Professional",
    "tagline": (
        "Analytical and business-minded Data Scientist with a strong foundation in computer science, "
        "statistics, machine learning, and applied business analytics."
    ),
    "phone": "(647) 328-9168",
    "email": "bokai.lai@rotman.utoronto.ca",
    "linkedin": "linkedin.com/in/jason-lllai",
    "location": "Toronto, Ontario, Canada",
}

skills = pd.DataFrame(
    [
        ["Python", "Programming", 95],
        ["SQL", "Programming", 90],
        ["R", "Programming", 78],
        ["JavaScript", "Programming", 72],
        ["PyTorch", "ML / Deep Learning", 92],
        ["TensorFlow", "ML / Deep Learning", 88],
        ["Scikit-learn", "ML / Deep Learning", 91],
        ["PySpark", "Data Engineering", 76],
        ["Pandas", "Analytics", 94],
        ["NumPy", "Analytics", 90],
        ["Tableau", "Visualization", 82],
        ["Excel", "Visualization", 85],
        ["AWS", "Cloud", 82],
        ["Azure", "Cloud", 74],
        ["Docker", "Cloud", 80],
        ["Git / GitHub", "Tools", 85],
        ["XGBoost / LightGBM", "ML / Deep Learning", 87],
        ["Transformers", "ML / Deep Learning", 86],
        ["ARIMA / LSTM", "Time Series", 83],
        ["Feature Engineering", "ML / Deep Learning", 92],
    ],
    columns=["Skill", "Category", "Proficiency"],
)

education = pd.DataFrame(
    [
        [
            "Rotman School of Management, University of Toronto",
            "Master of Management Analytics",
            "2025 – Expected July 2026",
            "Toronto, Ontario",
        ],
        [
            "CFA Institute",
            "CFA Level I Candidate",
            "2026",
            "Toronto, Ontario",
        ],
        [
            "University of British Columbia",
            "B.Sc. in Computer Science and Statistics",
            "2020 – 2024",
            "British Columbia",
        ],
    ],
    columns=["Institution", "Program", "Timeline", "Location"],
)

experience = pd.DataFrame(
    [
        [
            "Scotiabank (AML)",
            "Data Scientist Intern",
            "Toronto, Ontario",
            "2026-01",
            "2026-12",
            "Finance / AML",
            18,
            23,
            "Built anomaly detection and semi-supervised AML models across 6+ typologies and million-scale samples.",
        ],
        [
            "Scotiabank (AML)",
            "Data Scientist Intern",
            "Toronto, Ontario",
            "2026-01",
            "2026-12",
            "LLM / Risk AI",
            15,
            20,
            "Designed a multi-agent LLM framework with reinforcement learning from investigator feedback.",
        ],
        [
            "Scotiabank (AML)",
            "Data Scientist Intern",
            "Toronto, Ontario",
            "2026-01",
            "2026-12",
            "Feature Engineering",
            12,
            0,
            "Engineered 50+ behavioral and time-series features with leakage-safe evaluation.",
        ],
        [
            "Siemens (Digital Industries)",
            "Data Scientist Intern",
            "Beijing, China",
            "2024-10",
            "2025-05",
            "Text / Manufacturing ML",
            15,
            0,
            "Built hybrid CNN + Bi-LSTM + LightGBM pipeline and deployed on AWS with Docker.",
        ],
        [
            "Siemens (Digital Industries)",
            "Data Scientist Intern",
            "Beijing, China",
            "2024-10",
            "2025-05",
            "RAG / NLP",
            37,
            20,
            "Built a production RAG chatbot with persistent context and localized LLM support.",
        ],
        [
            "Pou Sheng International",
            "Data Analyst Intern",
            "Dalian, China",
            "2024-07",
            "2024-10",
            "Retail Analytics",
            12,
            0,
            "Diagnosed store profitability and recommended actions that reduced operating cost.",
        ],
        [
            "Pou Sheng International",
            "Data Analyst Intern",
            "Dalian, China",
            "2024-07",
            "2024-10",
            "Business Performance",
            9.8,
            0,
            "Used P&L and store traffic analysis to support mid-year sales growth.",
        ],
    ],
    columns=[
        "Company",
        "Role",
        "Location",
        "Start",
        "End",
        "Focus",
        "Impact_1",
        "Impact_2",
        "Summary",
    ],
)

experience_table = pd.DataFrame(
    [
        ["Scotiabank (AML)", "Data Scientist Intern", "Toronto, Ontario", "Jan 2026 – Present"],
        ["Siemens (Digital Industries)", "Data Scientist Intern", "Beijing, China", "Oct 2024 – May 2025"],
        ["Pou Sheng International", "Data Analyst Intern", "Dalian, China", "Jul 2024 – Oct 2024"],
    ],
    columns=["Company", "Role", "Location", "Timeline"],
)

projects = [
    {
        "name": "LLM-Powered Summer Home Recommender",
        "stack": "Python, Flask, HTML/CSS/JavaScript, Gemini 2.5 Pro",
        "summary": (
            "Built an end-to-end rental search application with CRUD functionality, a hybrid recommender, "
            "multi-filter search, date-conflict checks, and an AI travel assistant with validation and tests."
        ),
    }
]


def render_html_table(df: pd.DataFrame) -> None:
    """Render a table without depending on Streamlit's Arrow backend."""
    html_table = df.reset_index(drop=True).to_html(index=False, classes="resume-table", border=0)
    st.markdown(html_table, unsafe_allow_html=True)

# ---------- Styling ----------
st.markdown(
    """
    <style>
    .main {background-color: #f7f9fc;}
    .hero {
        padding: 1.2rem 1.4rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #0f172a, #1e3a8a 65%, #2563eb);
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.15);
    }
    .pill {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        margin: 0.15rem 0.2rem 0.15rem 0;
        border-radius: 999px;
        background: #e8eefc;
        color: #16325c;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .card {
        background: white;
        color: #0f172a;
        padding: 1rem 1rem 0.8rem 1rem;
        border-radius: 16px;
        border: 1px solid rgba(15,23,42,0.06);
        box-shadow: 0 8px 20px rgba(15,23,42,0.05);
        margin-bottom: 0.9rem;
    }
    .card b, .card p, .card span, .card div {
        color: inherit;
    }
    .small-muted {
        color: #6b7280;
        font-size: 0.92rem;
    }
    .resume-table {
        width: 100%;
        border-collapse: collapse;
        background: white;
        color: #0f172a;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(15,23,42,0.05);
    }
    .resume-table th {
        background: #eff4ff;
        color: #16325c;
        font-weight: 700;
        text-align: left;
    }
    .resume-table th, .resume-table td {
        padding: 0.7rem 0.8rem;
        border: 1px solid rgba(15,23,42,0.08);
        font-size: 0.93rem;
    }
    .resume-table td {
        color: #0f172a;
        background: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar Controls ----------
st.sidebar.title("Customize the Resume View")
selected_category = st.sidebar.selectbox(
    "Skill category",
    ["All"] + sorted(skills["Category"].unique().tolist()),
)
proficiency_threshold = st.sidebar.slider(
    "Minimum proficiency",
    min_value=60,
    max_value=100,
    value=80,
    step=5,
)
show_metrics = st.sidebar.checkbox("Show quantified impact metrics", value=True)
selected_focus = st.sidebar.multiselect(
    "Highlight experience focus areas",
    sorted(experience["Focus"].unique().tolist()),
    default=["Finance / AML", "LLM / Risk AI", "RAG / NLP"],
)
chart_style = st.sidebar.radio(
    "Chart view",
    ["Skill proficiency", "Experience impact"],
)
show_project = st.sidebar.toggle("Show technical project section", value=True)

# ---------- Filtered Data ----------
filtered_skills = skills.copy()
if selected_category != "All":
    filtered_skills = filtered_skills[filtered_skills["Category"] == selected_category]
filtered_skills = filtered_skills[filtered_skills["Proficiency"] >= proficiency_threshold]

filtered_experience = experience.copy()
if selected_focus:
    filtered_experience = filtered_experience[filtered_experience["Focus"].isin(selected_focus)]

# ---------- Header ----------
st.markdown(
    f"""
    <div class="hero">
        <h1 style="margin-bottom: 0.25rem;">{profile['name']}</h1>
        <h3 style="margin-top: 0; font-weight: 500;">{profile['title']}</h3>
        <p style="margin-top: 0.8rem; max-width: 900px; font-size: 1.02rem;">{profile['tagline']}</p>
        <p style="margin-top: 0.75rem; font-size: 0.95rem; opacity: 0.95;">
            📍 {profile['location']} &nbsp;&nbsp; | &nbsp;&nbsp; 📧 {profile['email']} &nbsp;&nbsp; | &nbsp;&nbsp; 📞 {profile['phone']}<br>
            🔗 {profile['linkedin']}
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Top Metrics ----------
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
metric_col1.metric("Experiences", 3)
metric_col2.metric("Core Skills", len(skills))
metric_col3.metric("Highest Model Accuracy Lift", "0.76 → 0.91")
metric_col4.metric("Expected Graduation", "Jul 2026")

# ---------- Summary + Skills ----------
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.subheader("Professional Summary")
    st.markdown(
        """
        <div class="card">
            <p>Data scientist with experience spanning AML modeling, LLM systems, manufacturing AI, and retail analytics.</p>
            <p>Strong in machine learning, feature engineering, NLP/RAG workflows, and business-focused storytelling.</p>
            <p>Looking for roles where technical rigor and decision impact matter.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Technical Skills Table")
    render_html_table(
        filtered_skills.sort_values(["Category", "Proficiency"], ascending=[True, False])
    )

with right:
    st.subheader("Skill Tags")
    st.markdown(
        " ".join([f'<span class="pill">{s}</span>' for s in filtered_skills["Skill"].tolist()[:18]]),
        unsafe_allow_html=True,
    )

    st.subheader("Education")
    render_html_table(education)

# ---------- Chart Section ----------
st.subheader("Interactive Analytics View")
if chart_style == "Skill proficiency":
    chart_df = filtered_skills.sort_values("Proficiency", ascending=True)
    fig = px.bar(
        chart_df,
        x="Proficiency",
        y="Skill",
        color="Category",
        orientation="h",
        title="Skills by Self-Assessed Proficiency",
        text="Proficiency",
    )
    fig.update_layout(height=560, legend_title_text="Category", margin=dict(l=10, r=10, t=55, b=10))
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)
else:
    impact_df = filtered_experience.copy()
    impact_df["Display"] = impact_df["Company"] + " | " + impact_df["Focus"]
    fig = px.bar(
        impact_df,
        x="Impact_1",
        y="Display",
        color="Company",
        orientation="h",
        title="Selected Experience Highlights (Quantified Impact)",
        text="Impact_1",
    )
    fig.update_layout(height=500, margin=dict(l=10, r=10, t=55, b=10), xaxis_title="Impact (%)")
    fig.update_traces(textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

# ---------- Experience ----------
exp_col1, exp_col2 = st.columns([0.95, 1.05], gap="large")

with exp_col1:
    st.subheader("Work History Table")
    render_html_table(experience_table)

with exp_col2:
    st.subheader("Experience Highlights")
    if filtered_experience.empty:
        st.info("No experience items match the selected focus filters.")
    else:
        for _, row in filtered_experience.iterrows():
            st.markdown(f"<div class='card'><b>{row['Company']}</b> · {row['Role']}<br>", unsafe_allow_html=True)
            st.markdown(f"<span class='small-muted'>{row['Location']} · {row['Start']} to {row['End']} · {row['Focus']}</span>", unsafe_allow_html=True)
            st.markdown(row["Summary"])
            if show_metrics:
                extra = f"Primary impact: {row['Impact_1']}%"
                if row["Impact_2"]:
                    extra += f" | Secondary impact: {row['Impact_2']}%"
                st.caption(extra)
            st.markdown("</div>", unsafe_allow_html=True)

# ---------- Project Section ----------
if show_project:
    st.subheader("Featured Technical Project")
    for project in projects:
        st.markdown(
            f"""
            <div class="card">
                <b>{project['name']}</b><br>
                <span class="small-muted">{project['stack']}</span>
                <p style="margin-top: 0.6rem;">{project['summary']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- Footer ----------
st.markdown("---")
st.caption(
    "Built in Streamlit as an interactive resume with filtering controls, tables, and charts. "
    "Recommended run command: streamlit run app.py"
)
