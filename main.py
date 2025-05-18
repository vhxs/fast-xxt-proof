from sympy import symbols, MatrixSymbol, Transpose, expand, ZeroMatrix

def main():
    n, m = symbols('n m', integer=True)

    Xi = {i: MatrixSymbol(f'X{i}', n, m) for i in range(1, 17)}
    X_blocks =[
        [Xi[1],  Xi[2],  Xi[3],  Xi[4]],
        [Xi[5],  Xi[6],  Xi[7],  Xi[8]],
        [Xi[9],  Xi[10], Xi[11], Xi[12]],
        [Xi[13], Xi[14], Xi[15], Xi[16]]
    ]

    # Build the expression
    m1 = (-Xi[2] + Xi[3] - Xi[4] + Xi[8]) * Transpose(Xi[8] + Xi[11])
    m2 = (Xi[1] - Xi[5] - Xi[6] + Xi[7]) * Transpose(Xi[15] + Xi[5])
    m3 = (-Xi[2] + Xi[12]) * Transpose(-Xi[10] + Xi[16] + Xi[12])
    m4 = (Xi[9] - Xi[6]) * Transpose(Xi[13] + Xi[9] - Xi[14])
    m5 = (Xi[2] + Xi[11]) * Transpose(-Xi[6] + Xi[15] - Xi[7])
    m6 = (Xi[6] + Xi[11]) * Transpose(Xi[6] + Xi[7] - Xi[11])
    m7 = Xi[11] * Transpose(Xi[6] + Xi[7])
    m8 = Xi[2] * Transpose(-Xi[14] - Xi[10] + Xi[6] - Xi[15] + Xi[7] + Xi[16] + Xi[12])
    m9 = Xi[6] * Transpose(Xi[13] + Xi[9] - Xi[14] - Xi[10] + Xi[6] + Xi[7] - Xi[11])
    m10 = (Xi[2] - Xi[3] + Xi[7] + Xi[11] + Xi[4] - Xi[8]) * Transpose(Xi[11])
    m11 = (Xi[5] + Xi[6] - Xi[7]) * Transpose(Xi[5])
    m12 = (Xi[2] - Xi[3] + Xi[4]) * Transpose(Xi[8])
    m13 = (-Xi[1] + Xi[5] + Xi[6] + Xi[3] - Xi[7] + Xi[11]) * Transpose(Xi[15])
    m14 = (-Xi[1] + Xi[5] + Xi[6]) * Transpose(Xi[13] + Xi[9] + Xi[15])
    m15 = (Xi[2] + Xi[4] - Xi[8]) * Transpose(Xi[11] + Xi[16] + Xi[12])
    m16 = (Xi[1] - Xi[8]) * Transpose(Xi[9] - Xi[16])
    m17 = Xi[12] * Transpose(Xi[10] - Xi[12])
    m18 = Xi[9] * Transpose(Xi[13] - Xi[14])
    m19 = (-Xi[2] + Xi[3]) * Transpose(-Xi[15] + Xi[7] + Xi[8])
    m20 = (Xi[5] + Xi[9] - Xi[8]) * Transpose(Xi[9])
    m21 = Xi[8] * Transpose(Xi[9] - Xi[8] + Xi[12])
    m22 = (-Xi[6] + Xi[7]) * Transpose(Xi[5] + Xi[7] - Xi[11])
    m23 = Xi[1] * Transpose(Xi[13] - Xi[5] + Xi[16])
    m24 = (-Xi[1] + Xi[4] + Xi[12]) * Transpose(Xi[16])
    m25 = (Xi[9] + Xi[2] + Xi[10]) * Transpose(Xi[14])
    m26 = (Xi[6] + Xi[10] + Xi[12]) * Transpose(Xi[10])

    s1 = Xi[1] * Transpose(Xi[1])
    s2 = Xi[2] * Transpose(Xi[2])
    s3 = Xi[3] * Transpose(Xi[3])
    s4 = Xi[4] * Transpose(Xi[4])
    s5 = Xi[13] * Transpose(Xi[13])
    s6 = Xi[14] * Transpose(Xi[14])
    s7 = Xi[15] * Transpose(Xi[15])
    s8 = Xi[16] * Transpose(Xi[16])

    C11 = s1 + s2 + s3 + s4
    C12 = m2 - m5 - m7 + m11 + m12 + m13 + m19
    C13 = m1 + m3 + m12 + m15 + m16 + m17 + m21 - m24
    C14 = m2 - m3 - m5 - m7 - m8 + m11 + m13 - m17 + m23 + m24
    C22 = m1 + m6 - m7 + m10 + m11 + m12 + m22
    C23 = m1 - m4 + m6 - m7 - m9 + m10 + m12 + m18 + m20 + m21
    C24 = m2 + m4 + m11 + m14 + m16 - m18 - m20 + m23
    C33 = m4 - m6 + m7 + m9 - m17 - m18 + m26
    C34 = m3 + m5 + m7 + m8 + m17 + m18 + m25
    C44 = s5 + s6 + s7 + s8

    C21 = Transpose(C12)
    C31 = Transpose(C13)
    C32 = Transpose(C23)
    C41 = Transpose(C14)
    C42 = Transpose(C24)
    C43 = Transpose(C34)

    C_blocks = [
        [C11, C12, C13, C14],
        [C21, C22, C23, C24],
        [C31, C32, C33, C34],
        [C41, C42, C43, C44],
    ]

    for i in range(4):
        for j in range(4):
            row_i = X_blocks[i]
            row_j = X_blocks[j]
            expected = sum((A * Transpose(B) for A, B in zip(row_i, row_j)), start=ZeroMatrix(n, n))
            diff = expand(C_blocks[i][j] - expected)
            assert diff.is_ZeroMatrix, f"Mismatch at C{i+1}{j+1}: {diff}"

if __name__ == "__main__":
    main()
