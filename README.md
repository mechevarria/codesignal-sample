# MySQL Sample

* Start a MySQL database with the `./run-mysql.sh` script. Defaults
```properties
name=mysql
rootpass=mysqlroot
user=user
userpass=userpass
```

* Connect via [DBeaver](https://dbeaver.io/download/) on `http://localhost:3306`. Make sure the connection parameter `allowPublicKeyRetrieval=true` is set'

* Run `main.py` csv parsing and ordering in [pandas](https://pandas.pydata.org/)
```bash
Country with the largest number of customers' contracts:
USA (25607 contracts)
```