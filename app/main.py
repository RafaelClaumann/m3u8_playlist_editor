import json
import helpers
import services as svcs

def main():
    svc = svcs.Services("../files/sample_playlist.m3u8")

    while True:
        print("Choose an option:")
        print("1. Remove low quality channels")
        print("2. Remove unwanted groups")
        print("3. Rename group")
        print("4. List groups")
        print("5. Groups info")
        print("6. Exit")
        
        escolha = input("Enter the number of the desired option: ")
        
        if escolha == '1':
            svc.remove_low_quality_channels()

        elif escolha == '2':
            print("Groups found in the channel list: \n")

            groups = svc.get_groups()
            for i in range(len(groups)): 
                print(f"\t[{i}] - {groups[i]}")

            print("\nChoose one or more groups to remove based on the integer value on the left side of the group name. ")
            input_str = input("Write numbers separated by comma(write -1 to cancel): ")
            group_ids = list(map(int, input_str.strip().split(',')))

            if sorted(group_ids)[0] != -1:
                selected_groups = []
                for i in sorted(group_ids, reverse=True):
                    if 0 <= i < len(groups):
                        selected_groups.append(groups[i])
                        del groups[i]
                
                svc.remove_unwanted_groups(groups_to_remove=selected_groups)
            
        elif escolha == '3':
            input_str = input("Write old_group_name and new_group_name separated by comma: ")
            group_names = input_str.strip().split(',')
            svc.rename_group(old_group=group_names[0], new_group=group_names[1])

        elif escolha == '4':
            groups_dict = svc.get_groups()
            print(json.dumps(groups_dict, indent=4, ensure_ascii=False))

        elif escolha == '5':
            groups_info_dict = svc.get_groups_info()
            print(json.dumps(groups_info_dict, indent=4, ensure_ascii=False))

        elif escolha == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

        channels = svc.get_channels_list()
        helpers.save_file("../files/output_playlist.m3u8", channels)
        print('\n')

if __name__ == "__main__":
    main()
