…or create a new repository on the command line
echo "# SIPB-SistemInformasiPemantauanBBM" >> README.md
git init (lakukan hanya pertama kali upload ke github/pertama kali membuat repo projectco)
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ittrh/SIPB-SistemInformasiPemantauanBBM.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/ittrh/SIPB-SistemInformasiPemantauanBBM.git
git branch -M main
git push -u origin main