
i = 1
with open("log.txt") as f:
    while True:
        content = f.readline()
        if "python" in content.lower():
            print(f"yes python present at line {i} ")
            print (content, end="")
            
        i += 1
    

    
