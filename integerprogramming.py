import cvxpy as cp
# from numpy import array
# c = array([40,90])
# a = array([[9, 7], [-7, -20]])
# b = array([56, -70])
# x = cp.Variable(2, integer = True)
# obj = cp.Minimize(c@x)
# cons = [a*x<=b, x>=0]
# prob = cp.Problem(obj, cons)
# prob.solve(solver='GLPK_MI', verbose = True)
# print("最优值为:", prob.value)
# print("最优解为L:", x.value)
import numpy as np
c = np.array([[4, 8, 7, 15, 12],
              [7, 9, 17, 14, 10],
              [6, 9, 12, 8, 7],
              [6, 7, 14, 6, 10],
              [6, 9, 12, 10, 6]])
x = cp.Variable((5,5), integer = True)
obj = cp.Minimize(cp.sum(cp.multiply(c, x)))
con = [0 <= x,  x <=1, cp.sum(x, axis = 0, keepdims = True)==1,
       cp.sum(x, axis = 1, keepdims = True)==1]
prob = cp.Problem(obj, con)
prob.solve(solver = 'GLPK_MI')
print("最优值为:",prob.value)
print("最优值为:", x.value)
