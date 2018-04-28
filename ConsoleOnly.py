#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:46:32 2018

@author: mohamed morsy

@About: Implement Contiguous Allocation in memory, on console
        first fit - best fit allgorithim
"""
# ** memory size ** #
Memory_Size = input("Please enter your memory's size\n")
Memory_Size = int(Memory_Size)

# ** Free Table Creation ** #
Holes_Number = input("How many holes do you have? \n")
Holes_Number = int(Holes_Number)
print("""Enter data of your holes:
Starting_Address  Size_of_the_hole""")
# ^ Base register   ^ limit register

Free_Table = [[0 for x in range(2)] for y in range(Holes_Number)]
#                               ^ no of cols       ^ no of rows
i = 0
while i != Holes_Number:
    # Loop made to take values only inside the memory size declared
    # overlap detection >> not implemented till now >> in memory before allocation
    total = input()
    base, limit = total.split()
    base = int(base)
    limit = int(limit)
    if base + limit > Memory_Size:
        print("invalid address space, please re-enter the last value to be within your memory range!")
    else:
        Free_Table[i][0] = base
        Free_Table[i][1] = limit
        i += 1

# ** sort the Free_Table with starting address **#
Free_Table.sort(key=lambda x: x[0])

# ** Overlap Handling **#
i = 0
# i = Holes_Number          ???
# while i != i-1:           ???
Table_Size = Holes_Number - 1
while i != Table_Size:
    # To handle the overlapping problem
    if Free_Table[i][0] + Free_Table[i][1] > Free_Table[i + 1][0]:
        print("Due to hole entry number ", i + 2, ": ", Free_Table[i + 1][0], " ", Free_Table[i + 1][1], "\n",
              "The program won't work because of overlapping so it will be removed.")
        del Free_Table[i + 1]
        Table_Size -= 1
        i -= 1
    i += 1

print("your entry is:", Free_Table)
Table_Size += 1
# ** Memory before allocation ** #
Memory = list()
Memory.append(0)
for i in range(Table_Size):
    # print(i)
    if (Free_Table[i][0] == 0) and (i == 0):
        # first hole in memory is not at zero >> normally "OS place"
        Memory.append("Free")
        Memory.append(Free_Table[i][0] + Free_Table[i][1])
    elif (i > 0) and (Free_Table[i - 1][0] + Free_Table[i - 1][1] == Free_Table[i][0]):
        # not first hole but the last value "hole" ends exactly at the start of the this hole
        index = Memory.index(Free_Table[i - 1][0] + Free_Table[i - 1][1])
        Memory[index] = Free_Table[i][0] + Free_Table[i][1]
    else:
        Memory.append("Full")
        Memory.append(Free_Table[i][0])
        Memory.append("Free")
        Memory.append(Free_Table[i][0] + Free_Table[i][1])

# ** Choose the Algorithim ** #
Algorithim = input(""" Please choose your algorithim:
1: First Fit
2: Best Fit
""")
Algorithim = int(Algorithim)
# ** Number of processes and Process_Table ** #
Process_Number = input("How many processes do you have? \n")
Process_Number = int(Process_Number)
print("""Enter name and size of your processes:
Name  Size
Example:
Process1  100""")

processes = [[0 for x in range(2)] for y in range(Process_Number)]
#                              ^ no of cols       ^ no of rows
for i in range(Process_Number):
    total = input()
    name, limit = total.split()
    limit = int(limit)
    processes[i][0] = name
    processes[i][1] = limit

# ** Print the different cases of the memory after each input
# Memory before any allocation
print("memory before any allocation: ")
print(Memory)
# first memory case
i = 0
# when i increments >> one process allocated in memory.
# when i doesn't incement >> reallocation occured > repeat / or ignore this process: too big
while i != Process_Number:
    # Get all indices of holes in memory each iteration "Can change"
    Deallocate_flag = 1
    free_indices = [j for j, x in enumerate(Memory) if x == "Free"]
    # get all sizes of holes
    holes_sizes = []
    for j in free_indices:
        hole_size = Memory[j + 1] - Memory[j - 1]
        holes_sizes.append(hole_size)
    if Algorithim == 1:
        # First Fit Algorithim
        for j in free_indices:
            # Most of the times: we get j only once >> break @ case1 / 2
            hole_size = Memory[j + 1] - Memory[j - 1]
            if processes[i][1] < hole_size:
                Memory[j] = processes[i][0]  # this free space > process name
                process_limit = processes[i][1] + Memory[j - 1]  # end address of the process in memory
                Memory.insert(j + 1, process_limit)  # j: process_name  >  process_limit > hole_limit
                Memory.insert(j + 2, "Free")  # j: process_name  >  process_limit > Free > hole_limit
                Deallocate_flag = 0
                i += 1
                break
            elif processes[i][1] == hole_size:
                Memory[j] = processes[i][0]
                Deallocate_flag = 0
                i += 1
                break
            elif processes[i][1] > hole_size:
                Deallocate_flag = 1
                # continue to other indices

        # if the loop ends + Deallocate_flag == 1 >>> no room for this process & we need to deallocate a process
        if Deallocate_flag == 1:
            if i == 0 or processes[i][1] > max(holes_sizes):
                # first process is too big and can't replace with other processes "no other processes"
                print("This process ", processes[i][0], " can't be stored in memory\n")
                print("There are no other processes to deallocate so OS will ignore this process", processes[i][0],
                      "\n")
                i += 1

            else:
                # reallocating
                print("This process", processes[i][0], "with size ", processes[i][1], "has no space in memory\n")
                print(Memory, "\n")
                bad_entry = 1  # not a valid address
                while bad_entry:
                    Deallocate_process_start = input("Please deallocate a process from memory shown"
                                                     " by entering the starting address of the process: ")
                    Deallocate_process_start = int(Deallocate_process_start)
                    address = Memory.index(Deallocate_process_start)
                    try:
                        if (Memory[address + 1] == "Free") or (Memory[address + 1] == "Full"):
                            bad_entry = 1
                            print("Not a process address, please re-enter your address\n")
                            i += 0
                        else:
                            Memory[address + 1] = "Free"
                            bad_entry = 0
                            i += 1
                    except:
                        bad_entry = 1
                        print("Invalid address, please re-enter your address\n")
                        i += 0
        # print(Memory)

    elif Algorithim == 2:
        # Best Fit Algorithm
        Best_fit = min(holes_sizes)
        max_hole_size = max(holes_sizes)
        no_holes = holes_sizes.__len__()
        while processes[i][1] > Best_fit:
            # process size bigger than min value
            # make the min value maximum & get the next lowest value .. etc.
            holes_sizes[holes_sizes.index(min(holes_sizes))] = max(holes_sizes) + 1
            Best_fit = min(holes_sizes)
            no_holes -= 1
            if no_holes == -1:
                # to stop inifinte loop @ case1: no space in the holes in smaller than the process
                break

        if no_holes == -1:
            print("This process with size ", processes[i][1], "has no space in memory\n")
            print(Memory, "\n")
            choice = input("""Please choose:
             1: Deallocate 
             2: Remove this process\n""")
            choice = int(choice)
            if choice == 1:
                bad_entry = 1  # not a valid address
                while bad_entry:
                    Deallocate_process_start = input("Please deallocate a process from memory shown"
                                                     " by entering the starting address of the process: ")
                    Deallocate_process_start = int(Deallocate_process_start)
                    address = Memory.index(Deallocate_process_start)
                    try:
                        if (Memory[address + 1] == "Free") or (Memory[address + 1] == "Full"):
                            # tried to de-allocate a hole or an allocated place which is not a process
                            bad_entry = 1
                            print("Not a process address, please re-enter your address\n")
                            i += 0
                        else:
                            Memory[address + 1] = "Free"
                            bad_entry = 0
                            i += 1
                    except:
                        bad_entry = 1
                        print("Invalid address, please re-enter your address\n")
                        i += 0
            elif choice == 2:
                i += 1
        else:
            for j in free_indices:
                # print(j)
                if Memory[j+1] - Memory[j-1] == Best_fit:
                    # we found our j: starting index of the hole
                    break



        # j: index of the hole itself
        if processes[i][1] < Best_fit:
            Memory[j] = processes[i][0]  # this free space > process name
            process_limit = processes[i][1] + Memory[j - 1]  # end address of the process in memory
            Memory.insert(j + 1, process_limit)  # j: process_name  >  process_limit > hole_limit
            Memory.insert(j + 2, "Free")  # j: process_name  >  process_limit > Free > hole_limit
            Deallocate_flag = 0
            i += 1
        elif processes[i][1] == Best_fit:
            Memory[j] = processes[i][0]
            i += 1
    print(Memory)
