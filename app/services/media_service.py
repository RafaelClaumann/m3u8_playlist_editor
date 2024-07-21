import re
from typing import List

import app.models.media as media_model


class MediaService:
    media_items = []

    def __init__(self, raw_media_list: List[str]):
        self.media_items = self.__parse_media_list(raw_media_list)

    @staticmethod
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
