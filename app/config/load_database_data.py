from typing import List

from services.database_service import DatabaseService

from app.models.group import Group
from app.models.media import Media


def load_data(groups: List[Group], database: DatabaseService):
    for group in groups:
        grp = Group(
            group_type=group.group_type,
            tvg_group=group.tvg_group,
            first_occurrence=group.first_occurrence,
            last_occurrence=group.last_occurrence,
            total_occurrences=group.total_occurrences
        )
        group_id = database.insert_group(grp)
        for media in group.media_list:
            med = Media(
                ext_inf=media.ext_inf,
                tvg_name=media.tvg_name,
                tvg_id=media.tvg_id,
                tvg_logo=media.tvg_logo,
                tvg_group=media.tvg_group,
                catchup=media.catchup,
                catchup_days=media.catchup_days,
                media_url=media.media_url
            )
            database.insert_media(med, group_id)
