"""SCI 论文常用配色方案（HEX 色值）。

用法:
    import matplotlib.pyplot as plt
    from palettes import PALETTES
    plt.rcParams["axes.prop_cycle"] = plt.cycler(color=PALETTES["okabe_ito"])
"""

PALETTES = {
    "npg": ["#E64B35", "#4DBBD5", "#00A087", "#3C5488", "#F39B7F",
            "#8491B4", "#91D1C2", "#DC0000", "#7E6148", "#B09C85"],
    "aaas": ["#3B4992", "#EE0000", "#008B45", "#631879", "#008280",
             "#BB0021", "#5F559B", "#A20056", "#808180", "#1B1919"],
    "nejm": ["#BC3C29", "#0072B5", "#E18727", "#20854E",
             "#7876B1", "#6F99AD", "#FFDC91", "#EE4C97"],
    "lancet": ["#00468B", "#ED0000", "#42B540", "#0099B4", "#925E9F",
               "#FDAF91", "#AD002A", "#ADB6B6", "#1B1919"],
    "jama": ["#374E55", "#DF8F44", "#00A1D5", "#B24745",
             "#79AF97", "#6A6599", "#80796B"],
    "okabe_ito": ["#000000", "#E69F00", "#56B4E9", "#009E73",
                  "#F0E442", "#0072B2", "#D55E00", "#CC79A7"],
    "tol_bright": ["#4477AA", "#EE6677", "#228833", "#CCBB44",
                   "#66CCEE", "#AA3377", "#BBBBBB"],
    "tol_muted": ["#332288", "#88CCEE", "#44AA99", "#117733", "#999933",
                  "#DDCC77", "#CC6677", "#882255", "#AA4499", "#DDDDDD"],
    "tol_high_contrast": ["#004488", "#DDAA33", "#BB5566"],
}
