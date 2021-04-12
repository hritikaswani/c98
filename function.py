def wordcountfromfile():
    fileName=input("ENTER THE FILE NAME : ")
    numberofwords=0
    file=open(fileName, 'r' )
    for i in file:
        words=i.split()
        numberofwords+=len(words)

    print('NUMBER OF WORDS : ')
    print(numberofwords)

wordcountfromfile()
