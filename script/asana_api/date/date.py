__author__ = 'ptesser'
from datetime import datetime


class Date(object):
    """TODO

    """
    @staticmethod
    def convert_date(d_str):
        """TODO

        Args:
            d_str: TODO

        Returns:
            TODO
        """
        year_int = int(d_str[0:4])
        month_int = int(d_str[5:7])
        day_int = int(d_str[8:10])
        dt = datetime(year_int, month_int, day_int)
        date_dtd = datetime.date(dt)
        return date_dtd