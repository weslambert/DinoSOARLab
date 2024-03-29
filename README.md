# DinoSOARLab
Security Onion + Automation + Response Lab including n8n and Velociraptor

![DinoSOARLab](https://user-images.githubusercontent.com/16829864/163741754-3d2823fd-6631-42ec-97dd-404397254ad2.png)

This repo was originally created to work in conjunction with the blog article here: 

https://wlambertts.medium.com/zero-dollar-detection-and-response-orchestration-with-n8n-security-onion-thehive-and-10b5e685e2a1

### **NOTE**: The above article has since been deprecated, as TheHive has been removed from Security Onion (as of version `2.3.100`) -- a new article is currently in development to address these changes.

The primary difference with the updated implementation is that instead of adding an observable to TheHive, it should be added to a case within Security Onion [Cases](https://docs.securityonion.net/en/2.3/cases.html). From there, an Elastalert rule will watch for new observable additions, then perform an HTTP POST to the webhook used for automating Hunts for Velociraptor.

## Feature parity updates (in progress):

- [ ] Mark case with label/tag (and/or create an alert inside Security Onion console) once a host is quarantined 

## NOTE 
This is NOT an officially supported Security Onion integration, so usage is at your own risk.

## Prerequisites
It is assumed that Security Onion is already running and configured as a standalone, manager, or managersearch node.  

To install Security Onion, consult the documentation here:

https://docs.securityonion.net/en/latest/installation.html

After Security Onion is installed, proceed to the lab installation steps.

## Installation

```
git clone https://github.com/weslambert/DinoSOARLab
cd DinoSOARLab 
sudo ./install_lab
```

Once setup is complete:

- Velociraptor GUI can be accessed via `https://$securityonion/velociraptor`
- n8n can be access via `https://$securityonion/n8n`

### Firewall 
To add a firewall exception for a particular IP or range of IPs (for Velociraptor clients), you can use the so-firewall script, like so:

`sudo so-firewall includehost velociraptor <IP/CIDR>` 

`sudo salt-call state.apply firewall queue=True`

### Velociraptor Clients
Original Velociraptor client binaries and repacked client binaries can be found in `/opt/so/conf/velociraptor/clients`.

The client configuration file can be found in `/opt/so/conf/velociraptor`.
