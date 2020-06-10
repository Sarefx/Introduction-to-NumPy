import numpy as np

# print(np.__version__)

gpas_as_list = [4.0, 3.286, 3.5]

gpas_as_list.append(4.0)

gpas_as_list.insert(1, "whatever")

gpas_as_list.pop(1)

gpas = np.array(gpas_as_list)

# in Jupyter you can use something like ?gpas to see all documentation

len(gpas)
gpas.size
gpas.nbytes

study_minutes = np.zeros(100)

study_minutes = np.zeros(100, np.uint16)

study_minutes[0] = 150

study_minutes[1] = 60

study_minutes[2:6] = [80, 60, 30, 90]

students_gpas = np.array([
    [4.0, 3.286, 3.5, 4.0],
    [3.2, 3.8, 4.0, 4.0],
    [3.96, 3.92, 4.0, 4.0]
], np.float16)

print(students_gpas)

students_gpas[1][2]

study_minutes = np.array([
    study_minutes,
    np.zeros(100, np.uint16)
])

print(study_minutes)

study_minutes[1][0] = 60

# study_minutes[1][0] is the same as study_minutes[1, 0]

rand = np.random.RandomState(42)  # will generate the same sequence of numbers as long as you use the same seed value

fake_log = rand.randint(30,180, size=100, dtype=np.uint16)

print(fake_log)

[fake_log[3],fake_log[8]]

fake_log[[3,8]]

study_minutes = np.append(study_minutes, [fake_log], axis=0)

study_minutes[1,1] = 360

fake_log < 60  # prints boolean statement based on the condition

np.array([False,True,True]) & np.array([True, False, True])  # checks the condition and the result is [False False  True]

study_minutes[(study_minutes < 60) & (study_minutes > 0)]  # will return values that are less than 60 and greater than 0

study_minutes[study_minutes < 60] = 0  # will set values less than 60 to 0

# comparing arrays need to use & to compare each value "and" will compare the whole array and most likely wont work

fruit = ["apple","banana","cherry","durian"]

fruit[1:2]  # will return banana
fruit[1:3]  # will return banana and cherry
fruit[:3]  # will return apple, banana and cherry
fruit[3:]  # will return durian
fruit[:]  # will return a copy of the list
fruit[::2]  # second colon represents a step. This will return apple and cherry
fruit[::-1]  # will return a reverse copy of the list

np.arange(20)  # will return all values up to 20

practice = np.arange(42)
practice.shape = (7,6)  # creates a matrix with 7 rows and 6 columns
print(practice)
practice[2:5]  # returns a sliced matrix with 3,4,5 row
practice[2:5, 3]  # returns a sliced matrix with 3,4,5 row, but only 4 column
practice[2:5, 3:]  # returns a sliced matrix with 3,4,5 row, but only columns starting with 4
not_copied = practice[:]  # this will create a view of practice matrix
print(not_copied)
#original_value = practice[0][0]
practice[0][0] = 99
print(not_copied) # this will return a view of practice matrix
#practice[0][0] = original_value
practice.base is None  # will return True
not_copied.base is None  # will return False
not_copied is practice  # will return True
practice.flags['OWNDATA']  # will return True
not_copied.flags['OWNDATA']  # will return False

practice_view = practice.reshape(3,14)  # creating a view with 3 rows and 14 columns
# reshape is great because we save space by redefining a matrix without taking extra space
practice.reshape(-1,2).shape  # will return (21,2)
practice.ravel()  # will return a single dimension view of the matrix.

# if you are using Jupyterm you can use a ? at the end of a function to get its documentation, like np.ravel?
# to find a documentation use np.lookfor("appending")

orders = np.array([
    [2,0,0,0],
    [4,1,2,2],
    [0,1,0,1],
    [6,0,1,2]
])
totals = np.array([3,20.50,10,14.25])
prices = np.linalg.solve(orders,totals)  # will return ([1.5, 8. , 1.25, 2. ])
# 2 * 1.5 = 3
# (4 * 1.5) + (1 * 8) + (2 * 1.25) + (2 * 2) = 20.5
# (1 * 8) + (1 * 2) = 10
# (6 * 1.5) + (1 * 1.25) + (2 * 2) = 14.25

orders @ prices  # will return ([3,20.50,10,14.25]) aka totals
orders.dot(prices)  # same as the line above

a, b = np.split(np.arange(1,11),2)

a + b  # will return ([7,9,11,13,15])
a - b
b - a
a * b
a + 2
a + np.repeat(2, 5)

students_gpas.mean()  # will return an average of all values
students_gpas.mean(axis=1)  # will return an average of each row

np.add.reduce(study_minutes[0])  # will add up all numbers in the array
np.add.accumulate(study_minutes[0])  # will add up all numbers in the array with the steps shown
np.sum(study_minutes[0])  # will add up all numbers in the array
np.sum(study_minutes, axis=1)  # same as the line above

import matplotlib.pyplot as plt

plt.boxplot(students_gpas.T)  # the .T will transpose the array so it shows up correctly on the graph
#plt.show()

plt.hist(study_minutes[study_minutes > 0])
plt.plot()
plt.show()
