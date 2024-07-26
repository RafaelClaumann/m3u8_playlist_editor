import os

import helpers
from config.config import Config
from models.group_type import GroupType
from services.database_service import DatabaseService


def show_menu(db: DatabaseService):
    while True:
        print("Choose an option:")
        print(" 1. Show movies groups")
        print(" 2. Show movies from a group")
        print(" 3. Remove movies groups")
        print(" 4. Remove movies from a group")
        print("-1. << Back to main menu >>")

        choice = input("Enter the number of the desired option: ")
        print()

        # SHOW MOVIES GROUPS
        if choice == '1':
            print("Groups of movies found in the list:")
            groups = db.fetch_groups_by_type(GroupType.MOVIES)
            helpers.print_groups_with_ids(groups)

        # SHOW MOVIES FROM A GROUP
        if choice == '2':
            groups = db.fetch_groups_by_type(GroupType.MOVIES)
            helpers.print_groups_with_ids(groups)

            print("Choose one group to show your media items.")
            input_str = input("Type the group number: ")
            media_items = db.fetch_media_by_group_id(group_id=int(input_str))
            helpers.print_media_with_ids(media_items)

        # REMOVE ONE OR MORE MOVIES GROUPS
        if choice == '3':
            groups = db.fetch_groups_by_type(GroupType.MOVIES)
            helpers.print_groups_with_ids(groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            group_ids = list(map(int, input_str.strip().split(',')))

            if helpers.user_confirmation():
                counter = 0
                for group_id in group_ids:
                    affected_rows = db.delete_group(group_id)
                    counter += affected_rows
                print(f"Total number of groups removed [ {counter} ].\n")
            else:
                print()

        # REMOVE MOVIES FROM A GROUP
        if choice == '4':
            groups = db.fetch_groups_by_type(GroupType.MOVIES)
            helpers.print_groups_with_ids(groups)

            print("Choose one group to show your media items.")
            input_str = input("Type the group number: ")
            media_items = db.fetch_media_by_group_id(group_id=int(input_str))
            helpers.print_media_with_ids(media_items)

            print("Choose one or more medias to be remove from a group, use the number displayed at left of the media title.")
            input_str = input("Type numbers separated by comma: ")
            media_ids = list(map(int, input_str.strip().split(',')))

            if helpers.user_confirmation():
                for media_id in media_ids:
                    db.delete_media(media_id)
                print()
            else:
                print()

        if choice == '-1':
            print("Returning... \n")
            break

        media_reprs = [repr(media) for media in db.fetch_medias()]
        media_reprs.insert(0, "#EXTM3U")
        helpers.save_file(Config.OUTPUT_PLAYLIST_PATH, media_reprs)

    os.system('clear')
