#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

    v_list = api.vms.list()

    if len(v_list) > 0:

        print("%-30s  %s" % ("name","id"))
        print("======================================================================")

        for v in v_list:
          # print "%-30s: (%s)" % (v.get_name(), v.get_id())
	  disks = v.disks.list()

	  disk_size = 0

	  for d in disks:
	      disk_size += d.get_size()

	  print("%-30s: %d" % (v.get_name(), disk_size))

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
