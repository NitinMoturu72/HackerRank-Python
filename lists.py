# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.


N = int(input())
cmd = []
my_list = []
for i in range(N):
    cmd.append(input())
# print(cmd)
for j in cmd:
    # print(j)
    indi_cmd = j.split()
    # print(indi_cmd)
    match (indi_cmd[0][0:3]):
        case 'ins':
            my_list.insert(int(indi_cmd[1]), int(indi_cmd[2]))
        case 'pri':
            print(my_list)
        case 'rem':
            my_list.remove(int(indi_cmd[1]))
        case 'app':
            my_list.append(int(indi_cmd[1]))
        case 'sor':
            my_list.sort()
        case 'pop':
            my_list.pop()
        case 'rev':
            my_list.reverse()