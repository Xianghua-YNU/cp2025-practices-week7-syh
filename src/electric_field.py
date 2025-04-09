import numpy as np
import matplotlib.pyplot as plt

# 定义物理常数
COULOMB_CONSTANT = 8.99e9  # 库仑常数 (N·m²/C²)
POSITIVE_CHARGE = 1e-9  # 正点电荷电量 (C)
NEGATIVE_CHARGE = -1e-9  # 负点电荷电量 (C)

# 定义电荷位置
POSITIVE_CHARGE_POSITION = np.array([0.05, 0])
NEGATIVE_CHARGE_POSITION = np.array([-0.05, 0])

def compute_potential(x_grid, y_grid):
    """
    计算二维空间中每个点的电势
    :param x_grid: 二维网格的x坐标矩阵
    :param y_grid: 二维网格的y坐标矩阵
    :return: 电势矩阵
    """
    distance_to_positive = np.sqrt((x_grid - POSITIVE_CHARGE_POSITION[0]) ** 2 + (y_grid - POSITIVE_CHARGE_POSITION[1]) ** 2)
    distance_to_negative = np.sqrt((x_grid - NEGATIVE_CHARGE_POSITION[0]) ** 2 + (y_grid - NEGATIVE_CHARGE_POSITION[1]) ** 2)
    potential = COULOMB_CONSTANT * (POSITIVE_CHARGE / distance_to_positive + NEGATIVE_CHARGE / distance_to_negative)
    return potential

def compute_electric_field(potential_matrix, grid_spacing):
    """
    根据电势矩阵计算电场强度
    :param potential_matrix: 电势矩阵
    :param grid_spacing: 网格间距
    :return: 电场在x和y方向的分量
    """
    field_y, field_x = np.gradient(-potential_matrix, grid_spacing, grid_spacing)
    return field_x, field_y

def main_function():
    # 生成计算网格
    x_values = np.linspace(-0.2, 0.2, 100)
    y_values = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x_values, y_values)

    # 计算电势和电场
    potential = compute_potential(X, Y)
    dx = x_values[1] - x_values[0]
    electric_field_x, electric_field_y = compute_electric_field(potential, dx)

    plt.figure(figsize=(8, 6))

    # 自定义电势等高线的级别
    potential_levels = np.linspace(-500, 500, 20)

    # 绘制电势等高线图
    contour_plot = plt.contourf(X, Y, potential, levels=potential_levels, cmap='RdBu_r')
    plt.clim(-500, 500)  # 限制颜色映射范围

    plt.colorbar(label='Electric Potential (V)')

    # 绘制电场线
    plt.streamplot(X, Y, electric_field_x, electric_field_y, color='k', density=1.2)

    # 添加坐标轴标签和标题
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Electric Field and Potential of an Electric Dipole')

    # 标记正负电荷位置
    plt.plot(POSITIVE_CHARGE_POSITION[0], POSITIVE_CHARGE_POSITION[1], 'ro', label='Positive Charge')
    plt.plot(NEGATIVE_CHARGE_POSITION[0], NEGATIVE_CHARGE_POSITION[1], 'bo', label='Negative Charge')

    # 显示图例
    plt.legend()

    # 设置坐标轴比例相等
    plt.axis('equal')

    # 显示网格线
    plt.grid(True)

    # 显示图形
    plt.show()

if __name__ == "__main__":
    main_function()    
