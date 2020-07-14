from tagsList import Tags
w = input ("Enter your text bro")

def getTags(list_of_keywords):
	tags = Tags['words']

	for key in list_of_keywords:
		for tag in Tags[key]:
			tags.append(tag)

	return list(set(tags))

def getHashTagString(list_of_tags):
	hashTagString = ""

	for tag in list_of_tags:
		hashTagString += "#" + w + tag

	return hashTagString

if __name__ == '__main__':
	import sys
	print(getHashTagString(getTags(sys.argv[1:])).strip() )