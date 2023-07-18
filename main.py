class MirrorDiagonals:
    def sum(self, array):
        k = 0
        sum = 0
        for j in range(row-1, -1, -1):
            sum += array[k][j]
            k += 1

        return sum


array = []
row = int(input("Enter no of rows: "))
for i in range(row):
    a = list(map(int, input().split()))
    array.append(a)

object = MirrorDiagonals()
print(object.sum(array))


"""You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

Input
[  [1, -2, -3],
   [-4, 5, -6],
   [-7, -8, 9]  ]

Output
-5


Input
[  [3, 2],
   [2, 3]  ]

Output
4"""