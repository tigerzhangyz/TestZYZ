#! /usr/bin/env python
# -*- coding : utf-8 -*-

import sys

# RegisterTime<|>PhoneNum<|>PortalType<|>SubPortalType<|>Channel<|>FeeType<|>Price<|>MGPCode<|>BehaviorType<|>UA<|>VersionNum<|>IMSI<|>UserId<|>SystemProductType<|>Preserver4<|>Preserver5

#这一行是我手工在github修改的
#这一行是我手工在github修改的  第二次： 必须先pull后更新本地才行

for line in sys.stdin:
	try:
	#  try begin ##########################################################			
		line = line.strip().replace('>null','>').replace('>NULL','>')
		fields = line.split('<|>')
		if len(fields)!=16: continue
		if fields[11]: print '%s\t%s' % ('|'.join([fields[2],fields[3],fields[11]]), line)
	#  try end   ##########################################################
	except:	pass

