# library of myConvexHull

def leftRight(p1,p2,p3): #Return boolean True apabila ada di left
    x = p1[0]*p2[1]+p3[0]*p1[1]+p2[0]*p3[1]-p3[0]*p2[1]-p2[0]*p1[1]-p1[0]*p3[1]
    return x>0

def distance(p1,p2,p3): #Return jarak dua titik terhadap satu titik
    return ((p1[0]-p3[0])**2+(p1[1]-p3[1])**2)**0.5+((p2[0]-p3[0])**2+(p2[1]-p3[1])**2)**0.5

def setOfPoint(points, p1, p2): #Return seluruh koordinat titik yang terdapat pada suatu partisi
    # Inisiasi nilai dan point max
    maxDistance = 0
    dist = 0
    farthest = []

    # Iterasi mencari nilai terbesar
    for i in range(len(points)):
        dist = distance(p1,p2,points[i])
        if(maxDistance<dist):
            maxDistance = dist
            farthest = points[i]

    # Apabila tidak ada yang menjadi poin terjauh langsung kembalikan list kosong
    if farthest == []:
        return []

    # Inisiasi bagian kiri dari garis antara p1 dan pmax serta bagian kanan dari garis antara pmax dan p2
    left = []
    right = []

    # check left and right dan bagi ke dalam list
    for point in points:
        if(leftRight(p1,farthest,point) and point != farthest):
            left.append(point)
        if(leftRight(farthest,p2,point) and point != farthest):
            right.append(point)
    
    # Inisiasi koordinat hull yang terdapat pada kiri p1,pmax dan koordinat hull pada kanan pmax,p2
    leftPoint = []
    rightPoint = []
    
    # Lakukan rekursi apabila masih terdapat titik yang diluar garis 
    if(len(left) != 0):
        leftPoint = setOfPoint(left,p1,farthest)
    if(len(right) != 0):
        rightPoint = setOfPoint(right,farthest,p2)

    return leftPoint+farthest+rightPoint
    

def myConvexHull(bucket): #Return Simplices yang merupakan hull
    # Melakukan sort pada list dari data
    sortedBucket = sorted(bucket, key=lambda x:[x[0],x[1]])

    # Inisiasi nilai list yang terdapat pada kiri dan kanan garis
    left = []
    right = []

    # Membagi koordinat titik yang ada menjadi dua oleh garis
    for i in range(1,len(sortedBucket)-1):
        if(leftRight(sortedBucket[0],sortedBucket[-1],sortedBucket[i])):
            left.append(sortedBucket[i])
        else:
            right.append(sortedBucket[i])
    
    # Melakukan rekursi partisi pada bagian kiri dan kanan garis hingga didapatkan koordinat hull
    leftPoint = setOfPoint(left,sortedBucket[0],sortedBucket[-1])
    rightPoint = setOfPoint(right,sortedBucket[-1],sortedBucket[0])

    # Gabungkan data koordinat titik sehingga terbentuk vertex-vertex searah jarum jam
    coordinatesOfVertices = []+sortedBucket[0]+leftPoint+sortedBucket[-1]+rightPoint

    # Membuat data menjadi point untuk setiap koordinatnya
    pointOfVertices = []
    for i in range(0,len(coordinatesOfVertices)-1,2):
        temp = []
        temp.append(coordinatesOfVertices[i])
        temp.append(coordinatesOfVertices[i+1])
        pointOfVertices.append(temp)
        
    # Membentuk vertex dari data koordinat point
    vertices = []
    for point in pointOfVertices:
        vertices.append(bucket.index(point))

    # Membentuk Simplices dari Vertices
    simplices = []
    simplices.append([vertices[0],vertices[-1]])
    for i in range(1,len(vertices)):
        simplices.append([vertices[i],vertices[i-1]])

    return simplices