try:   # В конструкции try ьы уверены что фаил всегда закроется
    f = open("file.txt")
    print(f.read())
finally:
    f.close()
