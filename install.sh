#!/bin/bash
# AlkariSpy otomatik kurulum scripti (Linux/Kali)
# Bu script, otomatik olarak bir sanal ortam oluşturur ve projeyi kurar.

set -e

VENV_DIR="venv"

# Python 3 yüklü mü kontrol et
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Sanal ortam oluştur
python3 -m venv "$VENV_DIR"

# Sanal ortamı aktive et
source "$VENV_DIR/bin/activate"

# pip güncelle
pip install --upgrade pip

# Projeyi kur
pip install .

echo "Kurulum tamamlandı! Sanal ortam aktif. Aracı çalıştırmak için:"
echo "source $VENV_DIR/bin/activate && alkariSpy"
