from setuptools import setup, find_packages

setup(
    name='alkarispy',  # Komut ismi
    version='0.1',  # Proje versiyonu
    description='An OSINT tool for searching usernames and personal data across various platforms using Google Dorking.',
    author='None',  # Yazar adı
    author_email='None',  # Yazar e-posta adresi
    url='https://github.com/Weatexx/AlkariSpy',  # Proje URL'si
    py_modules=['main', 'username_scan', 'dork_search', 'email_search'],  # Tek dosyalık modüller
    install_requires=[  # Gereksinimler
        'requests',
        'googlesearch-python',
        'colorama',
        'pyfiglet',
        'keyboard',  # veya 'pynput' kullanabilirsiniz
    ],
    entry_points={  # Komut satırında çalıştırılabilir yapmak için
        'console_scripts': [
            'alkarispy = main:run_osint_tool',  # main.py içindeki 'run_osint_tool' fonksiyonunu çalıştır
        ],
    },
    classifiers=[  # Python projeniz için sınıflandırmalar
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
