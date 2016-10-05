#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

    vm=sys.argv[1]

    try:
        api.vms.get(vm).stop()
    except Exception as ex:
        print "Unable to stop '%s': %s" % (vm.get_name(), ex)

    api.disconnect()

except Exception as ex:
     print "Unexpected error: %s" % ex

