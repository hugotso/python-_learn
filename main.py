# 导入所需的库
from sympy import symbols, Eq, solve

# 创建符号变量
N = symbols('N')

# 定义方程
equation = Eq(148, 10 * (N/110) * (365/365))

# 求解方程
solution = solve(equation, N)

# 输出解
print("解N的值为：", solution)

