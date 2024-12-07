input_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

# Split input into lines
lines = input_data.split("\n")

# Initialize operation and value arrays
op_arr = []
val_arr = []

# Populate op_arr and val_arr from input
for line in lines:
    parts = line.split()
    op = parts[0]
    val = int(parts[1]) if len(parts) > 1 else 0
    op_arr.append(op)
    val_arr.append(val)

# Global counters
global_count = 0

# Count the total number of cycles (to determine the number of iterations)
for line in lines:
    method = line.split()
    if method[0] == "noop":
        global_count += 1
    elif method[0] == "addx":
        global_count += 2  # addx takes 2 cycles

# Initialize simulation variables
delay = 0
index = 0
register = 1
print_count = 1
glob_total = 0

# Run the simulation
while global_count > 0:
    if delay == 0:
        if op_arr[index] == "noop":
            delay += 1
            index += 1
        elif op_arr[index] == "addx":
            delay += 2
            register += val_arr[index]
            index += 1
    else:
        delay -= 1

    # Print at cycle points
    if print_count == 20 or (print_count - 20) % 40 == 0:
        print(print_count, " -- ", register)
        glob_total += print_count * register

    print_count += 1
    global_count -= 1

print(f"Total sum: {glob_total}")
