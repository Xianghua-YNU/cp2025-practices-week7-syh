import sympy as sp
from sympy.plotting import plot, plot_implicit, plot3d_parametric_surface


# 绘制 cos(tan(pi*x)) 函数曲线
def draw_function_curve():
    x = sp.symbols('x')
    function = sp.cos(sp.tan(sp.pi * x))
    plot(function, (x, -1, 1), xlabel='x', ylabel='y',
         title='Plot of cos(tan(pi*x))')


# 绘制隐函数曲线 e^y + cos(x)/x + y = 0
def draw_implicit_curve():
    x, y = sp.symbols('x y')
    implicit_function = sp.exp(y) + sp.cos(x) / x + y
    plot_implicit(implicit_function, (x, 0.1, 10), (y, -10, 10),
                  xlabel='x', ylabel='y',
                  title='Implicit plot of exp(y)+cos(x)/x+y=0',
                  points=500)


# 绘制参数曲面
def draw_parametric_surface():
    s, t = sp.symbols('s t')
    x_expr = sp.exp(-s) * sp.cos(t)
    y_expr = sp.exp(-s) * sp.sin(t)
    z_expr = t
    plot3d_parametric_surface(x_expr, y_expr, z_expr, (s, 0, 8), (t, 0, 5 * sp.pi),
                              xlabel='x', ylabel='y', zlabel='z',
                              title='Parametric Surface Plot')


if __name__ == "__main__":
    draw_function_curve()
    draw_implicit_curve()
    draw_parametric_surface()
