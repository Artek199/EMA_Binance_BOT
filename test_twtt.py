#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota
# andre.scota@gmail.com
# MIT license

import os
import sys
import time

import notify

# ----------------------------------------------------------------------------------------

APIKEY = os.getenv('TWITTER_APIKEY', 'NOTDEF')
APISEKKEY = os.getenv('TWITTER_APISEKKEY', 'NOTDEF')
ACCSSTKN = os.getenv('TWITTER_ACCSSTKN', 'NOTDEF')
ACCSSSEKTKN = os.getenv('TWITTER_ACCSSSEKTKN', 'NOTDEF')

print(f'{APIKEY}')
print(f'{APISEKKEY}')
print(f'{ACCSSTKN}')
print(f'{ACCSSSEKTKN}')

#ntf = notify.botNotify('twitter')
ntf = notify.ntfTwitter()

ntf.auth(APIKEY, APISEKKEY, ACCSSTKN, ACCSSSEKTKN)
ntf.write("ABC", sys.argv[1])
