import logging
import re
from typing import List

import app.models.group as group_model
import app.models.group_type as group_type
import app.models.media as media_model


class MediaService:
    media_groups = []

    def __init__(self, groups_with_medias: List[group_model.Group]):
        self.media_groups = groups_with_medias

    def get_groups_by_type(self, desired_type: group_type.GroupType):
        return [group for group in self.media_groups if group.group_type == desired_type]

    def remove_groups(self, groups_to_remove: List[group_model.Group]):
        to_remove = []
        for group in groups_to_remove:
            group_index = self.media_groups.index(group)
            to_remove.append(group_index)

        for index in sorted(to_remove, reverse=True):
            logging.debug(f'removing group [ {self.media_groups[index].tvg_group} ]')
            self.media_groups.pop(index)

    @staticmethod
    def remove_media_from_group(group: group_model.Group, medias_to_remove: List[media_model.Media]):
        to_remove = []
        for media in medias_to_remove:
            to_remove.append(group.media_list.index(media))

        for index in sorted(to_remove, reverse=True):
            logging.debug(f'removing media [ {group.media_list[index].tvg_name} ]  from group [ {group.tvg_group} ]')
            group.media_list.pop(index)

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
                logging.debug(f'removing media [ {media_item.tvg_name} ]  from group [ {group.tvg_group} ]')
                channels_indexes_to_remove.append(index)

        for idx in sorted(channels_indexes_to_remove, reverse=True):
            group_media.pop(idx)

        group.total_occurrences = group.total_occurrences - len(channels_indexes_to_remove)
