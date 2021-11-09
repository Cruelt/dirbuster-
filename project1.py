#!/usr/bin/python3


import requests
from rich.console import Console
from sys import argv
from sys import exit




console = Console()

console.print("""[red bold]

  o__ __o__/_   o                 o                            o__ __o                                                      o              
 <|    v       <|>              _<|>_                         <|     v\                                                   _<|>_            
 < >           / \                                            / \     <\                                                                   
  |            \o/   o      o     o    \o__ __o     o__ __o/  \o/     o/   o__  __o   \o__ __o     o__ __o/   o       o     o    \o__ __o  
  o__/_         |   <|>    <|>   <|>    |     |>   /v     |    |__  _<|/  /v      |>   |     |>   /v     |   <|>     <|>   <|>    |     |> 
  |            / \  < >    < >   / \   / \   / \  />     / \   |         />      //   / \   / \  />     / \  < >     < >   / \   / \   / \ 
 <o>           \o/   \o    o/    \o/   \o/   \o/  \      \o/  <o>        \o    o/     \o/   \o/  \      \o/   |       |    \o/   \o/   \o/ 
  |             |     v\  /v      |     |     |    o      |    |          v\  /v __o   |     |    o      |    o       o     |     |     |  
 / \           / \     <\/>      / \   / \   / \   <\__  < >  / \          <\/> __/>  / \   / \   <\__  < >   <\__ __/>    / \   / \   / \ 
                        /                                 |                                              |                                 
                       o                          o__     o                                      o__     o                                 
                    __/>                          <\__ __/>                                      <\__ __/>                                 

                                                                                            Code by >>> Muhammad Zeeshan!
[/red bold]""")

def Help():

    print("""
    Help
    -u for url 
    -w for Wordlist
    e.g python3 dir.py -u https:///www.google.com -w /usr/worldlist.txt

    
    """)



if len(argv) == 5  :

    with open(argv[4],"r") as handle:
        path = handle.readlines()
        handle.close()
    for u in path :
        url = argv[2] + u.strip('\n')
        try:
            req = requests.get(url)
            console.print(f"[green bold]{url}[/green bold] -- [yellow]Status Code:[/yellow] {req.status_code}")
        except KeyboardInterrupt as err:
            exit(1)
        except Exception as err:
            exit(err)

else:
    
    Help()






