
import subprocess
import json
import xarray as xr

def download_sst():
    ''' This is a module for downloading the SST data from the CMEMS

    Here the address is a cmems data access portal:
    #https://resources.marine.copernicus.eu/?option=com_csw&task=results
    
    You have to register at the CMEMS (link above) and store your username and password in pass.json 
    in a form :
    {"username":"***",
    "password":"***"}'

    GLOBAL OCEAN OSTIA SEA SURFACE TEMPERATURE AND SEA ICE ANALYSIS
    #https://resources.marine.copernicus.eu/?option=com_csw&view=details&product_id=SST_GLO_SST_L4_NRT_OBSERVATIONS_010_001

    Read the description of this command line tool 
    https://resources.marine.copernicus.eu/?option=com_csw&view=order&record_id=9bee0cb0-343d-421a-9a19-150dd07fb0e5
    '''

    addr = 'https://nrt.cmems-du.eu/motu-web/Motu'

    with open('pass.json') as f:
        data = json.load(f)
        username=data['username']
        passw=data['password']


    s_id = 'SST_GLO_SST_L4_NRT_OBSERVATIONS_010_001-TDS'
    prod_id = "METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2"
    output_path_dir = '.'

    filename = 'Copernicus.nc'

    long_min = 2.5
    long_max = 6.5

    lat_min = 58
    lat_max = 61
    start = "2018-12-01 12:00:00"
    stop = "2020-12-31 12:00:00"

    cmd = f'python3 -m motuclient --motu {addr} --service-id {s_id} --product-id {prod_id} '\
        f'--longitude-min {long_min} --longitude-max {long_max} ' \
        f'--latitude-min {lat_min} --latitude-max {lat_max} '\
        f'--date-min {start} --date-max {stop} '\
        f'--variable analysed_sst --variable analysis_error --variable mask '\
        f'--out-dir {output_path_dir} --out-name {filename} --user {username} --pwd {passw}'
    print (cmd)


    subprocess.call(cmd, shell=True)

def read_nc_sst():
    with xr.open_dataset('Copernicus.nc') as ds:
        print (ds)


if __name__== '__main__':
    pass
