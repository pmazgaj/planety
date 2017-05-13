"""
Model for class Matches
"""

__author__ = "Przemek"


class Matches:
    """Model for matches (from csv files)"""

    def __init__(self, matching_id, top_priced_count):
        self.matching_id = int(matching_id)
        self.top_priced_count = int(top_priced_count)

    def __str__(self):
        return "matching_id: {} top_priced_count: {}". \
            format(self.matching_id, self.top_priced_count)
