# SCI 论文绘图指南：配色方案 + 绘图规范

一份面向 SCI 论文作者的科研绘图资源整理，包含**期刊风格配色方案**（含十六进制色值）与**主流期刊的图片投稿规范**，并附常用工具与学习资源链接（均已验证有效）。

## 目录

- [配色方案](docs/配色方案.md) — 期刊风格配色（NPG / AAAS / NEJM / Lancet / JAMA）、色盲友好配色（Okabe-Ito、Paul Tol）、连续型科学色图等
- [期刊绘图规范](docs/期刊绘图规范.md) — Nature、Science、Elsevier、PLOS 等期刊对图片尺寸、分辨率、字体、格式的要求
- [工具与资源清单](docs/工具与资源.md) — Python / R 绘图配色包、在线配色工具、学习资料
- [`palettes/`](palettes/) — 可直接使用的配色文件（Python 字典 / JSON）

## 快速使用

Python（Matplotlib）：

```python
import json
import matplotlib.pyplot as plt

with open("palettes/palettes.json") as f:
    palettes = json.load(f)

plt.rcParams["axes.prop_cycle"] = plt.cycler(color=palettes["npg"])
```

R（ggplot2）：

```r
# install.packages("ggsci")
library(ggsci)
ggplot(df, aes(x, y, color = group)) + geom_point() + scale_color_npg()
```

## 核心原则（TL;DR）

1. **色盲友好**：约 8% 男性存在红绿色觉障碍，避免红绿对比，优先使用 Okabe-Ito 或 Paul Tol 配色。
2. **矢量优先**：线图、散点图导出 PDF/EPS/SVG；照片类图像用 TIFF/PNG（≥300 dpi，线图 ≥600–1200 dpi）。
3. **避免彩虹色图（jet）**：连续数据使用感知均匀的色图（viridis、cividis、Crameri 的 batlow 等）。
4. **字体统一**：常用 Arial / Helvetica，最终版面字号 5–8 pt（视期刊要求），全文各图保持一致。
5. **按期刊栏宽作图**：单栏约 85–90 mm，双栏约 170–180 mm，避免投稿后被缩放导致字太小。
