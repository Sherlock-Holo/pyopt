import subprocess

class optdep(object):
    def get_raw_info(self,pkgname):
        bytes = subprocess.check_output(['pacman','-Qi','pkgname'])
        test = bytes.decode('utf-8')
        test = test.split()

        lengh = len(test)

        for info in range(1,lengh):
            if test[info] == '可选依赖':
                
