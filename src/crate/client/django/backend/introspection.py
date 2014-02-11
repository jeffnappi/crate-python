# -*- coding: utf-8 -*-
from django.db.backends import BaseDatabaseIntrospection


class DatabaseIntrospection(BaseDatabaseIntrospection):
    data_types_reverse = {
        "boolean": "BooleanField",
        "byte": "SmallIntegerField",
        "short": "SmallIntegerField",
        "integer": "IntegerField",
        "long": "BigIntegerField",
        "float": "FloatField",
        "double": "FloatField",  # no double type in python
        "timestamp": "DateTimeField",
        "ip": "CharField",
        "string": "CharField",
        # TODO: object
    }

    def get_table_list(self, cursor):
        """TODO"""
        return []

    def sequence_list(self):
        """sequences not supported"""
        return []

    def get_key_columns(self, cursor, table_name):
        return []

    def get_indexes(self, cursor, table_name):
        indexes = {}
        cursor.execute("select constraint_name from information_schema.table_constraints where table_name='{}'".format(table_name))
        for colname in cursor.fetchall():
            if isinstance(colname, list):
                colname = colname[0]
            indexes[colname] = {
                'primary_key': True,
                'unique': True
            }
        return indexes
