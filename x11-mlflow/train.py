"""Log one demo run into ./mlruns so `mlflow ui` opens with a populated
experiment list instead of empty tables.

    python train.py   # once, then `mlflow ui` (or `srvm`)
"""

import mlflow

mlflow.set_experiment("srvm-fixture-x11")

with mlflow.start_run(run_name="demo-run"):
    mlflow.log_param("model", "toy-linear")
    mlflow.log_param("features", 2)
    for epoch in range(10):
        mlflow.log_metric("loss", 1.0 / (epoch + 1), step=epoch)
    mlflow.log_metric("final_rmse", 0.12)

print("logged one run to ./mlruns — start `mlflow ui` (or `srvm`) to see it")
