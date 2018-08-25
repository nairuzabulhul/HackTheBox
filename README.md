## HackTheBox : 

__Tools and Techniques used while doing the boxes and watching @ippsec @Derek_Rook__

![Image](/img/h.JPG)

HBT: Tools and Techniques
--------------------------

Initial Scanning:
-----------------

- nmap -sC -sV -oA initial IPaddress



Web Enumeration: 
----------------
Note: GOOGLE EVERYTHING, Do not take anything for granted, It might be the CLUE

- View the source code

- curl http://IPaddress  | check if the website has hidden useful metadata

- Proxy the request and check the GET and POST requests

- Enumerate the site with dirbuster or gobuster:

	>> gobuster -u htpp://IPaddress -w wordList 
	
	>> gobuster -u http://IPaddress -w WordList  -x FileExtension 
	
- Use Wapplyzer add-on on Firefox for detecting the site technologies

- Check what type of framework the site is running on:

	Wordpress, Nibbleblog, Jeeves

- Login Pages:

	- Try default credentials 
	
	- Try SQL common injections 
	

- SQLMap: 


- Nikto: fingerprint the website : 

	>> nikto -host http://IPaddress  -o output.txt

	
- Oracle Padding Attack : "Invalid Padding" | used authentication cookies 

	>> Cookies: auth=$CookieValue$

	
- Cookies: 

	- auth : try Oracle Padding Attack     | Lazy HTB
	
	- auth : try Bit Flipper on BurpSuite  | Lazy HTB
	
	
- DirSearch: another enumeration tool, similar to gobuster | Github
	
	>> dirsearch -u http://IPaddress -e php -w wordList
	
		- e type of files : php, old, bak
		- w wordList



Exploitation:
-------------

- Google exploits for :

	- services type and version number
	
	- OS type and version: Ex: Windows 2003, Ubuntu 
	
	- Web frames version or vulnerable plugins
	
- Check previous HTB exploits: Exploit.txt


- Searchsploit for vulnerable services or operating system version

	>> searchsploit nibbleblog
	

- If an exploit is found, open it and read the description of how it used and check exploit reference
   Found it helpful in understanding how to use the exploit manually without Metasploit
   
 


Privilege Escalation
---------------------



