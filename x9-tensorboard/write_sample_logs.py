"""Write a few scalar curves into logs/ so `tensorboard --logdir logs`
opens with real data instead of an empty dashboard.

    python write_sample_logs.py
"""

import math

from tensorboardX import SummaryWriter

writer = SummaryWriter(logdir="logs")
for step in range(100):
    writer.add_scalar("train/loss", math.exp(-step / 25.0) + 0.05, step)
    writer.add_scalar("train/accuracy", 1.0 - math.exp(-step / 30.0), step)
writer.close()
print("wrote sample events to logs/ (run `tensorboard --logdir logs` or `srvm`)")
