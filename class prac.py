words = "?name=Bob&age=99&day=Wed".split()

for i in range(len(words)):
    words[i] = words[i].title()
text = ','.join(words)
print(text)
