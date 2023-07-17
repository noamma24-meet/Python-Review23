def createvid(title, description):
	vidiction={"title":title, "description":description, "like":0, "dislike":0, "comments":{}}
	return(vidiction)

def likestuff(vidiction):
	if "like" in vidiction:
		vidiction["like"]=vidiction["like"]+1
	return vidiction

def dislikestuff(vidiction):
	if "dislike" in vidiction:
		vidiction["dislike"]+=1
	return vidiction


def addcomment(vidiction,username,text):
	vidiction["comments"]={username:text}
	return vidiction


x=createvid("hilatheking","hila is the king")
likestuff(x)
dislikestuff(x)
addcomment(x,"noam","hila very good!")
print(x)

while x["like"]<495:
    likestuff(x)

print(x)
