import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="FeedSure",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------

st.title("🌾 FeedSure")

st.subheader(
    "Smart AI-Enabled Rapid Feed & Silage Quality Assessment System"
)

st.divider()

# -----------------------------
# Feed type
# -----------------------------

st.header("🐄 Feed Information")

feed_type = st.selectbox(
    "Select Feed Type",
    [
        "Silage",
        "Hay",
        "Green Fodder",
        "Concentrate Feed"
    ]
)

# -----------------------------
# Image upload
# -----------------------------

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

# -----------------------------
# Sample parameters
# -----------------------------

st.header("📊 Sample Parameters")

col1, col2, col3 = st.columns(3)

with col1:

    moisture = st.number_input(
        "Moisture (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )

with col2:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=4.2,
        step=0.1
    )

with col3:

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=28.0,
        step=1.0
    )

# -----------------------------
# Additional observations
# -----------------------------

st.subheader("🔍 Visual & Sensory Observations")

col4, col5 = st.columns(2)

with col4:

    odor = st.selectbox(
        "Odour",
        [
            "Normal",
            "Sour",
            "Musty",
            "Moldy",
            "Alcoholic"
        ]
    )

with col5:

    appearance = st.selectbox(
        "Visual Appearance",
        [
            "Green / Olive",
            "Golden / Yellow",
            "Light Brown",
            "Dark Brown / Black",
            "Visible Mold"
        ]
    )

st.divider()

# -----------------------------
# Analysis
# -----------------------------

if st.button(
    "🔍 Analyze Sample",
    type="primary"
):

    score = 100

    risk_factors = []
    positive_factors = []

    # Moisture analysis

    if moisture > 70:

        score -= 20

        risk_factors.append(
            "High moisture level"
        )

    elif moisture < 45:

        score -= 10

        risk_factors.append(
            "Low moisture level"
        )

    else:

        positive_factors.append(
            "Moisture within prototype target range"
        )

    # pH analysis

    if ph > 5:

        score -= 20

        risk_factors.append(
            "Elevated pH"
        )

    elif ph < 3.5:

        score -= 10

        risk_factors.append(
            "Very low pH"
        )

    else:

        positive_factors.append(
            "pH within prototype target range"
        )

    # Temperature analysis

    if temperature > 35:

        score -= 15

        risk_factors.append(
            "Elevated temperature"
        )

    else:

        positive_factors.append(
            "Temperature acceptable"
        )

    # Odour analysis

    if odor == "Moldy":

        score -= 25

        risk_factors.append(
            "Mold-associated odour"
        )

    elif odor == "Musty":

        score -= 15

        risk_factors.append(
            "Musty odour"
        )

    elif odor == "Alcoholic":

        score -= 10

        risk_factors.append(
            "Alcoholic odour"
        )

    else:

        positive_factors.append(
            "No major odour warning"
        )

    # Appearance analysis

    if appearance == "Visible Mold":

        score -= 30

        risk_factors.append(
            "Visible mold detected"
        )

    elif appearance == "Dark Brown / Black":

        score -= 15

        risk_factors.append(
            "Dark / abnormal appearance"
        )

    else:

        positive_factors.append(
            "No major visual warning"
        )

    # Keep score between 0 and 100

    score = max(0, min(score, 100))

    # -------------------------
    # Risk classification
    # -------------------------

    if score >= 80:

        status = "🟢 SAFE"
        risk = "LOW"

        advice = (
            "Sample passes the prototype screening rules. "
            "Maintain proper storage and continue periodic monitoring."
        )

    elif score >= 60:

        status = "🟡 ALERT"
        risk = "MEDIUM"

        advice = (
            "Some warning parameters were detected. "
            "Inspect the sample and monitor storage conditions."
        )

    else:

        status = "🔴 HIGH RISK"
        risk = "HIGH"

        advice = (
            "Multiple warning parameters were detected. "
            "Further inspection and laboratory confirmation "
            "are recommended before use."
        )

    # -------------------------
    # Results
    # -------------------------

    st.divider()

    st.header("🤖 FeedSure Assessment")

    col6, col7, col8 = st.columns(3)

    with col6:

        st.metric(
            "Quality Score",
            f"{score}/100"
        )

    with col7:

        st.metric(
            "Status",
            status
        )

    with col8:

        st.metric(
            "Risk Level",
            risk
        )

    # -------------------------
    # Parameter analysis
    # -------------------------

    st.subheader("📋 Parameter Check")

    if positive_factors:

        for item in positive_factors:

            st.success(
                "✓ " + item
            )

    if risk_factors:

        for item in risk_factors:

            st.warning(
                "⚠ " + item
            )

    # -------------------------
    # Farmer advisory
    # -------------------------

    st.subheader("🧑‍🌾 Farmer Advisory")

    st.info(advice)

    # -------------------------
    # Prototype disclaimer
    # -------------------------

    st.caption(
        "Prototype demonstration only. "
        "The scoring rules are illustrative and are not "
        "validated for real-world feed safety decisions."
    )
