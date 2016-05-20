##  CSRecon - Censys and Shodan Reconnasiance Tool

_Censys + Shodan = A Good Time :)_

[Shodan](https://www.shodan.io/) and [Censys](https://censys.io/) are two services that are known to provide a wealth of information about a specific target. This is a useful passive reconnaissance tool that leverages both of their APIs to grab useful network-related information about a target. Of course both of these APIs are capable of much more, however this is a fairly specific use case. As of now it retrieves the following without ever touching the actual network:

- IP addresses that were found to have an association with target 
- open ports and protocols per IP (Saves some nmap time) 
- os detection (if possible)
- geolocation of each IP
- hostnames and domains associated with IP
- related ISP
- banner grabbing (if possible)
- Hosting (Rackspace? Amazon?)

It's pretty useful because all of this information can be discovered, in about 15 seconds, by simply providing the target/organization name. 

### Prerequisites
It should work on any Linux/Unix/OSX platform with python 2.7+ installed. You'll want to make sure the shodan python API is installed as well. More information found: [here].(https://shodan.readthedocs.io/en/latest/) 

Also, you'll need to **get API keys from both Censys and Shodan.** Include these into the following appropriate fields. 

```
CENSYS_API_ID = "<CENSYS_API_ID>"
CENSYS_SECRET = "<CENSYS_SECRET>"
SHODAN_API_KEY = "<SHODAN_API_KEY>" 
```

### Usage
Clone this repository && cd into project directory
```
git clone https://github.com/markclayton/csrecon-python
cd csrecon-python
```
Run the project
```
% python csrecon.py                                                                          
usage: csrecon.py [-h] [-c] [-s] target

CSRecon - Censys and Shodan Reconnaisance Tool

positional arguments:
  target        specify a target company name

optional arguments:
  -h, --help    show this help message and exit
  -c, --censys  only run the censys module
  -s, --shodan  only run the shodan module
```
or simply
```
chmod +x csrecon.py
./csrecon.py
```

### Additional
- More to come. Feel free to contribute and improve upon. 
