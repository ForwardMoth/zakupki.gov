from bs4 import BeautifulSoup as bs
from config.auth import dict_regions


class Maindata:
    def __init__(self, bs_content):
        self.bs_content = bs_content
        self.data = {'notice_number': "-", 'name': "-", 'guid': "-", 'create_datetime': '-',
                     'publication_datetime': '-', 'modification_datetime': "-", 'version': "-",
                     'status': "-", 'purchase_codename': "-", "bitmask": ""}

    def get_guid(self):
        for line in self.bs_content.find_all("ns2:guid"):
            if line is not None:
                self.data['guid'] = line.text

    def get_notice_number(self):
        for line in self.bs_content.find_all("ns2:registrationnumber"):
            if line is not None:
                self.data["notice_number"] = int(line.text)

    def get_publication_datetime(self):
        for line in self.bs_content.find_all("ns2:publicationdatetime"):
            if line is not None:
                self.data["publication_datetime"] = line.text

    def get_modification_datetime(self):
        for line in self.bs_content.find_all("ns2:modificationdate"):
            if line is not None:
                self.data["modification_datetime"] = line.text

    def get_create_datetime(self):
        for line in self.bs_content.find_all("ns2:createdatetime"):
            if line is not None:
                self.data["create_datetime"] = line.text

    def get_name(self):
        for line in self.bs_content.find_all("ns2:name"):
            if line is not None:
                self.data["name"] = line.text.replace("\r\n", "").replace("\n", "").replace(".", "").replace(";", "") \
                    .replace("\\", "").rstrip()

    def get_status(self):
        for line in self.bs_content.find_all("ns2:status"):
            if line is not None:
                self.data["status"] = line.text

    def get_version(self):
        for line in self.bs_content.find_all("ns2:version"):
            if line is not None:
                self.data["version"] = line.text

    def set_region(self, region):
        self.data['region'] = dict_regions[region]

    def get_purchase_codename(self):
        for line in self.bs_content.find_all("ns2:purchasecodename"):
            if line is not None:
                self.data["purchase_codename"] = line.text

    def check_modification_datetime(self):
        if self.data['modification_datetime'] == '-':
            self.data['modification_datetime'] = '2001-01-01'

    def parser(self):
        """get guid"""
        self.get_guid()
        """get notice_number"""
        self.get_notice_number()
        """get publication_datetime"""
        self.get_publication_datetime()
        """get modification_datetime"""
        self.get_modification_datetime()
        """get create_datetime"""
        self.get_create_datetime()
        """get name"""
        self.get_name()
        """get status"""
        self.get_status()
        """get version"""
        self.get_version()
        """get purchaseCodeName"""
        self.get_purchase_codename()
