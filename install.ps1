# AlkariSpy otomatik kurulum scripti (Windows)
# Bu script, otomatik olarak bir sanal ortam oluşturur ve projeyi kurar.

$VenvDir = "venv"

# Python 3 yüklü mü kontrol et
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install Python 3 first."
    exit 1
}

# Sanal ortam oluştur
python -m venv $VenvDir

# Sanal ortamı aktive et
.\$VenvDir\Scripts\Activate.ps1

# pip güncelle
pip install --upgrade pip

# Projeyi kur
pip install .

Write-Host "Kurulum tamamlandı! Sanal ortam aktif. Aracı çalıştırmak için:"
Write-Host ".\venv\Scripts\Activate.ps1; alkariSpy"
