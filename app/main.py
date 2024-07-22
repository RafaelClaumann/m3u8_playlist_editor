import argparse
import os

import app.services.media_service as media_svc_import
import app.services.parse_service as parse_svc
from app import helpers
from config.config import Config
from config.logging_config import configure_logging
from view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    configure_logging(args.debug)

    raw_media_list = helpers.read_file(file_path=Config.INPUT_PLAYLIST_PATH)
    parsed_media_list = parse_svc.parse_raw_list(raw_list=raw_media_list)
    media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

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
            channel_groups_menu.show_menu(media_svc=media_svc)

        if choice == '2':
            os.system('clear')
            movies_group_menu.show_menu(media_svc=media_svc)

        if choice == '3':
            os.system('clear')
            series_group_menu.show_menu(media_svc=media_svc)

        if choice == '-1':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
