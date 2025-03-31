# plotHeader.py ====================================================================================================================
#
# Header with defaults for matplotlib
#
# © 2025 Matt Lenahan ==============================================================================================================

# Header ---------------------------------------------------------------------------------------------------------------------------
# Imports
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

# Figure defaults
plt.rcParams['figure.figsize']                = [6, 5]  # Inches
plt.rcParams['figure.dpi']                    = 118  # 118 dpi is 1:1 scaling on 25" monitor
plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['text.usetex']                   = True
plt.rcParams['font.size']                     = 14
plt.rcParams['grid.color']                    = '#002147'
plt.rcParams['grid.alpha']                    = 0.25
plt.rcParams['grid.linewidth']                = 0.5
plt.rcParams['axes.grid']                     = True

# Colourmap
nColours = 5
cmap = plt.get_cmap('plasma', nColours)
plt.rcParams['axes.prop_cycle'] = (cycler('color', cmap(np.linspace(0.0, 1.0, nColours))))