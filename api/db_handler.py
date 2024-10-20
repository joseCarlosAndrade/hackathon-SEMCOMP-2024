import sqlite3
from datetime import datetime


# queries
SELECT_ALL_USERS = """
    SELECT * FROM "users"
"""

FIND_USER_ID = """
SELECT "id" FROM "users" WHERE "discord_username" = '{}'
"""

INSERT_MESSAGES = """
INSERT INTO "messages" ("from_user_id", "msg", "datetime", "match")
VALUES
(1, 'Partida 1 prestes a começar!', {}, 'LoLcuras'),
(1, 'Partida 2 ira atrasar 15 minutos!', {}, 'LoLcuras),
(3, 'A premiação acontecerá amanhã', {}, 'Lobos solitários')
"""

INSERT_SINGLE_MESSAGE = """
INSERT INTO "messages" ("from_user_id", "to_user_id", "msg", "datetime", "match")
VALUES
({}, {}, '{}', '{}', '{}')
"""

INSERT_SINGLE_MESSAGE_FOR_ALL = """
INSERT INTO "messages" ("from_user_id", "msg", "datetime", "match")
VALUES
({}, '{}', '{}', '{}')
"""

GET_LAST_24HOURS_MESSAGES = """SELECT * FROM "messages" WHERE "datetime" >= DATETIME('now', '-24 hours') ;"""

class DataBaseHandler():
    """Handles data base handling, to decouple this logic from our api
    note: it is presumed that all the users are already registered in the database
    """
    def __init__(self, path=""):
        if path == "":
            raise Exception("Empty path")
        
        try:
            self.conn = sqlite3.connect('acad.db', check_same_thread=False)
        except Exception as err:
            print("could not connect to sqlite3 database, ", err)
            return False

        self.cursor = self.conn.cursor() # getting a cursor

    
    def populate_messages(self):
        # utility to populate the db
        date1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date2 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date3 = "2024-09-20 14:12:10"
        # self.cursor.execute(INSERT_MESSAGES.format(date1, date2, date3))
        self.cursor.execute('''
            INSERT INTO "messages" ("from_user_id", "msg", "datetime", "match")
            VALUES
            (1, 'Partida 1 prestes a começar!', ?, 'LoLcuras'),
            (1, 'Partida 2 ira atrasar 15 minutos!', ?, 'LoLcuras'),
            (3, 'A premiação acontecerá amanhã', ?, 'Lobos solitários')
            ''', (date1, date2, date3))

        self.conn.commit()

    
    def save_message(self, from_user, to_user, msg, datetime, match):
        """save a single message in the database. `to_user` is the only field that may be null (in cases where the msg is intended for all)

        Args:
            from_user (str): discord id from the sender
            to_user (str or None): discord id from the receiver (optional)
            msg (str): message content
            datetime (datetime str in format '%Y-%m-%d %H:%M:%S'): timestamp of the message
            match (str): match detail
        """
        query = FIND_USER_ID.format(from_user)
        rows = self.cursor.execute(query)
        
        from_user_id = 0

        for row in rows:
            print("found user: ", row[0])
            from_user_id = row[0]

        to_user_id = 0

        if to_user != None:
            query = FIND_USER_ID.format(to_user)
            rows = self.cursor.execute(query)

            for row in rows:
                to_user_id = print("found user: ", row[0])
        
        if to_user_id == 0:
            
            query = INSERT_SINGLE_MESSAGE_FOR_ALL.format(from_user_id, msg, datetime, match)
            print("final query: ", query)
            self.conn.execute(query)
            self.conn.commit()

        # if to_user != None:
        #     to_user_id = FIND_USER_ID.format(from_user_id)

            
    def get_last_24h_messages(self):
        query = GET_LAST_24HOURS_MESSAGES

        rows = self.conn.execute(query)
        
        messages = []

        for row in rows:
            message = {
                "id": row[0],
                "from_user_id": row[1],
                "to_user_id": row[2],
                "msg": row[3],
                "datetime": row[4],
                "match": row[5]
            }
            messages.append(message)

        return messages

if __name__ == "__main__":
    # test queries
    handler = DataBaseHandler(path="acad.db")
    handler.populate_messages() 

    handler.save_message("maria_o", None, "Premiaçao agendada", "2024-10-20 15:12:10", "Solitos")
    handler.get_last_24h_messages()