## Pfsense - OpenVPN Server

> Pfsense OpenVPN server and Mikrotik OpenVPN Client Configuration

> cipher (null | aes128-cbc | aes128-gcm | aes192-cbc | aes192-gcm | aes256-cbc | aes256-gcm | blowfish128; Default: blowfish128)
Allowed ciphers. In order to use GCM type ciphers, the "auth" parameter must be set to "null", because GCM cipher is also responsible for "auth", if used.

> auth=sha256 which is causing problem for cipher you have set (aes256-gcm), check also if other config and client parameters are aligned with doc...

> https://help.mikrotik.com/docs/display/ROS/OpenVPN

- General Information
```txt
Description: Zaravand
```

- Mode Configuration
```txt
Server mode:                Remote Access(SSL/TLS+User Auth)
Backend for authentication: Local Database
Device Mode:                tun - Layer3 Tunnel mode
```

- Endpoint Configuration
```txt
Protocol:     TCP IPv4 and IPv6 on all interface
Local port:   9494 <OpenVPN service port>
```

- Cryptographic Settings
```txt
TLS Encryption:                     [unckeck] Use a TLS Key
Peer Certificate Authority:         OpenVPNCA
Server certificate:                 OpenVPNCA
DH Parameter Length:                2048
ECDH Curve:                         Use Default
Data Encryption Algorithms:         AES-256-GCM
                                    AES-128-GCM
                                    CHACHA20-POLY1305
                                    AES-128-CBC
                                    AES-128-CFB
                                    AES-256-CBC
                                    AES-256-CFB
Fallback Data Encryption Algorithm: AES-128-CBC
Auth digest algorithm:              SHA-256
```

- Tunnel Settings
```txt
IPv4 Tunnel Network:      192.168.179.0/24
IPv4 Local network(s):    192.168.173.9/24
```

- Client Settings
```txt
Dynamic IP: [CHECK] Allow connected clients to retain their connections if their IP address changes.
```

- Advanced Configuration
```txt
Username as Common Name: [check] Use the authenticated client username instead of the certificate common name (CN).
```

## Mikrotik - OpenVPN client

### Import Certificates

- Import CA certificate
- Import Client certificate
- Import Client Key

### Mikrotik OpenVPN client Configuration

- PPP -> interface -> OVPN Client
```txt
Connct to:    <Pfsense WAN IP address>
Port:         9494 <OpenVPN service port>
Mode:         ip
Protocol:     tcp
User:         <OvpnUserName>
Password:     <OvpnUserPass>
Certificate:  <OvpncUserCert>
TLS Version:  any
Auth:         sha256
Cipher:       aes-128-cdc
```
