# Задача "Золотой песок" acmp.ru
def list_in_int(self):
    global int_list
    int_list =[]
    for i in self:
        i = int(i)
        int_list.append(i)
    return int_list


inp_list = list(input().split(','))
list_in_int(inp_list)

list_p = [int_list[0] ,int_list[1] ,int_list[2]]
list_v = [int_list[3] ,int_list[4], int_list[5]]
list_p.sort()
list_v.sort()
list_c = [list_p[0]*list_v[0],list_p[1]*list_v[1],list_p[2]*list_v[2]]
print(sum(list_c))