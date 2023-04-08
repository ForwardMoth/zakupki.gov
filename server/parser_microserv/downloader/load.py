import datetime
import ftplib
import logging
import os
from ftplib import FTP

"""Connection to ftp server - get object of ftp server"""


def connect():
    ftp = FTP("ftp.zakupki.gov.ru")
    ftp.login("fz223free", "fz223free")
    return ftp


"""Method, which used all methods of download and unite logic of load"""


def load_all(regions, directories):
    date = str(datetime.date.today())
    for region in regions:
        for directory in directories:
            """
            Load files from directory
            """

            """Connect to server"""
            ftp = connect()
            """Load zip-files"""
            loader(ftp, region, directory)
            ftp.close()

            """Connect to server"""
            ftp = connect()
            """Load zip-files from dirs like: full, manual, daily"""
            loader_dirs(ftp, region, directory)
            ftp.close()


"""Method, which checking new files, which haven't loaded yet - return list of zips"""


def get_zips(ftp_zips):
    return set(ftp_zips) - set(os.listdir())


"""Method, which load zips forms every month"""


def loader(ftp, region, directory):
    if (region == 'Krym_Resp' or region == 'Sevastopol') and directory == 'purchaseNoticeIS':
        return
    i = 0
    try:
        # 1
        """Change ftp directory to daily"""
        ftp.sendcmd('PASV')
        ftp.cwd(f"/out/published/{region}/{directory}/")
        # 2
        if not os.path.exists("zip" + '/' + region + '/' + directory):
            os.makedirs("zip" + '/' + region + '/' + directory)
        os.chdir("zip" + '/' + region + '/' + directory)
        out_way = os.getcwd()
        zips = get_zips(ftp.nlst())
        # 3
        for zip in zips:
            if zip != 'daily' and zip != 'full' and zip != 'manual':
                if ftp.size(zip) > 400:
                    host_file = os.path.join(out_way, zip)
                    i += 1
                    try:
                        with open(host_file, 'wb') as local_file:
                            ftp.retrbinary("RETR " + zip, local_file.write)
                            # logging.info(f'download:  {host_file}')
                    except ftplib.all_errors:
                        pass
                        # logging.exception("ftplib occured")
        for _ in range(3):
            os.chdir('..')
    except ftplib.all_errors:
        pass
        # logging.exception("ftplib occured")
    logging.info(f'files downloaded: {i} from directory /out/published/{region}/{directory}')


"""Method, which load zips from directories: full, manual, daily - zips forms every day"""


def loader_dirs(ftp, region, directory):
    if (region == 'Krym_Resp' or region == 'Sevastopol') and directory == 'purchaseNoticeIS':
        return
    i = 0
    try:
        ftp.sendcmd('PASV')
        ftp.cwd(f"/out/published/{region}/{directory}/")
        files = ftp.nlst()
        for ftp_dir in ['full', 'manual', 'daily']:
            if ftp_dir in files:
                # 1
                """Change ftp directory to daily"""
                ftp.cwd(f"/out/published/{region}/{directory}/{ftp_dir}")
                # 2
                if not os.path.exists("zip" + '/' + region + '/' + directory + '/' + ftp_dir):
                    os.makedirs("zip" + '/' + region + '/' + directory + '/' + ftp_dir)
                os.chdir("zip" + '/' + region + '/' + directory + '/' + ftp_dir)
                out_way = os.getcwd()
                zips = get_zips(ftp.nlst())
                # 3
                for zip in zips:
                    if ftp.size(zip) > 400:
                        host_file = os.path.join(out_way, zip)
                        i += 1
                        try:
                            with open(host_file, 'wb') as local_file:
                                ftp.retrbinary("RETR " + zip, local_file.write)
                                # logging.info(f'download:  {host_file}')
                        except ftplib.all_errors:
                            pass
                            # logging.exception("ftplib occured")
                for _ in range(4):
                    os.chdir('..')
    except ftplib.all_errors:
        pass
        # logging.exception("ftplib occured")
    logging.info(f'files downloaded: {i} from directory /out/published/{region}/{directory}')
