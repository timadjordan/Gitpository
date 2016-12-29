import itertools as it
import numpy as np
import math as m

nmax = 11
mat = np.linspace(1,nmax,nmax)
selected = np.zeros(nmax)

look_stop = 5

z = it.permutations(mat)
count = 0
for x in z:
   if count%100000 == 0:
      print count
   count += 1
   #print "current perm = ",x
   best_look = min(x[0:look_stop])
   for y in x[look_stop:nmax]:
      if y < best_look:
         selected[int(y)-1] += 1
         #print "selected = ",selected
         break
      
num_perms = m.factorial(nmax)
selected /= num_perms
#print float(count)/num_perms
print selected
