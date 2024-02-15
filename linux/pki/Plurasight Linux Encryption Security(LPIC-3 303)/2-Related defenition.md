## Related defenition

* The Secure Sockets Layer version 3.0 (SSLv3), as specified in RFC 6101, is not sufficiently secure.
  * https://datatracker.ietf.org/doc/html/rfc7568

* The replacement versions, in particular, Transport Layer Security (TLS) 1.2 (RFC 5246) are considerably more secure and
   capable protocols.
  * https://datatracker.ietf.org/doc/html/rfc5246
  * the protocol runs on layer six of the OSI model, between TCP and end user protocols like HTTP
  * ![osi](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/1-osi.png)
  * Common Encrypted and Unencrypted Ports
  * ![ports](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/2-ports.png)

* Symmetric Cryptography
  * the use of a single shared secret to share encrypted data between parties.
  * Ciphers in this category are called symmetric because you use the same key to encrypt and to decrypt the data.
  * ![symmetric ctryptography](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/3-symmetric%20cryptography.png)
* Asymmetric Cryptography
  * Uses pairs of keys. Each pair consists of a public key and a private key. 
  * ![asymmetric](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/4-Asymmetric%20Ctryptophragy.png)

* Certificate Authority (CA)
  * Responsible for issuing 
  * Revoking
  * Distributing Digital Certificate

* Digital Certificate contain
  * Owner Identity
  * Public key
  * CA particulars 
  * Cryptographic data

### cipher suite
* grouping of configuration choices that can serve to define a wide range of encryption and transfer behavior
  * TLS: defines the protocol that this cipher suite is for
  * ECDHE: key exchange algorithm
  * RSA: authentication mechanism during the handshake
  * AES session cipher
  * SHA
  * SHA: message authentication algorithm 

* e.g:
  * TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  *     TLS defines the protocol that this cipher suite is for; it will usually be TLS.
  *     ECDHE indicates the key exchange algorithm being used.
  *     RSA authentication mechanism during the handshake.
  *     AES session cipher.
  *     128 session encryption key size (bits) for cipher.
  *     GCM type of encryption (cipher-block dependency and additional options).
  *     SHA (SHA2)hash function. For a digest of 256 and higher. Signature mechanism. Indicates the message authentication algorithm which is used to authenticate a message.
  *     256 Digest size (bits).

### X509 Certificate encoding
* express the certificate's data structure

* two major encoding
  * PEM (Base64 ASCII)
    * .crt
    * .pem
    * .cer
    * .key
    * .ca-bundle
    * ![pem](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/5-pem%20format.png)
  * DER (binary) - most commonly seen in Java contexts.
    * .der
    * .cer
    * ![der](https://github.com/hojat-gazestani/linux/blob/main/pki/Plurasight%20Linux%20Encryption%20Security(LPIC-3%20303)/Pic/6-der%20format.png)
  
* .DER Distinguished Encoding Rules
* .PEM Privacy-enhanced Electronic Mail
* PKCS Public key Cryptography Standards

* PKCS#7 (P7B)
  * found in Windows and Java server contexts,
    * .p7b
* PKCS#12 (PKCS12 or PFX) 
  * binary format for storing a certificate chain and private key in a single, encryptable file
    * .p12
    * .pfx

### Openssl
* OpenSSL is a software library for applications that secure communications over computer networks against eavesdropping or need to identify the party at the other end. It is widely used by Internet servers, including the majority of HTTPS websites
* OpenSSL is a very useful open-source command-line toolkit for working with X.509 certificates, certificate signing requests (CSRs), and cryptographic keys