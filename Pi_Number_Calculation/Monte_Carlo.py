import random

#pi calculation using Monte_Carlo

#number of all random pins we want to land inside that area
#much more,much tenuous
num_of_all = 2000000

#number of landed inside circle
landed = 0

#randomly landing to see which are landed inside or on the border of circle
for i in range(num_of_all):
  x2 = random.uniform(0.0,1.0)**2
  y2 = random.uniform(0.0,1.0)**2
  if x2 + y2 < 1.0:
      landed += 1

#calculating pie
pi = (float(landed) / num_of_all) * 4
print(pi)
# the landed i get was 3.141688 not totally tenuous but just for fun!