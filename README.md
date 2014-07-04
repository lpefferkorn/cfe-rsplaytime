cfe-rsplaytime
=============

Compute CFEngine3 runtime splaytime for a given host.

Splaytime is the time cf-execd delays cf-agent execution to spread the load 
on CFEngine server over a period of time.

The length of this period is given by the "splaytime" statement in "body executor control",
and each host delays its execution within this timeframe by a specific delay, 
computed by a host-specific hashing.

Hashing parameters are:
  * hostname
  * main ip address
  * uid used to run cf-execd

Until cf-execd execution, it is not possible to know in advance this host-specific delay.

cfe-rsplaytime allows to compute this delay. It was used once to debug a huge clients to server connections problem,
(which was finally a promise issue)

Usage
=====

    cfe-rsplaytime.py <splaytime> <fqdn> <ip> <uid>

    $ ./cfe-rsplaytime.py 1 debian70.boring 192.168.2.110 0
    Runtime splaytime is 45.55s

Support
=======

The computed splaytime is valid for the following CFEngine versions:
  * 3.4.x
  * 3.5.x
  * 3.6.0

Contact
=======

Loic Pefferkorn <loic-cfengine@loicp.eu>, please use Github issues for bugs or enhancements ideas :)
