## Find IP Address for Google App Engine
Outbound traffic in google app engine can have many varying ip addresses.
This document here explains the commands you can do to determine the possibilities:  
https://cloud.google.com/appengine/docs/standard/python/outbound-ip-addresses

This answer on stack overflow has a python solution to help streamline these commands:  
https://stackoverflow.com/a/64255810

However, I was not able to get it running without some small modifications on my system and decided to create this repository.
Also, it is a good reference to remember how to execute the script since I do not use python that often.  
To run and write to file:
```
python3 gcloudips.py
```

To run just the commands and print to standard out:
```
python3 -c 'import gcloudips; print(list(gcloudips.get_all_ip_cidrs()))'
```

