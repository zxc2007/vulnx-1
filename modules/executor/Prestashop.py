
#!/usr/bin/env python3

from __future__ import (absolute_import, division, print_function)

from modules.exploits.prestashop_exploits import PSExploits
from modules.gathering.host_gathering import GatherHost
from modules.gathering.cmsgather import prestashop_version
from modules.dns_dump import dnsdumper,domain_info
from modules.scan_ports import ScanPort
import sys


class Prestashop(object):
    """
    call it when target is a prestashop cms.
    Usings method from other class.
    """

    def __init__(self, url=None, headers=None, port=None):
        
        # init the url & headers.
        self.url = url
        self.headers = headers
        # port to scan
        self.port = port

    def exploit(self):
        ps = PSExploits(self.url, self.headers)
        return ps.psexploits()

    def webinfo(self):
        whg = GatherHost(self.url,self.headers)
        whg.web_host()

    def serveros(self):
        whg = GatherHost(self.url,self.headers)
        whg.os_server()

    def cmsinfo(self):
        prestashop_version(self.url,self.headers)

    def dnsdump(self):
        return dnsdumper(self.url)

    def domaininfo(self):
        return domain_info(self.url)

    def ports(self,port):
        self.port = port
        sp = ScanPort(self.url,self.port)
        sp.portscan()
