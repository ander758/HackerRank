import json
import os


def sub_folders_in_folder(path, exclude=None):
    arr = next(os.walk(path))
    if exclude:
        for i in exclude:
            arr[1].remove(i)
    return [sub for sub in arr[1]]


class Domain:
    class Subdomain:
        def __init__(self, name, root_path):
            self.name = name
            self.root_path = root_path
            self.query_info_file = 'data.json'

        def count_challenges_in_path(self):
            foo = os.listdir(path=self.root_path)
            if self.query_info_file in foo:
                foo.remove(self.query_info_file)
            return len(foo)

        def query_url(self):
            url = 'https://www.hackerrank.com/domains/'
            with open(f'{self.root_path}/data.json') as json_file:
                data = json.load(json_file)
                url += data['domain']+'?'
                url += 'filters[subdomains][]='+data['query']
            return url

    def __init__(self, name, sub_folders, root_path):
        self.name = name
        self.sub_folders = sub_folders
        self.root_path = root_path
        self.subdomains = [self.Subdomain(name=sub_folder, root_path=f'{root_path}/{sub_folder}') for sub_folder in sub_folders]
