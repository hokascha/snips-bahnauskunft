#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import random
import time
import datetime
import re

class Bahnauskunft:

    def __init__(self, config):
        #https://reiseauskunft.bahn.de//bin/query.exe/dn?cb=processFahrtmoeglichkeiten&nrCons=3&S=Tübingen%20Hechinger%20Eck&SBH=1&Z=Hauptbahnhof&ZBH=1&journeyProducts=1023&wTime=&widget=1&start=1&now=1560866580&encoding=utf-8
        self.api_base_url = "https://reiseauskunft.bahn.de//bin/query.exe/dn?"
        try:
            self.default_city = config['global']['default_city']
        except:
            self.default_city = "Berlin"
        try:
            self.default_start = config['global']['default_start_station']
        except:
            self.default_start = "Alexanderplatz"

    def get_next(self, intent_message):
        auskunft = self.get_auskunft(intent_message)
        if auskunft['status'] == 'ok':
            for abfahrt in auskunft['fl']:
                response = "Die nächste Abfahrt von {0} nach {1} ist um {2} Uhr.".format(auskunft['S'],auskunft['Z'],abfahrt['ab'])
                return response
        else:
            return random.choice(["Es ist leider kein Internet verfügbar.", "Ich bin nicht mit dem Internet verbunden.", "Es ist kein Internet vorhanden."])

    def get_auskunft(self, intent_message):
        nowtime = time.mktime(datetime.datetime.today().timetuple())
        start = self.default_start
        try:
            for (slot_value, slot) in intent_message.slots.items():
                ziel =  slot[0].slot_value.value.value
        except:
                ziel = "Berlin Ostbahnhof"

        api_url = "{0}cb=processFahrtmoeglichkeiten&nrCons=3&S={1}&SBH=1&Z={2}&ZBH=1&journeyProducts=1023&wTime=&widget=1&start=1&now={3}&encoding=utf-8".format(
	       self.api_base_url,
            start,
            ziel,
            nowtime
        )
        try:
            r = requests.get(api_url)
            regex = r"= (\{.*\});"
            matches = re.finditer(regex, r.content.decode('utf-8'), re.MULTILINE | re.DOTALL)
            for matchNum, match in enumerate(matches, start=1):
                print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
    
                    json_obj = json.loads(match.group(groupNum))
                    json_obj['status'] = "ok"
                   
                    return json_obj

        except (requests.exceptions.ConnectionError,ValueError):
            return {"status": "error"}

    
