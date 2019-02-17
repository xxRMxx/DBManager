#!/usr/bin/env python
# -*- coding: utf-8 -*-

# caller function for DBManager

# TODO
# responsiveness
# more fresh design
# add focus (highlighting for current active field)
# rewrite all functions to send a call and retrieve the result
# describe the concrete exception

import sys

if __name__ == '__main__':

	# enable debugging options
	debug = False
	if ('--debug') in sys.argv or '-d' in sys.argv:
		debug = True

	execfile('Root/view.py')
