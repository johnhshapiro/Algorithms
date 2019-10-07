read_file = open("./words.txt", "r")
write_file = open("./better_words.txt", "w+")
reader = read_file.readlines()
last_i = ""
for i in reader:
    if i.lower() != last_i:
        write_file.write(i.lower()[:-1] + ',\n')
    last_i = i.lower()