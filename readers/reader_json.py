import json
from files import JSON_FILE_PATH


class ReaderJSON:
    with open(JSON_FILE_PATH, "r") as f:
        users = json.loads(f.read())
        u = []
        for user in users:
            u.append(user)

    # print(len(u))
    # print(u[27]['name'])

    def number_of_user(self):
        return len(self.u)
