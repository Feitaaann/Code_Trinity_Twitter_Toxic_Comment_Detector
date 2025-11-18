# Streamlit Cloud Deployment Guide

## ✅ Repository Information
- **Repository**: `Feitaaann/Code_Trinity`
- **Branch**: `main` (not master!)
- **Main File Path**: `app/ui/app.py` (not streamlit_app.py!)

## Deployment Settings

When deploying on Streamlit Cloud, use these settings:

### Required Fields:
1. **Repository**: `Feitaaann/Code_Trinity` ✅
2. **Branch**: `main` (change from "master" to "main")
3. **Main file path**: `app/ui/app.py` (change from "streamlit_app.py" to "app/ui/app.py")
4. **App URL**: `codetrinity-rq3ntdtdomxsteldogkukp` (or your preferred name)

### Steps to Fix:
1. In the Branch field, change `master` to `main`
2. In the Main file path field, change `streamlit_app.py` to `app/ui/app.py`
3. Click "Deploy"

## Additional Notes

- The Streamlit app is located at: `app/ui/app.py`
- Make sure all dependencies are in `requirements.txt`
- The app expects model files in `checkpoints/bert-base/best/`
- Make sure the repository is pushed to GitHub first

## Verify Before Deploying

1. ✅ Repository exists: https://github.com/Feitaaann/Code_Trinity
2. ✅ Branch is `main` (not master)
3. ✅ File exists at `app/ui/app.py`
4. ✅ `requirements.txt` is in the root directory

## After Deployment

Once deployed, you can access your app at:
`https://codetrinity-rq3ntdtdomxsteldogkukp.streamlit.app`

Or your custom URL if you set one.

