from downloader.load import *
from parser.archiver import *
from parser.parser import *
from database.db import *
from config.auth import notice_directories

def main():
    print("hello from main function")
    # """Creating dir"""
    # if not os.path.exists("log" + '/'):
    #     os.makedirs("log" + '/')
    # os.chdir("log" + '/')

    # """Creating log file"""
    # file_name = str(datetime.datetime.now().__format__("%Y-%m-%d-%H-%M-%S"))

    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     filename=f"{file_name}.log",
    #     format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    #     datefmt='%H:%M:%S',
    # )
    # """Change dir"""
    # for _ in range(1):
    #     os.chdir("..")

    """test data"""
    all_regions = ['Moskva']



    """load all zips (enough memory for this action)"""
    load_all(all_regions, notice_directories)
    print("Загрузка закончена")
    """unzip zips. This function works in cycle, because xml take up a lot of memory on the disk
       Iteration by regions 
    """
    for region in all_regions:
        """unzip"""
        archive_all([region], notice_directories)
        """create parser object"""
        parser = Parser([region], notice_directories)
        """get list of ways to xml for parsing (not empty dirs)"""
        parser.main_list_ways()
        """
            Parsing document + inserting in database, 
            1) Get data from parsed xml document. Deleting document after parsing 
                data = {'table_name': {'key': 'value', 'key2': 'value'}, 
                        'table_name2': {'key': 'value', 'key2': 'value'}
                       }
            2) Operations with database and inserting unique data 
            Iteration by ways to xml 
        """
        for way in parser.list_ways:
            """parsing"""
            data = parser.parser(way)
            """activity with database"""
            """ Algorythm inserting 
                1. Checking customer in table by inn + fullname if true: return id => customers_id
                2. If false: insert customer + get id after inserting => customers_id
                3. Do analogue actions for placer => placers_id
                4. Checking maindata by guid if true: return id => maindata_id
                5. If false: insert maindata + get id after inserting => maindata_id and 
                   after inserting lots! 
                Done all!!!
            """

            db = Database(data)
            db.add_all(way)
            db.session.close()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(go())


if __name__ == '__main__':
    main()
