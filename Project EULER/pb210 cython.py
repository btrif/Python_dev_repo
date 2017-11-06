#  Created by Bogdan Trif on 03-11-2017 , 6:06 PM.

# ==== Mon, 12 Oct 2015, 06:03, bukebuer, China
# Same as others, seperating points into 3 parts, and the most difficult part is the circle part.
#
# Pure Python code runs around 2 minutes. But if using Cython rewriting the cycling part,
# it takes only 6~7 seconds. Amazing!


from libc.math cimport sqrt

cpdef unsigned long long p_in_sector(unsigned long long rx):
    cdef:
        unsigned long long x = rx + 1
        unsigned long long r2  = rx * rx * 2
        unsigned long long xmax = int(sqrt(r2)) + 1
        long long y, c = 0

    while x < xmax:
        y = max(int(sqrt(r2 - x * x)), 1) - 1
        while x * x + y * y < r2:
            y += 1
        if y:
            y -= 1

        x += 1
        c += 8 * y
    return c

def pe210(N=1000000000):
    rx = N / 8
    r2 = rx * rx * 2
    r = int(sqrt(r2)) + 1

    # points in rectangles
    c = N * N * 3 / 2

    # points at diagonal radius
    c += 2 * (rx - 1)

    # points at orthogonal radius
    c += 4 * (r - 1)

    # points in 1/8 sectors
    c += 4 * (rx - 1) * rx

    x = rx + 1
    while x < r:
        y = max(int(sqrt(r2 - x * x)), 1) - 1
        while x * x + y * y < r2:
            y += 1
        if y:
            y -= 1

        c += 8 * y
        x += 1
    # c += p_in_sector(rx) # Cython function
    return c


