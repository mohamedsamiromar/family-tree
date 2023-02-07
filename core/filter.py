import json
from django.db.models import Q
from django.db import connection


class FilterService():

    @staticmethod
    def session_query(filters, session_defualt_key):
        # this function converts a list of filters to executable query
        # or defaultKey for filtration
        queries = {}
        fil = json.loads(filters)
        for filter in fil:
            for key, value in filter.items():
                queries[key] = value
        return queries
