# PAP

#Project Allotment Portal for MNNIT

Users are : 
Normal Users and Leader users
Leader is decided by cpi and assigned slot 1.

Leader can send request via a dynamic changing portal to fellow normal users.

Leader can fill the preference of professors dynamically.

Normal users can accept requests of leader and if leader request is already accepted by someone of same slot then it throws an error.


#Admin:
To create a admin user, execute "from administrator import create_database" in django shell and follow the instruction.
Admin can upload data of students and professor via a csv file(sample file is given) ,after that user tables get automatically created accordingly.
Algorithms for assigning mentors ,random group allotment etc. has been effectively implemented.


***
Sitewide login implemented.
Seperate page for group and professor data.
