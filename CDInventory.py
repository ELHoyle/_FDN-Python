#------------------------------------------#
# Title: CDInventory.py
# Desc: My wife doesn't believe love exists because
#       I worked on this all day on Valentine's Day 
# Change Log: 02-14-21 Updated by Eric Hoyle
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

menuChoice = '' 
cdTbl = []
cdRow = { } 
strFileName = 'CDInventory.txt' 
objFile = None
title='The Magic CD Inventory'

print('\t{0:*^26}'.format(title))
print()
while True:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    menuChoice = input('l, a, i, d, s or x: ').lower().strip()  # convert choice to lower case at time of input
    print()

    if menuChoice == 'x':
        break
    if menuChoice == 'l': #reads data from inventory file
        objFile=open(strFileName,'r')
        print("{:<10}{:30}{:30}".format('ID','Title','Artist'))
        for row in objFile:
            cdData = row.strip().split(',')
            cdRow={'ID':int(cdData [0]),'title':cdData[1],'artist':cdData[2]}
            cdTbl.append(cdRow)
            print("{:<10}{:30}{:30}".format(*cdRow.values()))
        objFile.close()
        print()
    elif menuChoice == 'a': #Adds data to inventory file
        cdID = int(input('Enter an ID: '))
        cdTitle = input('Enter the CD\'s Title: ')
        cdArtist = input('Enter the Artist\'s Name: ')
        cdRow={'ID':cdID,'title':cdTitle,'artist':cdArtist}
        print("\n{:<10}{:30}{:30} Status".format("ID", "Artist", "Album"))
        print("{:<10}{:30}{:30} ADDED".format(*cdRow.values()))
        print()
        cdTbl.append(cdRow)
    elif menuChoice == 'i': #displays current inventory data
        print("\n{:<10}{:30}{:30}".format("ID", "Artist", "Album"))
        for row in cdTbl:
            print("{:<10}{:30}{:30}".format(*row.values()))
        print()
    elif menuChoice == 'd': #deletes selected inventory data
        print("\n{:<10}{:30}{:30}".format("ID", "Artist", "Album"))
        for row in cdTbl:
            print("{:<10}{:30}{:30}".format(*row.values()))
        rowID = -1
        delEntry = int(input('\nPlease enter the ID of the entry you would like to delete: ').strip())
        for row in cdTbl:
            rowID+=1
            if row['ID'] == delEntry:
                print('\n',row)
                confirm=input('Are you sure you wish to delete this entry (Y/N)?: ')
                print()
                if confirm.lower().strip() == 'y':
                    del cdTbl[rowID]
                else: break
    elif menuChoice == 's':
        objFile = open(strFileName, 'w')
        for row in cdTbl:
            objFile.write("{},{},{}\n".format(*row.values()))
        objFile.close()
        print('Inventory file has been overwritten\n')
    else:
        print('Please choose either l, a, i, d, s or x!')

