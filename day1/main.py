# data_elements = [
#     "L68",
#     "L30",
#     "R48",
#     "L5",
#     "R60",
#     "L55",
#     "L1",
#     "L99",
#     "R14",
#     "L82",
# ]
# data = "\n".join(data_elements)

#load data from file data.txt
with open("data.txt", "r") as file:
    data = file.read()
print(data)



# split data into clean elements
raw_elements = data.strip().split("\n")

# convert each element into a structured dict
elements = []
start = 50
zero_count = 0
for entry in raw_elements:
    #print("start", start)
    direction = entry[0]
    distance = int(entry[1:])
    elements.append({"direction": direction, "distance": distance})

    # if distance is greater taht 100 then we only want to use the tens and units
    if distance > 100:
        distance = int(str(distance)[-2:])
        print("distance", distance)

    if direction == "L":
        start -= distance
    elif direction == "R":
        start += distance

    if start < 0:
        start += 100

    if start == 0 or start == 100:
        start =0
        zero_count += 1
        print(f"Visited 0")

    if start > 100:
        start -= 100


print(zero_count)
