import os, shutil
from jinja2 import Template, Environment, FileSystemLoader
from bs4 import BeautifulSoup
import requests
import json

class SiteGenerator(object):
    def __init__(self):
        self.frames = []
        self.env = Environment(loader=FileSystemLoader('template'))
        self.fetch_iframes()
        self.empty_public()
        self.copy_static()
        self.render_page()

    def fetch_iframes(self):
        """ Request iframes, saving them in self.iframes """
        
        link = 'https://bandcamp.com/USERNAME/wishlist' # Add your Bandcamp credentials here
        data = requests.get(link)

        #print(data.status_code)
        #print(data.headers)

        # Load data into BS4
        src = data.content
        soup = BeautifulSoup(src, 'html.parser')
        result = []
        for tag in soup.findAll(True,{'data-blob':True}) :
            result.append(tag['data-blob'])

        #print(result)

        #Extract wishlist tag
        for item in result:
            item = json.loads(item)
            #print(item['item_cache']['wishlist'])

        # Extract iframe values from wishlist tag
        values = item['item_cache']['wishlist']
        album_id = []
        track_id = []
        track_name = []

        for v_id, v_info in values.items():
                album_id.append(v_info['album_id'])

        for v_id, v_info in values.items():
                track_id.append(v_info['tralbum_id'])

        for v_id, v_info in values.items():
                track_name.append(v_info['item_title'])

        #print(album_id)
        #print(track_id)
        #print(track_name)

        #Create iframe templates from album_id and track_id
        stub_list = ['''<iframe style="border: 0; width: 100%; height: 120px;" src="https://bandcamp.com/EmbeddedPlayer/album=''', '''/size=large/bgcol=333333/linkcol=0687f5/tracklist=false/artwork=small/track=''','''/transparent=true/" seamless></iframe>''' ]
        self.iframes = [stub_list[0] + str(album) + stub_list[1] + str(track)+ stub_list[2] for album, track in zip(album_id, track_id)]
        iframes_tuples = {stub_list[0] + str(album) + stub_list[1] + str(track)+ stub_list[2] for album, track in zip(album_id, track_id)}

        #len(self.iframes)

    def empty_public(self):
        try:
            shutil.rmtree('./public') 
            os.mkdir('./public')
        except:
            print("Could not clean up old files")

    def copy_static(self):
        """ Copy static files to public directory """
        try:
            shutil.copytree('template/static', 'public/static')
        except:
            print("Error copying static files.")

    def render_page(self):
        print("Rendering page to static file.")
        template = self.env.get_template('_layout.html')
        with open('public/index.html', 'w+') as file:
            html = template.render(
                title = "The Goings On",
                iframes = self.iframes
            )
            file.write(html)


if __name__ == "__main__":
    SiteGenerator()