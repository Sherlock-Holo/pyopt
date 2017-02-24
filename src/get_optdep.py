import subprocess


class optdep(object):

    def get_optdep_list(self, pkgname):
        bytes = subprocess.check_output(['pacman', '-Qi', pkgname])
        test = bytes.decode('utf-8')
        info = test.split()

        lengh = len(info)
        optdep_raw_list = []
        optdep_list = []
        start_site = info.index('可选依赖') + 1
        stop_site = info.index('要求被')

        for site in range(start_site, stop_site):
            optdep_raw_list.append(info[site])

        for x in range(1, len(optdep_raw_list)):
            try:
                optdep_bytes = subprocess.check_output(['pacman', '-Qq', optdep_raw_list[x]])
                optdep_test = optdep_bytes.decode('utf-8')
                optdep_list.append(optdep_test)

        return optdep_list
