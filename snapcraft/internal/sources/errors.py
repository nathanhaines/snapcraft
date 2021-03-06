# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015-2017 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from snapcraft.internal import errors


class VCSError(errors.SnapcraftError):
    fmt = '{message}'


class IncompatibleOptionsError(errors.SnapcraftError):

    fmt = '{message}'

    def __init__(self, message):
        super().__init__(message=message)


class DigestDoesNotMatchError(errors.SnapcraftError):

    fmt = ('Expected the digest for source to be {expected}, '
           'but it was {calculated}')

    def __init__(self, expected, calculated):
        super().__init__(expected=expected, calculated=calculated)
