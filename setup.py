import commands
from proj import get_news

target = open('req.txt', 'r')
cmd='python -m pip install '
for module in target :
	cmd+=module
	(status, output) = commands.getstatusoutput(cmd)

get_news()