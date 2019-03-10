import yaml


def analyze_file(file_name, key_name):
    # contact_data
    file_path = "./data/" + file_name + ".yaml"
    with open(file_path, "r", encoding='utf-8') as f:

        data = yaml.load(f)
        data_list = list()
        for i in data[key_name].values():
            data_list.append(list(i.values()))
        return data_list