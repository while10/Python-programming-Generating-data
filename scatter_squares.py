import matplotlib.pyplot as plt

xvalue = list(range(1, 1000))
yvalue = [x**2 for x in xvalue]

#edgcolor='none'来消除轮廓

#plt.scatter(xvalue, yvalue, c=(0, 0, 0.8), edgecolors='none', s=40)#绘制单个点，并传递xy的坐标

#颜色渐变，用y轴作为渐变轴  蓝色作为渐变色
plt.scatter(xvalue, yvalue, c=yvalue, cmap=plt.cm.Blues, edgecolors='none', s=40)
#设置图标标题并给坐标轴加上标签
plt.title("Square Number", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("yvalue", fontsize=14)

#设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight') #第二个参数的意思是将多余的空白剪掉
plt.show()