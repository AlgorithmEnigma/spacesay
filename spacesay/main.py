import typer
from typing import Optional
from dotenv import load_dotenv

from spacesay.location import iss_location
from spacesay.speech import speech_bubble


load_dotenv()  # Export dotenv into enviroment


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
        location_time = iss_location()
        speech_bubble(location_time)

    else:
        speech_bubble(text)

    print(astronaut)
