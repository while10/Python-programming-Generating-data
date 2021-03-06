import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #创建一个randomwork实例，并将其包含的多有的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    #绘制窗口的大小
    plt.figure(figsize=(10, 6))

    point_number = list(range(rw.num_point))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, s=1)

    #突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=15)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=15)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # keep_running = input("Make another walk? y/n")
    # if keep_running == 'n':
    break