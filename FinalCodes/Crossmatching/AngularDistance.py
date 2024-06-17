import numpy as np

def angular_dist(ra1, dec1, ra2, dec2):
    r1 = np.radians(ra1)
    r2 = np.radians(ra2) 
    d1 = np.radians(dec1)
    d2 = np.radians(dec2)

    #formula implementation - Haversine Formula

    a = np.sin(np.abs(d1-d2)/2)**2
    b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
    d = 2*np.arcsin(np.sqrt(a+b))
    return np.degrees(d)

d = angular_dist(10.3, -3, 24.3, -29)
print(d)