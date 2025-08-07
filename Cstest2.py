from arc import Cesium
import numpy as np

atom = Cesium()

# 定义量子数 (7S1/2 -> 14P3/2 跃迁)
##n1, l1, j1 = 7, 0, 0.5  # 初态 6S1/2
##n2, l2, j2 = 14, 1, 1.5  # 末态 6P3/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 0.5
##mj2 = 1.5
##q = 1
# 定义量子数 (7S1/2 -> 22P3/2 跃迁)
n1, l1, j1 = 7, 0, 0.5  # 初态 6S1/2
n2, l2, j2 = 22, 1, 1.5  # 末态 6P3/2

waist = 50.0e-6  # 50 m um
P = 1000.0e-3  # 500 mW

mj1 = 0.5
mj2 = 1.5
q = 1
# 定义量子数 (22P3/2 -> 23S1/2 跃迁)
##n1, l1, j1 = 22, 1, 1.5  # 初态 6S1/2
##n2, l2, j2 = 23, 0, 0.5  # 末态 6P3/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 1.5
##mj2 = 0.5
##q = -1
# 定义量子数 (14P3/2 -> 13D5/2 跃迁)
##n1, l1, j1 = 14, 1, 1.5  # 初态 6S1/2
##n2, l2, j2 = 13, 2, 2.5  # 末态 6P3/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 1.5
##mj2 = 2.5
##q = 1
# 定义量子数 (6P3/2 -> 7S1/2 跃迁)
##n1, l1, j1 = 6, 1, 1.5  # 初态 6S1/2
##n2, l2, j2 = 7, 0, 0.5  # 末态 6P3/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 1.5
##mj2 = 0.5
##q = -1
# 定义量子数 (23S1/2 -> 6P3/2 跃迁)
##n1, l1, j1 = 23, 0, 0.5  # 初态 6S1/2
##n2, l2, j2 = 6, 1, 1.5  # 末态 6P3/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 0.5
##mj2 = 1.5
##q = 1
# Light Polarisation (sigma+)
##n1, l1, j1 = 6, 1, 1.5  # 初态 6P3/2
##n2, l2, j2 = 7, 0, 0.5  # 末态 7S1/2
##
##waist = 50.0e-6  # 50 m um
##P = 1000.0e-3  # 500 mW
##
##mj1 = 1.5
##mj2 = 0.5
##q = -1

rabiFreq = atom.getRabiFrequency(n1, l1, j1, mj1, n2, l2, j2, q, P, waist)
print(f"拉比频率: {rabiFreq/1e9:.2f} GHz")

# 计算跃迁波长（单位：米）
wavelength = atom.getTransitionWavelength(n1, l1, j1, n2, l2, j2)
print(f"谱线波长: {wavelength*1e9:.2f} nm")  # 转换为纳米

d_reduced = atom.getDipoleMatrixElement(n1, l1, j1, mj1, n2, l2, j2, mj2, q)
print(f"约化偶极矩阵元: {d_reduced*2:.6f} ea₀")



