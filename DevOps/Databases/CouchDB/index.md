# CouchDB

## Ubuntu 18.04
```bash
curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc | sudo apt-key add -

echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list

sudo apt update
sudo apt install couchdb


# Testing
curl http://127.0.0.1:5984/


# Edit options
vi /opt/couchdb/etc/local.ini
```


[API Reference](https://docs.couchdb.org/en/stable/api/index.html)
