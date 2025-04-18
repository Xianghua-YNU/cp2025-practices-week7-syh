# 实验报告 - Pandas 数据操作练习

## 一、实验目的
阐述本次实验的主要目的，可参考任务目的部分。

掌握 Pandas 数据处理全流程：读取、清洗、统计分析、可视化、保存，处理编码及缺失值问题。
## 二、实验步骤
详细描述你完成每个任务的步骤和方法，可结合代码进行说明。

### 任务 1: 读取数据
说明你使用的读取数据的函数和过程。

用pd.read_csv()

由于文件可能存在编码问题（如非 UTF-8 编码），先通过 chardet 库检测文件实际编码，再指定编码参数读取。
### 任务 2: 查看数据基本信息
描述如何查看数据的基本信息。

用data.info()查看列名、数据类型、非空值数。
### 任务 3: 处理缺失值
说明你找出缺失值列和填充缺失值的方法。

检测缺失值：通过 data.isnull().any() 找出存在缺失值的列。

填充缺失值：对数值型列（使用 pd.api.types.is_numeric_dtype 检测），用该列均值填充缺失值。
### 任务 4: 数据统计分析
说明你计算数值列均值、中位数和标准差的方法。

对数值型列（通过 select_dtypes(include=['number']) 筛选）计算均值、中位数、标准差。
### 任务 5: 数据可视化
描述你选择的数值列和绘制直方图的过程。

选择 “成绩” 列，使用 plot.hist() 绘制直方图，通过 Matplotlib 显示。
### 任务 6: 数据保存
说明你保存处理后数据的方法。

使用 to_csv() 函数将处理后的数据保存为新文件，不保留索引列。
## 三、实验结果
展示每个任务的结果，可使用表格或图表进行呈现。

### 任务 1: 读取数据
展示读取的数据的基本信息（如列名、行数等）。

数据基本信息：
行数：5 行
列名：姓名、年龄、成绩、城市
数据类型：2 个数值型列（年龄、成绩），2 个字符型列（姓名、城市）
### 任务 2: 查看数据基本信息
粘贴数据的基本信息输出。
![image](https://github.com/user-attachments/assets/51442b3d-4cd3-4fc5-b9c2-acddfafc8377)

### 任务 3: 处理缺失值
说明处理后缺失值的情况。

处理前 “年龄” 列有 1 个缺失值（NaN），处理后使用均值（26.25）填充，该列无缺失值
### 任务 4: 数据统计分析
列出数值列的均值、中位数和标准差。
![image](https://github.com/user-attachments/assets/fb19dbb2-81d4-4b5d-affb-b2f004f0812b)

### 任务 5: 数据可视化

![p1](https://github.com/user-attachments/assets/c23a35e4-c74b-4dbe-b0dd-f564c8a6905c)

### 任务 6: 数据保存
说明保存的文件路径和文件名。

保存文件：processed_data.csv

路径：当前工作目录（与代码文件同目录），包含处理后无缺失值的完整数据
## 四、总结
总结本次实验的收获和体会，分析遇到的问题及解决方法，对 Pandas 数据操作的理解和认识。

收获：掌握 Pandas 核心操作，解决路径、编码、依赖库问题。

问题与解决：
文件不存在→确认路径，用绝对路径。
编码错误→chardet检测编码（如 GBK），指定正确编码读取。
库缺失→pip install chardet安装。

理解：Pandas 高效处理数据，需结合业务选择清洗策略，重视细节（路径、编码）避免错误。
