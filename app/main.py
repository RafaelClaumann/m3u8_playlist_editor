import os
from config.config import Config
from services import services
from view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    svc = services.Services(Config.INPUT_PLAYLIST_PATH)

    while True:
        print("Choose an option to work with:")
        print(" 1. Channels")
        print(" 2. Movies/Vod")
        print(" 3. Series")
        print("-1. Exit")

        choice = input("Enter the number of the desired option: ")
        print()

        if choice == '1':
            os.system('clear')
            channel_groups_menu.show_menu(svc)

        if choice == '2':
            os.system('clear')
            movies_group_menu.show_menu(svc)

        if choice == '3':
            os.system('clear')
            series_group_menu.show_menu(svc)

        if choice == '-1':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
