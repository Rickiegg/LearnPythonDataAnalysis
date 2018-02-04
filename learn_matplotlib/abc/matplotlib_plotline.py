import numpy as np
import matplotlib.pyplot as plt

a = np.arange(10)

plt.plot(a, a * 1.5, 'go-', a, a * 2.5, 'rx', a, a * 3.5, '*', a, a * 4.5, 'b-.')
#如果不指定x轴，则默认以y轴元素下标作为x轴（0开始）
plt.show()
