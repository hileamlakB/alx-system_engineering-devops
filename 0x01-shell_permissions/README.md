**0x00.Shell, permissions**

In this directory ther are scripts that are ment to do a spacific task. The name of each file tries to 
explain what thiey do, but for more informaiton you can read the following content.

This table is prepared so as to show you what each script does.

Script | Task | Command used |
----------------------------- | -----------| ---------------|
0-iam_betty|this changes the user id to betty by making the current user betty| su betty
1-who_am_i|prints the effective user id as a name| id -un , the u flag is for user and n for name
10-mirror_permissions|copy permissions form olleh to hello|chmod --reference=olleh hello
100-Star_Wars|Plays the star wars move on the command line using the telnet protocol|telnet towel.blinkenlights.nl
101-man_holberton|Show how to create a manual page| codes is too long to includ here
11-directories_permissions|adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.|chmod -R a+x ./*/
12-directory_permissions|creates a dirctory with a 751 permission|mkdir -m 751 dir_holberton, -m for passing mode
13-change_group|change the group of the hello file|chgrp holberton hello
14-change_owner_and_group|changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.|chown betty:holberton ./*
15-symbolic_link_permissions|changes the owner and the group owner of the file _hello to betty and holberton respectively.|chown -h betty:holberton _hello
16-if_only| changes the owner of the file hello to betty only if it is owned by the user guillaume|chown --from=guillaume betty hello
2-groups|prints all group Ids not only the effective one| id -Gn, G-all group and n-name
3-new_owner|change ownership of file hello to betty| chown betty hello
4-empty|creats an empty file named hello| touch hello
5-execute|addes excute permion to the owner over the hello file|chmod u+x hello
6-multiple_permissions|adds execute permission to the owner and the group owner, and read permission to other users, to the file hello|chmod ug+x,o+r hello
7-everybody|adds execution permission to the owner, the group owner and the other users, to the file hello|chmod ugo+x hello
8-James_Bond|set the owner and group permission to none and all permision to other user.* A forigner to your own land*|chomd ug=,o=rwx hello
9-John_Doe|sets the mode of the file hello to 753|chmod 753 hello

