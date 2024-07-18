import unittest
from unittest.mock import patch, mock_open
import app.services.services as svc


class Testing(unittest.TestCase):
    # um grupo com canais validos e canais invalidos
    one_group_valid_and_invalid_channels = """#EXTM3U
#EXTINF:0 tvg-name="CNN FHD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN FHD
http://watch.com/cnn.fhd

#EXTINF:0 tvg-name="CNN FHD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN FHD²
http:// watch.com/cnn.fhd2

#EXTINF:0 tvg-name="CNN HD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN HD
http://watch.com/cnn.fhd

#EXTINF:0 tvg-name="CNN HD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN HD²
http://watch.com/cnn.hd2

#EXTINF:0 tvg-name="CNN SD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN SD
http://watch.com/cnn.sd

#EXTINF:0 tvg-name="CNN SD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN SD²
http://watch.com/cnn.sd2
"""

    one_group_only_invalid_channels = """#EXTM3U
#EXTINF:0 tvg-name="CNN HD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN HD²
http://watch.com/cnn.hd2

#EXTINF:0 tvg-name="CNN SD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN SD
http://watch.com/cnn.sd

#EXTINF:0 tvg-name="CNN SD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN SD²
http://watch.com/cnn.sd2
"""

    one_group_only_valid_channels = """#EXTM3U
#EXTINF:0 tvg-name="CNN 4K" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN 4K
http:// watch.com/cnn.4k

#EXTINF:0 tvg-name="CNN FHD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN FHD
http:// watch.com/cnn.fhd

#EXTINF:0 tvg-name="CNN FHD²" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN FHD²
http:// watch.com/cnn.fhd2

#EXTINF:0 tvg-name="CNN HD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN HD
http://watch.com/cnn.hd
"""

    # 3 groups
    #   NEWS [4K, FHD, HD] - first = 7, last = 13, total = 3
    #   DOCUMENTARY [H265, FHD, HD] - first = 1, last = 16, total = 3
    #   SPORTS [FHD, HD, HD²] - first = 19, last = 25, total = 3
    test = """#EXTM3U
#EXTINF:0 tvg-name="Discovery H265" tvg-id="discovery.br" tvg-logo="logo.png" tvg-group="DOCUMENTARY",Discovery H265
http://watch.com/discovery.h265

#EXTINF:0 tvg-name="Discovery FHD" tvg-id="discovery.br" tvg-logo="logo.png" tvg-group="DOCUMENTARY",Discovery FHD
http://watch.com/discovery.fhd
    
#EXTINF:0 tvg-name="CNN 4K" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN 4K
http:// watch.com/cnn.4k

#EXTINF:0 tvg-name="CNN FHD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN FHD
http:// watch.com/cnn.fhd

#EXTINF:0 tvg-name="CNN HD" tvg-id="cnn.br" tvg-logo="logo.png" tvg-group="NEWS",CNN HD
http:// watch.com/cnn.hd

#EXTINF:0 tvg-name="Discovery HD" tvg-id="discovery.br" tvg-logo="logo.png" tvg-group="DOCUMENTARY",Discovery HD
http://watch.com/discovery.hd

#EXTINF:0 tvg-name="Sports FHD" tvg-id="sports.br" tvg-logo="logo.png" tvg-group="SPORTS",Sports FHD
http://watch.com/sports.fhd

#EXTINF:0 tvg-name="Sports HD" tvg-id="sports.br" tvg-logo="logo.png" tvg-group="SPORTS",Sports HD
http://watch.com/sports.hd

#EXTINF:0 tvg-name="Sports HD²" tvg-id="sports.br" tvg-logo="logo.png" tvg-group="SPORTS",Sports HD²
http://watch.com/sports.hd2
"""

    # um unico grupo com alguns canais de baixa qualidade
    @patch("builtins.open", new_callable=mock_open, read_data=one_group_valid_and_invalid_channels)
    def test_one_group_valid_and_invalid_channels(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        news_group = svcs.get_groups_list()[0]
        svcs.remove_low_quality_channels_from_group(news_group)

        self.assertEqual(3, len(news_group.tvg_names))
        self.assertEqual(3, news_group.total_occurrences)
        self.assertEqual(1, news_group.first_occurrence)
        self.assertEqual(16, news_group.last_occurrence)
        self.assertTrue(any(channel == 'CNN FHD' for channel in news_group.tvg_names))
        self.assertTrue(any(channel == 'CNN FHD²' for channel in news_group.tvg_names))
        self.assertTrue(any(channel == 'CNN HD' for channel in news_group.tvg_names))

    # a lista de canais deve ter apenas o primeiro o elemento, os restantes devem se strings vazias
    # o grupo deve ser excluido já que não possui mais canais
    @patch("builtins.open", new_callable=mock_open, read_data=one_group_only_invalid_channels)
    def test_one_group_only_invalid_channels(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        news_group = svcs.get_groups_list()[0]
        svcs.remove_low_quality_channels_from_group(news_group)

        # guarantee that aren't elements with '#EXTINF:' in the list
        no_extinf = all('#EXTINF:' not in item for item in svcs.get_channels_list())

        self.assertTrue(no_extinf)
        self.assertEqual(0, len(svcs.get_groups_list()))

    @patch("builtins.open", new_callable=mock_open, read_data=one_group_only_valid_channels)
    def test_one_group_only_valid_channels(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        news_group = svcs.get_groups_list()[0]
        svcs.remove_low_quality_channels_from_group(news_group)

        self.assertEqual(1, len(svcs.get_groups_list()))
        self.assertEqual(4, news_group.total_occurrences)
        self.assertEqual(1, news_group.first_occurrence)
        self.assertEqual(10, news_group.last_occurrence)

    @patch("builtins.open", new_callable=mock_open, read_data=test)
    def test_v2(self, positional01):
        svcs = svc.Services("fake_input_playlist_path")

        svcs.remove_low_quality_channels_from_all_groups()
        sorted_groups = svcs.get_groups_list()

        documentary = sorted_groups[0]
        self.assertEqual(2, documentary.total_occurrences)
        self.assertEqual(1, documentary.first_occurrence)
        self.assertEqual(16, documentary.last_occurrence)
        self.assertTrue(all('H265:' not in item for item in documentary.tvg_names))

        news = sorted_groups[1]
        self.assertEqual(3, news.total_occurrences)
        self.assertEqual(7, news.first_occurrence)
        self.assertEqual(13, news.last_occurrence)

        sports = sorted_groups[2]
        self.assertEqual(2, sports.total_occurrences)
        self.assertEqual(19, sports.first_occurrence)
        self.assertEqual(25, sports.last_occurrence)
        self.assertTrue(all('HD²:' not in item for item in sports.tvg_names))
