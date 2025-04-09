import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置


def calculate_potential(X, Y):
    r_pos = np.sqrt((X - pos_charge_pos[0]) ** 2 + (Y - pos_charge_pos[1]) ** 2)
    r_neg = np.sqrt((X - neg_charge_pos[0]) ** 2 + (Y - neg_charge_pos[1]) ** 2)
    V = k * (q_pos / r_pos + q_neg / r_neg)
    return V


def calculate_electric_field(V, spacing):
    Ey, Ex = np.gradient(V, spacing)
    Ex = -Ex
    Ey = -Ey
    return Ex, Ey


def main():
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)

    # 调用计算函数并绘制结果
    V = calculate_potential(X, Y)
    dx = x[1] - x[0]
    Ex, Ey = calculate_electric_field(V, dx)

    plt.figure(figsize=(8, 6))
    # 绘制电势图
    plt.contourf(X, Y, V, levels=50, cmap='viridis')
    plt.colorbar(label='电势 (V)')

    # 绘制电场线
    plt.streamplot(X, Y, Ex, Ey, color='k', linewidth=0.5, density=1.5)

    # 添加必要的标签、图例和标题
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('电偶极子的电势分布和电场线')
    plt.show()


if __name__ == "__main__":
    main()
