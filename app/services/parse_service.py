import re
from typing import List

import app.models.group as group_model
import app.models.group_type as group_type
import app.models.media as media_model


def parse_raw_list(raw_media_list: List[str]):
    media_elements = __parse_media_list(raw_media_list=raw_media_list)
    media_groups = __parse_and_sort_media_groups(raw_media_list=raw_media_list)
    __join_media_on_groups(media_elements=media_elements, media_groups=media_groups)

    return media_groups


def __join_media_on_groups(media_groups: List[group_model.Group], media_elements: List[media_model.Media]):
    for group_item in media_groups:
        for media_item in media_elements:
            if group_item.tvg_group == media_item.tvg_group:
                group_item.media_list.append(media_item)


def __parse_and_sort_media_groups(raw_media_list: List[str]):
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
                group_type=define_group_type(tvg_group),
                tvg_group=tvg_group,
                first_occurrence=first_occurrence,
                last_occurrence=last_occurrence,
                total_occurrences=total_occurrences
            )
        )

    return enriched_groups


def define_group_type(tvg_group: str):
    channels_type_pattern = r'\|'
    series_type_pattern = r"((Series|Séries).*\|.*)"
    movies_type_pattern = r'((Filmes|Movies|Coletânea|Collection|Shows|Concerts|Vod|Especiais|Specials).*\|.*)'

    if re.search(channels_type_pattern, tvg_group, re.IGNORECASE) is None:
        return group_type.GroupType.CHANNELS
    elif re.search(movies_type_pattern, tvg_group, re.IGNORECASE) is not None:
        return group_type.GroupType.MOVIES
    elif re.search(series_type_pattern, tvg_group, re.IGNORECASE) is not None:
        return group_type.GroupType.SERIES

    return "undefined"


def __parse_media_list(raw_media_list: List[str]):
    parsed_media_list = []
    for index, media_item in enumerate(raw_media_list):
        ext_inf_result = re.search('(#EXTINF:-?[0-9]+)', media_item, re.IGNORECASE)

        media_url_result = None
        if index + 1 < len(raw_media_list):
            media_url_result = re.search('(^https?://.*)', raw_media_list[index + 1], re.IGNORECASE)

        if ext_inf_result and media_url_result:
            tvg_name_result = re.search('tvg-name="([^"]*)"', media_item, re.IGNORECASE)
            tvg_id_result = re.search('tvg-id="([^"]*)"', media_item, re.IGNORECASE)
            tvg_logo_result = re.search('tvg-logo="([^"]*)"', media_item, re.IGNORECASE)
            tvg_group_result = re.search('tvg-group="([^"]*)"', media_item, re.IGNORECASE)
            catchup_result = re.search('catchup="([^"]*)"', media_item, re.IGNORECASE)
            catchup_days_result = re.search('catchup-days="([^"]*)"', media_item, re.IGNORECASE)

            media_params = {
                'ext_inf': ext_inf_result.group(1) if ext_inf_result is not None else "",
                'tvg_name': tvg_name_result.group(1) if tvg_name_result is not None else "",
                'tvg_id': tvg_id_result.group(1) if tvg_id_result is not None else "",
                'tvg_logo': tvg_logo_result.group(1) if tvg_logo_result is not None else "",
                'tvg_group': tvg_group_result.group(1) if tvg_group_result is not None else "",
                'media_url': media_url_result.group(1) if media_url_result is not None else "https://url_not_found.com"
            }

            if catchup_result is not None:
                media_params['catchup'] = catchup_result.group(1)
            if catchup_days_result is not None:
                media_params['catchup_days'] = int(catchup_days_result.group(1))

            parsed_media_list.append(media_model.Media(**media_params))

    return parsed_media_list
