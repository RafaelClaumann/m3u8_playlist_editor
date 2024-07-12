import services as svc

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    return lines

def save_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines))

def main():

    channels = read_file("sample_playlist.m3u8")

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
            input_str = input("Write unwanted group names separated by comma: ")
            unwanted_groups = input_str.strip().split(',')
            svc.remove_unwanted_groups(channels=channels, groups=unwanted_groups)
            
        elif escolha == '3':
            input_str = input("Write old_group_name and new_group_name separated by comma: ")
            group_names = input_str.strip().split(',')
            svc.rename_group(channels=channels, old_group=group_names[0], new_group=group_names[1])

        elif escolha == '4':
            print(svc.list_all_groups(channels=channels))

        elif escolha == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

        save_file("output_playlist.m3u8", channels)


if __name__ == "__main__":
    main()
