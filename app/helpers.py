import app.models.group as models


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    return lines


def save_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines))


def user_confirmation():
    if input("Do you want to proceed? (y/n): ") != "y":
        print("Changes have been canceled.")
        return False
    return True


def print_groups_with_indexes(groups: list):
    for index, group in enumerate(groups):
        print(f"[{index}] - {group.tvg_group} - {len(group.media_list)} media elements")
    print()


def print_group_media_with_indexes(group: models.Group):
    for index, tvg_name in enumerate(group.media_list):
        print(f"[{index}] - {tvg_name}")
    print()
