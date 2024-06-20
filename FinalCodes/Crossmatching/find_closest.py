import numpy as np
import AngularDistance
from importingCatalouge import import_bss

cat = import_bss()
def find_closest_method1(cat, ra, dec):
    checklist = []
    for tup in cat:
        for i in tup:
            checklist.append(tuple((AngularDistance.angular_dist(tup[1], tup[2], ra, dec), tup[0])))

    return min(checklist)[1], min(checklist)[0]

#method 2 - better - memory efficient
def find_closest_method2(cat, ra, dec):
  min_dist = np.inf #this represents positive infinity - so that we can iteratively find the minimum value
  min_id = None
  for id1, ra1, dec1 in cat:
    dist = AngularDistance.angular_dist(ra1, dec1, ra, dec)
    if dist < min_dist:
      min_id = id1
      min_dist = dist
    
  return min_id, min_dist

print(find_closest_method2(cat, 175.3, -32.5))