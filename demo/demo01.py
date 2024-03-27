import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')

# 0から2πまでの範囲で等間隔に600個の点を作る
x = np.linspace(0, 2*np.pi, 600)

# サインとコサインの値を計算
sin_values = np.sin(x)
cos_values = np.cos(x)

# グラフを描画
plt.figure(figsize=(8, 6))
plt.plot(x, sin_values, label='sin(x)')
plt.plot(x, cos_values, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Curves')
plt.legend()
plt.grid()
plt.show()

# pip install matplotlib tkinter  -break-system-packages
