import os

from config.config import Config
import services.services as services
import helpers as helpers


def show_menu(svc: services.Services):
    while True:
        print("Choose an option:")
        print(" 1. Show channels groups")
        print(" 2. Remove low quality channels")
        print(" 3. Remove low quality channels from group")
        print(" 4. Remove channels groups")
        print("-1. << Back to main menu >>")

        choice = input("Enter the number of the desired option: ")
        print()

        if choice == '1':
            print("Groups found in the channel list:")
            channels_groups = svc.get_channels_groups()
            helpers.print_groups_with_indexes(channels_groups)

        if choice == '2':
            print("This will remove channels that contains H265, HD², SD² or SD in their names.")
            if helpers.user_confirmation():
                svc.remove_low_quality_channels_from_all_groups()
                print("Channels groups removed \n")
            else:
                print()

        if choice == '3':
            channels_groups = svc.get_channels_groups()
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one group to remove channels with H265, HD², SD² or SD in their title.")
            input_str = input("Type the group number: ")
            group_id = int(input_str)

            if helpers.user_confirmation():
                svc.remove_low_quality_channels_from_group(group=channels_groups[group_id])
                print()
                helpers.print_groups_with_indexes([channels_groups[group_id]])
            else:
                print()

        if choice == '4':
            channels_groups = svc.get_channels_groups()
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [channels_groups[id] for id in ids]
            if helpers.user_confirmation():
                svc.remove_groups(groups_to_remove=groups_to_remove)
                print()
                helpers.print_groups_with_indexes(groups_to_remove)
            else:
                print()

        if choice == '-1':
            print("Returning... \n")
            break

        channels = svc.get_channels_list()
        helpers.save_file(Config.OUTPUT_PLAYLIST_PATH, channels)

    os.system('clear')
