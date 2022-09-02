# Сортировки

# Сортировка вставками O(n^2)
# (insert sort)
def insert_sort(A: list) -> list:
    N = len(A)
    for top in range(1,N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    return A

# Сортировка методом выбора O(n^2)
# (choise sort)
def choise_sort(A: list) -> list:
    N = len(A)
    for pos in range(0,N-1):
        for k in range(pos+1,N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    return A

# Сортировка пузырьком O(n^2)
# (bubble sort)
def bubble_sort(A: list) -> list:
    N = len(A)
    for bypass in range(1,N):
        for k in range(0,N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    return A


# Сортировка подсчетом O(n)
def count_sort(A: list) -> list:
    out = list()
    d = {a: 0 for a in range(10)}
    for val in A:
        d[val] += 1
    for key in d.keys():
        for i in range(d[key]):
            out.append(key)
    return out


if __name__ == "__main__":
    mas = [0,1,3,3,2,9,8,8,6,4,0]
    print(insert_sort(mas))
    print(choise_sort(mas))
    print(bubble_sort(mas))
    print(count_sort(mas))
