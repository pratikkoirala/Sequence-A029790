#Digits of n are not present in n^2 and n^3

from sets import Set

def A029790_checker(N):
    square = str(N ** 2)
    cube = str(N ** 3)

    original = Set()
    first = Set()
    second = Set()

    for i in xrange(len(str(N))):
        original.add(str(N)[i])
    
    for i in xrange(len(square)):
        first.add(square[i])

    for i in xrange(len(cube)):
        second.add(cube[i])

    if original.intersection(first):
        return False

    if original.intersection(second):
        return False

    return True


def A029790(N):
    result = []
    for i in xrange(N):
        if A029790_checker(i):
            result.append(i)
        if i % 1000000 == 0:
            print "checked upto " + str(i)
            print result
    return result
        
