# Git LFS Setup for Large Model Files

## ✅ What is Git LFS?

Git LFS (Large File Storage) allows you to push large files to GitHub that exceed the 100MB limit. Files are stored separately and downloaded on-demand.

## ✅ Setup Complete

I've configured Git LFS to track:
- `*.bin` files (model files)
- Files in `checkpoints/` folder
- Files in `exports/` folder

## 🚀 Push Large Files

Now you can push the large model files:

```powershell
cd "C:\Users\ASUS\Desktop\Elective 4\Code_Trinity"
git push -u origin main
```

**When prompted:**
- Username: `Feitaaann`
- Password: Your Personal Access Token

## 📝 How Git LFS Works

1. Large files are stored in Git LFS (not in the main git repository)
2. Only pointers to the files are stored in git
3. Files are downloaded automatically when you clone the repository
4. GitHub provides 1GB of free LFS storage (enough for your models)

## ✅ Files Now Tracked with LFS

- `checkpoints/bert-base/best/pytorch_model.bin` (417MB)
- `checkpoints/bert-base/best/pytorch_model_quantized.bin` (173MB)
- `exports/pytorch_model.bin` (417MB)

## 🔍 Verify LFS Tracking

Check which files are tracked:
```powershell
git lfs ls-files
```

## 📦 Alternative: GitHub Releases

If Git LFS doesn't work or you want another option:
1. Create a GitHub Release
2. Upload model files as release assets
3. Link to them in your README

## ⚠️ Important Notes

- Git LFS requires authentication (same as regular git push)
- First push with LFS may take longer (uploading large files)
- Make sure you have enough LFS quota on GitHub (1GB free)

---

**Ready to push!** The large files will now be uploaded using Git LFS.

