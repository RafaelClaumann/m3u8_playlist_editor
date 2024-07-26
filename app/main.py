import argparse
import os
from typing import List

import helpers
import services.parse_service as parse_svc
from app.models.group import Group
from app.models.media import Media
from config.config import Config
from config.database_connection import DatabaseConnection
from config.logging_config import configure_logging
from services.database_service import DatabaseService
from services.media_service import MediaService
from view import channel_groups_menu, series_group_menu, movies_group_menu


def insert_data(groups: List[Group], database: DatabaseService):
    for group in groups:
        grp = Group(
            group_type=group.group_type,
            tvg_group=group.tvg_group,
            first_occurrence=group.first_occurrence,
            last_occurrence=group.last_occurrence,
            total_occurrences=group.total_occurrences
        )
        group_id = database.insert_group(grp)
        for media in group.media_list:
            med = Media(
                ext_inf=media.ext_inf,
                tvg_name=media.tvg_name,
                tvg_id=media.tvg_id,
                tvg_logo=media.tvg_logo,
                tvg_group=media.tvg_group,
                catchup=media.catchup,
                catchup_days=media.catchup_days,
                media_url=media.media_url
            )
            database.insert_media(med, group_id)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    configure_logging(args.debug)

    raw_media_list = helpers.read_file(file_path=Config.INPUT_PLAYLIST_PATH)
    parsed_media_list = parse_svc.parse_raw_list(raw_media_list=raw_media_list)
    media_svc = MediaService(groups_with_medias=parsed_media_list)

    connection = DatabaseConnection()
    db = DatabaseService(database_connection=connection.db_connection)
    insert_data(groups=media_svc.media_groups, database=db)

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
            channel_groups_menu.show_menu(db)

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
