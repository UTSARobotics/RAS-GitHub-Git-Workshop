# RAS-GitHub-Git-Workshop

## Installations Needed:
- Python
- VS Code/terminal
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


## Git/Github Activity
1. Initialize Git
   ```
   git init
   git status
   ```
2. Add both repositories to your pull/fetch respectively
   ```
   git remote add origin {RAS Github Repo}
   git remote set-url --push origin {Your Repo}
   git remote -v
   ```
3. Grab the files from the RAS repository
   ```
   git pull origin main
   ```
4. Save changes and make a "commit" for your repository
   ```
   git add .
   git commit - m “+ Python Hangman”
   ```
5. Push your changes to your own repository
   ```
   git push origin master
   git log
   ```
6. Have fun playing Hangman :)
