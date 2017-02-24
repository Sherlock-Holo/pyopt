import subprocess

class list(object):
    def get_list(self):
        bytes = subprocess.check_output(['pacman','-Qq'])
        test = bytes.decode('utf-8')
        list = test.split()
        return list
