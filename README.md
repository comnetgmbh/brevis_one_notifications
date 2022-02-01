# Brevis.one Notification Plugin for checkmk

This plugin for checkmk allows users to configure notification rules using Brevis.one SMS gateways.

To connect to the Brevis.one SMS gateway, a Web-API user has to be configured via the Brevis.one web interface.

Multiple Brevis.one SMS gateways can be configured as a fallback solution. Each configured SMS gateway will be checked for error messages and the next one will be used if an error occured.

This plugin has been tested with checkmk version 2.0.0p17.
