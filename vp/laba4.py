# функция для определения ориентации трех точек
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 # коллинеарны
    elif val > 0:
        return 1 # по часовой стрелке
    else:
        return 2 # против часовой стрелки


# функция для построения выпуклой оболочки
def convex_hull(points):
    n = len(points)
    if n < 3:
        return [] # не может быть выпуклой оболочкой
    hull = []
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    p = l
    q = 0
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    return hull


if __name__ == "__main__":
    # чтение данных из файла
    with open("input.txt", "r") as f:
        n = int(f.readline())
        points = []
        a = f.readline().split()
        for i in range(0, n*2, 2):
            x, y = int(a[i]), int(a[i+1])
            points.append((x, y))

    # построение выпуклой оболочки
    hull = convex_hull(points)

    # определение принадлежности точек многоугольнику
    belongs = [0] * n
    for i in range(n):
        for j in range(len(hull)):
            if points[i] == hull[j]:
                belongs[i] = 1
                break

    # запись результатов в файл
    with open("output.txt", "w") as f:
        f.write(" ".join(map(str, belongs)))
