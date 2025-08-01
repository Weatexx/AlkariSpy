from googlesearch import search
from colorama import Fore  # colorama.Fore modülünü import ettik
import time  # zaman ayarlamaları için import ettik

def name_search(name, language):
    """Perform a Google dork search for a full name."""
    query = f"\"{name}\""
    
    # Gelişmiş Dork Sorguları
    dorks = [
        f"site:linkedin.com {query}",         # LinkedIn üzerinde arama
        f"filetype:pdf {query}",              # PDF dosyalarında arama
        f"filetype:doc {query}",              # DOC dosyalarında arama
        f"filetype:docx {query}",             # DOCX dosyalarında arama
        f"filetype:xls {query}",              # XLS dosyalarında arama
        f"filetype:xlsx {query}",             # XLSX dosyalarında arama
        f"filetype:txt {query}",              # TXT dosyalarında arama
        f"filetype:ppt {query}",              # PPT dosyalarında arama
        f"filetype:pptx {query}",             # PPTX dosyalarında arama
        f"intitle:CV {query}",                # Sayfa başlığında CV kelimesi arama
        f"intitle:{query} resume",            # Resume başlığında arama
        f"intitle:{query} biography",        # Biyografi başlığında arama
        f"inurl:{query} CV",                 # URL'de CV ifadesi ile arama
        f"intext:{query} CV",                # Sayfa içeriğinde CV ifadesi ile arama
        f"site:github.com {query}",          # GitHub üzerinde arama
        f"site:reddit.com {query}",          # Reddit üzerinde arama
        f"site:twitter.com {query}",         # Twitter üzerinde arama
        f"site:facebook.com {query}",        # Facebook üzerinde arama
        f"site:medium.com {query}",          # Medium üzerinde arama
        f"site:behance.net {query}",         # Behance üzerinde arama
        f"site:stackoverflow.com {query}",   # StackOverflow üzerinde arama
        f"site:quora.com {query}",           # Quora üzerinde arama
        f"cache:{query}",                    # Google'ın önbelleğinde arama
        f"related:{query}",                  # Benzer sayfalarda arama
        f"link:{query}",                     # Bağlantı veren sayfalarda arama
        f"inurl:{query} blog",               # Blog URL'lerinde arama
        f"inurl:{query} profile",            # Profil URL'lerinde arama
        f"site:tiktok.com {query}",          # TikTok üzerinde arama
        f"site:instagram.com {query}",       # Instagram üzerinde arama
        f"site:youtube.com {query}",         # YouTube üzerinde arama
        f"site:pinterest.com {query}",       # Pinterest üzerinde arama
        f"site:github.com {query}",          # GitHub üzerinde arama
    ]
    
    if language == "en":
        print(f"\nSearching for the name '{name}' using Google Dorks...\n")
    else:
        print(f"\n'{name}' ismiyle Google Dork araması yapıyorum...\n")
    
    for dork in dorks:
        print(f"\nSearching with query: {dork}")
        
        # Burada Google Search sorgusu yapılırken arama sayısı sınırlanıyor
        try:
            results = search(dork, num_results=3)  # Her dork sorgusundan 3 sonuç alıyoruz
            for result in results:
                if "google.com/search" not in result:  # Google arama linklerini atla
                    print(f"{Fore.GREEN}{result}")
                else:
                    print(f"{Fore.RED}[SKIPPED] Google Search result skipped: {result}")
            
            # Sorgular arasında 20 saniye bekleme süresi ekliyoruz
            time.sleep(20)  # Arama başına bekleme süresi artırılabilir
        except Exception as e:
            print(f"{Fore.RED}[ERROR] There was an error with the search query: {e}")
