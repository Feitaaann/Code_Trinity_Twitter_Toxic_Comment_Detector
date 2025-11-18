# GitHub Repository Setup Guide

## Steps to Create and Push Repository

### 1. Initialize Git Repository

```bash
cd "C:\Users\ASUS\Desktop\Elective 4\Code_Trinity"
git init
```

### 2. Create .gitignore File

Create a `.gitignore` file with:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# Model files (large)
*.bin
*.safetensors
models/*.joblib
checkpoints/**/*.bin

# Data files (if too large)
*.csv
!ground_truth_test_set.csv
!test_ids.csv
!train_ids.csv
!val_ids.csv

# Exports (keep structure, ignore large files)
exports/*.bin
exports/*.png
exports/confusion_matrices/
exports/roc_curves/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.log
```

### 3. Add Files to Git

```bash
# Add all files
git add .

# Or add specific files/directories
git add Code_Trinity_Final_Project.ipynb
git add Code_Trinity_Final_Project.docx
git add requirements.txt
git add README.md
git add app/
git add ground_truth_test_set.csv
git add test_ids.csv train_ids.csv val_ids.csv
git add exports/*.csv exports/*.xlsx
git add experiment_runs_*.csv experiment_runs_*.xlsx
```

### 4. Create Initial Commit

```bash
git commit -m "Initial commit: Twitter Toxicity Detection Project

- Complete notebook with end-to-end workflow
- Baseline and BERT model implementations
- Experiment logs for all team members
- Ground truth test set
- Deployment-ready API and UI
- Comprehensive documentation"
```

### 5. Create GitHub Repository

1. Go to GitHub (your account)
2. Click "New repository"
3. Repository name: `code-trinity-twitter-toxicity-detection` (or your preferred name)
4. Description: "Toxic Comment Detection on Twitter Using Fine-Tuned BERT - Deep Learning Project"
5. Set to Public or Private (as required)
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create repository"

### 6. Connect Local Repository to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/code-trinity-twitter-toxicity-detection.git

# Or if using SSH
git remote add origin git@github.com:YOUR_USERNAME/code-trinity-twitter-toxicity-detection.git
```

### 7. Push to GitHub

```bash
# Push to main branch
git branch -M main
git push -u origin main
```

### 8. Verify Repository

1. Go to your GitHub repository URL
2. Verify all files are present
3. Check that README.md displays correctly
4. Verify ground_truth_test_set.csv is included

## Repository Structure

Your repository should include:

```
code-trinity-twitter-toxicity-detection/
├── Code_Trinity_Final_Project.ipynb
├── Code_Trinity_Final_Project.docx
├── README.md
├── requirements.txt
├── ground_truth_test_set.csv
├── test_ids.csv
├── train_ids.csv
├── val_ids.csv
├── experiment_runs_enriquez.csv
├── experiment_runs_enriquez.xlsx
├── experiment_runs_morales.csv
├── experiment_runs_morales.xlsx
├── experiment_runs_dulo.csv
├── experiment_runs_dulo.xlsx
├── exports/
│   ├── experiment_runs_all.csv
│   ├── experiment_runs_all.xlsx
│   ├── model_comparison.csv
│   └── ...
├── app/
│   ├── backend/
│   ├── inference/
│   └── ui/
├── checkpoints/
│   └── bert-base/
│       └── best/
└── models/
```

## Important Notes

1. **Large Files**: Model checkpoints (.bin files) are large. Consider using Git LFS or excluding them if repository size is a concern.

2. **Sensitive Data**: Ensure no sensitive information is committed.

3. **README.md**: Update README.md with the GitHub repository URL after creation.

4. **Branch Protection**: Consider setting up branch protection rules if working in a team.

## Troubleshooting

### If push fails due to large files:
```bash
# Use Git LFS for large files
git lfs install
git lfs track "*.bin"
git lfs track "checkpoints/**/*.bin"
git add .gitattributes
git commit -m "Add Git LFS tracking for model files"
git push
```

### If you need to update README with repository URL:
Edit README.md and add:
```markdown
## Repository
**GitHub URL:** https://github.com/YOUR_USERNAME/code-trinity-twitter-toxicity-detection
```

Then commit and push:
```bash
git add README.md
git commit -m "Update README with repository URL"
git push
```

## Next Steps After Repository Setup

1. ✅ Verify all deliverables are in repository
2. ✅ Update README.md with repository URL
3. ✅ Create Final_Project_Deliverables folder (optional, for organization)
4. ✅ Add repository URL to presentation and MRM documents


