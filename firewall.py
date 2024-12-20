'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment: Layer-2 Firewall Application

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta
'''

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
from collections import namedtuple
import os
''' Add your imports here ... '''

log = core.getLogger()
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

''' Add your global variables here ... '''
UDP = 17
TCP = 6
IPV4 = 0x800

def block_src_address_dst_port(address, port, protocol, event):
    msg = of.ofp_flow_mod()
    msg.match.dl_type = IPV4
    if address:
        msg.match.nw_src = IPAddr(address)
    msg.match.nw_proto = protocol
    msg.match.tp_dst = port
    event.connection.send(msg)

def block_pair_of_hosts(src_address, dst_address, event):
    msg = of.ofp_flow_mod()
    msg.match.dl_type = IPV4
    msg.match.nw_src = IPAddr(src_address)
    msg.match.nw_dst = IPAddr(dst_address)
    event.connection.send(msg)

def read_rule3_policies():
    pairs = []
    with open("rule3_policies.csv", "r") as file:
        for line in file.readlines()[1:]:
            line_data = line.split(',')
            pair = (line_data[1], line_data[2])
            pairs.append(pair)
    return pairs

def rule_1(event):
    block_src_address_dst_port(None, 80, TCP, event)
    block_src_address_dst_port(None, 80, UDP, event)

def rule_2(event):
    block_src_address_dst_port("10.0.0.1", 5001, UDP, event)

def rule_3(event):
    pairs = read_rule3_policies()
    for pair in pairs:
        block_pair_of_hosts(pair[0], pair[1], event)
        block_pair_of_hosts(pair[1], pair[0], event)

class Firewall (EventMixin):

    def __init__ (self, switch_id):
        self.listenTo(core.openflow)
        self.switch_id = switch_id
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        ''' Add your logic here ... '''
        if event.dpid != self.switch_id:
            return

        rule_1(event)
        rule_2(event)
        rule_3(event)

        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch (switch_id = 1):
    '''
    Starting the Firewall module
    '''
    core.registerNew(Firewall, switch_id)