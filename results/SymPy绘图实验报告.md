# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：
- 成员：
- 实验日期：

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法


分别说明三个问题的具体绘图方法和使用的函数接口。

问题 1：使用plot函数，定义符号变量x，绘制函数cos(tan(πx))，选择x∈(-1,1)避开间断点以展示曲线形态。

问题 2：通过plot_implicit函数，定义x、y，绘制隐函数e^y + cosx/x + y = 0，设置x∈(-5,5)（避开x=0）、y∈(-5,5)。

问题 3：利用plot3d_parametric_surface函数，定义参数u、v的参数方程（如球面 / 环面方程），设置参数范围（如u,v∈[0,2π]）绘制三维曲面。

---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

![s1](https://github.com/user-attachments/assets/91d56e00-e524-45ec-9bd5-7155da58829b)

### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

![s2](https://github.com/user-attachments/assets/c223dd1b-0214-4fbd-b89d-5b50653b175e)

### 问题3: 参数曲面绘制结果

![s3](https://github.com/user-attachments/assets/5816a86b-a528-4dad-93f4-d237e2bf4293)

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？

学会plot（显式曲线）、plot_implicit（隐函数曲线）、plot3d_parametric_surface（参数曲面）的使用，能根据函数特性调整变量范围。

- 实验中你遇到了哪些问题？如何解决？

函数间断点导致图像异常，通过缩小变量范围避开；参数曲面初始方程设置不当，通过查阅资料调整参数范围解决。

- 你对SymPy的绘图功能有什么建议或意见？

希望增加绘图自定义选项（颜色、样式等）和提升复杂函数绘图效率。
