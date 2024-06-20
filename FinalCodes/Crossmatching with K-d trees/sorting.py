#sorting cat2 about dec
import numpy as np
import time

def angular_dist(r1, d1, r2, d2):
  a = np.sin(np.abs(d1 - d2)/2)**2
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  return 2*np.arcsin(np.sqrt(a + b))

def crossmatch(cat1, cat2, max_radius):
  start = time.perf_counter()
  max_radius = np.radians(max_radius)
  
  matches = []
  noMatches = []
  
  cat1 = np.radians(cat1)
  cat2 = np.radians(cat2)
  ordered = np.argsort(cat2[:, 1])
  cat2_ordered = cat2[ordered]
  
  for id1, (ra1, dec1) in enumerate(cat1):
    min_dist = np.inf
    min_id2 = None
    for id2, (ra2, dec2) in enumerate(cat2_ordered):
        if dec2 < dec1 + max_radius: #dec1 - max_radius < dec2 < dec1 + max_radius: resulted in a wrong output
            dist = angular_dist(ra1, dec1, ra2, dec2)
            if dist < min_dist:
                min_dist = dist
                min_id2 = ordered[id2]
        else:
           break
        
    if min_dist > max_radius:
      noMatches.append(id1)
    else:
      matches.append((id1, min_id2, np.degrees(min_dist)))
      
  end = time.perf_counter() - start
  return matches, noMatches, end

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
np.random.seed(0)
cat1 = create_cat(10)
cat2 = create_cat(20)
matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
print('matches:', matches)
print('unmatched:', no_matches)
print('time taken:', time_taken)

#other solution
# import numpy as np
# import time

# def angular_dist(r1, d1, r2, d2):
#     a = np.sin(np.abs(d1 - d2) / 2)**2
#     b = np.cos(d1) * np.cos(d2) * np.sin(np.abs(r1 - r2) / 2)**2
#     return 2 * np.arcsin(np.sqrt(a + b))

# def crossmatch(cat1, cat2, max_radius):
#     start = time.perf_counter()
#     max_radius = np.radians(max_radius)
    
#     matches = []
#     no_matches = []

#     # Convert coordinates to radians
#     cat1 = np.radians(cat1)
#     cat2 = np.radians(cat2)
#     order = np.argsort(cat2[:, 1])  # Sort by declination
#     cat2_ordered = cat2[order]
    
#     for id1, (ra1, dec1) in enumerate(cat1):
#         min_dist = np.inf
#         min_id2 = None
#         max_dec = dec1 + max_radius
#         min_dec = dec1 - max_radius
#         for id2, (ra2, dec2) in enumerate(cat2_ordered):
#             if dec2 < min_dec:
#                 continue  # Skip objects with declination far below the current object
#             if dec2 > max_dec:
#                 break  # No need to check further as the catalog is sorted
            
#             dist = angular_dist(ra1, dec1, ra2, dec2)
#             if dist < min_dist:
#                 min_id2 = order[id2]
#                 min_dist = dist
        
#         # Ignore match if it's outside the maximum radius
#         if min_dist > max_radius:
#             no_matches.append(id1)
#         else:
#             matches.append((id1, min_id2, np.degrees(min_dist)))
      
#     time_taken = time.perf_counter() - start
#     return matches, no_matches, time_taken

# # Test cases
# cat1 = np.array([[180, 30], [45, 10], [300, -45]])
# cat2 = np.array([[180, 32], [55, 10], [302, -44]])
# matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
# print('matches:', matches)
# print('unmatched:', no_matches)
# print('time taken:', time_taken)

# # A function to create a random catalogue of size n
# def create_cat(n):
#     ras = np.random.uniform(0, 360, size=(n, 1))
#     decs = np.random.uniform(-90, 90, size=(n, 1))
#     return np.hstack((ras, decs))

# # Test your function on random inputs
# np.random.seed(0)
# cat1 = create_cat(10)
# cat2 = create_cat(20)
# matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
# print('matches:', matches)
# print('unmatched:', no_matches)
# print('time taken:', time_taken)
