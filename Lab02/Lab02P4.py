# Copyright (C) 2019 Seinu
#
# This file is part of CSC121.
# NOT FOR COLLEGE REUSE
#
# CSC121 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CSC121 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CSC121.  If not, see <http://www.gnu.org/licenses/>.
#
# NOT FOR COLLEGE REUSE

showonly = int(input("How many people wqnt to watch just the 3d shark show? "))
admitonly = int(input("How many people just want admission to the aquarium? "))
both = int(input("How many people want both? "))

showonly = showonly * 8
admitonly = admitonly * 14
both = (both * (14 + 8)) * 0.75
total = showonly + admitonly + both
print("The group total is $" + format(total, '.2f'))
