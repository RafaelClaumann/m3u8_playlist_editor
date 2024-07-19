import re
import app.helpers
import app.models.group as models


class Services:

    channels_list = []
    groups_list = []

    def __init__(self, playlist_path: str):
        self.channels_list = app.helpers.read_file(playlist_path)

        sorted_groups = self.__parse_groups()
        self.groups_list = self.__enrich_groups_data(sorted_groups)

    def get_channels_list(self):
        return self.channels_list

    def get_groups_list(self):
        return self.groups_list

    # groups of channels doesn't contain pipe(|) in their names
    def get_channels_groups(self):
        groups = []
        for group in self.groups_list:
            channels_search = re.search(r'\|', group.tvg_group, re.IGNORECASE)
            if channels_search is None:
                groups.append(group)
        return groups

    # groups of movies/vod should contain pipe(|) in their names
    # movies groups names: Filmes, Movies, Coletânea, Collection, Shows, Concerts, Vod, Especiais, Specials
    def get_movies_groups(self):
        groups = []
        for group in self.groups_list:
            movies_pattern = r'((Filmes|Movies|Coletânea|Collection|Shows|Concerts|Vod|Especiais|Specials).*\|.*)'
            movies_search = re.search(movies_pattern, group.tvg_group, re.IGNORECASE)
            if movies_search is not None:
                groups.append(group)
        return groups

    # groups of movies should contain pipe(|) in their names
    # series groups names: Series, Séries
    def get_series_groups(self):
        groups = []
        for group in self.groups_list:
            series_search = re.search(r"((Series|Séries).*\|.*)", group.tvg_group, re.IGNORECASE)
            if series_search is not None:
                groups.append(group)
        return groups

    # remove channels that contains H265, HD², SD² or SD in their names
    def remove_low_quality_channels_from_all_groups(self):
        for group in self.get_groups_list():
            self.remove_low_quality_channels_from_group(group)

    # remove channels(H265, HD², SD² or SD) from a specific group
    # update group total_occurrences according to quantity of channels removed
    # if all group channels are removed the group will be removed too
    def remove_low_quality_channels_from_group(self, group: models.Group()):
        lower_bound = group.first_occurrence
        upper_bound = group.last_occurrence

        channels_names_to_remove = []
        channels_indexes_to_remove = []
        group_pattern = r'#EXTINF:.*tvg-group="([^"]*)"'
        quality_pattern = r'tvg-name="([^"]*(\bHD²|SD|SD²|H265)[^"]*)"'
        for idx, channel in enumerate(self.channels_list[lower_bound:upper_bound + 1], start=lower_bound):
            result = re.search(quality_pattern, self.channels_list[idx])
            if result:
                if re.search(group_pattern, channel).group(1) == group.tvg_group:
                    channels_names_to_remove.append(result.group(1))
                    channels_indexes_to_remove.append(idx)
                    if idx + 1 < len(self.channels_list):
                        channels_indexes_to_remove.append(idx + 1)

        for idx in sorted(set(channels_indexes_to_remove), reverse=True):
            self.channels_list[idx] = ''

        total_channels_to_remove = int(len(channels_indexes_to_remove) / 2)
        if total_channels_to_remove == group.total_occurrences:
            self.remove_groups([group])
        elif total_channels_to_remove < group.total_occurrences:
            for i in channels_names_to_remove:
                group.tvg_names.remove(i)
            group.total_occurrences = group.total_occurrences - total_channels_to_remove

    # remove one or more groups
    # this means remove the group and all channels contained in
    def remove_groups(self, groups_to_remove: list):
        for group in groups_to_remove:
            channels_to_remove = []
            group_pattern = r'#EXTINF:.*tvg-group="{}"'.format(re.escape(group.tvg_group))
            for i in range(group.first_occurrence, group.last_occurrence + 1):
                if re.search(group_pattern, self.channels_list[i]):
                    channels_to_remove.append(i)
                    if i + 1 < len(self.channels_list):
                        channels_to_remove.append(i + 1)

            for index in sorted(set(channels_to_remove), reverse=True):
                self.channels_list[index] = ''

            self.groups_list = [item for item in self.groups_list if item.tvg_group != group.tvg_group]

    def remove_medias_from_group(self, group_param: models.Group, media_ids: list):
        for media_id in sorted(media_ids, reverse=True):
            media_name = group_param.tvg_names[media_id]
            self.remove_media_from_group_by_tvg_name(group_param, media_name)
            group_param.tvg_names.pop(media_id)

    def remove_media_from_group_by_tvg_name(self, group: models.Group(), media_name: str):
        lower_bound = group.first_occurrence
        upper_bound = group.last_occurrence

        channels_indexes_to_remove = []
        media_pattern = rf'#EXTINF.*tvg-name=\"({media_name})\"'
        for idx, channel in enumerate(self.channels_list[lower_bound:upper_bound + 1], start=lower_bound):
            result = re.search(media_pattern, self.channels_list[idx])
            if result:
                channels_indexes_to_remove.append(idx)
                if idx + 1 < len(self.channels_list):
                    channels_indexes_to_remove.append(idx + 1)

        for idx in sorted(set(channels_indexes_to_remove), reverse=True):
            self.channels_list[idx] = ''

    # return a list of unique groups found in channels_list
    def __parse_groups(self):
        groups = []
        for index, channel in enumerate(self.channels_list):
            group_search = re.search(r'#EXTINF:.*tvg-group="([^"]*)"', channel, re.IGNORECASE)
            if group_search is not None:
                group_title = group_search.group(1)
                groups.append(group_title)

        sorted_groups = list(set(groups))
        sorted_groups.sort()
        return sorted_groups

    # enrich groups with first, last and total group media occurrences and with his media list
    # groups_list param should be like: [{'tvg-group': 'group-1'}, {'tvg-group': 'group-02'}]
    def __enrich_groups_data(self, group_list: list):
        enriched_groups = []

        for group in group_list:
            enriched_group = models.Group()
            total_occurrences = 0
            first_occurrence = -1
            last_occurrence = -1
            for index, channel in enumerate(self.channels_list):
                if rf'tvg-group="{group}"' in channel:
                    if first_occurrence == -1:
                        first_occurrence = index
                    last_occurrence = index
                    total_occurrences += 1

                    name_search = re.search(r'#EXTINF:.*tvg-name="([^"]*)"', channel, re.IGNORECASE)
                    if name_search:
                        result = name_search.group(1)
                        enriched_group.tvg_names.append(result)

            enriched_group.tvg_group = group
            enriched_group.first_occurrence = first_occurrence
            enriched_group.last_occurrence = last_occurrence
            enriched_group.total_occurrences = total_occurrences
            enriched_groups.append(enriched_group)

        return enriched_groups
