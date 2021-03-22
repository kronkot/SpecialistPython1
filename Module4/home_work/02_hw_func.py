# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

xa = int(input("xA ="))
ya = int(input("yA ="))
xb = int(input("xB ="))
yb = int(input("yB ="))
xc = int(input("xC ="))
yc = int(input("yC ="))

ab = distance(xa, ya, xb, yb) #хранятся длины отрезков
bc = distance(xb, yb, xc, yc)
ac = distance(xa, ya, xc, yc)

min_dist = ab
name = "AB"
if bc < min_dist:
    min_dist = bc
    name = "BC"
if ac < min_dist:
    min_dist = ac
    name = "AC"

print("Самый короткий отрезок:", name)  # Выводим название отрезка, например “АС”.




#СПАСИБО!
