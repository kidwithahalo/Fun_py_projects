def gauss(A):
    '''converts a matrix into the identity matrix by Gaussian elimination
    ,with the last column containingthe solution for the variable'''

    m = len(A)
    n = len(A[0])

    for j, row in enumerate(A):
        # diagonal term to be 1 by dividing row by diagonal term
        if row[j] != 0:
            # diagonal entry can't be zero
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term/divisor

        # add the other rows to the additive inverse for every row
        for i in range(m):
            if i != j:
                # don't do it to row j , calculate the additive inverse
                addinv = -1*A[i][j]
                # for every term in ith row

                for ind in range(n):
                # add the corresponding term in the jth row
                # multiplied by the additive inverse
                # to the term in the ith rows
                    A[i][ind] += addinv*A[j][ind]
    return A

B = [
    [2,1,-1,8],
    [-3,-1,2,-1],
    [-2,1,2,-3]
    ]

print(gauss(B))
