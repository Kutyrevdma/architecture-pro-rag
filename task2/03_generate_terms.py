import json
import random
import string

def fake_name():
    return "".join(random.choices(string.ascii_lowercase, k=6)).capitalize()

terms = {
    "Darth Vader": "Xarn Velgor",
    "Luke Skywalker": "Lior Kassel",
    "Leia Organa": "Reya Solin",
    "Han Solo": "Keth Morren",
    "Yoda": "Oruun",
    "Obi-Wan Kenobi": "Tal-Ren Voss",
    "Emperor Palpatine": "Archon Malvek",
    "The Force": "Synth Flux",
    "Jedi": "Flux Adepts",
    "Sith": "Void Cult",
    "Death Star": "Void Core",
    "Tatooine": "Arkan-9",
    "Coruscant": "Prime Nexus",
    "Millennium Falcon": "Star Warden"
}

with open("terms_map.json", "w", encoding="utf-8") as f:
    json.dump(terms, f, ensure_ascii=False, indent=2)
