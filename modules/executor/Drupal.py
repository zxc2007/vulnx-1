
#!/usr/bin/env python3

from __future__ import (absolute_import, division, print_function)

from modules.gathering.host_gathering import GatherHost
from modules.gathering.cmsgather import drupal_version
from modules.dns_dump import dnsdumper,domain_info
from modules.scan_ports import ScanPort
import sys


class Drupal(object):
    """
    call it when target is a drupal cms.
    Usings method from other class.
    """

    def __init__(self, url=None, headers=None, port=None):
        
        # init the url & headers.
        self.url = url
        self.headers = headers
        # port to scan
        self.port = port

    def exploit(self):
        return print('no exploits found.')

    def webinfo(self):
        web = GatherHost(self.url,self.headers)
        web.web_host()

    def serveros(self):
        os = GatherHost(self.url,self.headers)
        os.os_server()

    def cmsinfo(self):
        drupal_version(self.url,self.headers)

    def dnsdump(self):
        return dnsdumper(self.url)

    def domaininfo(self):
        return domain_info(self.url)

    def ports(self,port):
        self.port = port
        sp = ScanPort(self.url,self.port)
        sp.portscan()
