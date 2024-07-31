CREATE TABLE group_type (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
    );

CREATE TABLE group_table (
    id INTEGER PRIMARY KEY,
    group_type INTEGER,
    tvg_group TEXT,
    first_occurrence INTEGER,
    last_occurrence INTEGER,
    total_occurrences INTEGER,
    FOREIGN KEY(group_type) REFERENCES group_type(id)
);

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
);
