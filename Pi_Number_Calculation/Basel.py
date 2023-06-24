#calculating pi using Basel 
import math

summation = 0.0
for i in range(2000000):
        summation = summation + (1/float((int(i)+1)**2))

pi = math.sqrt(6*summation)
print(pi)
#the value that i've got was 3.1415921761250813