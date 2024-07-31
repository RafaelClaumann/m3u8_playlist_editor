INSERT INTO group_type (id, name) VALUES (1, 'CHANNELS');
INSERT INTO group_type (id, name) VALUES (2, 'MOVIES');
INSERT INTO group_type (id, name) VALUES (3, 'SERIES');

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (1, 1, '24H FILMES', 11, 13, 2);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0101, '#EXTINF:-1', '24H FILMES ADAM SANDLER', '', 'sandler.png', '24H FILMES', '', 0, 'http://watch.com/channel/24hadam.m3u8', 1);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0102, '#EXTINF:-1', '24H FILMES BRUCE WILLIS', '', 'willis.png', '24H FILMES', '', 0, 'http://watch.com/channel/24bruce.m3u8', 1);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (2, 2, 'Coletânea | 007', 57, 57, 1);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0201, '#EXTINF:-1', '007: Operação Skyfall', '', 'skyfall.png', 'Coletânea | 007', '', 0, 'http://watch.com/movie/007skyfall.mp4', 2);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (3, 2, 'Coletânea | Rambo', 59, 61, 2);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0301, '#EXTINF:-1', 'Rambo I', '', 'ramboi.png', 'Coletânea | Rambo', '', 0, 'http://watch.com/movie/ramboi.mp4', 3);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (4, 1, 'ESPORTES', 5, 47, 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0401, '#EXTINF:0', 'ESPN FHD', 'espn.br', 'espn.png', 'ESPORTES', '', 0, 'http://watch.com/channel/espn.fhd', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0402, '#EXTINF:0', 'ESPN h265', 'espn.br', 'espn.png', 'ESPORTES', '', 0, 'http://watch.com/channel/espn.h265', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0403, '#EXTINF:0', 'ESPN SD²', 'espn.br', 'espn.png', 'ESPORTES', '', 0, 'http://watch.com/channel/espn.sd2', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0404, '#EXTINF:0', 'ESPN HD', 'espn.br', 'espn.png', 'ESPORTES', '', 0, 'http://watch.com/channel/espn.hd', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0405, '#EXTINF:0', 'ESPN HD²', 'espn.br', 'espn.png', 'ESPORTES', '', 0, 'http://watch.com/channel/espn.hd2', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0406, '#EXTINF:0', 'BAND SPORTS FHD', 'bandsports.br', 'bandsports.png', 'ESPORTES', '', 0, 'http://watch.com/channel/bandsports.fhd', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0407, '#EXTINF:0', 'BAND SPORTS H265', 'bandsports.br', 'bandsports.png', 'ESPORTES', '', 0, 'http://watch.com/channel/bandsports.h265', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0408, '#EXTINF:0', 'BAND SPORTS HD', 'bandsports.br', 'bandsports.png', 'ESPORTES', '', 0, 'http://watch.com/channel/bandsports.hd', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0409, '#EXTINF:0', 'BAND SPORTS HD²', 'bandsports.br', 'bandsports.png', 'ESPORTES', '', 0, 'http://watch.com/channel/bandsports.hd2', 4);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0410, '#EXTINF:0', 'BAND SPORTS SD²', 'bandsports.br', 'bandsports.png', 'ESPORTES', '', 0, 'http://watch.com/channel/bandsports.sd2', 4);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (5, 1, 'FREE', 49, 53, 3);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0501, '#EXTINF:0', 'Free channel SD²', 'free.br', 'free.png', 'FREE', '', 0, 'http://watch.com/channel/free.sd2', 5);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0502, '#EXTINF:0', 'Free channel H265', 'free.br', 'free.png', 'FREE', '', 0, 'http://watch.com/channel/free.h265', 5);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0503, '#EXTINF:0', 'Free channel HD²', 'free.br', 'free.png', 'FREE', '', 0, 'http://watch.com/channel/free.hd2', 5);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (6, 2, 'Filmes | Animação / Infantil', 65, 67, 2);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0601, '#EXTINF:-1', 'Vida de Inseto', '', 'vidadeinseto.png', 'Filmes | Animação / Infantil', '', 0, 'http://watch.com/movie/vidadeinseto.mp4', 6);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0602, '#EXTINF:-1', 'Ratatouille', '', 'ratatouille.png', 'Filmes | Animação / Infantil', '', 0, 'http://watch.com/movie/ratatouille.mp4', 6);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (7, 3, 'Séries | Amazon Prime Vídeo', 63, 75, 3);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0701, '#EXTINF:-1', 'The Boys S04E01', '', 'theboys.png', 'Séries | Amazon Prime Vídeo', '', 0, 'http://watch.com/series/theboys.s04.e01.mp4', 7);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0702, '#EXTINF:-1', 'The Boys S04E02', '', 'theboys.png', 'Séries | Amazon Prime Vídeo', '', 0, 'http://watch.com/series/theboys.s04.e02.mp4', 7);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0703, '#EXTINF:-1', 'The Boys S04E03', '', 'theboys.png', 'Séries | Amazon Prime Vídeo', '', 0, 'http://watch.com/series/theboys.s04.e03.mp4', 7);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (8, 3, 'Séries | Max', 69, 71, 2);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0801, '#EXTINF:-1', 'The Last of Us S01E08', '', 'tlou.png', 'Séries | Max', '', 0, 'http://watch.com/series/tlou.s01.e08.mp4', 8);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0802, '#EXTINF:-1', 'The Last of Us S01E09', '', 'tlou.png', 'Séries | Max', '', 0, 'http://watch.com/series/tlou.s01.e09.mp4', 8);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (9, 3, 'Séries | Netflix', 1, 55, 3);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0901, '#EXTINF:-1', 'Easy S01E01', '', 'easy.png', 'Séries | Netflix', '', 0, 'http://watch.com/series/easy.s01.e01.mp4', 9);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0902, '#EXTINF:-1', 'Easy S01E02', '', 'easy.png', 'Séries | Netflix', '', 0, 'http://watch.com/series/easy.s01.e02.mp4', 9);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (0903, '#EXTINF:-1', 'Easy S01E04', '', 'easy.png', 'Séries | Netflix', '', 0, 'http://watch.com/series/easy.s01.e04.mp4', 9);

INSERT INTO group_table (id, group_type, tvg_group, first_occurrence, last_occurrence, total_occurrences)
VALUES (10, 1, 'VARIEDADES', 15, 33, 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1001,'#EXTINF:0', 'E! FHD', 'e.br', 'e.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/e.fhd', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1002, '#EXTINF:0', 'E! FHD²', 'e.br', 'e.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/e.fhd2', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1003,'#EXTINF:0', 'E! H265', 'e.br', 'e.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/e.h265', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1004, '#EXTINF:0', 'E! H265', 'e.br', 'e.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/e.h265.2', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1005, '#EXTINF:0', 'E! HD²', 'e.br', 'e.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/e.hd2', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1006, '#EXTINF:0', 'Music Box 4K', 'musicbox.br', 'musicbox.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/musicbox.4k', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1007, '#EXTINF:0', 'Music Box FHD', 'musicbox.br', 'musicbox.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/musicbox.fhd', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1008, '#EXTINF:0', 'Music Box H265', 'musicbox.br', 'musicbox.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/musicbox.h265', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1009, '#EXTINF:0', 'Music Box HD²', 'musicbox.br', 'musicbox.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/musicbox.hd2', 10);
INSERT INTO media_table (id, ext_inf, tvg_name, tvg_id, tvg_logo, tvg_group, catchup, catchup_days, media_url, group_id)
VALUES (1010, '#EXTINF:0', 'Music Box SD²', 'musicbox.br', 'musicbox.png', 'VARIEDADES', '', 0, 'http://watch.com/channel/musicbox.Sd2', 10);
