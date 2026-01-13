<<<<<<< HEAD
print("Hello World")
=======
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Real-Time Anomaly Detection",
    layout="wide",
)

# -----------------------------
# CUSTOM CSS (Dark Dashboard)
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.metric-box {
    background-color: #161b22;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
.alert-critical { color: red; font-weight: bold; }
.alert-warning { color: orange; font-weight: bold; }
.alert-normal { color: lightgreen; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/simulated/system_metrics.csv")

df = load_data()

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
st.sidebar.title("⚙️ Control Panel")

window_size = st.sidebar.slider("Sliding Window Size", 10, 100, 50)
threshold = st.sidebar.slider("Anomaly Threshold", 0.5, 5.0, 2.0)
refresh_rate = st.sidebar.slider("Refresh Rate (sec)", 1, 5, 1)

st.sidebar.markdown("---")
st.sidebar.checkbox("Enable Normalization", value=True)
st.sidebar.checkbox("Enable Gradient Clipping", value=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("## 🧠 Real-Time System Anomaly Detection (LSTM)")
st.markdown("**Status:** 🟢 Model Running &nbsp;&nbsp; | &nbsp;&nbsp; **Latency:** ~120 ms")

# -----------------------------
# METRIC CARDS
# -----------------------------
latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Usage (%)", f"{latest.cpu:.2f}")

with col2:
    st.metric("Memory Usage (%)", f"{latest.memory:.2f}")

with col3:
    st.metric("Network I/O (MB/s)", f"{latest.network:.2f}")

# -----------------------------
# LIVE METRICS PLOT
# -----------------------------
st.markdown("### 📈 Live System Metrics")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["cpu"], label="CPU")
ax.plot(df["memory"], label="Memory")
ax.plot(df["network"], label="Network")
ax.legend()
ax.set_xlabel("Time")
ax.set_ylabel("Value")

st.pyplot(fig)

# -----------------------------
# ANOMALY SCORE (SIMULATED)
# -----------------------------
# (Later replaced with LSTM reconstruction error)
df["anomaly_score"] = (
    np.abs(df.cpu - df.cpu.mean()) +
    np.abs(df.memory - df.memory.mean()) +
    np.abs(df.network - df.network.mean())
) / 100

# -----------------------------
# ANOMALY DETECTION PLOT
# -----------------------------
st.markdown("### 🚨 Anomaly Detection")

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.plot(df["anomaly_score"], label="Anomaly Score")
ax2.axhline(threshold, color="red", linestyle="--", label="Threshold")

anomalies = df[df.anomaly_score > threshold]
ax2.scatter(
    anomalies.index,
    anomalies.anomaly_score,
    color="red",
    label="Detected Anomaly",
    s=10
)

ax2.legend()
ax2.set_xlabel("Time")
ax2.set_ylabel("Score")

st.pyplot(fig2)

# -----------------------------
# ALERT PANEL
# -----------------------------
st.markdown("### 🔔 Alerts")

if len(anomalies) > 0:
    last = anomalies.iloc[-1]
    st.markdown(
        f"<div class='alert-critical'>🔴 CRITICAL: Anomaly detected at time {int(last.time)} | Score: {last.anomaly_score:.2f}</div>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<div class='alert-normal'>🟢 System operating normally</div>",
        unsafe_allow_html=True
    )

# -----------------------------
# OPTIMIZATION ANALYSIS (PLACEHOLDER)
# -----------------------------
st.markdown("### 🧪 Optimization & Gradient Analysis")

loss = np.exp(-np.linspace(0, 5, 100)) + np.random.normal(0, 0.02, 100)
gradients = np.exp(-np.linspace(0, 6, 100))

fig3, ax3 = plt.subplots(1, 2, figsize=(12, 4))

ax3[0].plot(loss)
ax3[0].set_title("Loss vs Epochs")
ax3[0].set_xlabel("Epoch")
ax3[0].set_ylabel("Loss")

ax3[1].plot(gradients)
ax3[1].set_title("Gradient Norms (Vanishing Effect)")
ax3[1].set_xlabel("Epoch")
ax3[1].set_ylabel("Gradient Norm")

st.pyplot(fig3)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown("🎓 Final Year Project | LSTM-Based Real-Time Anomaly Detection")
>>>>>>> e664cf7 (app.py update)
