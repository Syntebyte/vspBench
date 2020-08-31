from progress.bar import ChargingBar
from os import system
import colorama
import hashlib
import random
import string
import time
import math


operatingSystem  = 'Windows'
appCopyright     = 'By SyntezQuery'
appVersion       = '1'
releaseDate      = '31.08.2020'

bytesSize = 16 * 1024 # 16 KiB
preparing = 10        # 10 seconds for preparing
repeat    = 10        # 10 repeats of steps
testing   = 1         # 1 second for one step
division  = 1         # Reduce results by 1


appTitle = ' vspBench version ' + appVersion + ' for ' + operatingSystem
system('title ' + appTitle )
system('cls')
colorama.init()

INVF = colorama.Back.WHITE + colorama.Fore.BLACK
RSTF = colorama.Back.RESET + colorama.Fore.RESET
CPRT = colorama.Fore.CYAN

def vspBenchGenRandomString(length):
	letters = string.ascii_lowercase
	return ''.join( random.choice(letters) for i in range(length) )

def vspBenchMakeHash():
	uRandom = vspBenchGenRandomString(bytesSize)
	hashStr = hashlib.sha512( uRandom.encode('utf-8') )


print('\n\n  ' + INVF + appTitle + ' (' + releaseDate + ') ' + RSTF)
print('   ' + CPRT + appCopyright + RSTF + '\n')
print('  > Preparing CPU and memory for benchmark ...\n  ', end='')

sT = int(time.time())
eT = sT + preparing

while int(time.time()) < eT:
	vspBenchMakeHash()


print('> Benchmark started ...\n')

pName = '  Testing'
pFill = '#'
pBS = '%(percent)d%% '

startTime = int(time.time())
operations = 0
progressBar  = ChargingBar(pName, max=repeat, suffix=pBS, fill=pFill )

cc = []
i  = 0

while i < repeat:

	cl = 0
	sT = int(time.time())
	eT = sT + testing

	while int(time.time()) < eT:
		vspBenchMakeHash()
		operations += 10
		cl += 1

	for _ in range(i-len(cc)+1):
		cc.append(None)

	cc[i] = math.ceil(cl/division)
	progressBar.next()
	i += 1

progressBar.finish()


print(RSTF + '  > Benchmark completed! Calculating results ...\n')

cc.sort()
seconds = int(time.time()) - startTime
operations = int(operations / seconds)
proceed = ' (~' + str(operations) + 'h/sec) '
bResult = INVF + ' ' + str( cc[repeat-1] ) + ' BQ ' + RSTF + proceed + '\n'

print('  > Benchmark result: ' + bResult )
input('  Press any key to exit ... ')