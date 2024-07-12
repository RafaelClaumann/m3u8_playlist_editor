import re

def remove_low_quality_channels(channels: list):
    quality_pattern = r'.*tvg-name=.*\".*\b(H265|HD²|SD²|SD)\".*,'
    i = 0
    while i < len(channels):
        if channels[i].startswith("#EXTINF:"):
            if re.search(quality_pattern, channels[i]):
                del channels[i]
                del channels[i]
            else:
                i += 1
        else:
            i += 1

def remove_unwanted_groups(channels: list, groups: list):
    group_pattern = r'group-title="{}"'
    i = 0
    while i < len(channels):
        if channels[i].startswith("#EXTINF:"):
            for group in groups:
                if re.search(group_pattern.format(re.escape(group)), channels[i]):
                    del channels[i]
                    del channels[i]
            i += 1  
        else:
            i += 1

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

def list_all_groups(channels: list):
    groups = []
    for channel in channels:
        if channel.startswith("#EXTINF:"):
            result = re.search(r'group-title="([^"]*)"', channel)
            groups.append(result.group(1))
    return set(groups)
