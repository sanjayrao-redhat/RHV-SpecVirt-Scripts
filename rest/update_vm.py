#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

#edit vm params here

    edit_vm = sys.argv[1]   
    vm_name = api.vms.get(edit_vm)

    vm_name.set_host("gprfc084")

    try:
        vm_name.update() 
        print "Virtual machine '%s' updated and console params added." % vm_name.name

    except Exception as ex:
	print "Updating virtual machine '%s' failed: %s" % (vm_name, ex)

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex

