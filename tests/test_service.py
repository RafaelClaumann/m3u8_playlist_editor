import re
import unittest
from unittest.mock import patch, mock_open

import app.services.media_service as media_svc_import
import app.services.parse_service as parse_service
from app import helpers
from app.config.config import Config


class Testing(unittest.TestCase):
    mock_channels_list = (
        '#EXTM3U\n'
        '#EXTINF:-1 tvg-name="Easy S01E01" tvg-logo="serie.png" tvg-group="Séries | Netflix",Easy S01E01\n'
        'http://watch.com/series/easy.s01.e01.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="Easy S01E02" tvg-logo="serie.png" tvg-group="Séries | Netflix",Easy S01E02\n'
        'http://watch.com/series/easy.s01.e02.mp4\n'
        ''
        '#EXTINF:0 tvg-name="ESPN FHD" tvg-id="espn.br" tvg-logo="logo.png" tvg-group="ESPORTES",ESPN FHD\n'
        'http://watch.com/channel/espn.fhd\n'
        ''
        '#EXTINF:0 tvg-name="ESPN H265" tvg-id="espn.br" tvg-logo="logo.png" tvg-group="ESPORTES",ESPN H265\n'
        'http://watch.com/channel/espn.h265\n'
        ''
        '#EXTINF:0 tvg-name="ESPN SD²" tvg-id="espn.br" tvg-logo="logo.png" tvg-group="ESPORTES",ESPN SD²\n'
        'http://watch.com/channel/espn.sd2\n'
        ''
        '#EXTINF:-1 tvg-id="" tvg-name="24H FILMES ADAM SANDLER" tvg-logo="movie.png" tvg-group="24H FILMES",24H FILMES ADAM SANDLER\n'
        'http://watch.com/channel/24hadam.m3u8\n'
        ''
        '#EXTINF:-1 tvg-id="" tvg-name="24H FILMES BRUCE WILLIS" tvg-logo="movie.png" tvg-group="24H FILMES",24H FILMES BRUCE WILLIS\n'
        'http://watch.com/channel/24bruce.m3u8\n'
        ''
        '#EXTINF:0 tvg-name="E! FHD" tvg-id="e.br" tvg-logo="logo.png" tvg-group="VARIEDADES",E! FHD\n'
        'http://watch.com/channel/e.fhd\n'
        ''
        '#EXTINF:0 tvg-name="E! FHD²" tvg-id="e.br" tvg-logo="logo.png" tvg-group="VARIEDADES",E! FHD²\n'
        'http://watch.com/channel/e.fhd2\n'
        ''
        '#EXTINF:0 tvg-name="E! H265" tvg-id="e.br" tvg-logo="logo.png" tvg-group="VARIEDADES",E! H265\n'
        'http://watch.com/channel/e.h265\n'
        ''
        '#EXTINF:0 tvg-id="e.br" tvg-name="E! H265" tvg-logo="logo.png" tvg-group="VARIEDADES",E! H265\n'
        'http://watch.com/channel/e.h265.2\n'
        ''
        '#EXTINF:0 tvg-name="E! HD²" tvg-id="e.br" tvg-logo="logo.png" tvg-group="VARIEDADES",E! HD²\n'
        'http://watch.com/channel/e.hd2\n'
        ''
        '#EXTINF:0 tvg-id="musicbox.br" tvg-name="Music Box 4K" tvg-logo="logo.png" tvg-group="VARIEDADES",Music Box 4K\n'
        'http://watch.com/channel/musicbox.4k\n'
        ''
        '#EXTINF:0 tvg-id="musicbox.br" tvg-name="Music Box FHD" tvg-logo="logo.png" tvg-group="VARIEDADES",Music Box FHD\n'
        'http://watch.com/channel/musicbox.fhd\n'
        ''
        '#EXTINF:0 tvg-id="musicbox.br" tvg-name="Music Box H265" tvg-logo="logo.png" tvg-group="VARIEDADES",Music Box H265\n'
        'http://watch.com/channel/musicbox.h265\n'
        ''
        '#EXTINF:0 tvg-id="musicbox.br" tvg-name="Music Box HD²" tvg-logo="logo.png" tvg-group="VARIEDADES",Music Box HD²\n'
        'http://watch.com/channel/musicbox.hd2\n'
        ''
        '#EXTINF:0 tvg-name="Music Box SD²" tvg-id="musicbox.br" tvg-logo="logo.png" tvg-group="VARIEDADES",Music Box SD²\n'
        'http://watch.com/channel/musicbox.sd2\n'
        ''
        '#EXTINF:0 tvg-id="espn.br" tvg-name="ESPN HD" tvg-logo="logo.png" tvg-group="ESPORTES",ESPN HD\n'
        'http://watch.com/channel/espn.hd\n'
        ''
        '#EXTINF:0 tvg-name="ESPN HD²" tvg-logo="logo.png" tvg-id="espn.br"  tvg-group="ESPORTES",ESPN HD²\n'
        'http://watch.com/channel/espn.hd2\n'
        ''
        '#EXTINF:0 tvg-name="BAND SPORTS FHD" tvg-id="bandsports.br" tvg-logo="logo.png" tvg-group="ESPORTES",BAND SPORTS FHD\n'
        'http://watch.com/channel/bandsports.fhd\n'
        ''
        '#EXTINF:0 tvg-name="BAND SPORTS H265" tvg-id="bandsports.br" tvg-logo="logo.png" tvg-group="ESPORTES",BAND SPORTS H265\n'
        'http://watch.com/channel/bandsports.h265\n'
        ''
        '#EXTINF:0 tvg-id="bandsports.br" tvg-name="BAND SPORTS HD" tvg-logo="logo.png" tvg-group="ESPORTES",BAND SPORTS HD\n'
        'http://watch.com/channel/bandsports.hd\n'
        ''
        '#EXTINF:0 tvg-id="bandsports.br" tvg-name="BAND SPORTS HD²" tvg-logo="logo.png" tvg-group="ESPORTES",BAND SPORTS HD²\n'
        'http://watch.com/channel/bandsports.hd2\n'
        ''
        '#EXTINF:0 tvg-name="BAND SPORTS SD²" tvg-id="bandsports.br" tvg-logo="logo.png" tvg-group="ESPORTES",BAND SPORTS SD²\n'
        'http://watch.com/channel/bandsports.sd2\n'
        ''
        '#EXTINF:0 tvg-name="Free channel SD²" tvg-id="free.br" tvg-logo="logo.png" tvg-group="FREE",Free channel SD²\n'
        'http://watch.com/channel/free.sd2\n'
        ''
        '#EXTINF:0 tvg-name="Free channel H265" tvg-id="free.br" tvg-logo="logo.png" tvg-group="FREE",Free channel H265\n'
        'http://watch.com/channel/free.h265\n'
        ''
        '#EXTINF:0 tvg-name="Free channel HD²" tvg-id="free.br" tvg-logo="logo.png" tvg-group="FREE",Free channel HD²\n'
        'http://watch.com/channel/free.hd2\n'
        ''
        '#EXTINF:-1 tvg-name="Easy S01E03" tvg-logo="serie.png" tvg-group="Séries | Netflix",Easy S01E03\n'
        'http://watch.com/series/easy.s01.e04.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="007: Operação Skyfall" tvg-logo="movie.png" tvg-group="Coletânea | 007",007: Operação Skyfall\n'
        'http://watch.com/movie/007skyfall.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="Rambo I" tvg-logo="movie.png" tvg-group="Coletânea | Rambo",Rambo I\n'
        'http://watch.com/movie/ramboi.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="Rambo II" tvg-logo="movie.png" tvg-group="Coletânea | Rambo",Rambo II\n'
        'http://watch.com/movie/ramboii.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="The Boys S04E03" tvg-logo="serie.png" tvg-group="Séries | Amazon Prime Vídeo",The Boys S04E03\n'
        'http://watch.com/series/theboys.s04.e03.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="Vida de Inseto" tvg-logo="movie.png" tvg-group="Filmes | Animação / Infantil",Vida de Inseto\n'
        'http://watch.com/movie/vidadeinseto.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="Ratatouille" tvg-logo="movie.png" tvg-group="Filmes | Animação / Infantil",Ratatouille\n'
        'http://watch.com/movie/ratatouille.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="The Last of Us S01E08" tvg-logo="serie.png" tvg-group="Séries | Max",The Last of Us S01E08\n'
        'http://watch.com/series/tlou.s01.e08.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="The Last of Us S01E09" tvg-logo="serie.png" tvg-group="Séries | Max",The Last of Us S01E09\n'
        'http://watch.com/series/tlou.s01.e09.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="The Boys S04E01" tvg-logo="serie.png" tvg-group="Séries | Amazon Prime Vídeo",The Boys S04E01\n'
        'http://watch.com/series/theboys.s04.e01.mp4\n'
        ''
        '#EXTINF:-1 tvg-name="The Boys S04E02" tvg-logo="serie.png" tvg-group="Séries | Amazon Prime Vídeo",The Boys S04E02\n'
        'http://watch.com/series/theboys.s04.e02.mp4\n'
    )

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_all_low_quality_channels(self, mock_channels_list):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        # before changes were made
        esportes_group = media_svc.media_groups[3]
        self.assertTrue(5, esportes_group.first_occurrence)
        self.assertTrue(47, esportes_group.last_occurrence)
        self.assertTrue(10, esportes_group.total_occurrences)

        free_group = media_svc.media_groups[4]
        self.assertTrue(49, free_group.first_occurrence)
        self.assertTrue(53, free_group.last_occurrence)
        self.assertTrue(3, free_group.total_occurrences)

        variedades_group = media_svc.media_groups[9]
        self.assertTrue(15, variedades_group.first_occurrence)
        self.assertTrue(33, variedades_group.last_occurrence)
        self.assertTrue(10, variedades_group.total_occurrences)

        # changes were made
        media_svc.remove_low_quality_channels_from_all_groups()

        # after changes were made
        self.assertTrue(5, esportes_group.first_occurrence)
        self.assertTrue(47, esportes_group.last_occurrence)
        self.assertTrue(3, esportes_group.total_occurrences)

        self.assertTrue(9, media_svc.media_groups)
        self.assertEqual(0, len(media_svc.media_groups[4].media_list))

        self.assertTrue(15, variedades_group.first_occurrence)
        self.assertTrue(33, variedades_group.last_occurrence)
        self.assertTrue(4, variedades_group.total_occurrences)

        for group in media_svc.media_groups:
            for media in group.media_list:
                quality_pattern = r'tvg-name="([^"]*(\bHD²|SD|SD²|H265)[^"]*)"'
                self.assertIsNone(re.search(quality_pattern, media.tvg_name))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_low_quality_from_a_group(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        esportes_group = media_svc.media_groups[3]
        media_svc.remove_low_quality_channels_from_group(esportes_group)

        # ensure that groups_list size still the same
        self.assertEqual(10, len(media_svc.media_groups))
        # ensure that esportes group have 6(low quality) channels removed
        self.assertEqual(4, esportes_group.total_occurrences)

        low_quality_esportes = [
            'ESPN H265',
            'ESPN SD²',
            'ESPN HD²',
            'BAND SPORTS H266',
            'BAND SPORTS HD²',
            'BAND SPORTS SD²'
        ]
        # ensure that no one low quality channel can be found in esportes group
        self.assertFalse(any(tvg_name in low_quality_esportes for tvg_name in esportes_group.media_list))
        # ensure that esportes group still exists in group list after low quality channels deletion
        self.assertTrue(any(group.tvg_group == "ESPORTES" for group in media_svc.media_groups))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_low_quality_from_a_group_that_contains_only_low_quality(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        free_group = media_svc.media_groups[4]
        free_channels = free_group.media_list
        media_svc.remove_low_quality_channels_from_group(free_group)

        # ensure that group free aren't in groups list
        self.assertTrue(not any(media.tvg_group == "FREE" for media in free_group.media_list))
        # ensure that free media_list aren't in channels list
        self.assertFalse(any(tvg_name in free_channels for tvg_name in free_group.media_list))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_esportes_group(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        esportes_group = media_svc.media_groups[3]
        media_svc.remove_groups([esportes_group])

        # ensure groups list has decreased in one element
        self.assertEqual(9, len(media_svc.media_groups))
        # ensure that group esportes aren't in groups list
        self.assertTrue(all(group.tvg_group != esportes_group.tvg_group for group in media_svc.media_groups))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_multiple_groups(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        twenty_four_movies_group = media_svc.media_groups[0]
        twenty_four_movies_group_name = twenty_four_movies_group.tvg_group

        free_group = media_svc.media_groups[4]
        free_group_name = free_group.tvg_group

        amazon_series_group = media_svc.media_groups[6]
        amazon_series_group_name = amazon_series_group.tvg_group

        max_series_group = media_svc.media_groups[7]
        max_series_group_name = max_series_group.tvg_group

        media_svc.remove_groups([twenty_four_movies_group, free_group, amazon_series_group, max_series_group])

        # ensure groups list has decreased in five elements
        self.assertEqual(6, len(media_svc.media_groups))

        # ensure that tvg-group(24H FILMES) aren't in groups list
        self.assertFalse(any(group.tvg_group == twenty_four_movies_group_name for group in media_svc.media_groups))

        # ensure that tvg-group(FREE) aren't in groups list
        self.assertFalse(any(group.tvg_group == free_group_name for group in media_svc.media_groups))

        # ensure that tvg-group(Séries | Amazon Prime Vídeo) aren't in groups list
        self.assertFalse(any(group.tvg_group == amazon_series_group_name for group in media_svc.media_groups))

        # ensure that tvg-group(Séries | Max) aren't in groups list
        self.assertFalse(any(group.tvg_group == max_series_group_name for group in media_svc.media_groups))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_all_groups(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        groups_to_remove = media_svc.media_groups
        media_svc.remove_groups(groups_to_remove)

        # ensure groups list has 0 elements
        self.assertEqual(0, len(media_svc.media_groups))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_medias_from_group(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        esportes_group = media_svc.media_groups[3]
        media_svc.remove_media_from_group(esportes_group, [5, 6, 7, 8, 9])

        # ensure the size of media_list was decreased correctly
        self.assertEqual(5, len(esportes_group.media_list))
        # ensure that group esportes was maintained in groups list
        self.assertTrue(any(group.tvg_group == "ESPORTES" for group in media_svc.media_groups))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_medias_from_group_with_one_element(self, positional01):
        raw_media_list = helpers.read_file(Config.INPUT_PLAYLIST_PATH)
        parsed_media_list = parse_service.parse_raw_list(raw_list=raw_media_list)
        media_svc = media_svc_import.MediaService(group_media_list=parsed_media_list)

        group_name = 'Coletânea | 007'
        media_index = 0

        collection_group = media_svc.media_groups[1]
        media_svc.remove_media_from_group(collection_group, [media_index])

        # ensure the size of tvg-group(Coletânea | 007) media_list was decreased correctly
        self.assertEqual(0, len(collection_group.media_list))
        # ensure that tvg-group(Coletânea | 007) was maintained in groups list
        self.assertTrue(any(group.tvg_group == group_name for group in media_svc.media_groups))
