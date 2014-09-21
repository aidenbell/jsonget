#
# A Python script for grabbing values from a JSON file.
# Useful for making standalone configuration setups for
# servers and programs.
#
# ]$ jsondump config.json -hostname "servers[0].hostname"
# -hostname host1.example.com
#
#
# ]$ jsondump config.json -bindaddress "config.bind_address" | xargs server
#
# That kind of thing.

import sys
import json

loadedjson = None

class ParseException(Exception):
	pass

def resolve_path(j,p):
	"""
	Using 'p' obtain the value from the JSON dictionary 'j'
	"""
	parts = p.split('.')
	lastpart = j
	for n,part in enumerate(parts):
		if '[' in part:
			if not type(lastpart) == list:
				raise ParseException("\"%s\" applied to non-list"%part)

			# Assumes <attribute?>[<index>] form
			# but we don't validate with a regexp.
			number = int(part[ part.index('[')+1:len(part)-1])
			lastpart = lastpart[number]
		else:
			lastpart = lastpart[part]
	
	# TODO: ensure that the value is unicode,str,float,int
	return lastpart


if __name__ == "__main__":
			
	with open(sys.argv[1], 'r') as f:
		loadedjson = json.loads(f.read())
	
	lastarg = None
	for arg in sys.argv[2:]:
		if lastarg:
			# Current arg is a path
			print lastarg, "\"%s\""%resolve_path(loadedjson,arg)
			lastarg = None
		else:
			lastarg = arg
