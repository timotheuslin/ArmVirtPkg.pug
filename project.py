#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

""" This is the project configuration file as well the starter script for iPug."""

import os

DEFAULT_EDK2_TAG = 'edk2-stable201908'
DEFAULT_UDK_DIR = os.environ.get('UDK_DIR', os.path.join(os.getcwd(), DEFAULT_EDK2_TAG))
DEFAULT_EDK2_REPO = os.environ.get('EDK2_REPO', 'https://github.com/tianocore/edk2.git')

#DEFAULT_EDK2_TAG = 'master'
#DEFAULT_UDK_DIR = os.environ.get('UDK_DIR', os.path.join(os.getcwd(), 'edk2-Googulator'))
#DEFAULT_EDK2_REPO = os.environ.get('EDK2_REPO', 'https://github.com/Googulator/edk2.git')

# Code tree layout for those remote repository(-ies).
CODETREE = {
    'edk2'              : {
        'path'          : DEFAULT_UDK_DIR,
        'source'        : {
            'url'       : DEFAULT_EDK2_REPO,
            'signature' : DEFAULT_EDK2_TAG,
        },
        'recursive'     : True,
        'multiworkspace': True,
        'patch'         : 'git apply --directory={} QemuVideoDxe.patch'.format(DEFAULT_EDK2_TAG),
    },
}
CODETREE.update({
    'Build_Tip'        : {
        'path'          : os.getcwd(),
        'multiworkspace': True,
    },
})


if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    PKG_ARGS = ''
    #os.environ['GCC5_AARCH64_PREFIX']=os.path.expanduser('~') + '/toolchain/gcc-arm-8.2-2019.01-x86_64-aarch64-elf/bin/aarch64-elf-'

    os.environ['GCC5_AARCH64_PREFIX']='aarch64-linux-gnu-'
    #PKG_DSC = 'ShellPkg/ShellPkg.dsc'
    PKG_DSC = 'ArmVirtPkg/ArmVirtQemu.dsc'
    PKG_ARGS = '-a AARCH64 -t GCC5'

    IPUG_CMD = 'ipug -p {0} {1} {2}'.format(PKG_DSC, PKG_ARGS, ' '.join(sys.argv[1:]))
    print(IPUG_CMD) 
    os.system(IPUG_CMD)
