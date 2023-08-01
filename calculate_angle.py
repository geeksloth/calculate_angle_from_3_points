import math
import numpy as np
import matplotlib.pyplot as plt


def calculate_angle(p1x, p1y, p2x, p2y, p3x, p3y):
    a = math.dist([p2x,p2y], [p3x,p3y])
    b = math.dist([p1x,p1y], [p2x,p2y])
    c = math.dist([p1x,p1y], [p3x,p3y])
    #print("a: {}, b: {}, c: {}".format(a, b, c))
    cos_C = ((a*a) + (b*b) - (c*c)) / (2*a*b)
    C_degree = math.acos(cos_C) * (180.0 / math.pi)
    #print("cos_C: {}, C_degree: {}".format(cos_C, C_degree))
    return C_degree


'''
Samples data and some flags.
'''
normalize = True
samples_total = 400
p1x = 16.5
p1y = 0.12319919
p2x = 34
p2y = 0.52208633
p3x = 47.5
p3y = 0.16700115
if normalize:
    p1x = p1x / samples_total
    p2x = p2x / samples_total
    p3x = p3x / samples_total


'''
Main purpose of the example.
'''
angle_c = calculate_angle(p1x, p1y, p2x, p2y, p3x, p3y)
print("Angle: {} degree".format(angle_c))


'''
Additional visualization.
'''
X = np.array([[p1x,p1y], [p2x,p2y], [p3x,p3y]])
Y = ['red', 'green', 'blue']
plt.figure()
plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])
t1 = plt.Polygon(X[:3,:], color=Y[0])
plt.gca().add_patch(t1)
if normalize:
    plt.xlim([0, 1])
    plt.ylim([0, 1])
plt.show()

