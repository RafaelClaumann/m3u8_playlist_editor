from typing import List

from app.models.group_type import GroupType
from app.models.media import Media


class Group:
    def __init__(self,
                 id: int = None,
                 group_type: GroupType = None,
                 tvg_group: str = None,
                 media_list: List[Media] = None,
                 first_occurrence: int = None,
                 last_occurrence: int = None,
                 total_occurrences: int = None
                 ):
        self.id = id
        self.group_type = group_type
        self.tvg_group = tvg_group
        self.media_list = media_list if media_list is not None else []
        self.first_occurrence = first_occurrence
        self.last_occurrence = last_occurrence
        self.total_occurrences = total_occurrences

    def __repr__(self):
        return (f"Group("
                f"group_type={self.group_type},"
                f"tvg_group={self.tvg_group},"
                f"media_list={self.media_list},"
                f"first_occurrence={self.first_occurrence},"
                f"last_occurrence={self.last_occurrence},"
                f"total_occurrences={self.total_occurrences})"
                )
