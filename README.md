## HackTheBox : 

__Tools and Techniques used while doing the boxes and watching @ippsec @Derek_Rook__

![Image](/img/h.JPG)

### Initial Scanning:
 
- nmap -sC -sV -oA initial IPaddress


-------------------------------------------------------------------------------------------------------------------------------------

### Web Enumeration: 
__Note: GOOGLE EVERYTHING, Do not take anything for granted, It might be the CLUE__

- View the source code

- curl http://IPaddress  | check if the website has hidden useful metadata

- Proxy the request and check the GET and POST requests

- __Gobuster__ : eumerate the site with dirbuster or gobuster:

	>> gobuster -u htpp://IPaddress -w wordList 
	
	>> gobuster -u http://IPaddress -w WordList  -x FileExtension 
	
- __Wapplyzer__ use the add-on on Firefox for detecting the site technologies

- Check what type of framework the site is running on:

	__Wordpress, Nibbleblog, Jeeves__

- __Login Pages__: if you come accross a login page

	- Try default credentials 
	
	- Try SQL common injections 
	


- __SQLMap:___



- __Nikto: fingerprint the website :__ 

	>> nikto -host http://IPaddress  -o output.txt
	
  
- __DirSearch:__ another enumeration tool, similar to gobuster | Github
	
	>> dirsearch -u http://IPaddress -e php -w wordList
	
		- e type of files : php, old, bak
		- w wordList
    
		
### Attacks:

- __Oracle Padding Attack___ "Invalid Padding" | used authentication cookies 

	>> Cookies: auth=$CookieValue$


-------------------------------------------------------------------------------------------------------------------------------------
### Exploitation:


- Google exploits for :

	- services type and version number
	
	- OS type and version: Ex: Windows 2003, Ubuntu 
	
	- Web frames version or vulnerable plugins
	
- Check previous HTB exploits: Exploit.txt




--------------------------------------------------------------------------------------------------------------------------------------
### Privilege Escalation





