import re
from enum import Enum
from typing import List

import app.models.group as group_model
import app.models.media as media_model


class GroupType(Enum):
    CHANNELS = 'channels'
    MOVIES = 'movies'
    SERIES = 'series'


class GroupsService:
    media_groups = []

    def __init__(self, raw_media_list: List[str]):
        self.media_groups = self.__parse_and_sort_media_groups(raw_media_list)

    def get_groups(self, group_type: GroupType):
        return [group for group in self.media_groups if group.group_type == group_type]

    def generate_writable_media_list(self):
        writable_media_list = []
        for group_item in self.media_groups:
            for media_item in group_item.media_list:
                writable_media_list.append(media_item.__repr__())
        return writable_media_list

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

    def join_media_on_groups(self, media_items: List[media_model.Media]):
        for group_item in self.media_groups:
            for media_item in media_items:
                if group_item.tvg_group == media_item.tvg_group:
                    group_item.media_list.append(media_item)

    def __parse_and_sort_media_groups(self, raw_media_list: List[str]):
        groups = []
        for index, media_item in enumerate(raw_media_list):
            group_result = re.search('#EXTINF:.*tvg-group="([^"]*)"', media_item, re.IGNORECASE)
            if media_item.startswith('#EXTINF:') and group_result is not None:
                group_title = group_result.group(1)
                groups.append(group_title)

        sorted_groups = sorted(set(groups))

        enriched_groups = []
        for tvg_group in sorted_groups:
            total_occurrences = 0
            first_occurrence = -1
            last_occurrence = -1

            for index, media_item in enumerate(raw_media_list):
                if media_item.startswith('#EXTINF:') and rf'tvg-group="{tvg_group}"' in media_item:
                    if first_occurrence == -1:
                        first_occurrence = index
                    last_occurrence = index
                    total_occurrences += 1

            enriched_groups.append(
                group_model.Group(
                    group_type=self.__define_group_type(tvg_group),
                    tvg_group=tvg_group,
                    first_occurrence=first_occurrence,
                    last_occurrence=last_occurrence,
                    total_occurrences=total_occurrences
                )
            )

        return enriched_groups

    @staticmethod
    def __define_group_type(tvg_group: str):
        channels_type_pattern = r'\|'
        series_type_pattern = r"((Series|Séries).*\|.*)"
        movies_type_pattern = r'((Filmes|Movies|Coletânea|Collection|Shows|Concerts|Vod|Especiais|Specials).*\|.*)'

        if re.search(channels_type_pattern, tvg_group, re.IGNORECASE) is None:
            return GroupType.CHANNELS
        elif re.search(movies_type_pattern, tvg_group, re.IGNORECASE) is not None:
            return GroupType.MOVIES
        elif re.search(series_type_pattern, tvg_group, re.IGNORECASE) is not None:
            return GroupType.SERIES

        return "undefined"
