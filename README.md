# RAS-GitHub-Git-Workshop
Code for people to pull and get the python hang man game on to their own repo.

## Installations Needed:
- Python
- VS Code
- GIT

## Steps:

1. Open "Git Bash" or Terminal
2. type ```git config --global user.name "Your Name"``` [Do not include the parethesis and change the contents inside with your own]
3. type ```git config --global user.email "Your@email.com"``` [Do not include the parethesis and change the contents inside with your own]

## Creating your SSH key

1. Open "Git Bash"
2. Start keyt agent by typing ```eval "$(ssh-agent -s)"```
4. Create SSH Key by typing ```ssh-keygen -t ed25519 -C "youremail@example.com"``` [Do not include the parethesis and change the contents inside with your own]
5. Copy SSH key by typing ```clip < ~/.ssh/id_rsa.pub```
6. Go to GitHub and add the SSH key in your account settings
7. Go back to "Git Bash" and type ```ssh -T git@github.com``` to confirm your SSH key was added

