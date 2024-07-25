from vis.visdom_cus import Visdom
import torch

vis = Visdom(1, visdom_info={"port": 8088})

for i in range(10):
    a = torch.randn(1, 4, 4)
    vis.register(a, mode="heatmap", debug_level=1, title="test1")
    b = torch.randn(1, 4, 4)
    vis.register(b, mode="heatmap", debug_level=1, title="test2")
