def export(file_path, num_bots):
    print("exporting...")
    with open(file_path, "a") as file:
        for count in range(num_bots):
            print("please enter the  bot id:")
            id = int(input())

            print("please enter the  bot name:")
            name = input()

            print("please enter the  bot paint:")
            paint = input()

            data = f"{id}, {name}, {paint}"
            file.write(data)
    print("done!")

def run():
    export("bots.csv", 3)

run()