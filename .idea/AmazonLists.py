print "----------------------------------------------"
amazonList = []
amazonList.append("delta")
amazonList.append("alpha")
amazonList.append("fruit")
amazonList.append("charlie")
# Concatenate string and list
print ("Original: " + ','.join(amazonList))

amazonList.sort()
print ("Sorted: " + ','.join(amazonList))

amazonList.sort(reverse=True)
print ("Reverse: " + ','.join(amazonList))

print "List length " + str(len(amazonList))

i = 0
lastItem = amazonList[-1]
for item in amazonList:
    i = i + 1
    if item == lastItem:
        print "***** Last item reached ***** "
    print item

print "-----***-----"
for item in amazonList:
    #print "This stmt is inside loop"
    print item
print "**This stmt is outside loop**"