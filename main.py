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
        while (notOpened):
            attempt = input("\nPlease enter the name of the .txt file you would like to input(with the .txt extension). Enter 'D' to view list of all files, or type 'Q' to quit: ")
            
            if (attempt == "D"):
                    if (len(fileList) != 0):
                        print(fileList)
                    else:
                        print("No Files. Why don't you add some?\n")
            
            elif (attempt == "Q"): quit = True

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

        print(f"Done!: {userFile}")



def quickUpdate(length, newFile):
    storedList = open("fileList.txt", "a")
    if  length == 0:
        storedList.write(f"{newFile}")
        return
    storedList.write(f"\n{newFile}")






if __name__ == "__main__":
    main()
