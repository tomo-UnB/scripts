#!/usr/bin/python

from obspy import read
from optparse import OptionParser

## Usage string:
use = "Usage: sac2segy.py -f file"
desc = """Script to convert a SAC-file to SEGY-format"""

## Calling Parser:
parser = OptionParser(usage = use, description = desc)
## Options:
parser.add_option("-f", "--file",   dest="file", type = str, help="SAC-file path")
## Parsing options into variables:
opts, args = parser.parse_args()
### Making sure all mandatory options appeared:
mandatory = ["file"]
for m in mandatory:
    if not opts.__dict__[m]:
        print ""
        parser.print_help()
        print ""
        print "Ex: "
        print "sac2segy.py -f ./file.sac"
        print ""
        print "Marcelo Rocha - UnB - 2014/04/21 - V1.0"
        print ""
        exit(-1)

filer=opts.file

st=read(filer)
st.write("test.segy",format="SEGY")
print ""
print "A SEGY-file (test.segy) was created in your workdir"
print "" 
quit()

