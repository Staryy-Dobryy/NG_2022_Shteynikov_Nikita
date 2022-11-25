from rich.console import Console
import os

def returnBlackList():
    blackListOptions = (7, 22, 26, 30, 33, 38) #8 23 27 31 34 39
    return blackListOptions

def parserSysInfo(target):
    try:
        if target <= 7:
            systeminfo = open("systeminfo.txt", "r", encoding="IBM866")
            systeminfo.close()
        else:
            biginfo = open("biginfo.txt", "r", encoding="utf-16")
            biginfo.close()
    except:
        if target <= 7:
            os.system("systeminfo>systeminfo.txt")
        else:
            os.system("msinfo32 /report biginfo.txt")

    match target:
        case 0:
            os.system("wmic cpu get name")
        case 1:
            dataFile = open("systeminfo.txt", "r", encoding="IBM866")
            fileContents = dataFile.readlines()
            line = int(fileContents[15][-3]) + 23
            index = 0
            print("\n[RAM]")
            while index < 5:
                print(fileContents[line], end="")
                line += 1
                index += 1
            dataFile.close()
        case 2:
            os.system("echo %PROCESSOR_ARCHITECTURE%")
        case 3:
            line = 15
            dataFile = open("systeminfo.txt", "r", encoding="IBM866")
            fileContents = dataFile.readlines()
            CPUcount = int(fileContents[line][-3])
            CPUindex = 0
            while fileContents:
                print(fileContents[line], end="")
                if CPUindex == CPUcount: break
                line += 1
                CPUindex += 1
            dataFile.close()
        case 4:
            dataFile = open("systeminfo.txt", "r", encoding="IBM866")
            fileContents = dataFile.readlines()
            line = 2
            index = 0
            print("\n[OS]")
            while index < 5:
                print(fileContents[line], end="")
                line += 1
                index += 1
            dataFile.close()
        case 5:
            dataFile = open("systeminfo.txt", "r", encoding="IBM866")
            fileContents = dataFile.readlines()
            line = 12
            index = 0
            print("\n[SYSTEM]")
            while index < 3:
                print(fileContents[line], end="")
                line += 1
                index += 1
            dataFile.close()
        case 6:
            dataFile = open("systeminfo.txt", "r", encoding="IBM866")
            fileContents = dataFile.readlines()
            line = 15 + int(fileContents[15][-3]) + 1
            print("\n[BIOS]")
            print(fileContents[line])
            dataFile.close()
        case _:
            if target in returnBlackList(): target += 1
            dataFile = open("biginfo.txt", "r", encoding="utf-16")
            fileContents = dataFile.readlines()
            index , option = 0, 0
            for line in fileContents:
                if "[" in line[0]: option += 1
                if "[" in line[0] and option == target - 5:
                    index = fileContents.index(line)
                    break
            while fileContents: 
                if "[" in fileContents[index+1][0]: break
                print (fileContents[index], end="")
                index += 1
            dataFile.close()

def printSysInfo(optionsList):
    for index in range(len(optionsList)):
        if list(optionsList.values())[index] == True:
            Console().rule()
            parserSysInfo(index)
    exit()

def checkBoxes(item):
    if item == True: return "@"
    else: return "u"

def editCheckBox(optionsList, option):
    def valueHendler():

        # To avoid distortion
        blackList = returnBlackList() 
        item = list(optionsList).index(list(optionsList.keys())[option - 1])
        if item in blackList:
            if item + blackList.index(item) in blackList and blackList.index(item) != 0: return -1 - blackList.index(item)
            else:
                if item + blackList.index(item) + 1 in blackList and blackList.index(item) != 0: return -1 - blackList.index(item)
                else: return 0 - blackList.index(item)
        else:
            index = 0
            while index < len(blackList):
                if item < blackList[index]:
                    if item + blackList.index(blackList[index]) in blackList: return 0 - blackList.index(blackList[index])
                    else:
                        if item + blackList.index(blackList[index]) > blackList[index]: 
                            if blackList[index] == blackList[-1]: return 1 - len(blackList)
                            index += 1; continue
                        else: return 1 - blackList.index(blackList[index])
                index += 1
        
    blackList = returnBlackList()
    if option == len(optionsList) + 1 - len(blackList): printSysInfo(optionsList)
    elif optionsList[list(optionsList.keys())[option - valueHendler()]] == False:
        optionsList[list(optionsList.keys())[option - valueHendler()]] = True
    else: optionsList[list(optionsList.keys())[option - valueHendler()]] = False

def printOptions(_list):
    os.system("cls")
    Console().rule("[bold red] Options list")
    keys = list(_list.keys())
    values = list(_list.values())
    iterator, index = 0, 0
    while iterator < len(_list):
        if iterator in returnBlackList():
            iterator += 1
            continue 
        print(f"{index + 1}. {keys[iterator]}\t[ {checkBoxes(values[iterator])} ]")
        index += 1
        iterator += 1
    print(f"{index + 1}. Proceed")

def menu():
    optionsList = {"CPU             " : False, 
                   "RAM             " : False,
                   "Architecture    " : False, 
                   "CPU Family      " : False,
                   "OS              " : False,
                   "SYSTEM          " : False,
                   "BIOS            " : False,
                   8 : False, #Black list option
                   "Conflicts & Sharing" : False,
                   "DMA channel     " :  False,
                   "Feedback equipment" : False,
                   "Input-Output    " : False,
                   "Interrupts (IRQs)" : False,
                   "Memory          " : False,
                   "Components      " : False,
                   "Multimedia      " : False,
                   "Audio codecs    " : False,
                   "Video codecs    " : False,
                   "CD-ROM          " : False,
                   "Sound device    " : False,
                   "Display/VRAM    " : False,
                   "Infrared devices" : False,
                   23 : False, #Black list option
                   "Keyboard        " : False,
                   "Pointing device " : False,
                   "Modem           " : False,
                   27 : False, #Black list option
                   "Network-Adapter " : False,
                   "Network-Protocol" : False,
                   "Network-WinSock " : False,
                   31 : False, #Black list option
                   "Ports-Consistent" : False,
                   "Ports-Parallel  " : False,
                   34 : False, #Black list option
                   "Disks           " : False,
                   "Disk partitions " : False,
                   "SCSI            " : False,
                   "IDE             " : False,
                   39 : False, #Black list option
                   "Problem divises " : False,
                   "USB             " : False,
                   "System drivers  " : False,
                   "Tasks in progress" : False,
                   "Auto load programs" : False, 
                   "OLE Registration" : False}
    while True:
        printOptions(optionsList)
        try:
            editCheckBox(optionsList, int(input("\n>>> ")))
        except:
            print("\nERROR: Invalid value!")
            exit()

menu()


