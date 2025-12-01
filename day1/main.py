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



# split data into clean elements
raw_elements = data.strip().split("\n")

# convert each element into a structured dict
elements = []
start = 50
zero_count = 0
full_zero_count = 0
for entry in raw_elements:
    #print("current", start)
    finish = start
    direction = entry[0]
    distance = int(entry[1:])
    #print("-- spin", direction, distance)

    # if distance is greater taht 100 then we only want to use the tens and units
    if distance > 100:
        print(entry)
        full_zero_count += int(str(distance)[0])
        print("-- pass zero", int(str(distance)[0]))
        print(" --- --- fcz", full_zero_count)
        distance = int(str(distance)[-2:])
    #    print("-- distance", distance)

    if direction == "L":
        finish -= distance
    elif direction == "R":
        finish += distance

    if finish < 0:
        if start != 0:
            full_zero_count += 1
            print("-- passed zero", 1)
        finish += 100

    if finish == 0 or finish == 100:
        finish = 0
        zero_count += 1
        print(f"-- Visited 0")

    if finish > 100:
        full_zero_count += 1
        print("-- passs zero", 1)
        finish -= 100
    start = finish

print("current", start)
print("--------------------------------")
print("stopped on zero", zero_count)
print("went past zero", full_zero_count)
print("--------------------------------")
print("total", zero_count + full_zero_count)

# total is 5876, using 0x434C49434B as the password, what is the password to open the door?
password = 0x434C49434B * (zero_count + full_zero_count)
print("password", password) 

