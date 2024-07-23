import argparse
import os

import helpers
import models.group as group_model
import services.media_service as media_svc_import
import services.parse_service as parse_svc
from config.config import Config
from config.logging_config import configure_logging
from view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    configure_logging(args.debug)

    raw_media_list = helpers.read_file(file_path=Config.INPUT_PLAYLIST_PATH)
    parsed_media_list = parse_svc.parse_raw_list(raw_media_list=raw_media_list)
    media_svc = media_svc_import.MediaService(groups_with_medias=parsed_media_list)

    while True:
        print("Choose an option to work with:")
        print(" 1. Channels")
        print(" 2. Movies/Vod")
        print(" 3. Series")
        print(" 4. Create new group")
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

        if choice == '4':
            os.system('clear')
            tvg_group = input("Type the tvg-group name: ")
            media_svc.add_group(
                group_model.Group(
                    group_type=parse_svc.define_group_type(tvg_group),
                    tvg_group=tvg_group
                )
            )

        if choice == '-1':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
