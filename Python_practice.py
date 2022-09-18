#counties = ["Arapahoe","Denver","Jefferson"]

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for i in range(len(voting_data)):
#    for county, registered_voters in county_dict:
#        print(f"{county} county has {registered_voters} registered voters.")
#   print (voting_data[i]['county'] + " county has " + str(voting_data[i]['registered_voters']) + " registered voters." )
    print (f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters.")