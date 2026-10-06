import numpy as np
import pandas as pd
import streamlit as st

st.title("09 - streamlit")
st.write("If you can read this, srvm launched the app on port 8501.")

points = st.slider("sample points", 10, 500, 100)
rng = np.random.default_rng(7)
data = pd.DataFrame(
    {"x": np.linspace(0, 10, points), "y": np.linspace(0, 10, points) ** 1.5 + rng.normal(0, 3, points)}
)
st.line_chart(data, x="x", y="y")
