import os
import os.path

import shutil
from distutils.dir_util import copy_tree

def get_mpmission_dir():
    if 'ARMA3_DIR' in os.environ:
        base_dir = os.environ['ARMA3_DIR']
    else:
        base_dir = os.path.abspath(os.path.join(os.getcwd(), os.path.pardir))
    return os.path.join(base_dir, 'MPMissions')

def get_subdirs(dirname):
    d = dirname
    return [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))]

def clean():
    clean_dir = os.path.abspath(os.path.join(get_mpmission_dir(), 'Antistasi.altis'))
    if os.path.exists(clean_dir):
        print("Removing output build found in: {}".format(clean_dir))
        shutil.rmtree(clean_dir)

def build(mission_template_name='A3-AATemplate.Altis'):
    repo_base_dir = os.path.join(os.getcwd(), 'A3-Antistasi')
    template_src = os.path.join(repo_base_dir, 'Templates', mission_template_name)
    mpmission_dir = get_mpmission_dir()
    dest = os.path.join(mpmission_dir, 'Antistasi.altis')
    print("*"*72)
    print("Copying {}\nto\n{}".format(template_src, dest))
    print("*"*72)
    print("")
    shutil.copytree(template_src, dest)
    copy_tree(repo_base_dir, dest)
    templates_dest_dir = os.path.join(dest, 'Templates')
    for subdir in get_subdirs(templates_dest_dir):
        shutil.rmtree(subdir)

def main():
    clean()
    build()

if __name__ == '__main__':
    main()
	
