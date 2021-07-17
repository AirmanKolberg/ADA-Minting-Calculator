import json


# Convert JSON file to Python dictionary
def json_to_dict(json_location):

    with open(json_location) as f:

        data = json.load(f)

    return data


# Save Python dictionary to JSON file
def dict_to_json(dictionary, json_location):

    with open(json_location, 'w') as json_file:

        json.dump(dictionary, json_file)


if __name__ == '__main__':
    
    pass
