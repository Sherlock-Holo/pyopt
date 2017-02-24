import subprocess

class optdep(object):
    def get_optdep_list(self,pkgname):
        bytes = subprocess.check_output(['pacman','-Qi',pkgname])
        test = bytes.decode('utf-8')
        info = test.split()

        lengh = len(info)
        optdep_list = []
        start_site = info.index('可选依赖') + 1
        stop_site = info.index('要求被')

        for site in range(start_site,stop_site):
            optdep_list.append(info[site])

        return optdep_list
