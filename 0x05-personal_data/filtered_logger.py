#!/usr/bin/env python3
"""
filtered_logger
"""
import re
import logging
import os
from typing import List
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def RedactingFormatter(logging.Formatter):
    """
    RedactingFormatter
    """

    def format(self, record):
        """
        format
        """
        return logging.Formatter.filter(self, record)


def filter_datum(fields, redaction, message, separator):
    """
    filter_datum
    """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)
    return message


def get_logger() -> logging.Logger:
    """
    get_logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get_db
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"))


def main():
    """
    main
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]
    logger = get_logger()

    for row in cursor:
        message = ""
        for i in range(len(fields)):
            message += "{}={}; ".format(fields[i], row[i])
        message = filter_datum(PII_FIELDS, "****", message, "; ")
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
