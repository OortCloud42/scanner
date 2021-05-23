import time

import requests
import untangle
from requests_toolbelt.downloadutils import stream

rStartScan = requests.post('https://192.168.223.1/eSCL/ScanJobs', verify=False, data='<scan:ScanSettings xmlns:scan="http://schemas.hp.com/imaging/escl/2011/05/03" xmlns:dd="http://www.hp.com/schemas/imaging/con/dictionaries/1.0/" xmlns:dd3="http://www.hp.com/schemas/imaging/con/dictionaries/2009/04/06" xmlns:fw="http://www.hp.com/schemas/imaging/con/firewall/2011/01/05" xmlns:scc="http://schemas.hp.com/imaging/escl/2011/05/03" xmlns:pwg="http://www.pwg.org/schemas/2010/12/sm"><pwg:Version>2.1</pwg:Version><scan:Intent>Document</scan:Intent><pwg:ScanRegions><pwg:ScanRegion><pwg:Height>3507</pwg:Height><pwg:Width>2481</pwg:Width><pwg:XOffset>0</pwg:XOffset><pwg:YOffset>0</pwg:YOffset></pwg:ScanRegion></pwg:ScanRegions><pwg:InputSource>Feeder</pwg:InputSource><scan:DocumentFormatExt>application/pdf</scan:DocumentFormatExt><scan:XResolution>300</scan:XResolution><scan:YResolution>300</scan:YResolution><scan:ColorMode>RGB24</scan:ColorMode><scan:Duplex>false</scan:Duplex><scan:CompressionFactor>0</scan:CompressionFactor><scan:Brightness>1000</scan:Brightness><scan:Contrast>1000</scan:Contrast></scan:ScanSettings>')

location = rStartScan.headers['location'] + '/NextDocument'

request = requests.get(location, verify=False, stream=True)

name = time.strftime("%H:%M:%S") + '.pdf'

stream.stream_response_to_file(request, path=name)
