import streamlit as st

st.set_page_config(
    page_title="FeedSure",
    page_icon="🌾"
)

st.title("🌾 FeedSure")

st.subheader(
    "Smart AI-Enabled Rapid Feed & Silage Quality Assessment System"
)

st.divider()

st.header("📷 Upload Feed / Silage Sample")

uploaded_file = st.file_uploader(
    "Upload an image of the feed or silage",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="Uploaded Sample",
        width=400
    )

st.header("📊 Sample Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    moisture = st.number_input(
        "Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

with col2:
    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=4.2
    )

with col3:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=28.0
    )

st.divider()

if st.button("🔍 Analyze Sample"):

    score = 100

    if moisture > 70:
        score -= 20

    if ph > 5:
        score -= 20

    if temperature > 35:
        score -= 15

    if score >= 80:
        status = "🟢 SAFE"
        risk = "LOW"
        advice = "Sample appears suitable based on the entered prototype parameters."

    elif score >= 60:
        status = "🟡 ALERT"
        risk = "MEDIUM"
        advice = "Further inspection and monitoring are recommended."

    else:
        status = "🔴 HIGH RISK"
        risk = "HIGH"
        advice = "Further laboratory testing is recommended before use."

    st.divider()

    st.header("🤖 FeedSure Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Quality Score", f"{score}/100")

    with col2:
        st.metric("Status", status)

    with col3:
        st.metric("Risk Level", risk)

    st.subheader("🧑‍🌾 Farmer Advisory")

    st.info(advice)

    st.caption(
        "Prototype demonstration only. "
        "The scoring rules are illustrative and not validated "
        "for real-world feed safety decisions."
    )
