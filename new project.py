import random

print("첫 번째 수: ")
f = random.randrange(10)
print(f)

fx = random.randrange(4)

if fx == 0:
    print("두 번째 수: ")
    s = random.randrange(10)
    print(s)

    sx = random.randrange(4)
    if sx == 0:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s+t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s+t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s+t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s+t/ft)
    elif sx == 1:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s-t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s-t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s-t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s-t/ft)
    elif sx == 2:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s*t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s*t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s*t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s*t/ft)
    else:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s/t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s/t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s/t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f+s/t/ft)
elif fx == 1:
    print("두 번째 수: ")
    s = random.randrange(10)
    print(s)

    sx = random.randrange(4)
    if sx == 0:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s+t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s+t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s+t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s+t/ft)
    elif sx == 1:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s-t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s-t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s-t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s-t/ft)
    elif sx == 2:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s*t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s*t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s*t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s*t/ft)
    else:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s/t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s/t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s/t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f-s/t/ft)
elif fx == 2:
    print("두 번째 수: ")
    s = random.randrange(10)
    print(s)

    sx = random.randrange(4)
    if sx == 0:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s+t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s+t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s+t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s+t/ft)
    elif sx == 1:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s-t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s-t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s-t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s-t/ft)
    elif sx == 2:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s*t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s*t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s*t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s*t/ft) 
    else:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s/t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s/t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s/t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f*s/t/ft)
else:
    print("두 번째 수: ")
    s = random.randrange(10)
    print(s)

    sx = random.randrange(4)
    if sx == 0:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s+t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s+t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s+t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s+t/ft)
    elif sx == 1:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s-t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s-t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s-t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s-t/ft)
    elif sx == 2:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s*t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s*t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s*t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s*t/ft)
    else:
        print("세 번째 수: ")
        t = random.randrange(10)
        print(t)

        tx = random.randrange(4)
        if tx == 0:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s/t+ft)
        elif tx == 1:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s/t-ft)
        elif tx == 2:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s/t*ft)
        else:
            print("네 번째 수:")
            ft = random.randrange(10)
            print(ft)

            ftx = random.randrange(4)

            print("결과값: ", f/s/t/ft)
            
