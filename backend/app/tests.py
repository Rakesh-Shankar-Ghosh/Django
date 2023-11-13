import time

def f1():
    print("f1 starts")
    time.sleep(2)
    print("f1 finishes")

def f2():
    print("f2 starts")
    time.sleep(5)
    print("f2 finishes")

def f3():
    print("f3 starts")
    time.sleep(1)
    print("f3 finishes")

def main():
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()
