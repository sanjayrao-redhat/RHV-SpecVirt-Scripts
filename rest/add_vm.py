#! /usr/bin/python

from ovirtsdk.api import API
from ovirtsdk.xml import params
import sys

try:
    api = API (url="https://dhcp31-79.perf.lab.eng.bos.redhat.com/ovirt-engine/api",
               username="admin@internal",
               password="100yard-",
               ca_file="/etc/pki/ovirt-engine/ca.pem")

#    import pdb;pdb.set_trace()

#defining vm params here

    vm_name = sys.argv[1]   
    vm_mem = 16384 * 1024 * 1024
    vm_cluster = api.clusters.get("new_cluster")
    vm_type = "server"

    vm_cpu_top = params.CpuTopology(cores = 4, sockets = 1)
    vm_cpu = params.CPU(topology = vm_cpu_top)

    vm_os = params.OperatingSystem(boot=[params.Boot(dev="network")])
    vm_template = api.templates.get("Blank")

    vm_params = params.VM(name = vm_name, memory = vm_mem, cluster = vm_cluster, type_ = vm_type, cpu = vm_cpu, os = vm_os, template = vm_template) 

    try:
	api.vms.add(vm = vm_params)
	print "Virtual machine '%s' added." % vm_name

    except Exception as ex:
	print "Adding virtual machine '%s' failed: %s" % (vm_name, ex)

    api.disconnect()

except Exception as ex:
    print "Unexpected error: %s" % ex     

