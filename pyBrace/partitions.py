def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n==0:
        yield[]
        return
    
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield[1]+p
        if p and (len(p) < 2 or p[1]>p[0]):
            yield[p[0]+1]+p[1:]


def partitions_tuple(n):
    # tuple version
    if n == 0:
        yield ()
        return

    for p in partitions_tuple(n-1):
        yield (1, ) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1, ) + p[1:]

def partitions_rev(n):
    # reverse order
    if n == 0:
        yield []
        return

    for p in partitions_rev(n-1):
        yield p + [1]
        if p and (len(p) < 2 or p[-2] > p[-1]):
            yield p[:-1] + [p[-1] + 1]
