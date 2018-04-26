#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 11:46:32 2018

@author: mohamed morsy

@About: Implement Contiguous Allocation in memory, on console
        first fit - best fit allgorithim
"""


def reallocation():
    flag = 0
    while flag == 0:
        print("Do you need to de-allocate any process in your memory ?")
        print(Memory)
        reallocate_descision = input("""1 : Yes
        2 : No""")
        reallocate_descision = int(reallocate_descision)
        if reallocate_descision == 0:
            pass
        elif reallocate_descision == 1:
            flag = 1
            process_size = Free_Table[i][1] - memory_sum  # (end adress - start address) of deallocated process
            while flag == 1:
                print("Choose enter the starting address of the block you want to deallocate (bigger size or equal):")
                print(Memory)
                reallocate_address = input()
                reallocate_address = int(reallocate_address)
                if (Memory[address + 2] - Memory[address]) < process_size:
                    print("wrong entry, choose again please")
                else:
                    flag = 0
            address = Memory.index(reallocate_address)  # TBChecked
            Memory[address + 1] = "Full"
            dealloc_process_end_address = Memory[address + 2]  # end adress of deallocated process
            Memory[address + 2] = int(Memory[address + 2]) - process_size
            # overrides !!! we need to create new places here
            Memory.insert(address + 3, "free")
            Memory.insert(address + 4, dealloc_process_end_address)
            # Memory[address + 3] = "free"
            # Memory[address + 4] = Dealloc_Process_EndAdd

# ** memory size ** #
Memory_Size = input("Please enter your memory's size")
Memory_Size = int(Memory_Size)

# ** Free Table Creation ** #
Holes_Number = input("How many holes do you have? \n")
Holes_Number = int(Holes_Number)
print("""Enter name and size of your processes:
Starting_Address  Size_of_the_hole""")
# ^ Base register   ^ limit register

Free_Table = [[0 for x in range(2)] for y in range(Holes_Number)]
#                               ^ no of cols       ^ no of rows
for i in range(Holes_Number):
    Memory_Size_Flag = 1
    while Memory_Size_Flag == 1:    # Loop made to take values only inside the memory size declared
        total = input()
        base, limit = total.split()
        base = int(base)
        limit = int(limit)
        Free_Table[i][0] = base
        Free_Table[i][1] = limit
        if Free_Table[i][0] + Free_Table[i][1] > Memory_Size:
            print("invalid address space, please re-enter the last value to be within your memory range!")
        else:
            Memory_Size_Flag == 0
# sort the Free_Table with starting address
Free_Table.sort(key=lambda x: x[0])
# print (Free_Table)

# ** Memory before allocation ** #
Memory = list()
Memory.append(0)
memory_sum = 0
for i in range (Holes_Number):
    memory_sum += Free_Table[i][0]
    # if (memory_sum + Free_Table[i][1]) < Memory_Size:
    if Free_Table[i][0] != 0:
        Memory.append("Full")
    Memory.append(memory_sum)
    Memory.append("Free")
    Memory.append(memory_sum + Free_Table[i][1])


# ** Choose the Algorithim ** #
Algorithim = input(""" Please choose your algorithim:
1: First Fit
2: Best Fit
""")
Algorithim = int(Algorithim)
# ** Number of processes and Process_Table ** #
Process_Number = input("How many processes do you have? \n")
Process_Number = int (Process_Number)
print ("""Enter name and size of your processes:
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


# This code is for entering a process "allocation" >> needs some adjustments to fit!
# memory_sum >> start value then end value of the current adress ^_^
'''
elif (memory_sum + Free_Table[i][1]) > Memory_Size:
    # message saying this process waits or cant be allocated and offer me to deallocate .. but after deallocation
    # I will have to enter it again to allocate it
    print("""The process can't be allocated, please deallocate some processes and enter this process again
    1 : Yes
    2 : No
    """)
    reallocateDescision = input()
    reallocateDescision = int(reallocateDescision)
    if reallocateDescision == 0:
        break
    elif reallocateDescision == 1:
        flag = 1
        Process_Size = Free_Table[i][1] - memory_sum  #  (end adress - start address) of deallocated process
        while flag == 1:
            print("Choose enter the starting address of the block you want to deallocate (bigger size or equal):")
            print (Memory)
            reallocateAddress = input()
            reallocateAddress = int(reallocateAddress)
            if (Memory[Address + 2] - Memory[Address]) < Process_Size:
                print("wrong entry, choose again please")
            else:
                flag = 0
        Address = Memory.index(reallocateAddress)  # TBChecked
        Memory[Address + 1] = "Full"
        Dealloc_Process_EndAddress = Memory[Address + 2]  # end adress of deallocated process
        Memory[Address + 2] = int (Memory[Address + 2]) - Process_Size
        # overrides !!! we need to create new places here
        Memory.insert(Address + 3, "free")
        Memory.insert(Address + 4, Dealloc_Process_EndAddress)
        # Memory[Address + 3] = "free"
        # Memory[Address + 4] = Dealloc_Process_EndAdd
    '''


# ** Print the different cases of the memory after each input

# ** Consider de-allocation in the code later + merging the spaces ** #
