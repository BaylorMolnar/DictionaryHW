text_file = open("text.txt", "r")


dict = {}

for line in text_file:
    line = line.lower()
    line = line.strip()
    spaces = line.split(" ")
    for word in spaces:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

# print(dict)
for TextWord in dict.keys():
    print(TextWord.rstrip(".,"), ":", dict[TextWord])
