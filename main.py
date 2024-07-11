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

def main():
    f = open("sample_playlist.m3u8", "r")
    
    channels = f.read().split('\n')
    unwanted_groups = ["NOTICIAS"]

    remove_low_quality_channels(channels=channels)
    remove_unwanted_groups(channels=channels, groups=unwanted_groups)

    f = open("output_playlist.m3u8", "w")
    f.write("\n".join(channels))
    f.close

if __name__ == "__main__":
    main()