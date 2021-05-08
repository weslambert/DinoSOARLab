# SOARLab
Security Onion + Automation + Response Lab including n8n and Velociraptor

![SOARLab](https://miro.medium.com/max/2400/1*gfzmeFm0hHFEwuRZknJ8bA.png)

This repo was created to work in conjunction with the blog article here: 

https://wlambertts.medium.com/zero-dollar-detection-and-response-orchestration-with-n8n-security-onion-thehive-and-10b5e685e2a1

## NOTE 
This is NOT an officially supported Security Onion integration, so usage is at your own risk.

## Prerequisites
It is assumed that Security Onion is already running and configured as a standalone, manager, or managersearch node.  

To install Security Onion, consult the documentation here:

https://docs.securityonion.net/en/latest/installation.html

After Security Onion is installed, proceed to the lab installation steps.

## Installation

```
git clone https://github.com/weslambert/SOARLab
cd SOARLab 
sudo ./install_lab
```

Once setup is complete:

- Velociraptor GUI can be accessed via `https://$securityonion/velociraptor`
- n8n can be access via `https://$securityonion/n8n`
