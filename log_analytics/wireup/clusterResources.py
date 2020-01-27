#!/usr/bin/python
# Copyright (c) 2020      Mellanox Technologies, Inc.
#                         All rights reserved.

import os

#                                                                    #
# ========================== Node state ============================ #
#                                                                    #

class clusterNode:
    START = 1
    WIREUP_START = 1
    WIREUP_INIT = 1

    def __init__(self, nodeid):
        self.nodeid = nodeid
        self.host_name = None
        self.progress = { }

    def set_hostname(self, hostname):
        self.host_name = hostname

    def hostname(self):
        return self.host_name

class clusterSystem:
    def __init__(self):
        self.nodes = { }

    def new_node(self, nodeid):
        self.nodes[nodeid] = clusterNode(nodeid)
        return self.nodes[nodeid]

    def node(self, nodeid):
        if( not (nodeid in self.nodes.keys())):
            self.new_node(nodeid)
        return self.nodes[nodeid]

    def start(self, nodeid, hostname, ts):
        n = self.node(nodeid)
        n.hostname = hostname
        n.progress[clusterNode.START] = ts

    def wireup_start(self, nodeid, ts):
        n = self.node(nodeid)
        n.progress[clusterNode.WIREUP_START] = ts

    def wireup_init(self, nodeid, ts):
        n = self.node(nodeid)
        n.progress[clusterNode.WIREUP_INIT] = ts

    def summary(self):
        boot = { }
        for i in self.nodes.keys():
            boot[i] = self.nodes[i].progress[clusterNode.START]
#        print boot
        boot_s = sorted(boot.items(), key = lambda kv : (kv[1]))
#        print boot_s
        l = len(boot_s)
        print "slurmd start imbalance: ", (boot_s[l - 1][1] - boot_s[0][1]), " fastest nodeid=", boot_s[0][0], " slowest nodeid=", boot_s[l - 1][0]

