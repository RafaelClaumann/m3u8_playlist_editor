import re
import helpers

class Services:

    channels_list = []
    groups_info = {}

    def __init__(self, playlist_path: str):
        self.channels_list = helpers.read_file(playlist_path)
        self.groups_info = self.__parse_groups_info()

    def get_channels_list(self):
        return self.channels_list

    def get_groups_info(self):
        return self.groups_info

    def remove_low_quality_channels(self):
        quality_pattern = r'.*tvg-name=.*\".*\b(H265|HD²|SD²|SD).*\".*,'
        channels_to_remove = []
        for i in range(len(self.channels_list)):
            if re.search(quality_pattern, self.channels_list[i]):
                channels_to_remove.append(i)
                if i + 1 < len(self.channels_list):
                    channels_to_remove.append(i + 1)
        
        for index in sorted(set(channels_to_remove), reverse=True):
            self.channels_list[index] = ''

        print(f"Total channels removed [ {int(len(channels_to_remove) / 2)} ].")
        self.groups_info = self.__parse_groups_info()

    def remove_unwanted_groups(self, group_ids: list):
        for group_id in group_ids:
            group_title = self.groups_info[group_id]['title']

            print(f'Removing channels from group [ group-title="{group_title}" ].')
            group_pattern = r'#EXTINF:.*group-title="{}"'.format(re.escape(group_title))
            
            lower_bound = self.groups_info[group_id]['first_occurrence']
            upper_bound = self.groups_info[group_id]['last_occurrence']

            channels_to_remove = []
            for i in range(lower_bound, upper_bound + 1):
                if re.search(group_pattern, self.channels_list[i]):
                    channels_to_remove.append(i)
                    if i + 1 < len(self.channels_list):
                        channels_to_remove.append(i + 1)
            
            for index in sorted(set(channels_to_remove), reverse=True):
                self.channels_list[index] = ''
            
            print(f"Total channels removed [ {int(len(channels_to_remove) / 2)} ].")

            print(f'Channels from group [ group-title="{group_title}" ] removed.')
        
        for group_id in sorted(set(group_ids), reverse=True):
            self.groups_info.pop(group_id)

    def __parse_groups_info(self):
        groups = []
        for channel in self.channels_list:
            result = re.search(r'#EXTINF:.*group-title="([^"]*)"', channel)
            if result != None:
                groups.append(result.group(1))

        unique_elements = set(groups)
        resulting_groups = sorted(unique_elements)

        infos = {}
        for idx, group in enumerate(resulting_groups):
            
            counter = 0
            first_occurrence = -1
            last_occurrence = -1
            for index, channel in enumerate(self.channels_list):
                if rf'group-title="{group}"' in channel:

                    if first_occurrence == -1:
                        first_occurrence = index
                    last_occurrence = index

                    counter += 1
                        
            infos[idx] = {
                    'title': group,
                    'total_channels': counter,
                    'first_occurrence': first_occurrence,
                    'last_occurrence': last_occurrence
            }

        return infos
