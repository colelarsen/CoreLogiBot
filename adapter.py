import json
def stock_json_to_sheet_data(incoming_json_string):
    incoming_json = json.loads(incoming_json_string)
    print(incoming_json)
    list = []
    for item in incoming_json["items"]:
        row = []
        row.append(item["quantity"])
        row.append(item["code"])
        list.append(row)
    return list