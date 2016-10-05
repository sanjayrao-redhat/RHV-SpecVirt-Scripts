#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

#defining vm params here

    vm_name = sys.argv[1]
    vm_cluster = api.clusters.get("new_cluster")

    v_n = sys.argv[2]
    vm_template = api.templates.get(v_n)
    vm_params = params.VM(name = vm_name, cluster = vm_cluster, template = vm_template)

    try:
        api.vms.add(vm = vm_params)
        print "Virtual machine clone '%s' added." % vm_name

    except Exception as ex:
        print "Adding virtual machine clone '%s' failed: %s" % (vm_name, ex)

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex

