class Media:
    def __init__(self,
                 ext_inf: str = None,
                 tvg_name: str = None,
                 tvg_id: int = None,
                 tvg_logo: int = None,
                 tvg_group: str = None,
                 catchup: str = None,
                 catchup_days: int = None,
                 media_url: str = None
                 ):
        self.ext_inf = ext_inf
        self.tvg_name = tvg_name
        self.tvg_id = tvg_id
        self.tvg_logo = tvg_logo
        self.tvg_group = tvg_group
        self.catchup = catchup
        self.catchup_days = catchup_days
        self.media_url = media_url

    def __repr__(self):
        attributes = [
            ('tvg-name', self.tvg_name),
            ('tvg-id', self.tvg_id),
            ('tvg-logo', self.tvg_logo),
            ('tvg-group', self.tvg_group),
            ('catchup', self.catchup),
            ('catchup-days', self.catchup_days)
        ]

        attr_str = ' '.join(f'{name}="{value}"' for name, value in attributes if value is not None)
        return f'{self.ext_inf} {attr_str}, {self.tvg_name} \n{self.media_url}'
