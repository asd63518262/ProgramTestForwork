#!/usr/bin/python
# -*- coding: UTF-8 -*-
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 下，上，右，左

def isInside(row_number,col_number,i,j):
    if i in range(row_number) and j in range(col_number):
        return True
    else:
        return False

def max_step_node(row_number,col_number,row,col,mat): ##深度优先搜索算法
    next_row_col = [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
    next_node_list = []
    max_path_long_list =[]
    for i in range(len(next_row_col)):
        if isInside(row_number,col_number,next_row_col[i][0],next_row_col[i][1]):
            if mat[row][col] > mat[next_row_col[i][0]][next_row_col[i][1]]:
                next_node_list.append(next_row_col[i])
    if len(next_node_list) == 0:
        return 1
    else:
        for next_node in next_node_list:
            max_path_long = 1 + max_step_node(row_number,col_number,next_node[0],next_node[1],mat)
            max_path_long_list.append(max_path_long)
        return max(max_path_long_list)


def get_max_step(row_number,col_number,mat):
    max_step_list =[]
    for row in range(row_number):
        for col in range(col_number):
            one_step = max_step_node(row_number,col_number,row,col,mat)
            max_step_list.append(one_step)
    return max(max_step_list)

if __name__ == '__main__':
    row_number = 6
    col_number = 6
    data = [[32,  34,   7,  33,  21,   2],
                [13,  12,   3,  11,  26,  36],
                [16,  30,  22,  1,   24,  14],
                [20,  23,  25,  5,   19,  29],
                [27,  15,   9,  17,  31,   4],
                [ 6,  18,   8,  10,  35,  28]]
    print get_max_step(row_number,col_number,data)