import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from urllib.request import urlopen
import bs4


class KonguEventNotifier(App):
    

    def build(self):
        t=[]
        home_page = urlopen("http://www.kongu.ac.in").read()
        soup=bs4.BeautifulSoup(home_page,'html.parser')
        name_box=soup.find('div',attrs={'class':'events'})
        for i in name_box.find_all('a'):
                t.append(i.text)
        return Label(text='\n'.join(t))
           

if name == 'main':
    KonguEventNotifier().run()