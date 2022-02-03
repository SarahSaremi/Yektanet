from advertisement.base_advertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    """
    --- Advertiser Class Description ---
    Each object of this class represents an advertiser.
    An advertiser can own multiple ads in the system.\n
    """
    __total_clicks = 0

    def __init__(self, advertiser_id, name):
        super().__init__(advertiser_id)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def help():
        return """
        --- Advertiser Help ---
        id -> A unique integer number for each advertiser.
        name -> A string representing advertiser's name. 
        click -> Total number of clicks of each advertiser. 
        views -> Total number of views of each advertiser.\n
        """

    def describe_me(self):
        return self.__doc__

    def inc_clicks(self):
        super().inc_clicks()
        Advertiser.__total_clicks += 1

    @staticmethod
    def get_total_clicks():
        return Advertiser.__total_clicks





