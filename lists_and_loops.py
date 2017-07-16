the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "coconuts", "grapes", "oranges"]

for i in the_count:
    print "%s" % i

for i in range(6, 10):
    print "adding %d to the list" % i
    the_count.append(i)

print the_count
