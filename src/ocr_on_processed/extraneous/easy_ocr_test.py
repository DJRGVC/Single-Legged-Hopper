import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('slide_256_image_1.png', detail = 10)

# save result to a text file
with open('result.txt', 'w') as f:
    for line in result:
        f.write(line[1] + '\n')

# print result
for line in result:
    print(line[1])

