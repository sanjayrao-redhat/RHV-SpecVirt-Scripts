#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

    vm_name = sys.argv[1]
    vm = api.vms.get(vm_name)

    nic_name = "nic_test"
    nic_interface = "virtio"
    nic_network = api.networks.get("10ge")

    nic_params = params.NIC(name = nic_name, interface = nic_interface, network = nic_network)

    try:
	nic = vm.nics.add(nic_params)
	print "Network interface '%s' added to '%s'." % (nic.get_name(), vm.get_name())

    except Exception as ex:
	print "Adding network interface to '%s' failed: %s" % (vm.get_name(), ex)


    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex
   
