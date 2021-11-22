# \[Networking\] - UwU Secrets

#### Points = 300

## Prompt

I found this weird DNS server that lets you query this weird domain. Can you help me uncover their secrets? `dig @ctf.isss.io -p 4628 0.flag.uwu.com`

by mattyp

#### Hints
\[None\]

## Provided Files

\[None\]

## Write Up

- the prompt says that this is a dns query
- im guessing the dns server is @ctf.isss.io and we're using port 4628
- I don't know how to use dig so I'll read about this. This <a href="https://www.howtogeek.com/663056/how-to-use-the-dig-command-on-linux/">article</a> is useful.

#### After reading

- okay so we have the ip associated with 0.flag.uwu.com.
- tried accessing it by putting it into my browser and using netcat. no luck.
- this is a request for an A class record. lets check if there is any other type of record.
	- `dig @ctf.isss.io -p 4628 0.flag.uwu.com ANY`
	- still nothing interesting
- lets check if there are any comments
	- `dig @ctf.isss.io -p 4628 0.flag.uwu.com ANY +comments`
	- disappointing
- lets check if there are any more entries by changing the 0 into a 1
	- `dig @ctf.isss.io -p 4628 1.flag.uwu.com ANY +comments`
	- nice, there are more entires in the server, lets check how many there are.
- trying the first 10 domains.
	- generate domains: 
		- `python3 -c "for i in range(0, 11): print(str(i) + '.flag.uwu.com')" > domains.txt`
	- check if there are associated IPs
		- `dig @ctf.isss.io -p 4628 -f domains.txt +short`
		- this returns 8 IPs, lets assume that there are no more for now.
		```
		117.116.102.108
		97.103.123.100
		111.109.97.105
		110.95.110.97
		109.101.115.95
		97.110.100.95
		115.101.99.114
		101.116.95.103
		97.109.101.125
		```

- I stopped here, I don't know what to do with these because I can't connect to them.

#### After Checking ISSS writup

- so these are actually utf-8 encodings for the flag characters
- I would not have guessed that, should think of this whenever I'm stuck in the future.
- code found in the files.
		
## Flag

utflag{domain_names_and_secret_game}