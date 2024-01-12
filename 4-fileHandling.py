def camelcase(filename, newfilename):                                          #defining function to capitalize first letters
    with open(filename, 'r') as file:                                          #opening given file to read contents
        content = file.read()                                                  #reading contents of file
        content = content.split(" ")                                           #converting into list
        new_content = ""
        for word in content:
            new_content += word.capitalize() + ' '                             #capitalizing each word
    with open(newfilename, 'w') as newfile:                                    #opening new file to write contents
        newfile.write(new_content)                                             #writing into new file

#function call with original file name and new file name as parameters        
camelcase('product_descriptions.txt', 'formatted_descriptions.txt')