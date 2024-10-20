# SERVER api

This is an REST api made in Flask using python that uses `sqlite` to store important messages notifications. It also provides a layer of abstraction from the `graphQL` api provided by Challengermode services. For further information, consult the `queries.py` file.

It handles the OAuth authentication flow in `Auth.py`, allowing the user to log in to our platform using the ChallengerMode credentials.

## Database

The saved messages and users are stored in `sqlite3` tables.
