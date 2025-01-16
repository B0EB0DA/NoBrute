import sys
import requests
from ipaddress import IPv4Network
from ipaddress import IPv4Address

class ip_russia:

    def __init__(self):
        ripe_url = "https://stat.ripe.net/data/country-resource-list/data.json?resource=RU&v4_format=prefix"
        r = requests.get(ripe_url)
        nets_list_str = r.json()["data"]["resources"]["ipv4"]

        n1 = [IPv4Network(supernet) for supernet in nets_list_str]

        n2 = [str(net) for supernet in n1 if supernet.prefixlen <= 24 for net in supernet.subnets(new_prefix=24)]
        # print(n2)

        # [for net := IPv4Network(supernet) in nets_list_str for net in supernet.]

        # list(ip_network('192.0.2.0/24').subnets(new_prefix=26))


        sx = dict()
        maskx = dict()

        for net in n2:
            spl = net.split('/')
            if len(spl) == 2:
                self.net_str = spl[0]
                self.mask_str = spl[1]
                self.mask = int(self.mask_str)
                pass
            else:
                print(f"Failed to parse network (mask): {net}")
            spl = self.net_str.split('.')
            if len(spl) == 4:
                self.oct1 = int(spl[0])
                self.oct2 = int(spl[1])
                self.oct3 = int(spl[2])
                self.oct4 = int(spl[3])
                self.is_good = True
                self.net = int(self.oct1) << 24 | int(self.oct2) << 16 | int(self.oct3) << 8 | int(self.oct4)

                sx.setdefault(self.oct1, dict()).setdefault(self.oct2, set()).add(self.oct3)
                maskx[self.mask] = maskx.setdefault(self.mask, 0) + 1
            else:
                print(f"Failed to parse network (octets): {net}")

        self.nets_list = [IPv4Network(addr) for addr in nets_list_str]
        print(sys.getsizeof(self.nets_list))
        print(sys.getsizeof(n2))
        for k1, v1 in sx.items():
            for k2, v2 in v1.items():
                print(k1, k2, len(v2))
        print(maskx)
        print(f"sx - {sys.getsizeof(sx)}")



    def __contains__(self, item):
        for net in self.nets_list:
            if item in net:
                return True
        return False

    def count(self):
        return sum([net.num_addresses for net in self.nets_list])
