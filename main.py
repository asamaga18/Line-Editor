import myDoublyLinkedList as DLL

def main():

    # This block populates fileList with all the file names stored in fileList.txt 
    fileList = set()
    storedList = open("fileList.txt", "r")
    for line in storedList:
        if "\n" in line:
            line = line.rstrip("\n")
        fileList.add(line)
    storedList.close

    # Menu Loop
    quit = False
    while (not quit):
        opened = False
        userFile = None

        while (not (quit or opened)):
            attempt = input("\nPlease enter the name of the .txt file you would like to input(with the .txt extension). Enter 'D' to view list of all files, or type 'Q' to quit: ")

            # List View of Files
            if (attempt == "D"):
                if (len(fileList) != 0):
                        print(fileList)
                else:
                    print("No Files. Why don't you add some?\n")
                
            # Exit Statement
            elif (attempt == "Q"):
                quit = True
                break

            # If valid file name
            elif (".txt" in attempt and attempt[-4:] == ".txt"):

                # If file is not in the file
                if attempt not in fileList:
                    confirm = input("This file does not exist yet. Would you like to create it? Y to confirm or anything else to go back: ")
                    if (confirm == "Y"):
                        userFile = open(attempt, "x")
                        #quickUpdate(len(fileList), attempt)
                        opened = True

                # If file is in the file list
                else:
                    userFile = open(attempt, "a")
                    opened = True

            # Invalid Input
            else:
                print("Please include a .txt at the end.\n")

        # File Name is correct and needs to be opened
        if (opened):
            opened = False
            print(f"\nOpening {userFile.name}")
            userList = fileToDLL(userFile.name)

            userList.printList()
            print("\n")


            # start file menu loop
            fileExit = False
            currLine = userList.getHead()
            #print(f"Head is: {currLine.data}")  #-debug line
            printFileMenu()
            while (not fileExit):
                
                cmd = input(f"Line(enter 'help' for menu): {currLine.data}\nCommand: ")


                # quit (q)
                if (cmd.strip() == "q"):
                    fileExit = True
                    break
                
                # delete (d)
                elif (cmd.strip() == "d"):
                    tempNode = currLine.next

                    if (userList.deleteNode(currLine)):
                        currLine = tempNode
                        print("Deleted")

                # forward (f)
                elif (cmd.strip() == "f"):
                    currLine = userList.getNext(currLine)
                
                # backward (b)
                elif (cmd.strip() == "b"):
                    currLine = userList.getPrev(currLine)

                # head (h)
                elif (cmd.strip() == "h"):
                    currLine = userList.getHead

                # tail (t)
                elif (cmd.strip() == "t"):
                    currLine = userList.getTail

                # insert (i)
                elif (cmd.strip() == "i"):
                    pass

                # print (p)
                elif (cmd.strip() == "p"):
                    userList.printList()

                # length
                elif(cmd.strip() == "l"):
                    pass 
                
                # help menu
                elif(cmd.strip() == "help"):
                    printFileMenu()
                    print("\n")

                    







# Takes a  valid filename as input and returns a DLL 
def fileToDLL (fileName):
    textFile = open(fileName, "r")
    list = DLL.DoublyLinkedList()

    for line in textFile:
        list.insertLast(line)
    
    textFile.close()

    return list

def printFileMenu():
    print("+-----------------MENU-----------------+")
    print("|                                      |")
    print("|'q'          Quit the program         |")
    print("|'d'          Delete Line              |")
    print("|'f'          Move Forward             |")
    print("|'b'          Move Backward            |")
    print("|'h'          Move to First Line       |")
    print("|'t'          Move to Last Line        |")
    print("|'i'          Insert Line after current|")
    print("|'p'          Print File               |")
    print("|'l'          Length of List           |")
    print("+--------------------------------------+")

if __name__ == "__main__":
    main()