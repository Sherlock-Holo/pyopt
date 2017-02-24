from installed_list import packages_list
from get_optdep import optdep

dict = {}

pkg_list = packages_list()
pkg_lists = pkg_list.get_packages_list()

pkg_optdep = optdep()

for name in pkg_lists:
    dict[name] = pkg_optdep.get_optdep_list(name)
