def generate_subsets(s):
    n = len(s)
    subsets = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(s[j])
        subsets.append(subset)
    return subsets


if __name__ == "__main__":
    a = [1, 2, 3]
    subs = generate_subsets(a)
    print(subs)
