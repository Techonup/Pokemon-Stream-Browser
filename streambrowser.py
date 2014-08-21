def streambrowser():
    import urllib2
    import json
    
    url = "https://api.twitch.tv/kraken/streams?game=Pok%C3%A9mon%20X%2FY"
    
    f = urllib2.urlopen(url)
    f_obj = f.read()
    
    data = json.loads(f_obj.decode('utf-8')).get('streams')

    streamdata = []

    for stream in data:
        streamdata.append([stream.get('channel').get('name'), stream.get('viewers'), stream.get('channel').get('url')])

    for stream in streamdata:
        print(stream)

    table = '<table><tr><th>Streamer</th><th>Viewers</th></tr>'
    for stream in streamdata:
        table = table + '<tr><td><a href="' + stream[2] + '">' + stream[0] + '</a></td><td>' + str(stream[1]) + '</td></tr>'
    table = table + '</table>'

    return(table)
    

if __name__ == '__main__':
    streambrowser()
