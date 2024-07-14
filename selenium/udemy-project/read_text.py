with open('text.txt', 'r') as reader:
    content = reader.readlines()
    # Logic to reverse the content
    print(content)
    for i in range(len(content)//2):
        end = len(content)-1
        content[i], content[end-i] = content[end-i], content[i]
    with open('text.txt', 'w') as writer:
        for line in content:
            print(line)
            writer.write(line)
    print(content)

    