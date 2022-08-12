from vec import *
def subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])
def distance(v1, v2):
    return length(subtract(v1, v2))
def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i + 1) % len(vectors)])
                 for i in range(len(vectors))]
    return sum(distances)

# Let u be the vector (1, 2). Suppose there is another vector v with positive integer coordinates (n, m)
# such that n > m and has a distance of 13 from u. What is the displacement from u to v?
for n in range(1, 14):
    for m in range(0, n - 1):
        if distance((n, m), (1, 2)) == 13:
            print((n, m))
print(perimeter(dino_vectors))