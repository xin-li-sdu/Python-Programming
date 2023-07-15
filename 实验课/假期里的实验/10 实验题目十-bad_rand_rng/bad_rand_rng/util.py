import os
import os.path
import filecmp


def check_challenge(fname):
    if os.path.isfile(fname+'_solution'):
        if (not os.path.isfile(fname)) or (not filecmp.cmp(fname, fname+'_solution')):
            print('Challenge failed!')
        else:
            print('Challenge solved!')
