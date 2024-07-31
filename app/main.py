import argparse
import os

import helpers
import services.parse_service as parse_svc
from config.database_connection import DatabaseConnection
from config.file_path_config import FilePathConfig
from config.load_initial_data import load_data
from config.logging_config import configure_logging
from services.database_service import DatabaseService
from view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    configure_logging(args.debug)

    raw_media_list = helpers.read_file(file_path=FilePathConfig.INPUT_PLAYLIST_PATH)
    media_groups = parse_svc.parse_raw_list(raw_media_list=raw_media_list)

    connection = DatabaseConnection()
    db = DatabaseService(database_connection=connection.db_connection)
    load_data(groups=media_groups, database=db)

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
            channel_groups_menu.show_menu(db)

        if choice == '2':
            os.system('clear')
            movies_group_menu.show_menu(db)

        if choice == '3':
            os.system('clear')
            series_group_menu.show_menu(db)

        if choice == '-1':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
