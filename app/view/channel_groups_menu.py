import os

import helpers as helpers
from config.config import Config

import app.models.group_type as group_type
import app.services.media_service as media_svc_import


def show_menu(media_svc: media_svc_import.MediaService):
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
            print("Groups found in the channels list:")
            channels_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.CHANNELS)
            helpers.print_groups_with_indexes(groups=channels_groups)

        # SHOW CHANNELS FROM A GROUP
        if choice == '2':
            channels_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.CHANNELS)
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = channels_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

        # REMOVE LOW QUALITY CHANNELS FROM ALL GROUPS
        if choice == '3':
            print("This will remove channels that contains H265, HD², SD² or SD in their names.")
            if helpers.user_confirmation():
                media_svc.remove_low_quality_channels_from_all_groups()
                print("Channels groups removed \n")
            else:
                print()

        # REMOVE LOW QUALITY CHANNELS FROM A SPECIFIC GROUP
        if choice == '4':
            channels_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.CHANNELS)
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one group to remove channels with H265, HD², SD² or SD in their title.")
            input_str = input("Type the group number: ")
            group_id = int(input_str)

            if helpers.user_confirmation():
                media_svc.remove_low_quality_channels_from_group(group=channels_groups[group_id])
                print()
                helpers.print_groups_with_indexes(groups=[channels_groups[group_id]])
            else:
                print()

        # REMOVE ONE OR MORE CHANNEL GROUPS
        if choice == '5':
            channels_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.CHANNELS)
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [channels_groups[idx] for idx in ids]
            if helpers.user_confirmation():
                media_svc.remove_groups(groups_to_remove=groups_to_remove)
                print()
                helpers.print_groups_with_indexes(groups=groups_to_remove)
            else:
                print()

        # REMOVE CHANNELS FROM A GROUP
        if choice == '6':
            channels_groups = media_svc.get_groups_by_type(desired_type=group_type.GroupType.CHANNELS)
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one group to show your media names.")
            input_str = input("Type the group number: ")
            chosen_group = channels_groups[int(input_str)]
            helpers.print_group_media_with_indexes(group=chosen_group)

            print("Choose one or more medias to remove from group.")
            input_str = input("Type numbers separated by comma: ")
            media_ids = list(map(int, input_str.strip().split(',')))

            to_remove = [chosen_group.media_list[index] for index in media_ids]
            if helpers.user_confirmation():
                media_svc.remove_media_from_group(group=chosen_group, media_to_remove=to_remove)
                print()
                helpers.print_group_media_with_indexes(group=chosen_group)
            else:
                print()

        if choice == '-1':
            print("Returning... \n")
            break

        channels = helpers.generate_writable_media_list(media_groups=media_svc.media_groups)
        helpers.save_file(Config.OUTPUT_PLAYLIST_PATH, channels)

    os.system('clear')
