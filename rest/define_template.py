#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

    
    v_n = sys.argv[1]
    vm_name = api.vms.get(v_n)

    template_name = sys.argv[2]

    from_cluster = api.clusters.get(id=vm_name.cluster.id).name
    n_temp = params.Template(vm = vm_name, name = template_name, cluster = from_cluster)
    
    try:
	api.templates.add(n_temp)
	print "Template added."

    except Exception as ex:
	print "Adding template '%s' failed: %s" % (template_name, ex)

    api.disconnect()

except Exception as ex:
   print "Unexpected error: %s" % ex
