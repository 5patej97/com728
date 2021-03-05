def search(file_path):
    print("searching.....")
    with open(file_path) as file:
        for location in file:
             print(f"looked in {location.strip()}")
    print("done!")

def run():
    search("library.txt")


run()

