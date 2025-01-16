import datetime


class mark:

    here = None

    def __init__(self, mes=""):
        self.mes = mes

    @property
    def here(self):
        print(f"{self.mes} {datetime.datetime.now()}")


