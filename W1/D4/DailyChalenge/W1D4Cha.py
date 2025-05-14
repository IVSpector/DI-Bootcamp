MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

step = []
matrix = []
new_matrix = ""

new_list = MATRIX_STR.split("\n")
for line in new_list:
    for character in line:
        step.append(character)
    if step:
        matrix.append(step.copy())
    step.clear()

for line_num, lane_matrix in enumerate(matrix, start=1):
    for index, cahr_lane in enumerate(lane_matrix):
        a = line_num*index + line_num - 1
        if not cahr_lane.isalpha():
            cahr_lane = " "
        new_matrix = new_matrix[:a] + cahr_lane + new_matrix[a:]
        print(new_matrix)

new_matrix = " ".join(new_matrix.split())
print(new_matrix)

# print(matrix)
# def matrix_2d():
#     matrix = []
#     for line in new_list:
#         matrix.append(list(line))
#         print("matrix", matrix)
#     return matrix