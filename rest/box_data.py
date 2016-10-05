#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

    dc_list = api.datacenters.list()
    c_list = api.clusters.list()
    h_list = api.hosts.list()
    n_list = api.networks.list()
    sd_list = api.storagedomains.list()
    disk_list = api.disks.list()
    t_list = api.templates.list()
    v_list = api.vms.list()

    print("\n==================Data Centers===================")

    for dc in dc_list:
        print "%s (%s)" % (dc.get_name(), dc.get_id())

    print("\n==================Clusters===================")

    for c in c_list:
        print "%s (%s)" % (c.get_name(), c.get_id())

    print("\n==================Hosts===================")

    for h in h_list:
        print "%s (%s)" % (h.get_name(), h.get_id())

    print("\n==================Networks===================")

    for n in n_list:
        print "%s (%s)" % (n.get_name(), n.get_id())

    print("\n==================Storage Domains===================")

    for sd in sd_list:
        print "%s (%s)" % (sd.get_name(), sd.get_id())

    print("\n==================Disks===================")

    for d in disk_list:
        print "%s (%s)" % (d.get_name(), d.get_id())    

    print("\n==================Virtual Machines===================")

    for v in v_list:
        print "%-3s: (%s)" % (v.get_name(), v.get_id())

    print("\n==================Templates===================")

    for t in t_list:
	print "%s (%s)" % (t.get_name(), t.get_id())

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
