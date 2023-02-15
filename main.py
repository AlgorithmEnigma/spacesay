import typer
import textwrap
import json
import requests
from datetime import datetime
from geopy.geocoders import Nominatim

astronaut="""
                 \  _________________________________/
                 | /                 
        _____    // 
      .'     '.  v   _ 
     /    .-""-\   _/ \ 
   .-|   /:.   |  |   |
   |  \  |:.   /.-'-./ 
   | .-'-;:__.'    =/  
   .'=  *=|NASA _.='   
  /   _.  |    ;       
 ;-.-'|    \   |       
/   | \    _\  _\      
\__/'._;.  ==' ==\     
         \    \   |    
         /    /   /    
         /-._/-._/     
         \   `\  \     
          `-._/._/
          """


def main(text: str):

    r = requests.get("http://api.open-notify.org/iss-now.json").json()
    timestamp = r["timestamp"]
    iss_position = r["iss_position"]
    dt = datetime.fromtimestamp(timestamp)

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(iss_position["latitude"]+","+iss_position["longitude"])

    print(dt)
    print(location)

    top_line="_"*35 # Creates a line 35 dashes long
    print("\n", top_line.rjust(52)) # Prints the line justified to the right
    print("/".rjust(18), "\ ".rjust(36)) # Prints the first line of slashes
    if len(text) < 30:
        print('/'.rjust(17), text.rjust(5 + len(text)), '\\'.rjust(34 - len(text)), end="\n", sep="")
    else:
        wrapper = textwrap.TextWrapper(width=30)
        word_list = wrapper.wrap(text=text)
        for i in range(len(word_list)):
            if i == 0:
                print('/'.rjust(17), word_list[i].rjust(2 + len(word_list[i])), '\\'.rjust(34 - len(word_list[i])))
            if i == 1:
                print('\\'.rjust(17), word_list[i].rjust(2 + len(word_list[i])), '/'.rjust(34 - len(word_list[i])), end="")
    print(astronaut)
    

if __name__ == "__main__":
    typer.run(main)
