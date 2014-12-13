#!/usr/bin/env python
import sys

def findneighborhoods(name):
    manhattan =["Clinton", "Downtown", "East Village", "Garment District", "Greenwich Village", "Greenwood", "Hamilton Heights", "Soho", "Washington Heights", "Woodhaven-Richmond Hill", "Yorkville", "Battery Park", "Chelsea", "Chinatown", "East Harlem", "Midtown", "Gramercy", "High Bridge", "Inwood", "Tribeca", "Upper East Side", "West Village", "Financial District", "Little Italy", "Lower East Side", "Morningside Heights", "Murray Hill", "Carnegie Hill", "Central Park", "Harlem", "North Sutton Area", "Upper West Side"]
    bronx = ["Bedford Park","Riverdale", "City Island", "Hunts Point", "Morris Heights", "Morris Park", "Mott Haven", "Parkchester", "South Bronx", "Fordham", "Throggs Neck", "Union Port", "Woodlawn-Nordwood", "Spuyten Duyvil", "University Heights", "Wakefield-Williamsbridge", "Williams Bridge", "Baychester", "Country Club", "Eastchester", "Kings Bridge", "Soundview", "Tremont"]
    brooklyn = ["Brownsville", "Carroll Gardens", "Mapleton-Flatlands", "Sunset Park", "Canarsie", "Williamsburg", "Bay Ridge", "Boerum Hill", "Bushwick", "Bensonhurst", "Cobble Hill", "Fort Green", "Park Slope", "Bedford-Stuyvesant", "Borough Park", "Dyker Heights", "East Brooklyn", "Flatbush", "Gravesend-Sheepshead Bay"]
    
    queens = ["Auburndale", "Middle Village", "Ridgewood", "Saintalbans", "Sunny Side", "Forest Hills", "Glendale",  "Steinway", "Astoria-Long Island City", "Clearview", "Jamaica", "Laurelton", "Nkew Gardens", "Corona", "Flushing", "Jackson Heights", "Maspeth", "Queensboro Hill", "The Rockaways", "College Point", "Douglastown-Little Neck", "Queens Village", "Springfield Gardens", "Utopia", "Woodside"]
    statenisland = []
    if name in manhattan:
        name = 'Manhattan'
    elif name in bronx:
        name = 'Bronx'
    elif name in brooklyn:
        name = 'Brooklyn'
    elif name in queens:
        name = 'Queens'
    return name

for line in sys.stdin:
    # remove leading and trailing whitespace
    
    # split the line into words
    names, values = line.strip().split('\t')
    
    # increase counters
    b = findneighborhoods(names)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
    print '%s\t%s' % (b, values)





