import json

lookup = {
    "Cloth": "Bmats",
    "HEGrenade": "Mammon",
    "RifleW": "Loughcaster",
    "GrenadeW": "Harpa",
    "ATGrenadeW": "Varsi",
    "HELaunchedGrenade": "Tremola"
}

def stock_json_to_sheet_data(incoming_json_string):
    incoming_json = json.loads(incoming_json_string)
    list = []
    for item in incoming_json["items"]:

        code_name = item["code"]
        usable_name = code_name
        if(code_name in lookup):
            usable_name = lookup[code_name]
        
       

        row = []
        row.append(item["quantity"])
        row.append(usable_name)
        list.append(row)
    #Fill end with empty values to clear out any garbage
    for i in range(0, 255):
        list.append(['',''])
    return list