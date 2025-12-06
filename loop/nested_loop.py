# 1, 2
for row in range(1, 3):
    for column in range(1, 3):
        print(f"row={row}, column={column}")

#    i1  j1
# i2 |1,  1|
# j2 |2,  2|

# i2,i1xi2,j1 + i2,i1xj2,j1 + j2,i1xi2,j1 + j2,i1xj2,j1 
#  1 x 1      +  1 x 2      +  2 x 1      +  2 x 2
#    1        +    2        +    2        +    4
#  1 + 2 + 2 + 4 
#     = 9