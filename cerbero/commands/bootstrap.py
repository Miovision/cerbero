# cerbero - a multi-platform build system for Open Source software
# Copyright (C) 2012 Andoni Morales Alastruey <ylatuya@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


from cerbero.commands import Command, register_command
from cerbero.utils import N_, _, ArgparseArgument
from cerbero.bootstrap.bootstrapper import Bootstrapper


class Bootstrap(Command):
    doc = N_('Bootstrap the build system installing all the dependencies')
    name = 'bootstrap'

    def __init__(self):
        args = [
            ArgparseArgument('--build-tools-only', action='store_true',
                default=False, help=_('only bootstrap the build tools')),
            ArgparseArgument('--apt-no-sudo', action='store_true',
                             default=False, help=_('do not use sudo when calling apt-get')),
            ArgparseArgument('--apt-yes', action='store_true',
                             default=False, help=_('pass the -y flag to apt-get install'))
        ]
        Command.__init__(self, args)

    def run(self, config, args):
        config.apt_yes = args.apt_yes
        config.apt_no_sudo = args.apt_no_sudo
        bootstrappers = Bootstrapper(config, args.build_tools_only)
        for bootstrapper in bootstrappers:
            bootstrapper.start()

register_command(Bootstrap)
