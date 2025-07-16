# Over OpenVPN

The following OpenVPN configuration:
✅ Protocol: UDP —  good for performance
✅ Ciphers: Secure and modern (GCM, CHACHA20) 
✅ No compression enabled —  avoids redundant rsync compression

```sh
dev tun
persist-tun
persist-key
data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC
data-ciphers-fallback AES-256-CBC
auth SHA512
tls-client
client
resolv-retry infinite
remote publiciip51832 udp4
nobind
verify-x509-name "OpenVPN_Server" name

this is the openvpn config
auth-user-pass
remote-cert-tls server
explicit-exit-notify


route 192.168.174.0 255.255.255.0
```

```sh
rsync -azP --inplace --partial --append-verify -e "ssh -T -c aes128-ctr -o Compression=no -x" src/ user@192.168.174.X:/path/
```

 -azP --partial --inplace --append-verify

`-a`: archive mode (preserves metadata)
`-z`: compress file data during transfer
`-P`: shows progress and resumes partial transfers (Don’t use in rsync)

`--partial`: Keep partially transferred files (default is to delete them on failure)
`--inplace`: Write directly to destination files (no temporary copy)
`--append-verify`: Resume file transfer and verify contents


-e "ssh -T -c aes128-ctr -o Compression=no -x"

`-T`: disables pseudo-tty
`-c aes128-ctr`: faster cipher than default
`-o Compression=no`: avoids double compression (already using -z)
`-x`: disables X11 forwarding