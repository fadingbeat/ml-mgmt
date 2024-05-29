DROP TABLE IF EXISTS models;

CREATE TABLE models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    m_name TEXT NOT NULL,
    m_description TEXT NOT NULL,
    m_version TEXT NOT NULL,
    m_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);