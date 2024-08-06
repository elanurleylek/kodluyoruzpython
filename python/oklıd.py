import math

points = [(0, 0), (3, 4), (5, 12), (8, 15)]

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

distances = []
# İki nokta arasındaki mesafeyi hesaplamak için döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(((points[i], points[j]), distance))