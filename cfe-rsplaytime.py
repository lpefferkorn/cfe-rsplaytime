#!/usr/bin/python2.7

import sys
import numpy as np

CF_HASHTABLESIZE = 8192

PROJECT_AUTHOR   = "Loic Pefferkorn <loic-cfengine@loicp.eu>"
PROJECT_URI      = "http://www.github.com/lpefferkorn/cfe-rsplaytime"
PROJECT_VERSION  = 1.0

# Overflows are expected to mimic c overflow behavior
# in the StringHash() function,
# because I don't want automatic int to long promotion
np.warnings.simplefilter("ignore", RuntimeWarning)

def StringHash(s, seed, max):
  """
  Python version of StringHash from string_lib.c
  """
  h = np.uint32(seed)
  for i in bytearray(s):
    h += np.uint32(i)
    h += np.uint32(h << 10)
    h ^= np.uint32(h >> 6)

  h += np.uint32(h << 3)
  h ^= np.uint32(h >> 11)
  h += np.uint32(h << 15)
  
  return np.uint32(h & (max - 1))

if __name__ == "__main__":

  if (len(sys.argv) < 5):
    print 'cfe-rsplaytime.py v%.1f - Compute CFEngine runtime splaytime of a given host' \
    %  PROJECT_VERSION 
    print 'Usage %s: <splaytime> <fqdn> <ip> <uid>' % sys.argv[0]
    print """Arguments are:
      \tsplaytime: the value defined in body executor control
      \tfqdn: FQDN of the host executing cf-execd
      \tip: default ip of the host executing cf-execd
      \tuid: user id of the user cf-execd is started under
      \nReport bugs to %s
    """ % PROJECT_URI
    sys.exit(1)

  else:
    hashStr = '{0}+{1}+{2}'.format(sys.argv[2], sys.argv[3], sys.argv[4])
    runSplaytime = int(sys.argv[1]) * 60 * StringHash(hashStr, 0, CF_HASHTABLESIZE) / float(CF_HASHTABLESIZE ) 
    print "Runtime splaytime is %.2fs" % runSplaytime
