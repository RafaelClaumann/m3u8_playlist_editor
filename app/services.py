import re
import helpers

class Services:

    channels_list = []
    groups_list = []
    groups_info = {}

    def __init__(self, playlist_path: str):
        self.channels_list = helpers.read_file(playlist_path)
        self.groups_list = self.__parse_groups()
        self.groups_info = self.__parse_groups_info()

    def get_channels_list(self):
        return self.channels_list

    def get_groups(self):
        return self.groups_list

    def get_groups_info(self):
        return self.groups_info

    def remove_low_quality_channels(self):
        quality_pattern = r'.*tvg-name=.*\".*\b(H265|HD²|SD²|SD).*\".*,'
        indices_to_remove = []
        for i in range(len(self.channels_list)):
            if self.channels_list[i].startswith("#EXTINF:"):
                if re.search(quality_pattern,self.channels_list[i]):
                    indices_to_remove.append(i)
                    if i + 1 < len(self.channels_list):
                        indices_to_remove.append(i + 1)
            
            for index in sorted(set(indices_to_remove), reverse=True):
                self.channels_list[index] = ''

    def remove_unwanted_groups(self, group_ids: list):

        selected_groups = []
        for i in sorted(group_ids, reverse=True):
            if 0 <= i < len(self.groups_list):
                selected_groups.append(self.groups_list[i])
                self.groups_info.pop(self.groups_list[i])
                del self.groups_list[i]
        
        for group in selected_groups:
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

        resulting_groups = list(set(groups))
        resulting_groups.sort()
        return resulting_groups

    def __parse_groups_info(self):
        infos = {}
        for group in self.groups_list:
            counter = 0
            first_element = 0
            last_element = 0

            for index, channel in enumerate(self.channels_list):
                if channel.startswith("#EXTINF:"):
                    if rf'group-title="{group}"' in channel:

                        if index > first_element and first_element == 0:
                            first_element = index
                        
                        if index > last_element:
                            last_element = index
                        
                        counter += 1
                        
            infos[group] = {
                'total_channels': counter,
                'first_element': first_element,
                'last_element': last_element
            }
        
        return {key: infos[key] for key in sorted(infos)}
