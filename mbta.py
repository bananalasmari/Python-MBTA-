Subway = {
    "Red": ["South Station", "Park St", "Kendall", "Central", "Harvard", "Porter", "Davis", "Alewife"],
    "Green": ["Haymarket", "Government center", "Park st", "Bolyston", "Arlington", "Copley"],
    "Orange": ["North Station", "Haymarket", "Park Street", "State", "Downtown Crossing", "Chinatown", "Back Bay", "Forest Hills"]
}

def totalStops(StartLine, StartStation, EndLine, EndStation):
    if StartLine == EndLine:
        return abs(Subway[EndLine].index(EndStation)-Subway[StartLine].index(StartStation))    

print(totalStops("Red", "Alewife", "Red", "Alewife")) 
print(totalStops("Red", "Alewife", "Red", "South Station")) 