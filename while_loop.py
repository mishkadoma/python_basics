i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At hte bottom i is %d" % i

print "The numbers: "

for element in numbers:
    print element

# 1. Study Drills_1

def while_loop(i):
    i = 0
    numbers_1 = []

    print "At the top i is %d" % i
    numbers_1.append(i)

    i += 1
    print "Numbers now: ", numbers_1
    print "At the bottom i is %d" % i

# 2. Study Drills_2

while_loop(2)
while_loop(5)

# 3. Study Drills_3

def while_loop_3(i, increment):
    numbers_3 = []

    print "At the top i is %d" % i
    numbers_3.append(i)

    i += increment
    print "Numbers now: ", numbers_3
    print "At the bottom i is %d" % i

# 4. Study Drills_4

while_loop_3(1, 2)
while_loop_3(0, 1)

# 5. Study Drills_5

def some_new_loop(i, increase_to, increment):
    numbers_5 = []

    for element_5 in (i, increase_to, increment):
        numbers_5.append(element_5)
    print "There are elements: ", numbers_5

some_new_loop(1, 10, 3)
