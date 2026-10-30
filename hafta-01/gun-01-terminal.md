# Gün 01 — Terminal ve Linux temelleri

Tarih: 30 Ekim 2026

## Ne öğrendim

**Yönlendirme (`>` ve `>>`):**
`echo` kendisine verilen metni ekrana yazdırır. `>` bu çıktıyı ekran yerine dosyaya yönlendirir ve dosyada ne varsa silip üzerine yazar. `>>` ise dosyanın sonuna ekler, eskisini silmez. (Yeni satıra geçmesinin sebebi `>>` değil, `echo`'nun her çıktının sonuna satır sonu koyması.)

**Dosya izinleri (`-rwxr-xr-x`):**
İlk karakter dosya türü: `-` dosya, `d` klasör. Sonra üç üçlü gelir: `rwx` dosyanın sahibi (kullanıcı), `r-x` dosyanın grubu, `r-x` diğer herkes. `r` okuma, `w` yazma, `x` çalıştırma izni. `chmod +x` çalıştırma iznini verir, `chmod -x` geri alır. `x` yokken `./merhaba.sh` "Permission denied" verdi çünkü sistem çalıştırmadan önce `x` iznine bakıyor.

**Pipe (`|`):**
Soldaki komutun çıktısı, sağdaki komutun girdisi olur. `cat liste.txt | grep "Linux" | wc -l` zincirinde: `cat` dosyadaki bütün satırları verdi, `grep` sadece "Linux" geçen 4 satırı geçirdi, `wc -l` kalan satırları saydı ve 4 yazdı. Aynı sonucu tek komutla almak için: `grep -c "Linux" liste.txt`.

**grep:**
Dosyada verilen ifadeyi arar ve o ifadenin geçtiği satırları gösterir. Varsayılan olarak büyük-küçük harfe duyarlıdır. `-i` (ignore case) harf ayrımını kaldırır, `-c` (count) satırları göstermek yerine kaç satırda geçtiğini sayar.

**sudo ve apt:**
`sudo` (superuser do) komutu yönetici, yani root olarak çalıştırır. `apt` Ubuntu'nun paket yöneticisidir, programları kurar ve sistem klasörlerine (`/usr`, `/etc`) yazar. Bu klasörlerin sahibi root olduğu için `apt install` sudo ister. `~` benim ev klasörüm (`/home/salih`) ve sahibi ben olduğum için `mkdir ~/deneme` sudo istemedi. `touch /etc/deneme.txt` ise hata verdi, çünkü `/etc`'de yazma (`w`) iznim yok. Kısacası sudo ihtiyacı, klasörün kime ait olduğuna bağlı.

## Ne yaptım

Windows'a WSL ile Ubuntu kurdum. `~/deneme` klasöründe `echo`, `>`, `>>`, `cat`, `grep`, pipe, `ls -la`, `nano`, `chmod` ve `mv` komutlarını denedim, `merhaba.sh` adında bir script yazıp çalıştırdım. Terminal kaydı: `kod/gun-01-komutlar.txt`.

## Projede nerede kullanacağım

Şirket sunucusuna ssh ile bağlandığımda arayüz olmayacak, sadece terminal olacak. Dosya okuma, log'larda `grep` ile arama, script çalıştırma ve izin sorunlarını çözme işlerini bu komutlarla yapacağım.

## Anlamadıklarım

- İzinler ve sudo konusu henüz tam oturmadı; sahiplik ile izin arasındaki bağı tekrar etmem lazım.
- ssh'ı denemedim.
