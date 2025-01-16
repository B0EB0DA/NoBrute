
class ip_network:

    def __init__(self, net: str):
        self.full_net_str = net
        self.is_good = False

        spl = net.split('/')
        if len(spl) == 2:
            self.net_str = spl[0]
            self.mask_str = spl[1]
        else:
            print(f"Failed to parse network (mask): {net}")

        spl = self.net_str.split('.')
        if len(spl) == 4:
            self.oct1 = spl[0]
            self.oct2 = spl[1]
            self.oct3 = spl[2]
            self.oct4 = spl[3]
            self.is_good = True
            self.net = int(self.oct1) << 24 | int(self.oct2) << 16 | int(self.oct3) << 8 | int(self.oct4)
            pass
        else:
            print(f"Failed to parse network (octets): {net}")

    def __str__(self):
        return f"{self.oct1}.{self.oct2}.{self.oct3}.{self.oct4}/{self.mask_str}"

