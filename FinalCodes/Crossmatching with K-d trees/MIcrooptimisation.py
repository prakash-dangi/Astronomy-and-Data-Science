#converting Ra and Dec from degrees to radians before crossmatching
import numpy as np
import time
# import hashlib

def angularDistance(r1, d1, r2, d2):
    a = np.sin(np.abs(d1-d2)/2)**2
    b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1-r2)/2)**2
    return 2*np.arcsin(np.sqrt(a+b))

def crossmatch(cat1, cat2, max_radius):
    start = time.perf_counter()
    max_radius = np.radians(max_radius)

    matches = []
    noMatches = []

    cat1 = np.radians(cat1)
    cat2 = np.radians(cat2)

    for id1, (ra1, dec1) in enumerate(cat1):
        closest_dist = np.inf
        closest_id2 = None
        for id2, (ra2, dec2) in enumerate(cat2):
            dist = angularDistance(ra1, dec1, ra2, dec2)
            if dist < closest_dist:
                closest_dist = dist
                closest_id2 = id2
            
        if closest_dist > max_radius:
            noMatches.append(id1) 
        else:
            matches.append((id1, closest_id2, np.degrees(closest_dist)))

    end = time.perf_counter() - start

    return matches, noMatches, end

# The example in the question
cat1 = np.array([[180, 30], [45, 10], [300, -45]])
cat2 = np.array([[180, 32], [55, 10], [302, -44]])
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)

# A function to create a random catalogue of size n
def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

# Test your function on random inputs
cat1 = create_cat(10)
cat2 = create_cat(20)
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)

# def angular_dist(r1, d1, r2, d2):
#   a = np.sin(np.abs(d1 - d2)/2)**2
#   b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
#   return 2*np.arcsin(np.sqrt(a + b))

# def hash_function(func):
#     return hashlib.md5(func.__code__.co_code).hexdigest()

# print(hash_function(angular_dist))
# print(hash_function(angularDistance))
