#!/usr/bin/python3
if __name__ == "__main__":
    from calculate_1 import add
    from calculate_1 import sub
    from calculate_1 import mul
    from calculate_1 import div
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} + {:d} = {:d}".format(a, b, div(a, b)))
