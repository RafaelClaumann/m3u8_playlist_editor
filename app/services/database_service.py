import sqlite3

from models.group import Group
from models.group_type import GroupType
from models.media import Media


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.populate_group_types()

    def __del__(self):
        self.connection.close()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE group_type (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        self.cursor.execute("""
        CREATE TABLE group_table (
            id INTEGER PRIMARY KEY,
            group_type INTEGER,
            tvg_group TEXT,
            first_occurrence INTEGER,
            last_occurrence INTEGER,
            total_occurrences INTEGER,
            FOREIGN KEY(group_type) REFERENCES group_type(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE media_table (
            id INTEGER PRIMARY KEY,
            ext_inf TEXT,
            tvg_name TEXT,
            tvg_id TEXT,
            tvg_logo TEXT,
            tvg_group TEXT,
            catchup TEXT,
            catchup_days INTEGER,
            media_url TEXT,
            group_id INTEGER,
            FOREIGN KEY(group_id) REFERENCES group_table(id)
        )
        """)

        self.connection.commit()

    def populate_group_types(self):
        for group_type in GroupType:
            try:
                self.cursor.execute("INSERT INTO group_type (name) VALUES (?)", (group_type.name,))
            except sqlite3.IntegrityError:
                pass
        self.connection.commit()

    def insert_group(self, group: Group):
        statement = """
        INSERT INTO group_table (group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
        VALUES (?, ?, ?, ?, ?)
        """

        parameters = (
            group.group_type.value,
            group.tvg_group,
            group.first_occurrence,
            group.last_occurrence,
            group.total_occurrences
        )

        try:
            self.cursor.execute(statement, parameters)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Error [insert_group]: {e}")
            return None

    def fetch_group(self, group_id: int):
        try:
            self.cursor.execute("SELECT * FROM group_table WHERE id = ?", (group_id,))
            row = self.cursor.fetchone()
        except Exception as e:
            print(f"Error [fetch_group]: {e}")
            return None

        if row:
            group = dict(row)
            return Group(**group)
        return None

    def fetch_groups(self):
        try:
            self.cursor.execute("SELECT * FROM group_table")
            rows = self.cursor.fetchall()
        except Exception as e:
            print(f"Error [fetch_groups]: {e}")
            return None

        groups = [Group(**dict(row)) for row in rows]
        return groups

    def update_group(self, group: Group):
        statement = """
        UPDATE  group_table
        SET     group_type = ?,
                tvg_group = ?,
                first_occurrence = ?,
                last_occurrence = ?,
                total_occurrences = ?
        WHERE   id = ?
        """

        parameters = (
            group.group_type,
            group.tvg_group,
            group.first_occurrence,
            group.last_occurrence,
            group.total_occurrences,
            group.id
        )

        try:
            self.cursor.execute(statement, parameters)
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [update_group]: {e}")
            return None

    def delete_group(self, group_id: int):
        try:
            self.cursor.execute("DELETE FROM media_table WHERE group_id = ?", (group_id,))
            self.cursor.execute("DELETE FROM group_table WHERE id = ?", (group_id,))
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_group]: {e}")
            return None

    def fetch_groups_by_type(self, group_type: GroupType):
        try:
            self.cursor.execute("SELECT * FROM group_table WHERE group_type = ?", (group_type.value,))
            rows = self.cursor.fetchall()
        except Exception as e:
            print(f"Error [fetch_groups_by_type]: {e}")
            return None

        groups = [Group(**dict(row)) for row in rows]
        return groups

    def insert_media(self, media: Media, group_id: int):
        statement = """
            INSERT INTO media_table (ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        parameters = (
            media.ext_inf,
            media.tvg_name,
            media.tvg_id,
            media.tvg_logo,
            media.tvg_group,
            media.catchup,
            media.catchup_days,
            media.media_url,
            group_id
        )

        try:
            self.cursor.execute(statement, parameters)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Error [insert_media]: {e}")
            return None

    def fetch_media(self, media_id: int):
        try:
            self.cursor.execute("SELECT * FROM media_table WHERE id = ?", (media_id,))
            row = self.cursor.fetchone()
        except Exception as e:
            print(f"Error [fetch_media]: {e}")
            return None

        if row:
            media = dict(row)
            return Media(**media)
        return None

    def fetch_medias(self):
        try:
            self.cursor.execute("SELECT * FROM media_table")
            rows = self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching [fetch_medias]: {e}")
            return None

        medias = [Media(**dict(row)) for row in rows]
        return medias

    def update_media(self, media: Media):
        statement = """
        UPDATE  media_table
        SET     ext_inf = ?,
                tvg_name = ?,
                tvg_id = ?,
                tvg_logo = ?,
                tvg_group = ?,
                catchup = ?,
                catchup_days = ?,
                media_url = ?
        WHERE   id = ?
        """

        parameters = (
            media.ext_inf,
            media.tvg_name,
            media.tvg_id,
            media.tvg_logo,
            media.tvg_group,
            media.catchup,
            media.catchup_days,
            media.media_url,
            media.id
        )

        try:
            self.cursor.execute(statement, parameters)
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [update_media]: {e}")
            return None

    def delete_media(self, media_id: int):
        try:
            self.cursor.execute("DELETE FROM media_table WHERE id = ?", (media_id,))
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_media]: {e}")
            return None

    def fetch_media_by_group_id(self, group_id: int):
        try:
            self.cursor.execute("SELECT * FROM media_table WHERE group_id = ?", (group_id,))
            rows = self.cursor.fetchall()
        except Exception as e:
            print(f"Error [fetch_media_by_group_id]: {e}")
            return None

        medias = [Media(**dict(row)) for row in rows]
        return medias

    def delete_media_by_group_id(self, group_id):
        try:
            self.cursor.execute("DELETE FROM media WHERE group_id = ?", (group_id,))
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_media_by_group_id]: {e}")
            return None

    def delete_media_by_group_and_media_id(self, group_id, media_id):
        try:
            self.cursor.execute("DELETE FROM media_table WHERE group_id = ? AND id = ?", (group_id, media_id))
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_media_by_group_and_media_id]: {e}")
            return None

    def delete_low_quality_channels_from_group(self, group_id):
        statement = """
        DELETE
        FROM    media_table
        WHERE   (tvg_name LIKE '%HD²%' OR
                 tvg_name LIKE '%SD%' OR
                 tvg_name LIKE '%SD²%' OR
                 tvg_name LIKE '%H265%') AND
                group_id = ?
        """

        try:
            self.cursor.execute(statement, (group_id,))
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_low_quality_channels_from_group]: {e}")
            return None

    def delete_all_low_quality_channels(self):
        statement = """
        DELETE
        FROM    media_table
        WHERE   (tvg_name LIKE '%HD²%' OR
                 tvg_name LIKE '%SD%' OR
                 tvg_name LIKE '%SD²%' OR
                 tvg_name LIKE '%H265%')
        """

        try:
            self.cursor.execute(statement)
            self.connection.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(f"Error [delete_all_low_quality_channels]: {e}")
            return None
