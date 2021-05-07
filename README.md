# securityonion-velociraptor
Run Velociraptor on [Security Onion (2)](https://github.com/Security-Onion-Solutions/securityonion)

![image](https://user-images.githubusercontent.com/16829864/97827312-e4d60900-1c91-11eb-9923-8899cf6ccba4.png)

### Overview
This script and the accompanying components will setup Velociraptor on [Security Onion (2)](https://github.com/Security-Onion-Solutions/securityonion), and output from client artifact collections/flows will be automatically streamed to the Elastic Stack for correlation with other events.

Currently, Velociraptor events will be displayed within Hunt and Kibana with as least the following characteristics:

`event.module: velociraptor`  
`event.dataset: artifact`

It is planned to migrate all artifact fields/output to [ECS](https://www.elastic.co/guide/en/ecs/current/index.html)-compliance as the integration continues to mature.  Velociraptor ECS mappings will be tracked in a separate repo ([velociraptor-ecs](https://github.com/weslambert/velociraptor-ecs)). 

### Notes
- This is NOT an officially supported Security Onion integration -- please use it at your own risk.
- This script and the accompanying components have only been tested on a standalone node, although it should work fine for a manager, or managersearch node.

### Installation
To get started, clone the repo, then run the `install_velociraptor` script:

```
git clone https://github.com/weslambert/securityonion-velociraptor    
cd securityonion-velociraptor  
sudo ./install_velociraptor
```
The script will do a few things:

- Pull down `wlambert/so-velociraptor` (pre-built Velociraptor Docker image)
- Copy Salt configuration for Velociraptor
- Copy Elastic configuration for Velociraptor
- Set up firewall and web server configuration for Velociraptor
- Restart services as necessary

Towards the end of the script, you will be prompted to supply a username and password.  You will use this username and password when logging in to Velociraptor.

Velociraptor can be accessed via `https://$yourhost/velociraptor` in a browser once installation is complete.

### Firewall 
To add a firewall exception for a particular IP or range of IPs, you can use the so-firewall script, like so:

`sudo so-firewall includehost velociraptor <IP/CIDR>` 

### Clients
Original client binaries and repacked client binaries can be found in `/opt/so/conf/velociraptor/clients`.

The client configuration file can be found in `/opt/so/conf/velociraptor`.
