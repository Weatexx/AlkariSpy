# AlkariSpy - OSINT Tool

**AlkariSpy** is an **Open Source Intelligence (OSINT)** tool that allows you to search for usernames and personal data across various social media platforms and websites. It uses **Google Dorking** to search for personal information and online profiles across the internet.

---

## Features / Özellikler

### **English:**

- **Username Search**: Allows you to search for a specified username across popular social media and web platforms (Twitter, Instagram, Facebook, GitHub, LinkedIn, etc.).
- **Google Dorking**: Uses Google Dorking search queries to search for a given name across various file types (PDF, DOCX, PPTX, etc.).
- **Proxy Rotation and VPN Support**: Enables proxy rotation and VPN support to bypass **Google IP bans** and prevent your IP from being blocked.
- **Bilingual Support**: Supports both **English** and **Turkish**, making it easy for users to navigate in different languages.
  
### **Türkçe:**

- **Kullanıcı Adı Araması**: Belirtilen bir kullanıcı adını popüler sosyal medya ve web platformlarında arama yapar (Twitter, Instagram, Facebook, GitHub, LinkedIn vb.).
- **Google Dorking**: Google Dorking sorgularını kullanarak verilen isimle ilgili çeşitli dosya türlerinde (PDF, DOCX, PPTX vb.) arama yapar.
- **Proxy Rotasyonu ve VPN Desteği**: **Google IP engellemelerinden** kaçınmak için proxy rotasyonu ve VPN desteği sağlar.
- **Çift Dilli Destek**: Hem **Türkçe** hem de **İngilizce** dil desteği ile kullanım kolaylığı sağlar.

---

## Installation / Kurulum

**Python 3.x** must be installed.

### Automatic Installation (Recommended for Kali/Linux/Windows)

#### Linux/Kali:
```bash
git clone https://github.com/Weatexx/AlkariSpy.git
cd AlkariSpy
chmod +x install.sh
./install.sh
```

#### Windows (PowerShell):
```powershell
git clone https://github.com/Weatexx/AlkariSpy.git
cd AlkariSpy
./install.ps1
```

This will automatically create a virtual environment and install all dependencies. The tool will be available as `alkarispy` in the activated environment.

### Manual Installation (If you prefer)

1. Clone the repository:
   ```bash
   git clone https://github.com/Weatexx/AlkariSpy.git
   cd AlkariSpy
   ```
2. Create and activate a virtual environment:
   - **Linux/Kali:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
3. Install the project:
   ```bash
   pip install .
   ```

**Do not install system-wide! Always use a virtual environment to avoid errors on Kali and similar systems.**

---
