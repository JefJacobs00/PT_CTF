# Challenge

scanning the net [medium]

## Description

Analysts intercept internet traffic, most of it is encrypted. Once quantum computing is on point the RSA algorithm will be broken. This will still take some time. Maybe there is some usefull information in the see of packets that isn't encrypted.   

## Solutions

Contestants have to download the provided 'pcapng' file. After a quick google search the should be able to determine that it can be opened and analysed by wireshark.
If contestents search for the string "flag" they will find that there was a http get request that downloaded the flag.jpg file. 

Contestants then have to export this file as jpg to read the flag.

## flag 
ctf{c4ptur1ng_th3_p4ckets}
