# How to Upload to GitHub

## Step-by-Step Instructions

### 1. Create a GitHub Repository
- Go to github.com and sign in
- Click the "+" icon in top right → "New repository"
- Name it (e.g., "data-cleaning-api" or "flask-pandas-api")
- Choose Public or Private
- **Don't** check "Initialize with README" (we already have one)
- Click "Create repository"

### 2. Open Terminal in Your Project Folder
- Make sure you're in: `C:\Users\goatm\Desktop\flask`

### 3. Initialize Git (if not already done)
```bash
git init
```

### 4. Add All Files
```bash
git add .
```

### 5. Make Your First Commit
```bash
git commit -m "Initial commit: Flask data cleaning API"
```

### 6. Connect to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```
(Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and repo name)

### 7. Push to GitHub
```bash
git branch -M main
git push -u origin main
```

### 8. Enter Credentials
- If prompted, enter your GitHub username
- For password, use a **Personal Access Token** (not your GitHub password)
  - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Generate new token with "repo" permissions
  - Copy and paste it as your password

### Done! 
Your code is now on GitHub. You can view it at: `https://github.com/YOUR_USERNAME/YOUR_REPO_NAME`

