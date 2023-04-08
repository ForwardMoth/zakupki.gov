import os

from parser.customer_parser.customer import *
from parser.placer_parser.placer import *
from parser.maindata_parser.maindata import *
from parser.lots_parser.lots import *

"""
The idea of new 1 is following:
using bs4 we read entire xml document and then using method "find_all" or "find"
we looking for data using specific tag and then extracting it
"""


class Parser:
    def __init__(self, regions, directories):
        self.regions = regions
        self.directories = directories
        self.list_ways = []
        self.parsers = {'customer': None, 'placer': None, 'maindata': None, 'lots': None}
        self.data = {}

    """Function to creating list of files"""
    def set_list_of_ways(self, directory):
        if len(os.listdir(directory)) != 0:
            os.chdir(directory)
            part_way = os.getcwd()
            files = os.listdir()
            for file in files:
                self.list_ways.append(part_way + '/' + file)
            os.chdir('..')

    """Function for iteration to dirs and checking daily, full dirs"""
    def dirs_iterator(self):
        """Get list of directories: daily, full, manual and monthly dirs with xml"""
        directories = os.listdir()
        """Iterate to directories"""
        for directory in directories:
            if directory != 'daily' and directory != 'full' and directory != 'manual':
                self.set_list_of_ways(directory)
            else:
                os.chdir(directory)
                """Get list of directories in daily, full or manual directory"""
                nested_directories = os.listdir()
                for nested_dir in nested_directories:
                    self.set_list_of_ways(nested_dir)
                os.chdir('..')

    """Main function of getting list ways: changing to needed directory"""
    def main_list_ways(self):
        os.chdir("xml")
        """Iterate to regions"""
        for region in self.regions:
            os.chdir(region)
            """Iterate to directories"""
            for directory in self.directories:
                """Check not existing directories for Krym_Resp and Sevastopol"""
                if not ((region == 'Krym_Resp' or region == 'Sevastopol') and directory == 'purchaseNoticeIS'):
                    """Change dir and use parse function"""
                    os.chdir(directory)
                    self.dirs_iterator()
                os.chdir('..')
            os.chdir('..')

    def create_bitmask(self, obj):
        for key in obj.data:
            if key != 'bitmask':
                """checking of existing tag and save value in bitmask"""
                if obj.data[key] != '-':
                    obj.data['bitmask'] = obj.data['bitmask'] + "1"
                else:
                    obj.data['bitmask'] = obj.data['bitmask'] + "0"

    """Iterator of parser"""
    def parse_all(self):
        for key in self.parsers:
            if self.parsers[key] is not None:
                self.parsers[key].parser()
                if key != 'lots':
                    self.create_bitmask(self.parsers[key])
                    if key == 'maindata':
                        self.parsers[key].set_region(self.regions[0])
                        self.parsers[key].check_modification_datetime()
                    self.data[key] = self.parsers[key].data
                else:
                    self.data[key] = self.parsers[key].lots

    def parser(self, document_path):
        with open(document_path, "r", encoding="utf-8") as file:
            content = file.readlines()
            content = "".join(content)
            bs_content = bs(content, "lxml")
            """Customer parser object"""
            self.parsers['customer'] = Customer(bs_content)
            """Placer parser object"""
            self.parsers['placer'] = Placer(bs_content)
            """Maindata parser object"""
            self.parsers['maindata'] = Maindata(bs_content)
            """Lots parser object"""
            self.parsers['lots'] = Lots(bs_content)

            self.parse_all()
        return self.data
