import os

def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        pass

def save_credentials(username, password, folder_path):
    create_folder(folder_path)
    credentials_file_path = os.path.join(folder_path, 'credentials.txt')
    with open(credentials_file_path, 'a') as file:
        file.write(f"Username: {username}, Password: {password}\n")

def main():
    folder_path = 'user_data'
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    try:
        save_credentials(username, password, folder_path)
        print(f"Логин и пароль сохранены в {folder_path}/credentials.txt.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
