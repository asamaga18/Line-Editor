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
                        quickUpdate(attempt)
                        userFile = open(attempt, "x")
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
            if currLine == None:
                currLine = userList.getDummyHead()
            #print(f"Head is: {currLine.data}")  #-debug line
            printFileMenu()
            while (not fileExit):
                print(f"\nLine(enter 'help' for menu): {currLine.data}")
                cmd = input("Command: ")


                # quit (q)
                if (cmd.strip() == "q"):
                    DLLToFile(userList, userFile.name)
                    fileExit = True
                    print(f"Saving and Exiting {userFile.name}")
                    break
                
                # delete (d)
                elif (cmd.strip() == "d"):
                    tempNode = currLine.prev

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

                    newLine = input("What Line would you like to input?: ")

                    if (not userList.insertAt(newLine + "\n", currLine)):
                        print("Cannot Insert At This Location")
                    else:
                        print("Added!")
                        currLine = currLine.next

                # print (p)
                elif (cmd.strip() == "p"):
                    userList.printList()
                    

                # length (l)
                elif(cmd.strip() == "l"):
                    print(f"Length of the File is {userList.getLength} Lines.") 
                
                # save (s)
                elif(cmd.strip() == "s"):
                    DLLToFile(userList, userFile.name)


                # help menu (help)
                elif(cmd.strip() == "help"):
                    printFileMenu()
                
                else:
                    print("Invalid Input.")
                

                
                    

                    


# Takes a valid DLL and filename and updates the file
def DLLToFile (listName, fileName):
    textFile = open(fileName, "w")

    currNode = listName.getHead()

    while (currNode != listName.getTail()):
        textFile.write(currNode.data)
        currNode = currNode.next
    
    textFile.close()



# Takes a  valid filename as input and returns a DLL 
def fileToDLL (fileName):
    textFile = open(fileName, "r")
    list = DLL.DoublyLinkedList()

    for line in textFile:
        list.insertLast(line)
    
    textFile.close()

    return list

# prints out the menu
def printFileMenu():
    print("+-----------------MENU-----------------+")
    print("|                                      |")
    print("|'q'          Save and Quit            |")
    print("|'d'          Delete Line              |")
    print("|'f'          Move Forward             |")
    print("|'b'          Move Backward            |")
    print("|'h'          Move to First Line       |")
    print("|'t'          Move to Last Line        |")
    print("|'i'          Insert Line After Current|")
    print("|'p'          Print File               |")
    print("|'l'          Length of List           |")
    print("|'s'          Save File                |")
    print("+--------------------------------------+")

# updates storage txt file with new filename
def quickUpdate(newFileName):
    textFile = open("fileList.txt", "a")
    textFile.write("\n" + newFileName)
    textFile.close()



if __name__ == "__main__":
    main()