import os, logging, zipfile
from pathlib import Path

"""Method, which archive zips forms every month"""


def archiver(region, directory):
    if (region == 'Krym_Resp' or region == 'Sevastopol') and directory == 'purchaseNoticeIS':
        return
    # 1
    """way of zips"""
    zip_way = os.getcwd() + '/zip' + '/' + region + '/' + directory
    """list of loaded zips"""

    # 2
    """create a directory"""
    if not os.path.exists('xml' + '/' + region + '/' + directory):
        os.makedirs("xml" + '/' + region + '/' + directory)
    """change directory"""
    os.chdir('xml' + '/' + region + '/' + directory)
    zip_dirs = set(os.listdir())
    # 3
    i = 0
    for fl in [str(f.absolute()) for f in Path(zip_way).iterdir()]:
        dir_name = fl.split('/')[-1]
        if dir_name != 'daily' and dir_name != 'full' and dir_name != 'manual':
            if dir_name not in zip_dirs:
                """create new name of dir like name of zip"""
                if not os.path.exists(dir_name):
                    os.makedirs(dir_name)
                os.chdir(dir_name)

                """way to xml"""
                out_way = os.getcwd()
                try:
                    with zipfile.ZipFile(fl) as zf:
                        zf.extractall(out_way)
                    i += 1
                except zipfile.BadZipFile as e:
                    print(e, fl)
                os.chdir('..')
        else:
            """new zip way """
            zip_way_ins = zip_way + '/' + dir_name
            """create new directory for xml"""
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            os.chdir(dir_name)
            """get names of directories with unzipped zips"""
            zip_dirs_ins = set(os.listdir())

            for fl_ins in [str(f.absolute()) for f in Path(zip_way_ins).iterdir()]:
                dir_name_ins = fl_ins.split('/')[-1]
                if dir_name_ins not in zip_dirs_ins:
                    """create new name of dir like name of zip"""
                    if not os.path.exists(dir_name_ins):
                        os.makedirs(dir_name_ins)
                    os.chdir(dir_name_ins)

                    """way to xml"""
                    out_way = os.getcwd()
                    try:
                        with zipfile.ZipFile(fl_ins) as zf:
                            zf.extractall(out_way)
                        i += 1
                    except zipfile.BadZipFile as e:
                        print(e, fl_ins)
                    os.chdir('..')
            os.chdir('..')

    for _ in range(3):
        os.chdir('..')
    logging.info(f'files unzipped: {i} from directory /zip/{region}/{directory}')


"""Main method"""


def archive_all(regions, directories):
    for region in regions:
        for directory in directories:
            archiver(region, directory)
