from bPlusTree import bPlusTree
import sys

def printError(msg):
    print("\033[91m {}\033[00m".format(msg))
    print()

def handleQuery(bpt, query, param1, param2=None):
    query = query.upper()
    if query == "INSERT":
        bpt.insert(param1)
    elif query == "FIND":
        bpt.search(param1)
    elif query == "COUNT":
        bpt.countKey(param1)
    elif query == "RANGE":
        bpt.range(param1,param2)
    else:
        printError("Query not supported")

def getQueries(bpt, fileName):
    # try:
        with open(fileName, "r") as f:
            while True:
                l= f.readline()
                if not l:
                    break
                l=l.strip('\n').split(' ')
                if len(l) == 3:
                    query = l[0]
                    param1 = int(l[1])
                    param2 = int(l[2])
                    handleQuery(bpt, query, param1, param2)
                elif len(l) == 2:
                    query = l[0]
                    param1 = int(l[1])
                    handleQuery(bpt,query, param1)
                else:
                    printError("Wrong query format. Supported queries:")
                    print("1. INSERT X \n 2. COUNT X. \n 3. FIND X \n 4. RANGE X Y \n")     
    # except Exception as E:
    #     print(E)

def main():
    if len(sys.argv) != 2:
        printError("Error: syntax to run program: python3 drive.py <QueryFileName>")
    fileName = sys.argv[1]
    bpt = bPlusTree(3)
    bpt.openFile()
    getQueries(bpt, fileName)
    bpt.closeFile()
main()
