#! /usr/bin/env python
# -*- coding : utf-8 -*-

import sys

# RegisterTime<|>PhoneNum<|>PortalType<|>SubPortalType<|>Channel<|>FeeType<|>Price<|>MGPCode<|>BehaviorType<|>UA<|>VersionNum<|>IMSI<|>UserId<|>SystemProductType<|>Preserver4<|>Preserver5


for line in sys.stdin:
	try:
	#  try begin ##########################################################			
		line = line.strip().replace('>null','>').replace('>NULL','>')
		fields = line.split('<|>')
		if len(fields)!=16: continue
		if fields[11]: print '%s\t%s' % ('|'.join([fields[2],fields[3],fields[11]]), line)
	#  try end   ##########################################################
	except:	pass

