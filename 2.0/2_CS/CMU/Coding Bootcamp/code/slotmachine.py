count = int(raw_input())

# 1st one
spin = list(raw_input())
length = len(spin)
spin.sort()
spin = [int(x) for x in spin]
# print spin
slots = []

for i in range(length):
    slots.append(spin[i])

for i in range(1, count):
    spin = list(raw_input())
    spin.sort()
    spin = [int(x) for x in spin]
    for j in range(length):
        if spin[j] > slots[j]:
            slots[j] = spin[j]

print(sum(slots))




index = 0

    while index < len(result):
        count = int(result[index])
        index += 1
        # 1st one
        spin = list(result[index])
        index += 1
        length = len(spin)
        spin.sort()
        spin = [int(x) for x in spin]
        # print spin
        slots = []

        for i in range(length):
            slots.append(spin[i])

        for i in range(1, count):
            spin = list(result[index])
            index += 1
            spin.sort()
            spin = [int(x) for x in spin]
            for j in range(length):
                if spin[j] > slots[j]:
                    slots[j] = spin[j]
        print sum(slots)
    return sum(slots)
