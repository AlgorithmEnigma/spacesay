import typer
import rich
import yaml
from typing import Optional


from spacesay.location import iss_location
from spacesay.speech import speech_bubble


# Create or open a YAML config file and set username
def set_username() -> str:
    try:
        stream = open("config.yaml", "w")
        rich.print(
            "Username not set, please visit [bold magenta]https://www.geonames.org/login[/bold magenta] to sign up and get a username."
        )
        username = input("Please enter your username: ")
        yaml.dump({"username": username}, stream)
        return username
    except:
        print("Failed to create config")
        raise FileNotFoundError


username = ""

try:
    stream = open("config.yaml", "r")
    config = yaml.safe_load(stream)
    try:
        if config["username"] is None:
            username = set_username()
        else:
            username = config["username"]
    except:
        username = set_username()

except:
    print("Failed to open config, creating config file")
    username: str = set_username()


astronaut = """
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


app = typer.Typer()


@app.command()
def main(text: Optional[str] = typer.Argument(None)):
    if text is None:
        location_time = iss_location(username)
        speech_bubble(location_time)

    else:
        speech_bubble(text)

    print(astronaut)
