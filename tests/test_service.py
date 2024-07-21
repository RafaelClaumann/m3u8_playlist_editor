import unittest
from unittest.mock import patch, mock_open

from app.services import services as svc


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
    def test_remove_all_low_quality_channels(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        # before changes were made
        esportes_group = svcs.get_groups_list()[3]
        self.assertTrue(5, esportes_group.first_occurrence)
        self.assertTrue(47, esportes_group.last_occurrence)
        self.assertTrue(10, esportes_group.total_occurrences)

        free_group = svcs.get_groups_list()[4]
        self.assertTrue(49, free_group.first_occurrence)
        self.assertTrue(53, free_group.last_occurrence)
        self.assertTrue(3, free_group.total_occurrences)

        variedades_group = svcs.get_groups_list()[9]
        self.assertTrue(15, variedades_group.first_occurrence)
        self.assertTrue(33, variedades_group.last_occurrence)
        self.assertTrue(10, variedades_group.total_occurrences)

        # changes were made
        svcs.remove_low_quality_channels_from_all_groups()
        sorted_groups = svcs.get_groups_list()
        channels = svcs.get_channels_list()

        # after changes were made
        self.assertTrue(5, esportes_group.first_occurrence)
        self.assertTrue(47, esportes_group.last_occurrence)
        self.assertTrue(3, esportes_group.total_occurrences)

        self.assertTrue(9, svcs.get_groups_list())
        self.assertTrue(not any(media.tvg_group == "FREE" for media in sorted_groups))

        self.assertTrue(15, variedades_group.first_occurrence)
        self.assertTrue(33, variedades_group.last_occurrence)
        self.assertTrue(4, variedades_group.total_occurrences)

        for group in sorted_groups:
            for tvg_name in group.media_list:
                self.assertTrue(all(f'{tvg_name} FHD²' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} H265' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} HD²' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} SD' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} SD²' not in item for item in channels))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_low_quality_from_a_group(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        esportes_group = svcs.get_groups_list()[3]
        svcs.remove_low_quality_channels_from_group(esportes_group)

        # ensure that groups_list size still the same
        self.assertEqual(10, len(svcs.get_groups_list()))
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
        self.assertTrue(any(group.tvg_group == "ESPORTES" for group in svcs.get_groups_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_low_quality_from_a_group_that_contains_only_low_quality(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        free_group = svcs.get_groups_list()[4]
        free_channels = free_group.media_list
        svcs.remove_low_quality_channels_from_group(free_group)

        # ensure groups list has decreased in one element
        self.assertEqual(9, len(svcs.get_groups_list()))
        # ensure that group free aren't in groups list
        self.assertTrue(not any(media.tvg_group == "FREE" for media in svcs.get_groups_list()))
        # ensure that group free aren't in channels list
        self.assertTrue(all('tvg-group="FREE"' not in item for item in svcs.get_channels_list()))
        # ensure that free media_list aren't in channels list
        self.assertFalse(any(tvg_name in free_channels for tvg_name in svcs.get_channels_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_esportes_group(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        esportes_group = svcs.get_groups_list()[3]
        esportes_channels = esportes_group.media_list
        svcs.remove_groups([esportes_group])

        # ensure groups list has decreased in one element
        self.assertEqual(9, len(svcs.get_groups_list()))
        # ensure that group esportes aren't in groups list
        self.assertFalse(any(group.tvg_group == "ESPORTES" for group in svcs.get_groups_list()))
        # ensure that group esportes aren't in channels list
        self.assertTrue(all('tvg-group="ESPORTES"' not in item for item in svcs.get_channels_list()))
        # ensure that esportes media_list aren't in channels list
        self.assertFalse(any(tvg_name in esportes_channels for tvg_name in svcs.get_channels_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_multiple_group(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        twenty_four_movies_group = svcs.get_groups_list()[0]
        twenty_four_movies_group_name = twenty_four_movies_group.tvg_group
        twenty_four_movies_medias = twenty_four_movies_group.media_list

        free_group = svcs.get_groups_list()[4]
        free_group_name = free_group.tvg_group
        free_medias = free_group.media_list

        amazon_series_group = svcs.get_groups_list()[6]
        amazon_series_group_name = amazon_series_group.tvg_group
        amazon_series_media = amazon_series_group.media_list

        max_series_group = svcs.get_groups_list()[7]
        max_series_group_name = max_series_group.tvg_group
        max_series_media = max_series_group.media_list

        svcs.remove_groups([twenty_four_movies_group, free_group, amazon_series_group, max_series_group])

        # ensure groups list has decreased in five elements
        self.assertEqual(6, len(svcs.get_groups_list()))

        # ensure that tvg-group(24H FILMES) aren't in groups list
        self.assertFalse(any(group.tvg_group == twenty_four_movies_group_name for group in svcs.get_groups_list()))
        # ensure that tvg-group(24H FILMES) aren't in channels list
        self.assertTrue(all(f'tvg-group="{twenty_four_movies_group_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg-group(24H FILMES) media_list aren't in channels list
        self.assertFalse(any(tvg_name in twenty_four_movies_medias for tvg_name in svcs.get_channels_list()))

        # ensure that tvg-group(FREE) aren't in groups list
        self.assertFalse(any(group.tvg_group == free_group_name for group in svcs.get_groups_list()))
        # ensure that tvg-group(FREE) aren't in channels list
        self.assertTrue(all(f'tvg-group="{free_group_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg-group(FREE) media_list aren't in channels list
        self.assertFalse(any(tvg_name in free_medias for tvg_name in svcs.get_channels_list()))

        # ensure that tvg-group(Séries | Amazon Prime Vídeo) aren't in groups list
        self.assertFalse(any(group.tvg_group == amazon_series_group_name for group in svcs.get_groups_list()))
        # ensure that tvg-group(Séries | Amazon Prime Vídeo) aren't in channels list
        self.assertTrue(all(f'tvg-group="{amazon_series_group_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg-group(Séries | Amazon Prime Vídeo) media_list aren't in channels list
        self.assertFalse(any(tvg_name in amazon_series_media for tvg_name in svcs.get_channels_list()))

        # ensure that tvg-group(Séries | Max) aren't in groups list
        self.assertFalse(any(group.tvg_group == max_series_group_name for group in svcs.get_groups_list()))
        # ensure that tvg-group(Séries | Max) aren't in channels list
        self.assertTrue(all(f'tvg-group="{max_series_group_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg-group(Séries | Max) media_list aren't in channels list
        self.assertFalse(any(tvg_name in max_series_media for tvg_name in svcs.get_channels_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_medias_from_group(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        # original esportes media_list 09 channels
        # original esportes media_list elements 05 to 09 will be removed, remaining 5 channels
        # original esportes media_list size after removal 5 elements
        media_to_remove = [
            {"index": 5, "name": 'BAND SPORTS FHD'},
            {"index": 6, "name": 'BAND SPORTS H265'},
            {"index": 7, "name": 'BAND SPORTS HD'},
            {"index": 8, "name": 'BAND SPORTS HD²'},
            {"index": 9, "name": 'BAND SPORTS SD²'}
        ]

        media_indexes = [item["index"] for item in media_to_remove]
        media_names = [item["name"] for item in media_to_remove]

        esportes_group = svcs.get_groups_list()[3]
        svcs.remove_medias_from_group(esportes_group, media_indexes)

        # ensure the size of media_list was decreased correctly
        self.assertEqual(5, len(esportes_group.media_list))
        # ensure that group esportes was maintained in groups list
        self.assertTrue(any(group.tvg_group == "ESPORTES" for group in svcs.get_groups_list()))
        # ensure that no one media_list from 'media_to_remove' are in esportes media_list list
        self.assertTrue(not any(tvg_name in media_names for tvg_name in esportes_group.media_list))
        # ensure that no one media_list from 'media_to_remove' are in channels_list
        for media_name in media_names:
            self.assertTrue(all(f'tvg-name="{media_name}"' not in item for item in svcs.get_channels_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=mock_channels_list)
    def test_remove_medias_from_group_with_one_element(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        group_name = 'Coletânea | 007'
        media_name = "007: Operação Skyfall"
        media_index = 0

        collection_group = svcs.get_groups_list()[1]
        svcs.remove_medias_from_group(collection_group, [media_index])

        # ensure the size of media_list was decreased correctly
        self.assertEqual(0, len(collection_group.media_list))
        # ensure that tvg-group(Coletânea | 007) was removed from channels list
        self.assertTrue(all(f'tvg-group="{group_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg-group(Coletânea | 007) was maintained in groups list
        self.assertTrue(any(group.tvg_group == group_name for group in svcs.get_groups_list()))
        # ensure the tvg_name(007: Operação Skyfall) from tvg-group(Coletânea | 007) are not in channels_list
        self.assertTrue(all(f'tvg-name="{media_name}"' not in item for item in svcs.get_channels_list()))
        # ensure that tvg_name(007: Operação Skyfall) was removed from tvg-group(Coletânea | 007)
        self.assertTrue(all(media_name not in item for item in collection_group.media_list))
