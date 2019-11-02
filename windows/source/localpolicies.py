#Author David Gofman

import configparser, os

with open('data\\secedit.log', 'r', encoding='utf16') as file:
    org_data = file.read()

with open(os.environ['TEMP'] + '\\secedit.log', 'r', encoding='utf16') as file:
    my_data = file.read()

config1 = configparser.RawConfigParser()
config1.read_string(org_data)

config2 = configparser.RawConfigParser()
config2.read_string(my_data)
hint=0
for sec in config1.sections():
	if config2[sec] is None:
		print('Section is missing: ' + sec)
	else:
		for key in config1[sec]:
			if config2[sec].get(key) is None:
				hint=1
				print('Section key is missing: ' + sec, '->', key)
			elif config1[sec][key] != config2[sec][key]:
				hint=1
				print('Value changed: ' + sec, '->', key, '\nLOG: ', config1[sec][key], '\nNOW: ', config2[sec][key])

if hint:
	print('\nHint: Start -> Run -> secpol.msc -> Local Policies')
	
