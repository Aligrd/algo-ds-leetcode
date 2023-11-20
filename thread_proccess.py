from threading import Thread


def cube(n):
    print(f"cube is {n*n*n}")


def squre(n):
    print(f"square is {n*n}")


t2 = Thread(target=cube, args={10})
t1 = Thread(target=squre, args={10})

t1.start()
t2.start()

print("done")
