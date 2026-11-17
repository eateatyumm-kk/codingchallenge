



L = lattice.shape[0]
    up = lattice[(i-1)% L,j] 
    left = lattice[i, (j-1)% L]
    down = lattice[(i+1)% L,j]
    right = lattice[i, (j+1)% L]

-> this code allow you to find the number in end for edge cases

np.roll shifts the matrix column/row by given number. and you can add them