from pathlib import Path #Path class from pathlib is used to work with file and folder paths 
#Path(folder or folders) / fileName > / means join
#Path() create a path object
data_file = Path("data") / "students.txt"
print(data_file) #path of the file > data/students.txt
print(data_file.name) #name of the file
print(data_file.suffix) #suffix of the file

data_dir = Path("data")
data_dir.mkdir(exist_ok=True) #mkdir() creates this dir if it doesn't exist
#mkdir(parents=True, exist_ok=True) > parents=True creates any missing parent directories
data_file = data_dir / "students.txt" #concatenate path and file name
print(data_dir.is_dir()) #is_dir() checks if the dir is a directory
print(data_file.exists()) #exists() checks if the file exists

#"r" read an existing file
#"w" write and replace content
#!"a" append after existing content
#!"x" create only when absent
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")

path = Path("notes.txt")
with path.open("r", encoding="utf-8") as file:
    content = file.read() #read() return one string
print(content)
print(file.closed) #.closed 

same_text = path.read_text(encoding="utf-8") #read_text() 
print(content == same_text)

path = Path("data/students.txt")
with path.open("r", encoding="utf-8") as file:
    for line in file:
        name = line.strip()
        if name:
            print(name)

with path.open("w", encoding="utf-8") as file:
    count = file.write("Sara\nAli\n")
print(count)

path = Path("activity.log") #.log
with path.open("a", encoding="utf-8") as file:
    file.write("Student enrolled: Sara\n")
print("Activity saved")

names = ["Sara", "نورة", "Ali"]
text = "\n".join(names) + "\n"
Path("data/students.txt").write_text(text, encoding="utf-8")