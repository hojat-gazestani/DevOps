# install

```sh
sudo apt update
sudo apt upgrade
sudo apt install -y suricata
sudo suricata-update
```

```sh
sudo ls /var/lib/suricata/rules
sudo ls /etc/suricata/rules
sudo chmod 640 /etc/suricata/rules/*.rules
sudo chmod 640 /var/lib/suricata/rules/*.rules
```

```sh
sudo vim /etc/suricata/suricata.yaml
  address-groups:
    HOME_NET: "[192.168.0.0/16,10.0.0.0/8,172.16.0.0/12]"
    EXTERNAL_NET: "any"
  rule-files:
    - suricata.rules
  af-packet:
    - interface: ens224

sudo systemctl restart suricata.service
```

```sh
sudo systemctl status wazuh-agent.service
sudo vim /var/ossec/etc/ossec.conf
	<ossec_config>
	  <localfile>
	    <log_format>json</log_format>
	    <location>/var/log/suricata/eve.json</location>
	  </localfile>

sudo systemctl restart wazuh-agent.service
sudo systemctl status wazuh-agent.service
```
