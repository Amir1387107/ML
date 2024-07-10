import numpy as np

a=np.array([[2,3],[4,5]])
b=np.matrix([[2,3],[3,4]])
c=np.ones((4,4))
o=np.zeros((2,5))
e=np.array([[2,4,3,5]])
d=c+e          #the same result on - * /
# nothing=np.math.nan
# infinity=np.math.inf
radical1=np.random.uniform(1,5,(3,4))
radical2=np.random.standard_normal((2,3))

#how to sum =>  a@a or np.dot(a,a)   how to sum the things inside=> np.sum(a)  how to sum the numbers an put each result(1,1+2,1+2+3,1+2+3+4)=> np.cumsum(a , axis=(1or0))
#how to multiple=> np.multiply(a,a) or a*a      how to multiple the things inside=> np.prod(a)
#if you put c=a+5 each number in a will sum with 5
#aubtracting= np.subtract(a,b)
#divide= np.divide(a,5)   **np.floor_divide(a,3)-> حاصل رند
#radical= np.math.sqrt(5)

arangic=np.arange(1,10,2)
howmuchnumber=np.linspace(1,10,8)
ar=np.logical_and(a>1,a<5)
# print(ar)
# print(a[ar])
#to see the shape and the size of an array=> np.size(a) , np.shape(a)

aa=np.array([[1,2,3,4,5,1,3,5]])
bb=np.array([[6,7,8,9,1,3]])
print(np.unique(aa))   #unrepeated and repeated (one time)
print(np.union1d(aa,bb))  #sum with puting repeated once
print(np.intersect1d(aa,bb)) #repeated items in both
print(np.mean(np.union1d(aa,bb)))  #average
print(np.median(np.union1d(aa,bb)))  #median
print(np.std(np.union1d(aa,bb)))  #standard division
print(np.var(np.union1d(aa,bb)))  #variance (difference)

# ______________________________________________
# x^2+2x+2=0

chandjoomleii=np.array([1,2,2]) #ضریب ها
print(np.polyval(chandjoomleii,1))
print(np.polyder(chandjoomleii))  #مشتق
print(np.polyint(chandjoomleii))  #انتگرال
