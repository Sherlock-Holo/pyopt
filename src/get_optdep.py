import subprocess

class optdep(object):
    def get_raw_info(self,pkgname):
        bytes = subprocess.check_output(['pacman','-Qi','pkgname'])
        test = bytes.decode('utf-8')
        test = test.split()

        lengh = len(test)
        optdep_list = []
        start_site = test.index('可选依赖')
        stop_site = test.index('要求被')

        for site in range(start_site,stop_site):
            optdep_list.append(test[site])
