CREATE TABLE IF NOT EXISTS Stats(
    User_ID integer PRIMARY KEY,
    Experince integer default 0,
    XP_Lock text DEFAULT CURRENT_TIMESTAMP
);
