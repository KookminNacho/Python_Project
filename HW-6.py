try:
    rnumbernote = open("contact.txt", 'r')
    print("읽기 성공")
except:
    wnumbernote = open("contact.txt", 'w')
    print("만듬")
    rnumbernote = open("contact.txt", 'r')

namedat, numdat = input("").split()

