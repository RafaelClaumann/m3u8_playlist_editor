import os

import app.services.groups_service as group_svc_import
import app.services.media_service as media_svc_import
from app import helpers
from config.config import Config
from view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
    media_svc = media_svc_import.MediaService(raw_media_list=raw_media_list)
    group_svc = group_svc_import.GroupsService(raw_media_list=raw_media_list)
    group_svc.join_media_on_groups(media_items=media_svc.media_items)

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
            channel_groups_menu.show_menu(groups_svc=group_svc)

        if choice == '2':
            os.system('clear')
            movies_group_menu.show_menu(groups_svc=group_svc)

        if choice == '3':
            os.system('clear')
            series_group_menu.show_menu(groups_svc=group_svc)

        if choice == '-1':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
