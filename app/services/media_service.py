import re
from typing import List

import app.models.group as group_model
import app.models.group_type as group_type


class MediaService:
    media_groups = []

    def __init__(self, group_media_list: List[group_model.Group]):
        self.media_groups = group_media_list

    def get_groups_by_type(self, param: group_type.GroupType):
        return [group for group in self.media_groups if group.group_type == param]

    def remove_groups(self, groups_to_remove: List[group_model.Group]):
        for group_item in groups_to_remove:
            self.media_groups.remove(group_item)

    @staticmethod
    def remove_media_from_group(group: group_model.Group, media_to_remove: List[int]):
        for idx in sorted(media_to_remove, reverse=True):
            group.media_list.pop(idx)

    def remove_low_quality_channels_from_all_groups(self):
        for group in self.media_groups:
            self.remove_low_quality_channels_from_group(group)

    @staticmethod
    def remove_low_quality_channels_from_group(group: group_model.Group):
        group_media = group.media_list
        channels_indexes_to_remove = []
        quality_pattern = r'tvg-name="([^"]*(\bHD²|SD|SD²|H265)[^"]*)"'

        for index, media_item in enumerate(group_media):
            if re.search(quality_pattern, f'tvg-name="{media_item.tvg_name}"'):
                channels_indexes_to_remove.append(index)

        for idx in sorted(channels_indexes_to_remove, reverse=True):
            group_media.pop(idx)

        group.total_occurrences = group.total_occurrences - len(channels_indexes_to_remove)
