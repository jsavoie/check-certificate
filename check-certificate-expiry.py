#!/usr/bin/python3
import os
from datetime import datetime
from datetime import timedelta
from OpenSSL import crypto

certpath = "/etc/ssl/certs"
fileextension = ".pem"
threshold = timedelta( days=30 )
today = datetime.today()

for filename in os.listdir(certpath):
	fullpath = os.path.join(certpath, filename)
	if os.path.isfile(fullpath) and filename.endswith(fileextension):
		cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(fullpath).read())
		expirydate = datetime.strptime(cert.get_notAfter().decode('ascii'),"%Y%m%d%H%M%SZ")
		if (today + threshold >= expirydate):
			daysleft = (expirydate - today).days
			if (daysleft >= 0):
				print ("Certificate " + filename + " expires in " + str(daysleft) + " days")
			else:
				print ("Certificate " + filename + " has already expired")
