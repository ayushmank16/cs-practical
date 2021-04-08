def count_words():
    file = open("sample.txt","r")
    count=0
    for line in file :
        words=line.split()
        count += len(words )
    file.close()
    print("Number of words in the text file :", count)
    main()


def count_lines():
    a=open("sample.txt",'r')
    lines=0
    for line in a :
        lines+=1
    a.close()
    print("Number of lines in text file ",lines)
    main()


def count_char():
    f=open("sample.txt ",'r')
    num_char=0
    lines=f.read()
    for line in lines :
        num_char+=1
    f.close()
    print('number of lines in given file : ',num_char)
    main()


def main():
    print('''***********PROGRAMS FOR TEXT FILE***************
        1)COUNT WORDS                   
        2)COUNT LINES                   
        3)COUNT CHARACTERS     
''')
    choice = input("Enter Task No. > ")

    print("************************")
    if choice == '1':
        count_words()
    elif choice == '2':
        count_lines()
    elif choice == '3':
        count_char()
    else:
        print("Wrong choice..........")
        main()

main()

