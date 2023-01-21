import pandas 

def courier_code(companyName):
    csv = pandas.read_csv("order_track/c.csv")
    liste = []
    courier_name = companyName
    csv["Courier Name\t"] = csv["Courier Name\t"].str.lower() 
    result = csv[csv["Courier Name\t"] == courier_name+ '\t'] if not csv[csv["Courier Name\t"] == courier_name+ '\t'].empty else csv[csv["Courier Name\t"].str.contains(courier_name.lower())]
    return result['Carrier Code\t'].values[0]
