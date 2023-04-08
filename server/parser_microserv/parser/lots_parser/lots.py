from bs4 import BeautifulSoup as bs


class Lots:
    def __init__(self, bs_content):
        self.bs_content = bs_content
        self.data = {}
        self.line = None
        self.lots = []

    def get_guid(self):
        for tag in self.line.find_all("guid"):
            if tag is not None:
                self.data["guid"] = tag.text

    def get_order_number(self):
        for tag in self.line.find("ordinalnumber"):
            if tag is not None:
                self.data["order_number"] = int(tag.text)

    def get_subject(self):
        for tag in self.line.find_all("subject"):
            if tag is not None:
                self.data["subject"] = tag.text.replace("\r\n", "").replace("\n", "").replace(";", "").strip()\
                    .replace("  ", " ").replace("\\0", "").replace('\\.', "").replace('\\', '')

    def get_initial_price(self):
        for tag in self.line.find_all("initialsum"):
            if tag is not None:
                self.data["initial_price"] = float(tag.text)

    def get_maxContractPrice(self):
        if self.data['initial_price'] == -1:
            for tag in self.line.find_all("maxcontractprice"):
                if tag is not None:
                    self.data["initial_price"] = float(tag.text)

    def get_currency(self):
        for tag in self.line.find_all("currency"):
            if tag is not None:
                self.data["currency"] = tag.findChildren()[0].text

    def set_data(self):
        self.data = {"guid": "-", "subject": "-", "order_number": "-", "initial_price": -1, 'currency': "-",
                     "bitmask": ""}

    def create_bitmask(self):
        for key in self.data:
            if key != 'bitmask':
                """checking of existing tag and save value in bitmask"""
                if type(self.data[key]) == str:
                    if self.data[key] != '-':
                        self.data['bitmask'] = self.data['bitmask'] + "1"
                    else:
                        self.data['bitmask'] = self.data['bitmask'] + "0"
                else:
                    if self.data[key] != -1:
                        self.data['bitmask'] = self.data['bitmask'] + "1"
                    else:
                        self.data['bitmask'] = self.data['bitmask'] + "0"

    def parser(self):
        """get lots"""
        for line in self.bs_content.find_all("lot"):
            self.set_data()
            self.line = line
            if self.line is not None:
                """get guid lot"""
                self.get_guid()
                """get order_number lot"""
                self.get_order_number()
                """get subject lot"""
                self.get_subject()
                """get initialsum lot"""
                self.get_initial_price()
                """get maxContractPrice (Alternative field of price)"""
                self.get_maxContractPrice()
                """get currency of initialsum lot"""
                self.get_currency()
                """create bitmask for current lot"""
                self.create_bitmask()

                self.lots.append(self.data)