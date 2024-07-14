import json
import helpers
import services

def print_formated_groups(groups: list):
    print("Groups found in the channel list: \n")
    for index, group in groups.items():
        print(f"[{index}] - {group['title']}")
    print("\n")

def user_confirmation():
    if input("Do you want to proceed? (y/n): ") != "y":
        print("Changes have been canceled.")
        return False
    return True

def main():
    svc = services.Services("../files/sample_playlist.m3u8")

    while True:
        print("Choose an option:")
        print("1. Remove low quality channels")
        print("2. Remove unwanted groups")
        print("3. Rename group")
        print("4. List channels info")
        print("5. Exit")
        
        escolha = input("Enter the number of the desired option: ")
        print()

        if escolha == '1':
            print("This will remove channels that contains H265, HD², SD² or SD in their names.")
            if(user_confirmation()):
                svc.remove_low_quality_channels()

        elif escolha == '2':
            groups = svc.get_groups_info()
            print_formated_groups(groups=groups) 

            print("Choose one or more groups to be removed, use the number displayed at left of the group name.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            if(user_confirmation()):
                svc.remove_unwanted_groups(group_ids=ids)
            
        elif escolha == '3':
            groups = svc.get_groups_info()
            print_formated_groups(groups=groups)

            print("Choose one group to rename, use the number displayed at left of the group name.")
            group_id = int(input("Type the desired number: "))
            new_group_name = input(f"Type new name for group [{groups.get(group_id)['title']}]: ")

            if(user_confirmation()):
                svc.rename_group(group_id, new_group_name)

        elif escolha == '4':
            print(json.dumps(svc.get_groups_info(), indent=4, ensure_ascii=False))

        elif escolha == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

        channels = svc.get_channels_list()
        helpers.save_file("../files/output_playlist.m3u8", channels)
        print('\n----------------------------------------------------\n')

if __name__ == "__main__":
    main()
