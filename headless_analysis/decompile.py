from ghidra.app.decompiler import DecompileOptions
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

# usage: decompile.py [funcname]

args = getScriptArgs()
target = ''
if len(args) == 0:
    target = 'all'
else:
    target = args[0] # ignore other args

monitor = ConsoleTaskMonitor()
program = getCurrentProgram()
options = DecompileOptions()
ifc = DecompInterface()
ifc.setOptions(options)
ifc.openProgram(program)

output = '// Decompiled by Ghidra\n'
# get all functions from listings
functionManager = program.getFunctionManager()
funcs = functionManager.getFunctions(True)

if target == 'all':
    # iterate over all functions
    for func in funcs:
        print('[*] Decompiling ' + func.getName())
        output += '/**********************************/\n'
        output += '//           FUNCTION               \n'
        output += '/**********************************/\n'
        results = ifc.decompileFunction(func, 0, monitor)
        output += results.getDecompiledFunction().getC()
        output += '\n'
else:
    found = False
    for func in funcs:
        if func.getName() == target:
            print('[*] Decompiling ' + func.getName())
            output += '/**********************************/\n'
            output += '//           FUNCTION               \n'
            output += '/**********************************/\n'
            results = ifc.decompileFunction(func, 0, monitor)
            output += results.getDecompiledFunction().getC()
            output += '\n'
            found = True
            break
    if not found: print('[!] ' + target + ' not found!')

# write the decompilation result in a file
outputname = program.getName() if target == 'all' else target
with open(outputname + '-decompiled.c', 'w') as fp:
    fp.write(output)
print('[*] Written to ' + outputname + '-decompiled.c')
