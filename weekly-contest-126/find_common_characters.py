def commonChars(A):
    chars = dict.fromkeys(''.join(A))
    result = []
    for c in chars.keys():
        counts = [s.count(c) for s in A]
        cnt = min(counts)
        if cnt > 0:
            for _ in range(cnt):
                result.append(c)

    return result


print(commonChars(["cool", "lock", "cook"]))
