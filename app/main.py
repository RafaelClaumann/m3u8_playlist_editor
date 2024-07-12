import services as svc
import helpers

def main():
    channels = helpers.read_file("../files/sample_playlist.m3u8")

    while True:
        print("Choose an option:")
        print("1. Remove low quality channels")
        print("2. Remove unwanted groups")
        print("3. Rename group")
        print("4. List groups")
        print("5. Exit")
        
        escolha = input("Enter the number of the desired option: ")
        
        if escolha == '1':
            svc.remove_low_quality_channels(channels=channels)

        elif escolha == '2':
            print("Groups found in the channel list: \n")

            groups = svc.list_groups(channels=channels)
            for i in range(len(groups)): 
                print(f"\t[{i}] - {groups[i]}")

            print("\nChoose one or more groups to remove based on the integer value on the left side of the group name. ")
            input_str = input("Write numbers separated by comma: ")
            group_ids = list(map(int, input_str.strip().split(',')))

            selected_groups = []
            for i in sorted(group_ids, reverse=True):
                if 0 <= i < len(groups):
                    selected_groups.append(groups[i])
                    del groups[i]
            
            svc.remove_unwanted_groups(channels=channels, groups=selected_groups)
            
        elif escolha == '3':
            input_str = input("Write old_group_name and new_group_name separated by comma: ")
            group_names = input_str.strip().split(',')
            svc.rename_group(channels=channels, old_group=group_names[0], new_group=group_names[1])

        elif escolha == '4':
            print(svc.list_groups(channels=channels))

        elif escolha == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

        helpers.save_file("../files/output_playlist.m3u8", channels)
        print('\n')


if __name__ == "__main__":
    main()
