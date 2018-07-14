w=["Hindi","English","Kannada"]

wd={lang:(len(lang),sum(lang.lower().count(v) for v in "aeiou")) for lang in w}


dc={'x':["c","b","a"],
    'y':["f","e","d"],
    'z':["i","h","g"]}

cd={player:country for country,players in dc.items() for player in players}

e={player:country
          for country,players in dc.items()
                 for player in players}

f={}
for country,players in dc.items():
       for player in players:
              f[player]=country
print(f)
print(e)


def rgb2hex(r,g,b):
       return r+b+g

red=(222,11,22)
redd={'r':220,'g':15,'b':25}
print(rgb2hex(*red))
print(rgb2hex(**redd))
