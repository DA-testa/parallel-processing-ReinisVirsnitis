# python3

def parallel_processing(n, m, data):
    output = []
    t = []
    for i in range(n):
        t.append(0)
    laiks = 0
    while data:
        for i in range(n):
            if t[i] == 0:
                output.append((i, laiks))
                t[i] = data[0] - 1
                data.pop
            else:
                t[i] = t[i] - 1
        laiks = laiks + 1
    return output

def main():
    mainigie = list(map(int, input().split()))
    n = mainigie[0]
    m = mainigie[0]

    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for i,j in result:
        print(i,j)

if __name__ == "__main__":
    main()
