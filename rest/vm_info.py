#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

#    v_list = api.vms.list()

    print("\n==================Virtual Machines INFO===================")

    n = sys.argv[1]
    vm_name = api.vms.get(n)

    cluster_name = api.clusters.get(id=vm_name.cluster.id).name
    host_name = api.hosts.get(id=vm_name.host.id).name
    sockets = vm_name.cpu.topology.sockets
    memory = vm_name.memory
#    os_type = vm_name.os.type
    template = api.templates.get(id=vm_name.template.id).name    

    print("Running on host: %s" % host_name)
    print("Belongs to cluster: %s" % cluster_name)
    print("Virtual CPUs: %i" % sockets)  
    print("Created based on template: %s" % template)

    h_list = api.hosts.list()

    print("Migration options: ")

    for h in h_list:
       if(h.get_name() != host_name):
         print("%s" % h.get_name())

except Exception as ex:
   print "Unexpected error: %s" % ex
