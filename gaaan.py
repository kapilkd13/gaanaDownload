import os

import requests
from pydub import AudioSegment as AS

def download_file(url):
    i=1
    headers = {'content-type': 'application/json', 'Host': 'vodhls-vh.akamaihd.net',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0', \
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
        , 'Accept-Language': 'en-US,en;q=0.5','Origin':'http://gaana.com',  \
             'Cookie':'_alid_=RBUUolKP+ljUgs343S686w==; hdntl=exp=1494850096~acl=%2fi%2fsongs%2f88%2f1833588%2f21045267%2f21045267_64.mp4%2f*~data=hdntl~hmac=88820773e6767c5762772243d132c146cb21cdc933c3a048b22784abd8b1feac',  'Connection': 'keep-alive',
               'Referer': 'http://gaana.com/playlist/gaana-dj-gaana-international-top-50',
               }
    while(i<25):
        url = 'http://vodhls-vh.akamaihd.net/i/songs/91/1799591/20774921/20774921_64.mp4/segment'+str(i)+'_0_a.ts?set-akamai-hls-revision=5'

        data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
        params = {'Expires': '', 'Signature': '', 'Key-Pair-Id': 'APKAJB334VX63D3WJ5ZQ'}
        local_filename = 'kk.mpeg'
            # NOTE the stream=True parameter
        r = requests.get(url, headers=headers ,stream=True)
        with open(local_filename, 'ab') as f:
               for chunk in r.iter_content(chunk_size=1024):
                   if chunk: # filter out keep-alive new chunks
                        f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        i+=1
    r.close()
    return local_filename

filename=download_file("https://aa.cf.saavncdn.com/441/ZMC00493_01_002_64.mp3")
#filename="kk.mpeg"
mp3_filename = os.path.splitext(os.path.basename(filename))[0] + '.mp3'
AS.from_file(filename).export(mp3_filename, format='mp3')

# Host: vodhls-vh.akamaihd.net
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: http://gaana.com/playlist/gaana-dj-gaana-international-top-50
# Origin: http://gaana.com
# Cookie: _alid_=pAuM9EU3wxwlJvZxMCW6vQ==; hdntl=exp=1494778037~acl=%2fi%2fsongs%2f52%2f1839852%2f21100412%2f21100412_64.mp4%2f*~data=hdntl~hmac=4e94290fef721ce9069adec93b6adc7112bcd1338eead64f7f14784390ee43b8
# Connection: keep-alive
#http://vodhls-vh.akamaihd.net/i/songs/52/1839852/21100412/21100412_64.mp4/segment5_0_a.ts?set-akamai-hls-revision=5