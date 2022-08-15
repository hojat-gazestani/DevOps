[TOC]

# DevNet
    - Abstration (Yang, NetConf, RestConf, Grpc)
    - Version Control (Rool Back, Git, IaC, Terraform)
    - Automation (Ansible, Puppet)

# DevNet concept Model:
    - Standard Data Structure (YANG) -> MIB, OID
    - Transport (NetConf, Restconf, gRPC) -> SNMP
    - Data Encoding (XML, JSON, YAML)

## Standard Data Structure
----------------------------------------------------------
    SNMP Server     --->     SNMP Agent
                    Set      MIB1
                                OID
                    <--      MIB2
                    Get         OID
                    
                    		

-------------------------------------------
```text
netprog_basic/network_device_apis/yang/ietf-interface.yang
                       YANG (IETF Standard)
                           namespace
                               container
                                    name
                                    description
                                    type
```



```text
OID -> leaf
folder -> container

```





## Transport 

- Netconf : SSH 					-> XML
- Restconf: HTTP, HTTPS    -> XML, JSON
- gRPC    : Google                 -> Google Protobuf



## Data encoding



![img.png](img.png)
                       
     

## Transport (Protocol) vs Data (Model)

![Screenshot from 2022-07-16 08-23-24](/home/hojat/Pictures/Screenshots/Screenshot from 2022-07-16 08-23-24.png)





# Yang



github.com/YangModels/VENDOR

github.com/YangModels/standard/ietf/rfc/...

```bash
yank explorer

pyang

pyang -f tree ietf-interface.yang

ssh hojat@192.168.1.1 -p 830 -s netconf

ssh hojat@192.168.1.1 -p 830 -s netconf | | ietf-interface
```



# Netconf



ssh, rpc (remote procedure call)



![netconf_proto_stack](/home/hojat/Documents/git/DevOps/DevNet/netconf_proto_stack.png)





Operations netconf actions

​                                ![operation](/home/hojat/Documents/git/DevOps/DevNet/operation.jpg)



    # Restconf

