from bs4 import BeautifulSoup as bs


class Customer:
    def __init__(self, bs_content):
        self.bs_content = bs_content
        self.data = {'fullname': "-", 'shortname': "-", 'inn': "-", 'kpp': "-", 'ogrn': "-", 'legal_address': "-",
                     'postal_address': "-", "bitmask": ""}
        self.children = None

    def get_fullname(self):
        fullname = self.children[0].find('fullname')
        if fullname is not None:
            self.data['fullname'] = fullname.text.lower().replace(";", "").replace("\r\n", "").replace("\n", "").strip()

    def get_shortname(self):
        shortname = self.children[0].find("shortname")
        if shortname is not None:
            self.data['shortname'] = shortname.text.replace("\r\n", "").replace("\n", "").rstrip(".") \
                .replace(";", "").rstrip()

    def get_inn(self):
        inn = self.children[0].find("inn")
        if inn is not None:
            self.data["inn"] = inn.text

    def get_kpp(self):
        kpp = self.children[0].find("kpp")
        if kpp is not None:
            self.data["kpp"] = kpp.text

    def get_ogrn(self):
        ogrn = self.children[0].find("ogrn")
        if ogrn is not None:
            self.data["ogrn"] = ogrn.text

    def get_legaladdress(self):
        legaladdress = self.children[0].find("legaladdress")
        if legaladdress is not None:
            self.data["legal_address"] = legaladdress.text.replace("\r\n", "").replace("\n", "").rstrip(".") \
                .replace(";", "").rstrip()

    def get_postaladress(self):
        postaladdress = self.children[0].find("postaladdress")
        if postaladdress is not None:
            self.data["postal_address"] = postaladdress.text.replace("\r\n", "").replace("\n", "").rstrip(".") \
                .replace(";", "").rstrip()

    def parser(self):
        """get customer"""
        for line in self.bs_content.find_all("ns2:customer"):
            self.children = line.findChildren()
        if self.children is not None:
            """get fullname"""
            self.get_fullname()
            """get shortname"""
            self.get_shortname()
            """get inn"""
            self.get_inn()
            """get kpp"""
            self.get_kpp()
            """get ogrn"""
            self.get_ogrn()
            """get legaladdress"""
            self.get_legaladdress()
            """get postaladdress"""
            self.get_postaladress()
