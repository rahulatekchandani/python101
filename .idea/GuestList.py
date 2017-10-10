
def printInvites(glist):
    print "--**--"
    for g in glist:
        print "Welcome "+ g
    print "--**--"

guestList = ['Mike Butterworth','Mark Carson','Kiet Pham']
#print guestList
printInvites(guestList)

print "Kiet cant make it :("
del guestList[2]
#print guestList
printInvites(guestList)

print "Sid will be invited instead :)"
guestList.append("Sid Paliwal")
#print guestList
printInvites(guestList)

print "Invite family first"
guestList.insert(0,"Dad")
guestList.insert(2,"Sam")
#print guestList
printInvites(guestList)

print guestList.__len__()

print "Too many guests! Remove until two left"

for i in guestList:
    #print guestList.__len__()
    #print guestList.pop()
    guestList.pop()
    if guestList.__len__() == 2:
        #print "Loop "+ str(guestList.__len__())
        break

printInvites(guestList)

