# How to fork the repo and use it.

- Create 3 groups
- One person from each group will fork the repo.  
	- If you don't have a github account, create one.
	- Go to the repo page and click on the `Fork` button on the top right corner. (This will create a copy of the repo in your account)
	- Add members to the group as collaborators.
		- Go to the repo page in your account.
		- Click on `Settings` tab.
		- Click on `Collaborators` on the left side.
		- Add the other members in the group as collaborators.
- Clone the repo to your local machine.
	- create a key pair
		```
		ssh-keygen -t rsa -b 4096 -C 
		```
	- copy the public key to your github account
		```
		cat ~/.ssh/id_rsa.pub
		```
	- Go to settings>SSH and GPG keys> New SSH key and paste the key.
	- Clone the repo
		```
		git clone <repo_url>
		```
