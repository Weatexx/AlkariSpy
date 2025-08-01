#!/usr/bin/env python3
import sys
import pyfiglet
from colorama import Fore, init
from username_scan import username_search  # Burada username_search fonksiyonunu import ediyoruz
from dork_search import name_search  # name_search fonksiyonunu import ediyoruz
from email_search import email_search

# Başlangıçta colorama'yı başlatıyoruz
init(autoreset=True)

# ASCII Art ile "AlkariSpy" yazdırma ve kurt figürü
def display_ascii_art():
    """Show ASCII Art for AlkariSpy and a wolf symbol."""
    ascii_art_text = pyfiglet.figlet_format("AlkariSpy", font="slant")
    ascii_art_wolf = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣄⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⣡⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠙⣦⡙⢦⡀⠀⠀⠀⠀⠀⠀⡀⣄⡀⠀⡴⠸⣄⠀⣠⠎⢦⠀⢀⣠⢀⠀⠀⠀⠀⠀⠀⢀⡴⢋⣴⠏⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠘⢯⣦⣉⡳⠦⣄⡾⠶⠄⠛⢄⠉⣙⠁⣆⣌⠶⢃⣰⠈⢛⠉⠠⠚⠢⠶⠿⣠⠤⠞⣋⢴⡿⠋⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢠⠀⠈⢻⡻⣽⣶⣦⣄⠠⣄⠕⣤⣢⣞⣷⡜⣿⣶⣿⢧⣾⣷⣗⣤⠪⢀⠄⣠⣴⣶⣟⣟⡟⠁⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⡸⡂⠀⠀⠓⠘⢦⠀⠁⠁⠘⣦⢪⢿⣿⣿⠻⣿⣿⣿⠟⣿⣿⣿⡵⣴⠃⠘⠉⠐⡵⠋⠞⠀⠀⢀⢇⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣧⡀⠀⠀⠀⠄⠘⣧⠀⠀⠀⠸⣿⣿⣿⣿⣇⠘⣿⠃⣸⣿⣿⣿⣿⠇⠀⠀⠀⣼⠃⠀⠀⠀⠀⠘⢼⡸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⢿⡳⠀⠀⠀⠀⠀⠘⣧⡘⣦⣷⣻⢿⡿⣿⣿⣧⠀⣰⣿⣿⢿⡿⣿⣼⣴⣇⣼⠃⠀⠀⠀⠀⢀⠞⣿⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢸⡀⡈⢷⠄⠀⠀⠄⣲⣶⣾⡿⠿⢝⠿⢷⡕⠸⡿⣿⢷⣿⣯⡏⢪⡾⠫⣻⠿⢿⣷⣶⣖⠢⠀⠀⠀⡾⢃⠀⡇⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⡛⠁⠘⠀⠀⠀⠀⡴⣖⣚⣿⣧⣄⠠⡀⠀⠹⣆⢳⠉⠀⠉⡞⣠⠏⠀⢀⠄⣠⣼⣿⣓⣒⠦⠀⠀⠀⠀⠂⡈⠛⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⣤⣤⡖⠋⠁⠀⣠⣴⣟⢿⡿⣿⣿⣽⣦⣄⠈⠎⠣⠀⠘⠱⠁⢠⣴⣯⣿⣿⢿⡿⣿⣦⣄⠀⠈⠛⣶⣦⣄⡘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢟⡖⢀⣤⡤⠔⠂⠠⠼⢿⡡⠌⠁⠈⡀⠻⣝⣿⣿⣆⡆⠀⠀⠀⢠⣴⣿⣿⢿⠟⢁⠁⠈⠀⢉⡿⠷⠄⠐⠢⠤⣤⡀⢲⡛⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠐⡻⠉⠀⠀⠀⠀⣀⡬⠀⠀⡤⡀⠻⣦⡀⠙⣿⡿⠇⠀⠀⠀⠸⢿⣿⠃⢁⣴⡟⢀⣤⠀⠀⢥⣄⠀⠀⠀⠀⠉⢝⠂⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢇⣼⣧⢾⣽⡂⢠⣾⠿⢿⣿⣧⣝⣿⣦⣄⠀⠀⠀⠀⠠⣴⣀⣦⡤⠀⠀⠀⠀⣀⣴⣟⣫⣴⣿⣿⠿⣷⣄⢀⢮⡷⢮⣧⡘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡚⠉⠐⣩⡯⠖⢀⣤⢆⡀⠀⠉⠛⢻⡭⠀⠀⠲⢮⣽⣦⠸⣿⠏⣴⣏⡽⠖⠀⠀⢹⡟⠛⠋⠀⠀⡰⣤⡄⠰⢽⣍⠂⠉⢛⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣠⠀⢚⡭⠂⠀⢉⣾⡿⠉⠀⠀⠀⢠⡶⢿⣷⣿⣦⠸⠿⠳⠉⠞⠿⠏⣴⣿⣾⡿⢶⣄⠀⠀⠀⠨⢿⣷⡍⠀⠐⢮⡓⠄⣄⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⡴⢋⣔⠄⠀⠀⡟⠀⡴⣾⠀⠀⡏⠀⢰⣿⢿⡇⠐⠊⠻⣿⠟⠉⠂⢹⣿⣿⡞⠀⠸⡄⠀⢳⢦⠀⢻⠀⠀⠠⡢⡙⢦⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠟⡀⢸⣿⠊⠀⠀⠃⠀⠁⡏⡆⠀⠀⠐⢌⠻⣟⣧⡀⠀⠀⠀⠀⠀⢀⣼⣳⡟⡡⠂⠀⠀⢰⢿⠈⠂⠈⠀⠀⠑⣽⡇⢀⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡧⠀⠀⡀⠀⠀⠀⠁⢟⣆⠀⠀⠠⡓⢽⡿⡗⠆⠀⠀⠀⠠⢾⢟⡿⢊⠅⠀⢠⣸⡻⠈⠀⠀⠀⢀⠀⠀⢾⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠈⣠⡎⣾⠄⠰⡁⠄⠀⠀⠈⢻⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⢀⡾⠁⠀⠀⠀⣀⠆⠀⣳⢰⣄⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣰⠋⣧⠟⢀⢀⣿⡔⢰⠇⠀⠀⠁⠀⠀⣿⠀⡇⢰⢠⠀⡆⡆⢸⠀⣷⠁⠀⠈⠀⠀⠐⡆⢢⣻⡀⡀⠻⣸⠙⣆⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⠸⡄⡾⣆⠻⡇⠘⠀⢀⠀⠀⠀⢀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠀⠀⠀⠀⡀⠀⠃⢸⠟⣰⣿⢀⠏⠀⠸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠁⣿⠀⣴⠀⢸⢺⠀⠀⠀⠘⠀⢸⠀⠀⠀⠀⠀⠀⠀⡇⠀⡇⠀⠀⠀⢳⡄⠀⣶⠀⢹⠈⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡜⠹⠳⣌⣿⡄⠀⠀⢇⠀⢻⢠⠀⠀⠀⠀⠀⡄⡯⠀⢰⠀⠀⢠⣿⢡⠞⠏⢧⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠫⢳⣔⢠⠀⠀⡌⠈⠋⠃⠂⠘⠉⠁⢁⠀⠀⡄⣤⡞⠝⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⡆⣦⠈⠓⠒⠒⠒⠒⠒⠚⠁⣰⢠⣵⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠘⢧⡈⢾⣴⣾⣦⠶⢃⡼⠃⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡈⠛⢃⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    print(Fore.RED + ascii_art_text)  # AlkariSpy yazısını yeşil renkte
    print(Fore.RED + ascii_art_wolf)  # Kurt ASCII art'ı sarı renkte

# Dil seçimi fonksiyonu
def language_selection():
    """Detect or ask the user for language selection (English or Turkish)."""
    language = input("Select your language / Dil seçin (en/tr): ").strip().lower()
    if language == "en":
        return "en"
    elif language == "tr":
        return "tr"
    else:
        print("Invalid selection, defaulting to English.")
        return "en"

def main_menu(language):
    """Display the main menu options."""
    if language == "en":
        print("\nOSINT Tool - Main Menu")
        print("1. Username Search")
        print("2. Name-based Google Dork Search")
        print("3. Advanced Options")
        print("4. Exit")
    else:
        print("\nOSINT Aracı - Ana Menü")
        print("1. Kullanıcı Adı Ara")
        print("2. İsim Tabanlı Google Dork Arama")
        print("3. İleri Seçenekler")
        print("4. Çıkış")

    choice = input("\nEnter your choice / Seçiminizi yapın: ").strip()
    return choice

def advanced_menu(language):
    """Display advanced menu options."""
    if language == "en":
        print("\nAdvanced Options")
        print("1. Search by Username")
        print("2. Search by Email Address")
        print("3. Exit")
    else:
        print("\nİleri Seçenekler")
        print("1. Kullanıcı Adı Ara")
        print("2. E-posta Adresi Ara")
        print("3. Çıkış")

    choice = input("\nEnter your choice / Seçiminizi yapın: ").strip()
    return choice

def run_osint_tool():
    """Run the OSINT tool based on user input."""
    display_ascii_art()  # Show ASCII art at the start
    language = language_selection()
    
    while True:
        choice = main_menu(language)
        
        if choice == "1":  # Username Search
            username = input("Enter the username to search for: ")
            username_search(username, language)
        
        elif choice == "2":  # Name-based Google Dork Search
            name = input("Enter the full name to search for: ")
            name_search(name, language)  # This calls the name_search function from dork_search.py
        
        elif choice == "3":  # Advanced Search Options
            advanced_choice = advanced_menu(language)
            if advanced_choice == "1":
                username = input("Enter the username to search for: ")
                username_search(username, language)
            elif advanced_choice == "2":
                email = input("Enter the email address to search for: ")
                email_search(email, language)  # Email search functionality
            else:
                print("Exiting...")
                sys.exit(0)
        
        elif choice == "4":  # Exit
            print("Exiting the tool... Çıkılıyor...")
            sys.exit(0)
        
        else:
            print("Invalid choice, please try again / Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    run_osint_tool()
