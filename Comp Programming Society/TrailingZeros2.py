def solve(N):
    if N == 0:
        return 0
    return N // 5 + solve(N // 5)

def main():
    N = int(input(""))
    print(solve(N))

if __name__ == "__main__":
    main()