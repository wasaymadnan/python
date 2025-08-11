jvote = 0
avote = 0
svote = 0

vote = input ("Please enter voter's name : ")
if vote == "john":
    jvote = jvote + 1
elif vote == "adam":
    avote = avote + 1
elif vote == "sam":
    svote = svote + 1
else:
    print ("Please enter a valid entry!")

print ("john total vote :",jvote)
print ("adam total votes :",avote)
print ("sam total vote :",svote)