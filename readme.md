# 用于处理物联网专业综合课程设计实验一的数据
# 流程
- 隔行读入数据（字符串16进制）
- 将16进制字符串转化为数组（二进制）
- 将二进制计算补码
- 转化为10进制存为数组
- 与距离成为关系并拟合
- 剔除坏值

# 问题
- 处理订单数据到底是什么，要不要求原码？------做判断，是否转源码。
- 拟合曲线函数------已解决
- 生成距离与功率的模型，即给定功率可以得到计算距离------已解决
- 如何剔除坏值-------已解决



# 思路

先针对不同节点采用大量数据训练模型，得到模型再进行定位验证模型。