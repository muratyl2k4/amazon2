import pandas 

def courier_code(companyName):
    csv = pandas.read_csv("order_track/c.csv")
<<<<<<< HEAD
    courier_name = companyName.lower().replace('ı','i')
    csv["Courier Name\t"] = csv["Courier Name\t"].str.lower() 
    result = csv[csv["Courier Name\t"] == courier_name+ '\t'] if not csv[csv["Courier Name\t"] == courier_name+ '\t'].empty else csv[csv["Courier Name\t"].str.contains(courier_name.lower())]
    return result['Carrier Code\t'].values[0]

print(courier_code('EVRi'))
=======
    liste = []
    courier_name = companyName
    csv["Courier Name\t"] = csv["Courier Name\t"].str.lower() 
    result = csv[csv["Courier Name\t"] == courier_name+ '\t'] if not csv[csv["Courier Name\t"] == courier_name+ '\t'].empty else csv[csv["Courier Name\t"].str.contains(courier_name.lower())]
    return result['Carrier Code\t'].values[0]
>>>>>>> 5f7a6717028ff0f0ffdea12332705fcd4a2c02bc
