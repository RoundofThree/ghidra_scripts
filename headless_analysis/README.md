## Headless scripts

Example commands:
```sh
# -readOnly so that the imported file is not saved to project
./analyzeHeadless ~/ghidra_projects decomp -import ~/example-c64 -readOnly -scriptPath ~/ghidra_scripts -postscript decompile.py main

# work on a process in the project
# -readOnly if the state is not to be saved
./analyzeHeadless ~/ghidra_projects decomp -process example-c64 -scriptPath /home/zyj20/ghidra_scripts -postscript decompile.py main
```

See detailed docs at https://github.com/CTSRD-CHERI/ghidra/blob/morello/main/Ghidra/RuntimeScripts/Common/support/analyzeHeadlessREADME.html.

