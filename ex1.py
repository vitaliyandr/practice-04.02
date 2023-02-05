text_input = input()

print (text_input.title())

print (len(text_input))

count = 0
for i in range (0, len (text_input)):
    if text_input[i] in (".",",",";","-"):
        count = count + 1
print (count)

temp = 0
for h in range (0, len (text_input)):
    if text_input[h] in ("!"):
        temp = temp + 1
print (temp)
