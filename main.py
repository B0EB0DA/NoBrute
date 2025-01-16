
import requests
from ip_russia import *
from mark import *

from ipaddress import IPv4Network
from ipaddress import IPv4Address

m = mark()

m.here

my = IPv4Address("213.33.160.66")
g = IPv4Address("8.8.8.8")
r = ip_russia()

print(r.count())
print()

print(my in r)
print()
print(g in r)

# dx = dict()
#
#
# for a in addr_list:
#     n = IPv4Network(a)
#
#     dx[n.network_address] = n.broadcast_address
#
#     # print(n, n.network_address, int(n.network_address), int(n.broadcast_address))
#
# mx = []
#
# for k, v in dx.items():
#     if IPv4Address(int(v) + 1) in dx:
#         mx.append(k)
#
#
#
# print(len(addr_list))
# print(len(mx))