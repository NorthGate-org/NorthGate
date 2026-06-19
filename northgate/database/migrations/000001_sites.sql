CREATE TABLE IF NOT EXISTS sites (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    visibility TEXT NOT NULL,
    path TEXT NOT NULL,
    local BOOLEAN NOT NULL DEFAULT 0,
    password TEXT,
    entry TEXT,
    allowed_extensions TEXT,
    description TEXT
)