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
    def test_v3(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        # before changes were made
        esportes = svcs.get_groups_list()[3]
        self.assertTrue(5, esportes.first_occurrence)
        self.assertTrue(47, esportes.last_occurrence)
        self.assertTrue(10, esportes.total_occurrences)

        free = svcs.get_groups_list()[4]
        self.assertTrue(49, free.first_occurrence)
        self.assertTrue(53, free.last_occurrence)
        self.assertTrue(3, free.total_occurrences)

        variedades = svcs.get_groups_list()[9]
        self.assertTrue(15, variedades.first_occurrence)
        self.assertTrue(33, variedades.last_occurrence)
        self.assertTrue(10, variedades.total_occurrences)

        # changes were made
        svcs.remove_low_quality_channels_from_all_groups()
        sorted_groups = svcs.get_groups_list()
        channels = svcs.get_channels_list()

        # after changes were made
        esportes = svcs.get_groups_list()[3]
        self.assertTrue(5, esportes.first_occurrence)
        self.assertTrue(47, esportes.last_occurrence)
        self.assertTrue(3, esportes.total_occurrences)

        self.assertTrue(9, svcs.get_groups_list())
        self.assertTrue(not any(media.tvg_group == "FREE" for media in sorted_groups))

        variedades = svcs.get_groups_list()[8]
        self.assertTrue(15, variedades.first_occurrence)
        self.assertTrue(33, variedades.last_occurrence)
        self.assertTrue(4, variedades.total_occurrences)

        for group in sorted_groups:
            for tvg_name in group.tvg_names:
                self.assertTrue(all(f'{tvg_name} FHD²' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} H265' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} HD²' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} SD' not in item for item in channels))
                self.assertTrue(all(f'{tvg_name} SD²' not in item for item in channels))
