import re
import json
from collections import Counter

def remove_low_quality_channels(channels: list):
    quality_pattern = r'.*tvg-name=.*\".*\b(H265|HD²|SD²|SD).*\".*,'
    i = 0
    while i < len(channels):
        if channels[i].startswith("#EXTINF:"):
            if re.search(quality_pattern, channels[i]):
                channels[i] = ''
                channels[i + 1] = ''
                i = i + 2
            else:
                i += 1
        else:
            i += 1

def remove_unwanted_groups(channels: list, groups: list):
    for group in groups:
        group_pattern = rf'group-title="{group}"'
        print("Removing group:", group_pattern)

        indices_to_remove = []
        for i in range(len(channels)):
            if channels[i].startswith("#EXTINF:") and re.search(group_pattern, channels[i]):
                indices_to_remove.append(i)
                if i + 1 < len(channels):
                    indices_to_remove.append(i + 1)

        for index in sorted(set(indices_to_remove), reverse=True):
            channels[index] = ''
        
        print("Group removed:", group_pattern)

def rename_group(channels: list, old_group, new_group: str):
    group_pattern = r'group-title="{}"'
    i = 0
    while i < len(channels):
        if channels[i].startswith("#EXTINF:"):
            if re.search(group_pattern.format(re.escape(old_group)), channels[i]):
                channels[i] = channels[i].replace(f'group-title="{old_group}"', f'group-title="{new_group}"')
            else:
                i += 1
        else:
            i += 1

def list_groups(channels: list):
    groups = []
    for channel in channels:
        if channel.startswith("#EXTINF:"):
            result = re.search(r'group-title="([^"]*)"', channel)
            groups.append(result.group(1))

    dict_groups = dict(Counter(groups))
    json_output = json.dumps(dict_groups, indent=4, ensure_ascii=False)
    print(json_output)

    return list(set(groups))
