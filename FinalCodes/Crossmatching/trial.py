import numpy as np
def angularDistance(ra1, dec1, ra2, dec2):
  r1 = np.radians(ra1)
  r2 = np.radians(ra2)
  d1 = np.radians(dec1)
  d2 = np.radians(dec2)
  
  a = np.sin(np.abs(d1-d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a+b))
  return np.degrees(d)

def hms2deg(hms):
  ra = 15*(hms[0] + hms[1]/60 + hms[2]/(60*60))
  return ra

def dms2deg(dms):
  if dms[0] < 0:
    dec = (-1*(-1*dms[0] + dms[1]/60 + dms[2]/(60*60)))
  else:
    dec = dms[0] + dms[1]/60 + dms[2]/(60*60)
  return dec

def import_bss():
  cat = np.loadtxt('FinalCodes/Crossmatching/bss.dat', usecols=range(1, 7))
  
  data = []
  for ID, c in enumerate(cat, start=1):
    ra = hms2deg(c[0:3])
    dec = dms2deg(c[3:6])
    data.append(tuple((ID, ra, dec)))
  
  return data

def import_super():
  cat = np.loadtxt('FinalCodes/Crossmatching/super.csv', delimiter=',', skiprows=1, usecols=[0, 1])
  data = []
  for ID, c in enumerate(cat, start=1):
    data.append(tuple((ID, c[0], c[1])))
    
  return data
bss_cat = import_bss()
super_cat = import_super()

def crossmatch(cat1, cat2, max_radius):
  match = []
  noMatch = []
  for ID, ra, dec in cat1:
    closest_dist = np.inf
    
def crossmatch(cat1, cat2, max_radius):
  match = []
  noMatch = []
  for ID, ra, dec in cat1:
    closest_dist = np.inf
    closest_id = None
    for ID_s, ra_s, dec_s in cat2:
      dist = angularDistance(ra, dec, ra_s, dec_s)
      if dist < closest_dist:
        closest_id = ID_s
        closest_dist = dist
        
    if closest_dist > max_radius:
      noMatch.append(ID)
    else:
      match.append(tuple((ID, ID_s, closest_dist)))
  return match, noMatch

bss_cat = import_bss()
super_cat = import_super()

# First example in the question
max_dist = 40/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))

# Second example in the question
max_dist = 5/3600
matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
print(matches[:3])
print(no_matches[:3])
print(len(no_matches))