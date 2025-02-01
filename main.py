import myDoublyLinkedList as DLL

def main():
    fileList = set()
    storedList = open("fileList.txt", "r" )

    for line in storedList:
        if "\n" in line:
            line = line.rstrip("\n")
        fileList.add(line)

    storedList.close()
    quit = False

    while (not quit):
        notOpened = True
        userFile = None
        
        while (notOpened and not quit):
            attempt = input("\nPlease enter the name of the .txt file you would like to input(with the .txt extension). Enter 'D' to view list of all files, or type 'Q' to quit: ")
            
            if (attempt == "D"):
                    if (len(fileList) != 0):
                        print(fileList)
                    else:
                        print("No Files. Why don't you add some?\n")
            
            elif (attempt == "Q"): 
                quit = True
                break

            elif (".txt" in attempt and attempt[-4:] == ".txt"):

                if attempt not in fileList:
                    confirm = input("This file does not exist yet. Would you like to create it? Y to confirm or anything else to go back: ")
                    if (confirm == "Y"):
                        userFile = open(attempt, "x")
                        quickUpdate(len(fileList), attempt)
                        notOpened = False

                else:
                    userFile = open(attempt, "a")
                    notOpened = False

            else:
                print("Please include a .txt at the end.\n")


        if (not quit):
            notOpened = False
            print(f"\nOpening {userFile.name}")
            userList = fileToDLL(userFile.name)
            #userList.printList()

            fileExit = False

            currLine = userList.getHead() #.next.next
            
            userList = insertHeader(userList)
            print(f"The head is {userList.getHead().data}")

            while (not fileExit):
                cmd = input(f"Line(enter 'help' for menu): {currLine.data}\nCommand: ")
                #need to add verification to check for first and last file.

                if (cmd.strip() == "q"):
                    fileExit = True

                elif (cmd.strip() == "d"):
                    if (not currLine.isEdge()):
                        (userList, currLine) = deleteLine(userList, currLine)
                    else:
                        print("You Cannot Delete this File.\n")

                elif (cmd.strip() == "f"):
                    pass

                elif (cmd.strip() == "b"):
                    pass

                elif (cmd.strip() == "h"):
                    pass

                elif (cmd.strip() == "t"):
                    pass

                elif (cmd.strip() == "i"):
                    pass

                elif (cmd.strip() == "p"):
                    userList.printList()
                
                elif (cmd.strip() == "l"):
                    print(f"Length of Textfile: {userList.getLength()} lines.")

                elif (cmd.strip() == "help"):
                    pass
            

                #test
                #update
                test = open(userFile.name, "w")
                
                userList = removeHeader(userList)
                curr = userList.head

                while curr is not None:
                    test.write(curr.data)
                    curr = curr.next

                #userList = insertHeader(userList)


            print("exited file\n")

                

                



    
    print("exited editor")








def fileToDLL(textFileName):
    textFile = open(textFileName, "r")
    list = DLL.DoublyLinkedList()

    for line in textFile:
        list.insertLast(line)
    
    textFile.close()
    return list



def quickUpdate(length, newFile):
    storedList = open("fileList.txt", "a")
    if  length == 0:
        storedList.write(f"{newFile}")
        return
    storedList.write(f"\n{newFile}")


def insertHeader(tempList):
    tempList.insertFirst("BEGINNING OF FILE.\n")
    tempList.insertLast("\nEND OF FILE.")
    return tempList

def removeHeader(tempList):
    tempLine = None
    (result, tempLine) = deleteLine(tempList, tempList.getHead())
    (result, tempLine) = deleteLine(result, tempList.getTail())
    return result

def deleteLine(tempList, tempLine):
    temp = tempLine.deleteNode()
    tempList.deleteNode(tempLine)  # Add this line to update the list
    tempLine = temp
    return (tempList, tempLine)

if __name__ == "__main__":
    main()
