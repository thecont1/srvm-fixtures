import numpy as np
from fastapi import FastAPI

rng = np.random.default_rng(7)
xs = rng.uniform(-3.0, 3.0, 64)
ys = 2.0 * xs - 1.0 + rng.normal(0.0, 0.1, 64)
slope, intercept = np.polyfit(xs, ys, 1)
rmse = float(np.sqrt(np.mean((slope * xs + intercept - ys) ** 2)))
print(f"trained toy model: y = {slope:.3f}x + {intercept:.3f} (rmse {rmse:.3f})")

app = FastAPI()


@app.get("/predict")
def predict(x: float):
    return {"x": x, "y": slope * x + intercept}
