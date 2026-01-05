import json
def stock_json_to_sheet_data(incoming_json_string):
    incoming_json = json.loads(incoming_json_string)
    list = []
    for item in incoming_json["items"]:
        row = []
        row.append(item["quantity"])
        row.append(item["code"])
        list.append(row)
    #Fill end with empty values to clear out any garbage
    for i in range(0, 255):
        list.append(['',''])
    return list