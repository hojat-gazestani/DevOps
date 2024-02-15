## Introduction

### X509

* X509
  * ITU Standard which Define the format of public key certificates.
  * Used in TLS/SSL, which is the basis for HTTPS,

  * An X.509 certificate binds an identity to a public key using a digital signature
  * identity : hostname, or an organization, or an individual
  * public key (RSA, DSA, ECDSA, ed25519, etc.)
  * someone holding that certificate can use the public key it contains to establish secure communications with another party,
  * or validate documents digitally signed by the corresponding private key. 

* Certificate Revocation Lists
  * certificates that have been deemed invalid by a signing authority,

* certification path validation algorithm
  * allows for certificates to be signed by intermediate CA certificates, which are, in turn, signed by other certificates, eventually reaching a trust anchor. 


