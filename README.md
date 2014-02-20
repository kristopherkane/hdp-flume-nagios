###Hortonworks Data Platform 2 Nagios Plugin - Flume Agent

This plugin will identify and alert the availability of Flume agent accessibility via the metrics web service


###Dependencies
HDP 2 installation, via Ambari, with  Nagios enabled.
Python
Flume agents running with the metric HTTP interface enabled Example: bin/flume-ng agent --conf-file example.conf --name a1 -Dflume.monitoring.type=http -Dflume.monitoring.port=34545
Port 34545 is hard coded in [flume-services.cfg](/nagios-conf/objects/flume-services.cfg)

###Tested
HDP 2 - CentOS 6


###Installation
All actions are conducted on the HDP2 Nagios server

**Read Carefully** -- When adding configuration to existing files, do not overwrite the installed file.  Simply append to them.  Specifically talking about [nagios.cfg.erb](/ambari-puppet-modules/hdp-nagios/templates/nagios.cfg.erb)

***There are two options for identifying hosts in the HDP installation.  If the Flume agent is running on existing client
servers in the stack, You don't need to populate the [flume-hosts.cfg](/nagios-conf/objects/flume-hosts.cfg) file. If not,
Create entries with hostnames of the Flume agents. Nagios will fail to start if there are duplicate host declarations.

1. Append the Nagios Puppet template [nagios.cfg.erb](/ambari-puppet-modules/hdp-nagios/templates/nagios.cfg.erb) to the Ambari agent Puppet template at: /var/lib/ambari-agent/puppet/modules/hdp-nagios/templates/nagios.cfg.erb
2. Add all Nagios configuration [files](/nagios-conf/objects/) to /etc/nagios/objects on the Nagios server
3. Add the Python check [script](/src/check_flume.py) to the Nagios plugins directory at /usr/lib64/nagios/plugins and ensure permissions are 0755
4. Restart Nagios via Ambari


##Help
To troubleshoot Nagios startup failure, test the configuration file first:
root@host>nagios -v /etc/nagios/nagios.cfg
