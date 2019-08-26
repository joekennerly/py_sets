# Empty set
showroom = set()

showroom.add("mustang")
showroom.add("model t")
showroom.add("jeep")
showroom.add("hummer")
print(len(showroom))

showroom.add("hummer")
print(len(showroom))

two_cars = ["convertable", "el camino"]
showroom.update(two_cars)
print(showroom)

showroom.discard("convertable")
print(showroom)

# Junk yard
junkyard = {"mustang", "hummer", "chevy", "truck", "van"}
crossover = showroom.intersection(junkyard)
print(crossover)

union = showroom | junkyard
union.discard("jeep")
print(union)