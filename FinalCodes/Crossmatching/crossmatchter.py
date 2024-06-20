import numpy as np
import AngularDistance as adist
import importingCatalouge as ic

cat1 = ic.import_bss()
cat2 = ic.import_super()

def crossmatch(cat1, cat2, max_dist):
    matchList = []
    noMatchList = []
    for ID, ra, dec in cat1:
        for ID_s, ra_s, dec_s in cat2:
            dist = adist.angular_dist(ra, dec, ra_s, dec_s)
            if dist <= max_dist:
                matchList.append(tuple((ID, ID_s, dist)))
                t = 0
                break #recieved wrong results when this break was not included
            else:
                t = 1
        if t == 1:
            noMatchList.append(ID)
    
    return matchList, noMatchList

matches, no_matches = crossmatch(cat1, cat2, 40/3600)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))