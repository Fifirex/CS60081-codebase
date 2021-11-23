not10 = 0
start9 = 0
start8 = 0
start7 = 0
start6 = 0
total = 0

fileIn = open("database/pipalInput.txt", "r")
for line in fileIn:
    password = line.strip()
    if password.isnumeric():
        if len(password) != 10:
            not10 += 1
        else:
            if password[0] == "9":
                start9 += 1
            elif password[0] == "8":
                start8 += 1
            elif password[0] == "7":
                start7 += 1
            elif password[0] == "6":
                start6 += 1
            total += 1

fileIn.close()

print ("total   : " + str(total))
print ("not 10  : " + str(not10/total*100) + "%")
print ("start 9 : " + str(start9/total*100) + "%")
print ("start 8 : " + str(start8/total*100) + "%")
print ("start 7 : " + str(start7/total*100) + "%")
print ("start 6 : " + str(start6/total*100) + "%")
print (str(start9/total*100 + start8/total*100 + start7/total*100) + "%")
