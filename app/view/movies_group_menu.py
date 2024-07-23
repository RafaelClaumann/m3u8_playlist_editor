import os

import app.config.config as config
import app.helpers as helpers
import app.models.group_type as group_type
import app.services.media_service as media_svc_import


def show_menu(media_svc: media_svc_import.MediaService):
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
            movies_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

        # SHOW MOVIES FROM A GROUP
        if choice == '2':
            movies_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = movies_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

        # REMOVE ONE OR MORE MOVIES GROUPS
        if choice == '3':
            movies_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [movies_groups[idx] for idx in ids]
            if helpers.user_confirmation():
                media_svc.remove_groups(groups_to_remove=groups_to_remove)
                print()
                helpers.print_groups_with_indexes(groups=groups_to_remove)
            else:
                print()

        # REMOVE MOVIES FROM A GROUP
        if choice == '4':
            movies_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.MOVIES)
            helpers.print_groups_with_indexes(groups=movies_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = movies_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

            print("Choose one or more medias to remove from group.")
            input_str = input("Type numbers separated by comma: ")
            media_ids = list(map(int, input_str.strip().split(',')))

            to_remove = [chosen_group.media_list[index] for index in media_ids]
            if helpers.user_confirmation():
                media_svc.remove_media_from_group(group=chosen_group, medias_to_remove=to_remove)
                print()
                helpers.print_group_media_with_indexes(group=chosen_group)
            else:
                print()

        if choice == '-1':
            print("Returning... \n")
            break

        channels = helpers.generate_writable_media_list(media_groups=media_svc.media_groups)
        helpers.save_file(config.Config.OUTPUT_PLAYLIST_PATH, channels)

    os.system('clear')
