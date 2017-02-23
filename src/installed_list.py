import subprocess

class raw(object):
    def get_raw_list(self):
        bytes = subprocess.check_output(['pacman','-Qq'])
        test = bytes.decode('utf-8')
        return test

class list(object):
    def get_list(self):
        list = raw.get_raw_list
        list = list.split()
        return list
