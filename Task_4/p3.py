def write_log(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")

def read_logs():
    try:
        with open("log.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No logs found.")

write_log("Observing Jupiter's moons")
write_log("Nebula filter applied")
read_logs()