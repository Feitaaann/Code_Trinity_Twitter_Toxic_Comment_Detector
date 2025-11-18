# Code_Trinity Final Project - Deliverables Checklist

Based on the requirements, here are the deliverables needed:

## Part I: Scientific Verification

### 1. Final Draft of IEEE Report (.docx)
- **Status:** ❌ Missing - Only .txt version exists
- **Required:** Code_Trinity_Final_Project.docx
- **Action:** Convert .txt to .docx or create from paper

### 2. Ground-Truth Test Set (.csv)
- **Status:** ⚠️ Need to verify export in notebook
- **Required:** ground_truth_test_set.csv with review and label columns
- **Action:** Add export code to notebook

### 3. Code Repository (GitHub URL)
- **Status:** ❌ No git repository initialized
- **Required:** GitHub repository URL
- **Action:** Initialize git, create repository, push code

### 4. Experiment Logs and Checkpoints (.xlsx)
- **Status:** ✅ Available
- **Files:**
  - experiment_runs_enriquez.xlsx
  - experiment_runs_morales.xlsx
  - experiment_runs_dulo.xlsx
  - exports/experiment_runs_all (1).xlsx
- **Action:** Verify all are complete

### 5. Reproducibility Notebook (.ipynb)
- **Status:** ✅ Exists but needs fixes
- **File:** Code_Trinity_Final_Project.ipynb
- **Issues Found:**
  - ❌ Uses `plt.close()` preventing inline display
  - ❌ Missing ground truth test set export
  - ⚠️ Need to verify end-to-end execution
- **Action:** Fix visualization display and add test set export

## Part II: Individual Contribution (Accountability)

### 6. Member Responsibility Matrix (MRM) (.docx)
- **Status:** ❌ Missing
- **Required:** Member_Responsibility_Matrix_Code_Trinity.docx
- **Team Members:**
  - Fercy T. Enriquez
  - Russel Troy Dulo
  - Vince Gabrielle Morales
- **Action:** Create MRM document

### 7. Final Presentation with Individual Segments (.pptx)
- **Status:** ❌ Missing
- **Required:** Final_Presentation_Code_Trinity.pptx
- **Action:** Create presentation with segments for each member

### 8. Signed Final Project Integrity and AI Usage Statement (.pdf)
- **Status:** ❌ Missing
- **Required:** Code_Trinity_Integrity_Statement.pdf
- **Action:** Create integrity statement document

## Current Project Status

### ✅ Available:
- Notebook: Code_Trinity_Final_Project.ipynb
- Paper (text): Code_Trinity_Final_Project.txt
- Experiment logs: Multiple .xlsx and .csv files
- Test IDs: test_ids.csv
- Model checkpoints: checkpoints/bert-base/best/
- Exports: exports/ directory with results

### ❌ Missing:
- IEEE Report (.docx)
- Ground truth test set export in notebook
- GitHub repository
- MRM document
- Presentation
- Integrity statement

### ⚠️ Needs Fix:
- Notebook inline visualizations (plt.close() issue)
- Notebook ground truth test set export

## Next Steps

1. Fix notebook: Remove plt.close(), add plt.show(), add ground truth export
2. Create .docx version of paper
3. Initialize git repository and push to GitHub
4. Create MRM document
5. Create presentation with individual segments
6. Create integrity statement
7. Organize all deliverables in Final_Project_Deliverables folder


