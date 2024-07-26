import re
import sqlite3
import unittest

from app.services.database_service import DatabaseService


class Testing(unittest.TestCase):

    def setUp(self):
        self.db_connection = sqlite3.connect(':memory:')
        self.db_connection.row_factory = sqlite3.Row
        self.cursor = self.db_connection.cursor()

        with open('00_schema.sql', 'r', encoding='utf-8') as file:
            schema = file.read()
        self.cursor.executescript(schema)
        self.db_connection.commit()

        with open('01_data.sql', 'r', encoding='utf-8') as file:
            schema = file.read()
        self.cursor.executescript(schema)
        self.db_connection.commit()

    def tearDown(self):
        self.db_connection.close()

    def test_database_setup(self):
        db = DatabaseService(database_connection=self.db_connection)

        groups = db.fetch_groups()
        medias = db.fetch_medias()

        self.assertEqual(10, len(groups))
        self.assertEqual(37, len(medias))

    def test_remove_group_and_their_media(self):
        db = DatabaseService(database_connection=self.db_connection)

        # id            = 4
        # tvg_group     = ESPORTES
        # media_items   = 10
        group_before = db.fetch_group(4)
        medias_before = db.fetch_media_by_group_id(4)

        total_affected_rows = db.delete_group(4)

        group_after = db.fetch_group(4)
        medias_after = db.fetch_media_by_group_id(4)

        self.assertEqual(11, total_affected_rows)
        self.assertIsNotNone(group_before)
        self.assertIsNone(group_after)
        self.assertEqual(10, len(medias_before))
        self.assertEqual([], medias_after)

    def test_remove_media(self):
        db = DatabaseService(database_connection=self.db_connection)

        # id            = 4
        # tvg_group     = ESPORTES
        # media_items   = 10 (6 low quality)
        medias_before = db.fetch_media_by_group_id(4)
        media_id = medias_before[0].id

        total_affected_rows = db.delete_media(media_id)

        medias_after = db.fetch_media_by_group_id(4)
        media_after = db.fetch_media(media_id)

        self.assertEqual(1, total_affected_rows)
        self.assertEqual(10, len(medias_before))
        self.assertEqual(9, len(medias_after))
        self.assertIsNone(media_after)

    def test_remove_low_quality_channels(self):
        db = DatabaseService(database_connection=self.db_connection)

        total_affected_rows = db.delete_all_low_quality_channels()
        resulting_medias = db.fetch_medias()

        self.assertEqual(16, total_affected_rows)
        for media in resulting_medias:
            quality_pattern = r'tvg-name="([^"]*(\bHD²|SD|SD²|H265)[^"]*)"'
            self.assertIsNone(re.search(quality_pattern, media.tvg_name))

    def test_remove_low_quality_from_a_group(self):
        db = DatabaseService(database_connection=self.db_connection)

        # id            = 4
        # tvg_group     = ESPORTES
        # media_items   = 10 (6 low quality)
        group = db.fetch_group(4)
        medias_before = db.fetch_media_by_group_id(group_id=group.id)

        total_affected_rows = db.delete_low_quality_channels_from_group(group_id=group.id)

        medias_after = db.fetch_media_by_group_id(group_id=group.id)

        self.assertEqual(6, total_affected_rows)
        self.assertEqual(10, len(medias_before))
        self.assertEqual(4, len(medias_after))
        for media in medias_after:
            quality_pattern = r'tvg-name="([^"]*(\bHD²|SD|SD²|H265)[^"]*)"'
            self.assertIsNone(re.search(quality_pattern, media.tvg_name))
