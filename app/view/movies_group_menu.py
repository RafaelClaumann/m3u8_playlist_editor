import os

import helpers as helpers
from config.config import Config

import app.services.groups_service as group_svc_import


def show_menu(groups_svc: group_svc_import.GroupsService):
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
            print("Groups found in the movies list:")
            movies_groups = groups_svc.get_groups(group_type=group_svc_import.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

        # SHOW MOVIES FROM A GROUP
        if choice == '2':
            movies_groups = groups_svc.get_groups(group_type=group_svc_import.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = movies_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

        # REMOVE ONE OR MORE MOVIES GROUPS
        if choice == '3':
            movies_groups = groups_svc.get_groups(group_type=group_svc_import.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [movies_groups[idx] for idx in ids]
            if helpers.user_confirmation():
                groups_svc.remove_groups(groups_to_remove=groups_to_remove)
                print()
                helpers.print_groups_with_indexes(groups=groups_to_remove)
            else:
                print()

        # REMOVE MOVIES FROM A GROUP
        if choice == '4':
            movies_groups = groups_svc.get_groups(group_type=group_svc_import.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = movies_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

            print("Choose one or more medias to remove from group.")
            input_str = input("Type numbers separated by comma: ")
            media_ids = list(map(int, input_str.strip().split(',')))

            if helpers.user_confirmation():
                groups_svc.remove_media_from_group(group=chosen_group, media_to_remove=media_ids)
                print()
                helpers.print_group_media_with_indexes(group=chosen_group)
            else:
                print()

        if choice == '-1':
            print("Returning... \n")
            break

        channels = groups_svc.generate_writable_media_list()
        helpers.save_file(Config.OUTPUT_PLAYLIST_PATH, channels)

    os.system('clear')
