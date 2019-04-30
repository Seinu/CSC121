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

totalwon = int(input("What is your total jackpot winnings? "))

annpayment_bfortax = totalwon / 20
print("Your annual winnings before tax is $" + format(annpayment_bfortax, '.2f'))
annpayment_aftrtax = annpayment_bfortax * 0.07
print("Your annual winnings after tax is $" + format(annpayment_aftrtax, '.2f'))

allatonce_bfortax = totalwon * 0.65
print("Your instant winnings before tax is $" + format(allatonce_bfortax, '.2f'))
allatonce_aftrtax = allatonce_bfortax * 0.7
print("Your instant winnings before tax is $" + format(allatonce_aftrtax, '.2f'))
