# This file is part of HadesMem.
# Copyright (C) 2010 Joshua Boyce (aka RaptorFactor, Cypherjb, Cypher, Chazwazza).
# <http://www.raptorfactor.com/> <raptorfactor@raptorfactor.com>
# 
# HadesMem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# HadesMem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with HadesMem.  If not, see <http://www.gnu.org/licenses/>.

ProcPath = raw_input("Process path: ")
WorkingDir = raw_input("Process working dir (optional): ")
ProcArgs = raw_input("Process arguments (optional): ")
ModPath = raw_input("Module path: ")
ExpName = raw_input("Export name (optional): ")
InjectData = PyHadesMem.CreateAndInject(ProcPath, WorkingDir, ProcArgs, 
  ModPath, ExpName)
MyMem = InjectData[0]
ModBase = InjectData[1]
ExpRet = InjectData[2]
ExpLastErr = InjectData[3]
print("Module Base: " + hex(ModBase))
if ExpName:
  print("Export Ret: " + hex(ExpRet) + " " + str(ExpRet))
  print("Export Last Err: " + hex(ExpLastErr) + " " + str(ExpLastErr))
