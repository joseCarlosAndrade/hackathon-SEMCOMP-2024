CREATE TABLE "users" (
    "id" INTEGER,
    "discord_username" TEXT UNIQUE NOT NULL,
    "challengermode_username" TEXT,
    "email" TEXT,
    "number" NUMBER,
    PRIMARY KEY("id")
);

CREATE TABLE "messages" (
    "id" INTEGER,
    "from_user_id" INTEGER,
    "to_user_id" INTEGER, -- for the mvp, there will be only the broadcasting for everyone option
    "msg" TEXT NOT NULL,
    "datetime" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "match" TEXT, -- may be match specific, for future
    PRIMARY KEY("id"),
    FOREIGN KEY("from_user_id") REFERENCES "users"("id"),
    FOREIGN KEY("to_user_id") REFERENCES "users"("id")
);