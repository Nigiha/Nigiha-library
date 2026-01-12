#-----------二分法-----------
# region=[0.0, 4.0]
# step=0.1
# eps=1e-4

# def f1(x:float):
#     return 3*x**3-17*x**2+26*x-10

# def judge(a:float, b:float):
#     return f1(a)*f1(b)

# def bisection(a, b):
#     n=0
#     dx=b-a
#     while dx > eps:
#         x=(b+a)/2
#         if judge(x, a)<0:
#             b=x
#         else:
#             a=x
#         dx=abs(b-a)
#         print("Search from {:4.2f}to{:4.2f}. F(x)={:>10.3e}".format(x, dx, f1(x)))
#         n+=1
#     else:
#         print('--Solution found at x={:10.6f} in {:4.0f} iterations.'.format(x, n))

# def main():
#     x0=region[0]
#     while x0 <= region[1]-step:
#         if judge(x0, x0+step) < 0:
#             print("Rough Search from {:4.2f} to {:4.2f}".format(x0, x0+step))
#             bisection(x0, x0+step)
#         x0+=step

# main()



#-----------ニュートン法-----------
# xmax=4.0
# step=1.5
# eps=1.0e-5
# def func(x:float):
#     return 3.0*x**3-17.0*x**2+26.0*x-10.0,\
#            9.0*x**2-34.0*x+26.0

# def main():
#     x=0.0
#     while x < xmax: #stepが浅いと無限ループ
#         n=0
#         evl=step
#         while evl >= eps:
#             f, df=func(x)
#             x-=f/df
#             n+=1
#             evl=abs(f/df)
#             print("Time:{:3.0f} x={:11.7f} f={:11.7f} evl={:12.7f}".format(n, x, f, evl))
#             if evl < eps:
#                 print("Solution: {:11.7f}{:11.7f}".format(x, f))
#                 break
#         x+=step
#         print(x)

# main()



#-----------ニュートン法+二分法-----------
# import numpy as np
# def f0(x:float):
#     return x*np.cos(2*x)-2*x**2+2*np.exp(x/2)+3
# def seek(a:float, b:float, f):
#     return f(a)*f(b)
# def main(xval:list, step:float, eps:float, func):
#     h=1.0e-4
#     n=0
#     x=xval[0]
#     while x >= xval[0] and x <= xval[1]-step:
#         a=x
#         b=a+step
#         if seek(a, b, func) < 0.0:
#             evl=float('inf')
#             x=0.5*(a+b)
#             print("x={:11.7f} evl={:13.6f} f={:13.6e}".format(x, evl, func(x)))
#             while evl >= eps:
#                 x1=x-h*func(x)/(func(x)-func(x-h))
#                 if x1 >= a and x1 <= b:
#                     pass
#                 else:
#                     if seek(x, a, func) < 0:
#                         b=x
#                     else:
#                         a=x
#                     x1=0.5*(a+b)
#                 evl=abs(x1-x)
#                 x=x1
#                 print("x={:11.7f} evl={:13.6f} f={:13.6e}".format(x, evl, func(x)))
#             n+=1
#             print("Solution no.{:3.0f}:x={:13.6f}, f={:13.6f}".format(n, x, func(x)))
#         x+=step

# xval=[-10.0, 10.0]
# step=0.2
# eps=1.0e-5
# main(xval, eps, step, f0)