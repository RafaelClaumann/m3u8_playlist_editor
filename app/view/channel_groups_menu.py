import os
import time

from config.config import Config
import services.services as services
import helpers as helpers


def show_menu(svc: services.Services):
    while True:
        print("Choose an option:")
        print(" 1. Remove low quality channels")
        print(" 2. Remove channels groups")
        print(" 3. Show channels groups")
        print("-1. << Back to main menu >>")

        choice = input("Enter the number of the desired option: ")
        print()

        if choice == '1':
            print("This will remove channels that contains H265, HD², SD² or SD in their names.")
            if helpers.user_confirmation():
                svc.remove_low_quality_channels()
                print("Channels groups removed \n")

        if choice == '2':
            channels_groups = svc.get_channels_groups()
            helpers.print_groups_with_indexes(groups=channels_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [channels_groups[id] for id in ids]
            if helpers.user_confirmation():
                svc.remove_groups(groups_to_remove=groups_to_remove)

        if choice == '3':
            channels_groups = svc.get_channels_groups()
            helpers.print_groups_with_indexes(channels_groups)

        if choice == '-1':
            print("Returning... \n")
            break

        channels = svc.get_channels_list()
        helpers.save_file(Config.OUTPUT_PLAYLIST_PATH, channels)

    os.system('clear')
