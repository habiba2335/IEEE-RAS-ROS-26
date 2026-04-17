import platform
from datetime import datetime

def log_system_info():
    os_type = platform.system()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"OS: {os_type}, Timestamp: {current_time}\n"
    
    with open("sys_log.txt", "a") as file:
        file.write(log_message)
    print("System info logged.")

def main():
    log_system_info()

if __name__ == "__main__":
    main()