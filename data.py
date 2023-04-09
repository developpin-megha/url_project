import sqlite3
import logging

conn = sqlite3.connect('url_short.db')
short_url_db = "SHORT_URL"


def create_table():
    sql = "CREATE TABLE IF NOT EXISTS " + short_url_db + "(" \
                                                         "ID INTEGER PRIMARY KEY AUTOINCREMENT," \
                                                         "SHORT_URL VARCHAR(255) NOT NULL UNIQUE," \
                                                         "LONG_URL TEXT  NOT NULL" \
                                                         ")"
    conn.execute(sql)
    logging.info('Opened database successfully')
    logging.info(short_url_db + ' Table created')


def insert_short_url(result, url):
    logging.info("Opened database successfully")
    try:
        conn.execute("INSERT INTO " + short_url_db + " (SHORT_URL,LONG_URL) VALUES(?,?);", (result, url))
        conn.commit()
        logging.info('Data committed')
    except ValueError:
        logging.exception("Error while inserting in the table")

    logging.info("connection closed")


def get_long_url(input_url):
    long_url = None
    try:
        cursor1 = conn.execute("SELECT long_url FROM %s where short_url=?" % short_url_db, (input_url,))
        result = cursor1.fetchone()
        if result:
            long_url = result[0]
    except ValueError:
        logging.warning("short url does not exist in the database")

    return long_url
