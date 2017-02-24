import subprocess

class list(object):
    def get_list(self):
        bytes = subprocess.check_output(['pacman','-Qq'])
        test = bytes.decode('utf-8')
        self.list = test.split()
        return self.list
