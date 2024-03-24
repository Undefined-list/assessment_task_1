Input = input("Enter what you want to check. ")
words = Input.split()
Hashtags = []
for x in words:
    hashtag = "#"
    if x[0] =="#":
        for y in x:
            if hashtag != "#":
                hashtag += y
                continue
            if y != "#":
                hashtag += y
        Hashtags.append(hashtag)
print(Hashtags)