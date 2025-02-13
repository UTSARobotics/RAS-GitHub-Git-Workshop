# RAS-GitHub-Git-Workshop
Code for people to pull and get the python hang man game on to their own repo.

## Installations Needed:
- Python
- VS Code
- GIT

## Steps:

1. Open "Git Bash" or Terminal
2. [Do not include the parethesis and change the contents inside with your own]
   ```
   git config --global user.name "Your Name"
   ``` 
3. [Do not include the parethesis and change the contents inside with your own]
   ```
   git config --global user.email "Your@email.com"
   ```

## Creating your SSH key

1. Open "Git Bash"
2. Start keyt agent by typing
   ```
   eval "$(ssh-agent -s)"
   ```
3. Create SSH Key, [Do not include the parethesis and change the contents inside with your own]
   ```
   ssh-keygen -t ed25519 -C "youremail@example.com"
   ``` 
4. Copy SSH key by typing
   ```
   clip < ~/.ssh/id_ed25519.pub
   ```
5. Go to GitHub and add the SSH key in your account settings
6. Go back to "Git Bash" and type this to confirm your SSH key was added
   ```
   ssh -T git@github.com
   ```
    

