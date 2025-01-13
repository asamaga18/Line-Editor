def main():

    fileInput = input("What is the name of the file? (include the .txt)")

    try:
        newFile = open(fileInput, "r")
        print("worked")

    except:
        print("didnt work")







if __name__ == "__main__":
    main()
