try:
    with open("DOB.txt", "r") as f:
        lines = f.readlines()

    with open("new_DOB.txt", "w") as f:
        f.write("Name" + "\n")
        for line in lines:
            parts = line.strip().split(" ")
            name = ' '.join(parts[:2])
            f.write(name + "\n")
            
        f.write("\n" "Birthdate" + "\n")        
        for line in lines:
            parts = line.strip().split(" ")
            birthday = ' '.join(parts[2:])
            f.write(birthday + "\n")
            
except IOError as e:
    print(e)