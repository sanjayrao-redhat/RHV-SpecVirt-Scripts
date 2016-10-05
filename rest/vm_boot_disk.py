#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

#    vm = api.vms.get("vm_2")

    vm_name = sys.argv[1]
    vm = api.vms.get(vm_name)

#    import pdb;pdb.set_trace()

    sd = params.StorageDomains(storage_domain=[api.storagedomains.get(name="dom_rhgs")])
    disk_size = 20*1024*1024*1024
    disk_type = "system"
    disk_interface = "virtio"
    disk_format = "cow"
    disk_bootable = True

    disk_params = params.Disk(storage_domains = sd, size = disk_size, type_ = disk_type, interface = disk_interface, format = disk_format, bootable = disk_bootable)

    try:
	d = vm.disks.add(disk_params)
	print "Disk '%s' added to '%s'." % (d.get_name(), vm.get_name())

    except Exception as ex:
	print "Adding disk to '%s' failed: %s" % (vm.get_name(), ex)

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
   

