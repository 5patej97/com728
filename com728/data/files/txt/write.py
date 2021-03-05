def search(file_path):
    print("searching.....")

    sections = ""
    books = "books:\n"


    with open(file_path) as file:
        for line in file:
            if line.startswith("section"):
                sections += line
            else:
                books += line

    print("done")

    return f"{sections}\n\n{books}"

def save(file_path, data):
    print("saving....")
    with open(file_path, "w") as file:
         file.write(data)
    print("done!")

def run():
    data = search("books.txt")
    save("books.txt", data)

run()