import sys
import time
# txt vars
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
mvmtverbs = ["walk","go","move","travel","run"]
nverbs = ["north","forward","straight","ahead"]
sverbs = ["south","backward","behind","back"]
everbs = ["east","right"]
wverbs = ["west","left"]
dirverbs = [nverbs,sverbs,everbs,wverbs]
instruct = ["help","hint","guide","instructions","commands"]
idleverbs = ["check","look","inspect"]
getverbs = ["grab","pick","take"]
giveverbs = ["drop"]

def delay_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)
	print("")
def slow_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)
	print("")
def fast_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.001)
	print("")
def fastest_print(s):
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(.0001)
	print("")



#works with print, not stdout
def delete_last_lines(l):
	for ln in range(l):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)
