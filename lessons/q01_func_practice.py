

def foo(a: int, b: int, c: int) -> int:
    if(a < b):
        return c + b
    elif(b < a):
        return c + a
    

def bar(a: int, b: int, c: int) -> int:
    if(c < a):
        return a + b
    elif(a < c):
        return c + b
    else:
        return b
    

def main() -> None:
    a: int = 2
    b: int = 3
    c: int = 1
    c = foo(b, c, a)
    b = bar(a, c, b)
    print(a)
    print(b)
    print(c)


if __name__ == "__main__":
    main()