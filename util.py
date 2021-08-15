import subprocess as sp
import json

# Format of returned output
# [username, encrypted_password, user_id_number, group_id_number, fullname_of_user, user_home_directory, login_shell]


def getAllSystemUsers():
    pr = sp.Popen(
        ["/bin/bash", "-c", "getent passwd {1000..60000}"], stdout=sp.PIPE)

    linux_users = []

    count_r = 0
    idx = 0
    prev = None

    while True:
        output = pr.stdout.readline()
        output = output.decode("utf-8").replace('\n', '')
        if output == '':
            break

        if output:
            # print(output)
            if output != '':
                parts = output.split(':')
                obj = {
                    'username': parts[0],
                    'user_id': parts[2],
                    'group_id': parts[3],
                    'fullname_of_user': parts[4],
                    'home_dir': parts[5],
                    'login_shell': parts[6]
                }
                linux_users.append(obj)

        prev = output

    return linux_users


def getAllSudoUsers():
    pr = sp.Popen(
        ["/bin/bash", "-c", "getent group sudo"], stdout=sp.PIPE)

    linux_users = []

    count_r = 0
    idx = 0
    prev = None

    while True:
        output = pr.stdout.readline()
        output = output.decode("utf-8").replace('\n', '')
        if output == '':
            break

        if output:
            # print(output)
            if output != '':
                parts = output.split(':')
                linux_users.append(parts[3])

        prev = output

    return linux_users


# if __name__ == "__main__":
#    print(json.dumps(getAllSudoUsers(), indent=1))
