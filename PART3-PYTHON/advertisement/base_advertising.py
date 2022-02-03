
class BaseAdvertising:
    """--- BaseAdvertising Class Description ---
    Ad and Advertiser inherit this class.
    This class contains common fields and methods between these two classes.\n"""

    def __init__(self, base_id=None):
        self.base_id = base_id
        self.__clicks = 0
        self.__views = 0

    def get_clicks(self):
        return self.__clicks

    def get_view(self):
        return self.__views

    def inc_views(self):
        self.__views += 1

    def inc_clicks(self):
        self.__clicks += 1

    def describe_me(self):
        return self.__doc__


