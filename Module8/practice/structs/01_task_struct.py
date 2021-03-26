# Бегун проводил ежедневные тренировки и записывал расстояния которые пробел за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

# distances_f = []
# for dist in distances:
#     distances_f.append(dist * 3.28)

print(list(map(lambda dist: dist * 3.281, distances)))

# print(distances_f)
