from die import Die
import pygal

#创建一个D6
die_6 = Die(6)
die_10 = Die(10)
results = []
for roll_num in range(1000):
    result = die_6.roll() + die_10.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1, die_6.num_sides+die_10.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)


#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6+D10 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6',7,8,9,10,11,12,13,14,15,16]
hist.x_title = "Result"
hist.y_title = "Frequencies of Result"

hist.add('D6+D10', frequencies)
hist.render_to_file('die_visual.svg')