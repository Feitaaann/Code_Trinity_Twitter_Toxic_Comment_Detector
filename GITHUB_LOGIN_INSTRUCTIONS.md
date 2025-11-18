# GitHub Login Instructions - New Account

## Credentials Cleared ✅

I've cleared your previous GitHub credentials. You can now log in with a new account.

## Next Steps to Login with New Account

### Option 1: Login via Git Push (Recommended)

When you push to GitHub for the first time, Git will prompt you to authenticate:

1. **Initialize your repository:**
   ```bash
   cd "C:\Users\ASUS\Desktop\Elective 4\Code_Trinity"
   git init
   ```

2. **Add files and commit:**
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

3. **Create repository on GitHub:**
   - Go to https://github.com
   - Click "New repository"
   - Create repository (don't initialize with README)
   - Copy the repository URL

4. **Add remote and push:**
   ```bash
   git remote add origin https://github.com/YOUR_NEW_USERNAME/REPO_NAME.git
   git push -u origin main
   ```

5. **When prompted for credentials:**
   - Username: Your new GitHub username
   - Password: Use a **Personal Access Token** (not your password)
     - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
     - Generate new token with `repo` scope
     - Use this token as your password

### Option 2: Use GitHub Desktop

1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your new GitHub account
3. Add the repository
4. Push from GitHub Desktop

### Option 3: Use SSH Keys

1. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. Add SSH key to GitHub:
   - Copy public key: `cat ~/.ssh/id_ed25519.pub`
   - Go to GitHub → Settings → SSH and GPG keys → New SSH key
   - Paste and save

3. Use SSH URL:
   ```bash
   git remote add origin git@github.com:YOUR_USERNAME/REPO_NAME.git
   ```

## Verify New Account

After logging in, verify:
```bash
git config --global user.name "Your New Username"
git config --global user.email "your_new_email@example.com"
```

## Important Notes

- **Personal Access Token**: GitHub no longer accepts passwords for Git operations. You must use a Personal Access Token.
- **Token Scope**: Make sure your token has `repo` scope for full repository access.
- **Security**: Never commit tokens or passwords to your repository.

## If You Need to Switch Accounts Again

To clear credentials again:
```bash
cmdkey /delete:LegacyGeneric:target=git:https://github.com
```

Or use:
```bash
git credential-manager-core erase
```

Then enter:
```
protocol=https
host=github.com
```

Press Enter twice to confirm.


