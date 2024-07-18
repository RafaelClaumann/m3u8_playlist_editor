class Group:
    def __init__(self,
                 tvg_group: str = None,
                 tvg_names: list = None,
                 first_occurrence: int = None,
                 last_occurrence: int = None,
                 total_occurrences: int = None
                 ):
        self.tvg_group = tvg_group
        self.tvg_names = tvg_names if tvg_names is not None else []
        self.first_occurrence = first_occurrence
        self.last_occurrence = last_occurrence
        self.total_occurrences = total_occurrences

    def __repr__(self):
        return (f"Media("
                f"tvg_group={self.tvg_group},"
                f"tvg_names={self.tvg_names},"
                f"first_occurrence={self.first_occurrence},"
                f"last_occurrence={self.last_occurrence},"
                f"total_occurrences={self.total_occurrences})"
                )
