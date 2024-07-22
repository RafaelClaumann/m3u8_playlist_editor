from typing import List

import app.models.group as group_model
import app.models.group as models


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    return lines


def save_file(file_path, lines):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines))


def generate_writable_media_list(media_groups: List[group_model.Group]):
    writable_media_list = ["#EXTM3U"]
    for group_item in media_groups:
        for media_item in group_item.media_list:
            writable_media_list.append(media_item.__repr__())
    return writable_media_list


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
    for index, media_item in enumerate(group.media_list):
        print(f"[{index}] - {media_item.tvg_name}")
    print()
