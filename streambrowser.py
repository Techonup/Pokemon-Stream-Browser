import urllib.request
import json

streams = {}

def update():
    url = "https://api.twitch.tv/kraken/streams?game=Pok%C3%A9mon%20X%2FY"
    
    f = urllib.request.urlopen(url)
    charset = f.info().get_param('charset', 'utf8')
    f_obj = f.read()
    
    data = json.loads(f_obj.decode(charset)).get('streams')

    streamdata = []

    for stream in data:
        streamdata.append([stream.get('channel').get('name'), stream.get('viewers'), stream.get('channel').get('url')])

    for stream in streamdata:
        print(stream)
    
update()
