# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QDialog, QWidget, QMessageBox
import sys


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'About'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        QMessageBox.information(self, 'Message', """By Mohamed Morsy & Maged Mabrouk
        Github: https://github.com/M-Morsy/Memory_Allocation""")
        self.show()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Simulation"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 884)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(780, 10, 21, 771))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.ProgramGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ProgramGroupBox.setGeometry(QtCore.QRect(30, 60, 721, 731))
        self.ProgramGroupBox.setObjectName("ProgramGroupBox")
        self.ProcessGroupBox = QtWidgets.QGroupBox(self.ProgramGroupBox)
        self.ProcessGroupBox.setGeometry(QtCore.QRect(370, 230, 311, 421))
        self.ProcessGroupBox.setObjectName("ProcessGroupBox")
        self.ProcessesTable = QtWidgets.QTableWidget(self.ProcessGroupBox)
        self.ProcessesTable.setGeometry(QtCore.QRect(10, 30, 301, 341))
        self.ProcessesTable.setAutoFillBackground(True)
        self.ProcessesTable.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProcessesTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ProcessesTable.setRowCount(10)
        self.ProcessesTable.setColumnCount(2)
        self.ProcessesTable.setObjectName("ProcessesTable")
        item = QtWidgets.QTableWidgetItem()
        self.ProcessesTable.setItem(0, 0, item)
        self.add_row_process = QtWidgets.QPushButton(self.ProcessGroupBox)
        self.add_row_process.setGeometry(QtCore.QRect(10, 380, 115, 30))
        self.add_row_process.setObjectName("add_row_process")
        self.deallocate_process = QtWidgets.QPushButton(self.ProcessGroupBox)
        self.deallocate_process.setEnabled(False)
        self.deallocate_process.setGeometry(QtCore.QRect(160, 380, 115, 30))
        self.deallocate_process.setObjectName("deallocate_process")
        self.Start_Simulation = QtWidgets.QPushButton(self.ProgramGroupBox)
        self.Start_Simulation.setGeometry(QtCore.QRect(250, 670, 181, 30))
        self.Start_Simulation.setObjectName("Start_Simulation")
        self.FreeGroupBox = QtWidgets.QGroupBox(self.ProgramGroupBox)
        self.FreeGroupBox.setGeometry(QtCore.QRect(10, 230, 321, 421))
        self.FreeGroupBox.setObjectName("FreeGroupBox")
        self.FreeTable = QtWidgets.QTableWidget(self.FreeGroupBox)
        self.FreeTable.setGeometry(QtCore.QRect(10, 30, 301, 341))
        self.FreeTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.FreeTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.FreeTable.setRowCount(10)
        self.FreeTable.setColumnCount(2)
        self.FreeTable.setObjectName("FreeTable")
        item = QtWidgets.QTableWidgetItem()
        self.FreeTable.setItem(0, 0, item)
        self.add_row_hole = QtWidgets.QPushButton(self.FreeGroupBox)
        self.add_row_hole.setGeometry(QtCore.QRect(10, 380, 115, 30))
        self.add_row_hole.setObjectName("add_row_hole")
        self.EntryGroupBox = QtWidgets.QGroupBox(self.ProgramGroupBox)
        self.EntryGroupBox.setGeometry(QtCore.QRect(20, 40, 661, 121))
        self.EntryGroupBox.setObjectName("EntryGroupBox")
        self.SingleEntry_text = QtWidgets.QTextEdit(self.EntryGroupBox)
        self.SingleEntry_text.setGeometry(QtCore.QRect(10, 60, 221, 41))
        self.SingleEntry_text.setObjectName("SingleEntry_text")
        self.SignleEntry_label = QtWidgets.QLabel(self.EntryGroupBox)
        self.SignleEntry_label.setGeometry(QtCore.QRect(10, 30, 231, 22))
        self.SignleEntry_label.setObjectName("SignleEntry_label")
        self.Holes_Entry = QtWidgets.QTextEdit(self.EntryGroupBox)
        self.Holes_Entry.setGeometry(QtCore.QRect(250, 60, 161, 41))
        self.Holes_Entry.setObjectName("Holes_Entry")
        self.SignleEntry_label_2 = QtWidgets.QLabel(self.EntryGroupBox)
        self.SignleEntry_label_2.setGeometry(QtCore.QRect(250, 30, 231, 22))
        self.SignleEntry_label_2.setObjectName("SignleEntry_label_2")
        self.Processes_Entry = QtWidgets.QTextEdit(self.EntryGroupBox)
        self.Processes_Entry.setGeometry(QtCore.QRect(460, 60, 161, 41))
        self.Processes_Entry.setObjectName("Processes_Entry")
        self.SignleEntry_label_3 = QtWidgets.QLabel(self.EntryGroupBox)
        self.SignleEntry_label_3.setGeometry(QtCore.QRect(460, 30, 191, 22))
        self.SignleEntry_label_3.setObjectName("SignleEntry_label_3")
        self.label = QtWidgets.QLabel(self.ProgramGroupBox)
        self.label.setGeometry(QtCore.QRect(10, 170, 241, 51))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.ProgramGroupBox)
        self.label2.setGeometry(QtCore.QRect(370, 170, 241, 51))
        self.label2.setWordWrap(True)
        self.label2.setObjectName("label2")
        self.ProcessGroupBox.raise_()
        self.Start_Simulation.raise_()
        self.FreeGroupBox.raise_()
        self.label.raise_()
        self.label2.raise_()
        self.EntryGroupBox.raise_()
        self.Tivial_Title = QtWidgets.QLabel(self.centralwidget)
        self.Tivial_Title.setGeometry(QtCore.QRect(210, 10, 361, 22))
        self.Tivial_Title.setObjectName("Tivial_Title")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClick_Me = QtWidgets.QAction(MainWindow)
        self.actionClick_Me.setVisible(True)
        self.actionClick_Me.setObjectName("actionClick_Me")
        self.actionClick_Me_2 = QtWidgets.QAction(MainWindow)
        self.actionClick_Me_2.setObjectName("actionClick_Me_2")
        self.actionClick_Me_3 = QtWidgets.QAction(MainWindow)
        self.actionClick_Me_3.setObjectName("actionClick_Me_3")
        self.menuAbout.addAction(self.actionClick_Me_3)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Memory Allocation"))
        self.ProgramGroupBox.setTitle(_translate("MainWindow", "Main Program Body"))
        self.ProcessGroupBox.setTitle(_translate("MainWindow", "Processes:"))
        __sortingEnabled = self.ProcessesTable.isSortingEnabled()
        self.ProcessesTable.setSortingEnabled(False)
        self.ProcessesTable.setSortingEnabled(__sortingEnabled)
        self.add_row_process.setText(_translate("MainWindow", "Add Row"))
        self.deallocate_process.setText(_translate("MainWindow", "Dellocate"))
        self.Start_Simulation.setText(_translate("MainWindow", "Start Simulation"))
        self.FreeGroupBox.setTitle(_translate("MainWindow", "Free Table:"))
        __sortingEnabled = self.FreeTable.isSortingEnabled()
        self.FreeTable.setSortingEnabled(False)
        self.FreeTable.setSortingEnabled(__sortingEnabled)
        self.add_row_hole.setText(_translate("MainWindow", "Add Row"))
        self.EntryGroupBox.setTitle(_translate("MainWindow", "Single Entry:"))
        self.SignleEntry_label.setText(_translate("MainWindow", "Enter Memory Size here:"))
        self.SignleEntry_label_2.setText(_translate("MainWindow", "Holes Number"))
        self.SignleEntry_label_3.setText(_translate("MainWindow", "Processes\' Number"))
        self.label.setText(_translate("MainWindow", "Put your free memory spaces in free table"))
        self.label2.setText(_translate("MainWindow", "Put processes names and sizes  in processes table"))
        self.Tivial_Title.setText(_translate("MainWindow", "Memory Contiguous Allocation Simulation"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionClick_Me.setText(_translate("MainWindow", "Click Me"))
        self.actionClick_Me_2.setText(_translate("MainWindow", "Click Me"))
        self.actionClick_Me_3.setText(_translate("MainWindow", "Click Me"))

        self.actionClick_Me_3.triggered.connect(self.open_about_window)
        self.Start_Simulation.clicked.connect(self.start_simulation)
        #self.add_row_hole.clicked.connect(self.add_row_table())
        #self.add_row_process.clicked.connect(self.add_row_table())

    def open_about_window(self):
        ex = About()

    def start_simulation(self):
        # get data and make algorithim
        no_rows = self.FreeTable.rowCount()
        no_cols = self.FreeTable.columnCount()
        Free_Table = [[0 for x in range(no_cols)] for y in range(no_rows)]
        for i in range(no_rows):
            for j in range(no_cols):
                try:
                    Free_Table[i][j] = self.FreeTable.item(i, j).text()
                except:
                    Free_Table[i][j] = 0
                    pass
        print(Free_Table)
        no_rows = self.ProcessesTable.rowCount()
        no_cols = self.ProcessesTable.columnCount()
        processes = [[0 for x in range(no_cols)] for y in range(no_rows)]
        for i in range(no_rows):
            for j in range(no_cols):
                try:
                    processes[i][j] = self.ProcessesTable.item(i, j).text()
                except:
                    processes[i][j] = 0
                    pass
        print(processes)

        Memory_Size = self.SingleEntry_text.toPlainText()
        Memory_Size = int(Memory_Size)

        Holes_Number = self.Holes_Entry.toPlainText()
        Holes_Number = int(Holes_Number)

        Process_Number = self.Processes_Entry.toPlainText()
        Process_Number = int(Process_Number)

        self.algorithim(Memory_Size, Holes_Number, Process_Number, Free_Table, processes)

    def algorithim (Memory_Size, Holes_Number, Process_Number, Free_Table, processes):
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
                    if i == 0:
                        # first process is too big and can't replace with other processes "no other processes"
                        print("This process ", processes[i][0], " can't be stored in memory\n")
                        print("There are no other processes to deallocate so OS will ignore this process",
                              processes[i][0], "\n")
                        i += 1

                    else:
                        # reallocating
                        print("This process", processes[i][0], "with size ", processes[i][1],
                              "has no space in memory\n")
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
                print(Memory)

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
                        if Memory[j + 1] - Memory[j - 1] == Best_fit:
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
        pass


'''
        def add_row_table(self):
            no_rows = self.FreeTable.rowCount()
            no_cols = self.FreeTable.columnCount()
            data = [[0] * no_cols] * no_rows
            data = [[0 for x in range(no_cols)] for y in range(no_rows)]
            for i in range(no_rows):
                for j in range(no_cols):
                    try:
                        data[i][j] = self.FreeTable.item(i, j).text()
                    except:
                        data[i][j] = 0
                        pass

            no_rows = self.ProcessesTable.rowCount()
            no_cols = self.ProcessesTable.columnCount()
            data = [[0] * no_cols] * no_rows
            data = [[0 for x in range(no_cols)] for y in range(no_rows)]
            for i in range(no_rows):
                for j in range(no_cols):
                    try:
                        data[i][j] = self.ProcessesTable.item(i, j).text()
                    except:
                        data[i][j] = 0
                        pass

            self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
            self.tableWidget.setGeometry(QtCore.QRect(50, 170, 231, 341))
            self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.tableWidget.setRowCount(no_rows + 1)
            self.tableWidget.setColumnCount(2)
            self.tableWidget.setObjectName("tableWidget")
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(0, 0, item)
            MainWindow.show()
'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
