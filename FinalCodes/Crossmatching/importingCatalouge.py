import numpy as np

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

# print(import_bss())
# print(import_super())