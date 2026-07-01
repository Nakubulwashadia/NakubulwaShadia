#1-07-2026
#MORNING SESSION
#Matplotlib -> Is a python library for creating static, interactive and animated visualizations from data.
#It provides flexible and customizable plotting functions that help in understanding data patterns, trends and relationships effectively.

#matplotlip pyplot - is a module that is found within matplotlib that provides a MATLABfor makingplots.
#It simplifies the process of adding plot elements such as titles, labels, legends and gridlines to the plots.

#Steps to use Pyplot
#1 - import Matplotlib
#2 - create data
#3 - Plot data using plt.plot()
#4 - customize plot.Add titles, lables
#5 - Display the plot, we use plt.show()

#Basic Line graph

# import matplotlib.pyplot as plt

# x = [0,2,4,5,7,5]
# y = [0,4,6,7,8,10]

# fig,ax = plt.subplots()                          #fig represents the entire figure and ax means axes(represents where our figure passes ie the boundary of the graph)
# ax.plot (x,y,marker="o", label = "Data Points" )

# ax.set_title("Basic Line graph")
# ax.set_xlabel("X-Axis")
# ax.set_ylabel("Y-Axis")

# ax.legend()
# plt.plot(x,y)
# plt.show()


#Bar Graph
#Bar charts display categorical data using rectangula bars whose lengths are proportional to the values they represent.
#These are plotted vertically or horizontally to compare different categories.

#Simple Bar Chart

import matplotlib.pyplot as plt

# w = ['John', 'Peter', 'Ruth', 'Simon']
# z = [20,30,40,50]

# plt.bar(w,z)
# plt.title("Simple Bar Graph")
# plt.xlabel('Names of Students')
# plt.ylabel("Ages of the Students")

# plt.show()


#Histogram
#Pie chart

#Boxplot -> A simple graph that shows how data is spread out. 

# data = [[20,10,12,15,14,24],[8,9,12,13,14,15],[13,14,15,16,17,18,20]]
# plt.boxplot(data)
# plt.xlabel("Groups")
# plt.ylabel("Values")
# plt.title("Box Plot")

# plt.show()

#Scatter Plot
# x = [1,2,3,4,5]
# y= [2,3,5,7,11]
# fig,ax = plt.subplots()                          #fig represents the entire figure and ax means axes(represents where our figure passes ie the boundary of the graph)
# ax.scatter(x,y, color = 'green', marker="o")

# ax.set_title("Basic Scatter graph")
# ax.set_xlabel("X-Axis")
# ax.set_ylabel("Y-Axis")

# plt.show()


#Pie chart
# activities = ['reading', 'coding', 'sports', 'music']
# hours = [2,5,1,2]

# plt.figure (figsize=(6, 6))
# plt.pie(hours, labels=activities, autopct="%1.1f%%", startangle=90)
# plt.title("Pie Chart: Daily Activities")
# plt.tight_layout()
# plt.savefig('pie_chart_demo.png')
# plt.show()

#Histogram
ages = [18,19,19,20,21,21,22,23,23,24,25]
Student_name = ['rita','suzan','Grill','Akram','Roger','Zam','Sam','Patu','Mellow','Agness','Pingu']

plt.bar(Student_name, ages, color='pink', edgecolor='green')
plt.title('Student Ages')
plt.xlabel('Student Name')
plt.ylabel('Age')
plt.xticks(rotation=45)
plt.show()