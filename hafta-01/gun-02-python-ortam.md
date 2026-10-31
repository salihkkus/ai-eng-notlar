# Gün 02 — Python ortamı (venv, pip, uv)

Tarih: 31 Ekim 2026

> Bu not, sözlü anlattığım cevapların düzeltilmiş halidir.

## Ne öğrendim

**Ubuntu neden `pip install`'a izin vermedi?**
Ubuntu'nun sistem Python'unu sistemin kendi araçları da kullanıyor ve onların paketlerini `apt` kuruyor. Ben oraya `pip` ile paket kurarsam apt'nin kurduğu bir paketin üzerine yazıp sistemi bozabilirim. Bu yüzden Ubuntu `externally-managed-environment` hatası verip "sanal ortam aç" diyor.

**Sanal ortam (venv) nedir, neden lazım?**
Her projenin bağımlılıkları ayrı bir kutuda dursun, birbirine karışmasın diye. Bir proje requests 2.28, diğeri 2.32 isterse ikisi aynı makinede ayrı venv'lerde sorunsuz çalışır. venv aynı makinedeki projeleri ayırır; projeyi başka sunucuya taşımak Docker'ın işi.

**`.venv` içinde ne var? `activate` ne değiştirdi?**
`.venv` içinde üç şey var: o ortama ait `python`, o ortama ait `pip` ve kurulan paketler (`lib/.../site-packages`). `source .venv/bin/activate` komutu `PATH`'i değiştirir; artık `python` yazınca sistemdeki değil, `.venv` içindeki çalışır.

```
activate öncesi:  python  →  /usr/bin/python3            (sistem, requests yok)
activate sonrası: python  →  ~/gun02/.venv/bin/python    (requests burada)
```

`which python` hangi Python'un çalıştığını gösterir.

**`deactivate` sonrası script neden çalışmadı?**
Sistem Python'una döndüm. requests sadece `.venv` içine kuruluydu, sistem Python'unda yoktu, bu yüzden `ModuleNotFoundError` aldım.

**`requirements.txt` ne işe yarıyor?**
Projenin çalışması için gereken paketleri tam sürümleriyle listeler (`pip freeze > requirements.txt`). Proje klasöründe durur, `.venv` içinde değil. `.venv`'i silip `pip install -r requirements.txt` ile aynı ortamı yeniden kurdum.

**uv ne farklı yapıyor?**
uv, venv ve pip'in işini tek araçta, çok daha hızlı yapan modern bir araç; `.venv`'i de kendisi açıyor. İki dosya kullanıyor:
- `pyproject.toml`: **ne istediğimi** yazar ("requests lazım").
- `uv.lock`: **tam olarak ne kurulduğunu** yazar; requests'in kendi bağımlılıkları dahil her şeyin kesin sürümü.

requirements.txt bu ikisini tek dosyada karıştırıyor.

**`.venv` neden git'e girmez?**
Asıl sebep: `.venv` benim makineme özel, içinde benim bilgisayarımdaki yollar var, başka bilgisayarda çalışmaz. Zaten requirements.txt'ten saniyeler içinde yeniden kurulabiliyor. Yer kaplaması ikinci sebep. Repodaki `.gitignore`'da `.venv` satırı bunu sağlıyor.

## Ne yaptım

WSL'de sistem pip'inin hatasını gördüm, `~/gun02` içinde venv kurup requests yükledim ve GitHub API'den repo sayımı çeken bir script çalıştırdım. Ortamı silip requirements.txt'ten yeniden kurdum, sonra aynı işi uv ile yaptım. Kod: `kod/gun-02/`.

## Projede nerede kullanacağım

Model servisi, RAG ve API ayrı ortamlarda çalışacak; sunucuya kurulurken Docker image'ı requirements.txt veya uv.lock üzerinden oluşturulacak.

## Anlamadıklarım

- Terminal komutlarının çokluğu kafamı karıştırıyor.
