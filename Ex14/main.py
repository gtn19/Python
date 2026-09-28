s_hourOfDeparture = str(input('Heure de départ du train sous forme XXhYY'))
s_hourOfArrival = str(input('Heure d arrivé du train sous forme XXhYY'))

def GetHours(hour:str):
    return int(hour[0:2])

def GetMinutes(hour:str):
    return int(hour[3:5])

i_travelTime = int((GetHours(s_hourOfArrival) - GetHours(s_hourOfDeparture)) * 60 + (GetMinutes(s_hourOfArrival) - GetMinutes(s_hourOfDeparture)))

if i_travelTime < 0:
    i_travelTime += 24 * 60
    print(i_travelTime, "min")
    print(str((GetHours(s_hourOfArrival) - GetHours(s_hourOfDeparture))+24)+"h"+str(GetMinutes(s_hourOfArrival) - GetMinutes(s_hourOfDeparture)))
else:
    print(i_travelTime , "min")
    print(str((GetHours(s_hourOfArrival) - GetHours(s_hourOfDeparture)))+"h"+str(GetMinutes(s_hourOfArrival) - GetMinutes(s_hourOfDeparture)))
