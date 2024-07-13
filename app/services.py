import re
import json
import helpers
from collections import Counter

class Services:

    channels_list = []
    groups_list = []

    def __init__(self, playlist_path: str):
        self.channels_list = helpers.read_file(playlist_path)
        self.groups_list = self.__parse_groups()

    def get_channels_list(self):
        return self.channels_list

    def get_groups(self):
        return self.groups_list

    def remove_low_quality_channels(self):
        quality_pattern = r'.*tvg-name=.*\".*\b(H265|HD²|SD²|SD).*\".*,'
        i = 0
        while i < len(self.channels_list):
            if self.channels_list[i].startswith("#EXTINF:"):
                if re.search(quality_pattern,self.channels_list[i]):
                    self.channels_list[i] = ''
                    self.channels_list[i + 1] = ''
                    i = i + 2
                else:
                    i += 1
            else:
                i += 1

    def remove_unwanted_groups(self, groups_to_remove: list):
        for group in groups_to_remove:
            group_pattern = r'group-title="{}"'.format(re.escape(group))
            print(f'Removing group: group-title="{group}"', )

            indices_to_remove = []
            for i in range(len(self.channels_list)):
                if self.channels_list[i].startswith("#EXTINF:"):
                    if re.search(group_pattern, self.channels_list[i]):
                        indices_to_remove.append(i)
                        if i + 1 < len(self.channels_list):
                            indices_to_remove.append(i + 1)

            for index in sorted(set(indices_to_remove), reverse=True):
                self.channels_list[index] = ''
            
            print(f'Group removed: group-title="{group}"', )

    def rename_group(self, old_group, new_group: str):
        group_pattern = r'group-title="{}"'
        i = 0
        while i < len(self.channels_list):
            if self.channels_list[i].startswith("#EXTINF:"):
                if re.search(group_pattern.format(re.escape(old_group)), self.channels_list[i]):
                    self.channels_list[i] = self.channels_list[i].replace(f'group-title="{old_group}"', f'group-title="{new_group}"')
                else:
                    i += 1
            else:
                i += 1

    def __parse_groups(self):
        groups = []
        for channel in self.channels_list:
            if channel.startswith("#EXTINF:"):
                result = re.search(r'group-title="([^"]*)"', channel)
                groups.append(result.group(1))

        return list(set(groups))
