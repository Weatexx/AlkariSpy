import requests
import json
import time
from colorama import Fore, init
import keyboard  # Kullanıcı tuşlarına basmayı dinleyeceğiz

# Başlangıçta colorama'yı başlatıyoruz
init(autoreset=True)

# JSON dosyasındaki platformları yükle
def load_platforms():
    with open('platforms.json', 'r') as f:
        data = json.load(f)
    return data['platforms']

def save_results_to_file(results, filename="results.json"):
    """Save the results to a JSON file."""
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

def username_search(username, language):
    """Check if the username exists on various platforms."""
    platforms = load_platforms()  # JSON dosyasından platformları alıyoruz
    found_platforms = []  # Bulunan platformları kaydedecek bir liste
    results = {}
    
    if language == "en":
        print(f"\nSearching for the username '{username}' on popular platforms...\n")
    else:
        print(f"\n'{username}' kullanıcı adını popüler platformlarda arıyorum...\n")
    
    stop_search = False  # Varsayılan olarak arama durmayacak

    for platform in platforms:
        url = platform + username
        found = False
        
        # Her platform için 2 deneme yapacağız
        for attempt in range(2):  # Deneme sayısını 2'ye düşürüyoruz
            if keyboard.is_pressed('q'):  # Kullanıcı 'q' tuşuna bastıysa
                stop_search = True
                break  # Arama işlemini sonlandırıyoruz
            
            try:
                print(f"Attempt {attempt + 1} for {url}")
                # İstek gönderirken 10 saniye bekleme süresi ekleyelim
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    results[url] = "Found"
                    found = True
                    found_platforms.append(url)  # Bulunan platformu ekle
                    # Başarı durumunda yeşil renk ve basit simge
                    if language == "en":
                        print(f"{Fore.GREEN}[FOUND] {url}")
                    else:
                        print(f"{Fore.GREEN}[BULUNDU] {url}")
                    break  # Platform bulundu, denemeyi sonlandırıyoruz
                else:
                    results[url] = "Not Found"
                    # Bulunmayan platformlar için kırmızı renk ve basit simge
                    if language == "en":
                        print(f"{Fore.RED}[NOT FOUND] {url}")
                    else:
                        print(f"{Fore.RED}[BULUNAMADI] {url}")
                    break  # Kullanıcı adı bulunmadı, denemeyi sonlandırıyoruz
                
            except requests.exceptions.RequestException as e:
                # Bağlantı hatası durumunda ⚠️ simgesi ile uyarı
                if language == "en":
                    print(f"{Fore.YELLOW}[ERROR] Error accessing {url}: {str(e)}. Retrying...")
                else:
                    print(f"{Fore.YELLOW}[HATA] {url} erişilemedi: {str(e)}. Yeniden deniyorum...")
                
                # Denemeler arasında 10 saniye bekleyelim
                time.sleep(10)
        
        # Eğer 'q' tuşuna basıldıysa ve arama durdurulmuşsa
        if stop_search:
            print(f"{Fore.RED}Search stopped by user, returning to main menu...")
            break  # Ana menüye dönüyoruz

    # Tarama tamamlandıktan sonra bulunan tüm platformları listele
    if language == "en":
        print(f"\nThe following platforms were found for the username '{username}':")
    else:
        print(f"\n'{username}' kullanıcı adı için bulunan platformlar:")
    
    for platform in found_platforms:
        print(f"{Fore.GREEN}[FOUND] {platform}")

    # Save the results to a file
    save_results_to_file(results)
