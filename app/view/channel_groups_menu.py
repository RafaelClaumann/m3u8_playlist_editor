import os

import helpers
from config.config import Config
from models.group_type import GroupType
from services.database_service import DatabaseService


def show_menu(db: DatabaseService):
    while True:
        print("Choose an option:")
        print(" 1. Show channels groups")
        print(" 2. Show channels from a group")
        print(" 3. Remove low quality channels from all groups")
        print(" 4. Remove low quality channels from a specific group")
        print(" 5. Remove channels groups")
        print(" 6. Remove channels from a group")
        print("-1. << Back to main menu >>")

        choice = input("Enter the number of the desired option: ")
        print()

        # SHOW CHANNELS GROUPS
        if choice == '1':
            print("Groups of channels found in the list:")
            groups = db.fetch_groups_by_type(GroupType.CHANNELS)
            helpers.print_groups_with_ids(groups)

        # SHOW CHANNELS FROM A GROUP
        if choice == '2':
            groups = db.fetch_groups_by_type(GroupType.CHANNELS)
            helpers.print_groups_with_ids(groups)

            print("Choose one group to show your media items.")
            input_str = input("Type the group number: ")
            media_items = db.fetch_media_by_group_id(group_id=int(input_str))
            helpers.print_media_with_ids(media_items)

        # REMOVE LOW QUALITY CHANNELS FROM ALL GROUPS
        if choice == '3':
            print("This will remove channels that contains H265, HD², SD² or SD in their names.")
            if helpers.user_confirmation():
                affected_rows = db.delete_all_low_quality_channels()
                print(f"Total number of channels removed [ {affected_rows} ].\n")
            else:
                print()

        # REMOVE LOW QUALITY CHANNELS FROM A SPECIFIC GROUP
        if choice == '4':
            groups = db.fetch_groups_by_type(GroupType.CHANNELS)
            helpers.print_groups_with_ids(groups)

            print("Choose a group to removed your low quality channels(H265, HD², SD² or SD).")
            input_str = input("Type the group number: ")

            if helpers.user_confirmation():
                affected_rows = db.delete_low_quality_channels_from_group(group_id=int(input_str))
                print()

                output = [group for group in groups if group.id == int(input_str)]
                print(f"Total number of channels removed [ {affected_rows} ] from group [ {output} ].\n")
            else:
                print()

        # REMOVE ONE OR MORE CHANNEL GROUPS
        if choice == '5':
            groups = db.fetch_groups_by_type(GroupType.CHANNELS)
            helpers.print_groups_with_ids(groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type the group numbers separated by commas: ")
            group_ids = list(map(int, input_str.strip().split(',')))

            if helpers.user_confirmation():
                counter = 0
                for group_id in group_ids:
                    affected_rows = db.delete_group(group_id)
                    counter += affected_rows
                print(f"Total number of groups removed [ {counter} ].\n")
            else:
                print()

        # REMOVE CHANNELS FROM A GROUP
        if choice == '6':
            groups = db.fetch_groups_by_type(GroupType.CHANNELS)
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
