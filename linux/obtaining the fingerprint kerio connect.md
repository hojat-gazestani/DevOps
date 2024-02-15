openssl s_client -connect YOUR_SERVER:YOUR_PORT < /dev/null 2>/dev/null | openssl x509 -fingerprint -md5 -noout -in /dev/stdin
