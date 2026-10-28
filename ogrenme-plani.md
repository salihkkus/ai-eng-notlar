# Sıfırdan AI Engineer Öğrenme Planı

Başlangıç: 28 Ekim 2026

## Planın mantığı

12 hafta, haftada 5 iş günü, günde 1–2 saat. Her gün tek bir konu: önce kavramı anla (video/okuma, ~40 dk), sonra elinle bir şey yap (~40 dk), sonra 3–5 cümle not al. Notlar birikince Ferat Bey'e anlatacağın dili de hazır olmuş olur.

Sıra, Real Cam projesinin ihtiyacına göre dizildi: önce araçlar, sonra LLM'in ne olduğu, sonra lokalde model çalıştırma, sonra RAG (projenin kalbi), sonra API/agent katmanı, en sonda fine-tuning. Fine-tuning sona bırakıldı çünkü iyi bir RAG çoğu şirket asistanı ihtiyacını karşılar ve fine-tuning'e gerçekten gerekip gerekmediği ancak RAG denendikten sonra belli olur.

Kurallar:

- Bir günü bitirmeden sonrakine geçme; bir konu uzarsa ertesi güne sarkabilir, plan esnektir.
- Her gün en az bir satır kod yaz veya bir komut çalıştır. Sadece izleme{ yetmez.
- Her hafta sonu (Cuma) o haftanın notlarını 10 satırda özetle; bu özetler Ferat Bey'e ilerleme raporu olarak kullanılabilir.
- Takıldığın her şeyi bana sor; ben de kodda bir değişiklik yaptığımda hangi haftanın konusuna girdiğini söylerim.

| Hafta | Faz | Hedef |
| --- | --- | --- |
| 1 | Faz 0 | Python, Git, terminal, Docker ile rahat çalışmak |
| 2–3 | Faz 1 | LLM'in nasıl çalıştığını ve temel terimleri kavramak |
| 4–5 | Faz 2 | Açık kaynak bir modeli şirket sunucusunda çalıştırabilmek |
| 6–7 | Faz 3 | Şirket dokümanlarıyla çalışan basit bir RAG kurmak |
| 8–9 | Faz 4 | Bunu bir API ve araç kullanan asistana dönüştürmek |
| 10–11 | Faz 5 | Fine-tuning'in ne olduğunu ve ne zaman gerektiğini bilmek |
| 12 | Faz 6 | Güvenlik, deployment ve kalite ölçümü |

## Faz 0 — Temel araçlar (Hafta 1)

Hedef: proje boyunca her gün kullanacağın araçlarda hiç duraksamamak. Python'u biliyorsan hızlı geçersin; bilmediğin yerde durup tamamla.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 1 | Terminal ve Linux temelleri | cd, ls, cat, grep, pipe, chmod, ssh, nano/vim. Şirket sunucusuna ssh ile bağlan, bir dosya oluştur, düzenle, sil. |
| 2 | Python ortamı | venv veya uv ile sanal ortam kur; pip, requirements.txt, pyproject.toml ne işe yarar. Bir paket kur, bir script çalıştır. |
| 3 | Python'da sık kullanacakların | Tip ipuçları (type hints), dataclass, async/await temel mantığı, with/context manager, json okuma-yazma, requests ile bir API'ye istek atma. |
| 4 | Git ve GitHub | clone, branch, commit, push, pull request, .gitignore. Proje için bir repo aç, ilk commit'i at, bir branch'te değişiklik yapıp merge et. |
| 5 | Docker | Image vs container, Dockerfile, docker compose, volume, port mapping. Basit bir Python uygulamasını Docker'da çalıştır. On-prem deployment'ta her şey Docker'la gidecek. |

Haftanın sonunda yapabilmen gereken: sunucuya ssh ile girip, git'ten bir repo çekip, Docker ile ayağa kaldırmak.

## Faz 1 — LLM temelleri (Hafta 2–3)

Hedef: bir LLM'in içinde ne olduğunu, hangi ayarın neyi değiştirdiğini ve terimleri duyunca ne kastedildiğini anlamak. Matematiğin derinine inmek gerekmiyor; kavramsal netlik yeter.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 6 | ML ve derin öğrenmeye kuşbakışı | Supervised/unsupervised, eğitim vs çıkarım (training vs inference), model ağırlığı, parametre ne demek. 3Blue1Brown'un neural network serisinin ilk iki videosu. |
| 7 | Token ve tokenizer | Token nedir, neden kelime değildir, Türkçe metin neden daha çok token yer. OpenAI tokenizer veya tiktoken ile birkaç Türkçe cümleyi tokenlara ayır. |
| 8 | Transformer ve attention | Kavramsal düzeyde: attention "hangi kelime hangisine bakıyor". 3Blue1Brown'un transformer/attention videoları. Andrej Karpathy'nin "Intro to LLMs" konuşması. |
| 9 | Context window ve bellek | Context window nedir, neden sınırlı, modelin "hafızası" aslında ne. Uzun bir metni bir modele verip sınırı aşınca ne olduğunu gör. |
| 10 | Üretim parametreleri | temperature, top_p, max_tokens, stop sequence, seed. Aynı prompt'u farklı temperature'larla 5 kez çalıştır, farkı gözle. |
| 11 | Model türleri | Base vs instruct/chat modeli, parametre sayısı (7B, 70B) ne anlama gelir, model kartı nasıl okunur. Hugging Face'te 3 modelin kartını oku. |
| 12 | Prompt engineering temelleri | System prompt, few-shot örnek, rol verme, adım adım düşündürme, çıktıyı JSON istemek. Aynı görev için 3 farklı prompt yaz, sonuçları karşılaştır. |
| 13 | Chat formatı ve mesaj yapısı | system/user/assistant rolleri, chat template, konuşma geçmişi nasıl gönderilir. Bir modele 5 mesajlık bir konuşmayı elle gönder. |
| 14 | LLM'in zayıf noktaları | Halüsinasyon, bilgi kesim tarihi, aritmetik, uzun belge içinde kaybolma. Bu zayıflıkların her birini kendin tetikle ve not al; RAG'in neden gerektiğini burada anlayacaksın. |
| 15 | Embedding kavramı | Metnin sayı vektörüne dönüşmesi, benzerlik (cosine similarity). sentence-transformers ile 10 cümleyi embed et, en benzer ikisini bul. |

Haftanın sonunda yapabilmen gereken: Ferat Bey'e "model nedir, context window nedir, neden halüsinasyon görür" sorularını 2'şer cümleyle açıklamak.

## Faz 2 — Açık kaynak LLM'leri lokalde çalıştırma (Hafta 4–5)

Hedef: bulut olmadan, şirket sunucusunda bir modeli çalıştırıp ona API üzerinden istek atabilmek. Bu faz projenin ilk somut çıktısı olacak.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 16 | Donanım: GPU, VRAM, CPU | Modelin kaç GB VRAM istediği nasıl hesaplanır (parametre × hassasiyet), CPU'da çalıştırmanın maliyeti. nvidia-smi çıktısını okumayı öğren. Şirket sunucusunun GPU'sunu ve VRAM'ini not et. |
| 17 | Ollama ile ilk model | Ollama kur, 7–8B bir model çek (ör. Llama 3.x veya Qwen), terminalden konuş, sonra REST API'sine curl ile istek at. |
| 18 | Quantization | FP16, INT8, Q4 ne demek; GGUF formatı; kalite/hız/bellek dengesi. Aynı modelin Q4 ve Q8 halini çalıştırıp hız ve cevap kalitesini karşılaştır. |
| 19 | Hugging Face ekosistemi | Hub, model kartı, lisanslar (ticari kullanıma uygun mu?), transformers kütüphanesi. Bir modeli huggingface-cli ile indir. |
| 20 | Türkçe performansı | Hangi açık modeller Türkçede iyi; aynı Türkçe soruyu 3 modele sor, karşılaştır. Lisans + Türkçe kalitesi + VRAM üçlüsüne göre proje için 2 aday seç. |
| 21 | vLLM ve üretim sunucuları | Ollama (kolay) vs vLLM (hızlı, çok kullanıcılı) vs llama.cpp (CPU). Hangisi ne zaman. vLLM'i Docker'da ayağa kaldır. |
| 22 | OpenAI-uyumlu API | Çoğu lokal sunucu OpenAI API formatını taklit eder; bu sayede kod değişmeden model değişir. Python openai kütüphanesiyle lokal modele bağlan. |
| 23 | Streaming ve performans ölçümü | Token streaming, tokens/sec, ilk token gecikmesi, aynı anda kaç istek. Basit bir benchmark scripti yaz. |
| 24 | Prompt caching ve batching | KV cache nedir, system prompt tekrarının maliyeti, batch istek. vLLM'de bunların nasıl açıldığına bak. |
| 25 | Haftalık toparlama | Seçtiğin 2 aday modeli Docker compose ile kalıcı şekilde kur; bir sayfalık "model seçimi" notu yaz (Ferat Bey'e sunulabilir). |

Haftanın sonunda yapabilmen gereken: şirket sunucusunda sürekli çalışan bir model servisi ve ona Python'dan istek atan bir script.

## Faz 3 — RAG: şirket bilgisiyle konuşan asistan (Hafta 6–7)

Hedef: "şirketin projelerini bilen asistan" tam olarak RAG demek. Modeli eğitmeden, doğru dokümanı bulup prompt'a eklemek. Bu iki hafta projenin çekirdeğini kurar.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 26 | RAG nedir, neden | Retrieval-Augmented Generation'ın adımları: doküman → parçala → embed → sakla → soru gelince en yakınları bul → prompt'a ekle → cevapla. Akışı kendi cümlelerinle bir sayfaya çiz. |
| 27 | Doküman okuma | PDF, Word, Excel, e-posta, tarama (OCR) dosyalarından metin çıkarma. Şirketten 5 örnek dosya al, hepsinden metin çıkar; nerede bozuluyor not et. |
| 28 | Chunking | Parça boyutu, örtüşme (overlap), başlığa göre bölme. Aynı dokümanı 3 farklı chunk ayarıyla böl, hangisi daha anlamlı bak. |
| 29 | Embedding modeli seçimi | Çok dilli embedding modelleri (Türkçe destekli olanlar), boyut, hız. 2 modeli aynı Türkçe sorularda karşılaştır. |
| 30 | Vektör veritabanı | Chroma, Qdrant, pgvector farkları. Qdrant'ı Docker'da kur, chunk'ları yükle, bir soru ile arama yap. |
| 31 | İlk uçtan uca RAG | Soru → arama → prompt → lokal model → cevap. 50 satırlık bir script yaz, şirket dokümanlarıyla çalıştır. |
| 32 | Hybrid search ve reranking | Sadece vektör yetmez; BM25 anahtar kelime araması + vektör birleşimi, reranker modeli. Birini ekle, cevap kalitesine etkisini gör. |
| 33 | Metadata ve filtreleme | Dosya adı, tarih, proje adı, departman gibi bilgileri chunk'a eklemek; "sadece X projesine bak" filtresi. |
| 34 | Kaynak gösterme ve halüsinasyonu azaltma | Cevabın hangi dokümandan geldiğini göstermek; "bilmiyorsan uydurma" talimatı; context boşsa ne yapmalı. |
| 35 | RAG değerlendirme | 20 soru-cevap çiftlik bir test seti yaz; retrieval isabeti ve cevap doğruluğunu elle puanla. Ragas gibi araçlara göz at. |

Haftanın sonunda yapabilmen gereken: şirket dokümanları hakkında soru sorulunca kaynağını göstererek cevaplayan, Docker'da çalışan bir RAG prototipi.

## Faz 4 — Uygulama katmanı: API, araçlar, agent (Hafta 8–9)

Hedef: RAG scriptini başkalarının kullanabileceği bir servise çevirmek ve asistana "iş yaptırmayı" öğrenmek.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 36 | FastAPI | Endpoint, request/response modeli (Pydantic), async. RAG'ı /ask endpoint'i olarak sun. |
| 37 | Konuşma geçmişi ve oturum | Çok turlu sohbet, geçmişi saklama (Redis veya Postgres), context window dolunca özetleme. |
| 38 | Structured output | Modelden JSON/şema istemek, Pydantic ile doğrulamak, bozuksa tekrar istemek. Bir sipariş/teklif bilgisini JSON'a çıkaran prompt yaz. |
| 39 | Function calling / tool use | Modele araç tanımlamak (ör. "proje durumunu sorgula", "ölçü hesapla"), modelin aracı çağırması, sonucun geri verilmesi. Bir araç tanımla, çalıştır. |
| 40 | Agent döngüsü | Plan → araç çağır → sonucu oku → devam et. Basit bir ReAct döngüsü yaz; nerede sonsuz döngüye giriyor gör. |
| 41 | Framework'ler | LangChain, LlamaIndex, Haystack ne sunar, ne zaman gereksiz. Birini 1 saat dene; kendi 50 satırlık kodunla kıyasla. |
| 42 | MCP (Model Context Protocol) | Araçları standart biçimde sunma protokolü. Basit bir MCP sunucusu yaz, Claude Code'dan bağlan. |
| 43 | Basit arayüz | Streamlit veya Gradio ile sohbet arayüzü; ya da Open WebUI'ı kendi API'na bağla. Ferat Bey'in deneyebileceği bir ekran çıkar. |
| 44 | Loglama ve izleme | Her isteğin prompt'u, cevabı, süresi, retrieval sonuçları loglansın. Langfuse veya basit bir veritabanı tablosu. |
| 45 | Haftalık toparlama | Tümünü docker compose'da birleştir (model + vektör DB + API + arayüz). Mimari şemasını çiz. |

Haftanın sonunda yapabilmen gereken: tek komutla ayağa kalkan, arayüzü olan, araç çağırabilen bir asistan ve onun mimari şeması.

## Faz 5 — Fine-tuning (Hafta 10–11)

Hedef: iş ilanında geçen "şirket verisiyle fine-tune" işini doğru yerde kullanmak. Fine-tuning bilgi öğretmek için değil, üslup, format ve alan diline alıştırmak içindir; bilgi RAG'dan gelir. Bunu Ferat Bey'e net anlatabilmen önemli.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 46 | Ne zaman fine-tune, ne zaman RAG | Karar ağacı: bilgi mi değişiyor (RAG), davranış mı (fine-tune)? Projedeki 5 ihtiyacı bu ağaçtan geçir. |
| 47 | Pretraining, SFT, RLHF/DPO | Bir modelin nasıl eğitildiği: ham metin → talimat verisi → tercih verisi. Kavramsal. |
| 48 | LoRA ve QLoRA | Tüm ağırlıkları değil küçük bir ek katmanı eğitmek; neden tek GPU'da mümkün. Rank, alpha, hangi katmanlara uygulanır. |
| 49 | Veri seti hazırlama | Talimat-cevap çiftleri, JSONL formatı, kalite > miktar, kişisel veri temizliği. Şirket yazışmalarından 50 örneklik küçük bir set hazırla (anonimleştirerek). |
| 50 | İlk fine-tune | Unsloth veya Hugging Face TRL ile küçük bir modeli (1–3B) LoRA ile eğit. Loss eğrisini oku. |
| 51 | Eğitim parametreleri | learning rate, epoch, batch size, overfitting belirtileri. Bir parametreyi değiştirip sonucu gör. |
| 52 | Değerlendirme | Eğitim öncesi/sonrası aynı 20 soruyu sor, kör karşılaştırma yap. Sayı olmadan "iyi oldu" deme. |
| 53 | Merge ve dağıtım | LoRA adaptörünü ana modelle birleştirme, GGUF'a çevirme, Ollama/vLLM'de çalıştırma. |
| 54 | Embedding modelini fine-tune etmek | Şirket terimleriyle (cam balkon, profil, sürgülü sistem vb.) retrieval'ı iyileştirmek; çoğu zaman LLM fine-tune'dan daha değerli. |
| 55 | Haftalık toparlama | Bir sayfalık "fine-tuning ne zaman gerekir" notu + deney sonuçları. Ferat Bey'e sunulabilir. |

Haftanın sonunda yapabilmen gereken: küçük bir modeli kendin eğitip, kazanç sağladı mı sağlamadı mı sayıyla göstermek.

## Faz 6 — Güvenlik, deployment, kalite (Hafta 12)

Hedef: on-prem olmanın asıl nedeni veri güvenliği; bunu teknik olarak sağlamak ve sistemi sürekli ölçmek.

| Gün | Konu | Bugün yap |
| --- | --- | --- |
| 56 | Erişim ve kimlik | API anahtarı, kullanıcı girişi, rol bazlı erişim (muhasebe dokümanını herkes göremesin). Basit bir yetki katmanı ekle. |
| 57 | Prompt injection ve kötüye kullanım | Dokümanın içine gizlenmiş talimatlar, sistem prompt'unu sızdırma. 5 saldırı denemesi yap, savunma ekle. |
| 58 | Kişisel veri ve KVKK | Loglarda ve eğitim verisinde kişisel veri; maskeleme; verinin sunucudan hiç çıkmadığını kanıtlama (dış ağ erişimi kapalı). |
| 59 | Sürekli değerlendirme | Test setini otomatik koş, her değişiklikte puan al; regresyon yakala. Kullanıcı geri bildirimi (beğendim/beğenmedim) topla. |
| 60 | Operasyon | Yedekleme, model güncelleme süreci, sunucu izleme, hata olunca ne olur. Bir sayfalık "işletme kılavuzu" yaz. |

Haftanın sonunda: sistemin tamamını, güvenlik gerekçeleriyle birlikte, Ferat Bey'e 15 dakikada anlatabilmek.

## Günlük rutin ve Ferat Bey'e raporlama

Günlük (1–2 saat):

1. 10 dk: dünkü notu oku, bugünün konusunu planın tablosundan al.
2. 30–40 dk: kavramı öğren (video, doküman, bana sorarak).
3. 30–40 dk: elinle yap (kod, komut, deney). Çalışmazsa bana getir.
4. 10 dk: 3–5 cümle not: ne öğrendim, projede nerede kullanacağım, ne anlamadım.

Haftalık (Cuma):

- Haftanın notlarını 10 satırda özetle.
- O hafta ortaya çıkan somut şeyi (script, servis, karşılaştırma notu) kaydet.
- Ferat Bey'e kısa bir ilerleme mesajı: ne öğrendim, projede ne ilerledi, gelecek hafta ne var. Böylece "yavaş ve dikkatli" ilerleme isteği de görünür olur.

Notlar bu repoda (ai-eng-notlar) tutulur: her gün bir `hafta-XX/gun-YY-konu.md`, her Cuma `haftalik-ozet/hafta-XX.md`, kod `kod/` altında. Şirkete ait doküman, müşteri bilgisi, sunucu adresi bu repoya girmez; öğrenme egzersizleri kendi uydurduğun veya herkese açık verilerle yapılır, aynı egzersiz şirket verisiyle proje reposunda tekrarlanır.

## Kaynaklar

Çoğu ücretsiz ve İngilizce; Türkçe karşılığı zayıf olan konularda İngilizce altyazıyla ilerle. Adresler bellekten, bugün tek tek doğrulanmadı; biri açılmazsa adını arat.

| Faz | Kaynak | Ne için |
| --- | --- | --- |
| 0 | Docker resmi "Get started" rehberi (docs.docker.com) | Gün 5 |
| 0 | Pro Git kitabı (git-scm.com/book), ilk 3 bölüm | Gün 4 |
| 1 | 3Blue1Brown — Neural networks serisi (YouTube) | Gün 6, 8 |
| 1 | Andrej Karpathy — "Intro to Large Language Models" (YouTube) | Gün 8 |
| 1 | Hugging Face LLM Course (huggingface.co/learn) | Gün 7–15 boyunca |
| 1 | Anthropic prompt engineering dokümanları (docs.claude.com) | Gün 12 |
| 2 | Ollama dokümanları (ollama.com) | Gün 17 |
| 2 | vLLM dokümanları (docs.vllm.ai) | Gün 21–24 |
| 2 | Hugging Face model kartları ve lisans sayfaları | Gün 19–20 |
| 3 | Qdrant dokümanları (qdrant.tech) | Gün 30 |
| 3 | sentence-transformers dokümanları (sbert.net) | Gün 15, 29 |
| 4 | FastAPI dokümanları (fastapi.tiangolo.com) | Gün 36 |
| 4 | MCP tanıtım sayfası (modelcontextprotocol.io) | Gün 42 |
| 5 | Unsloth dokümanları ve örnek notebook'ları | Gün 50 |
| 5 | Hugging Face TRL dokümanları | Gün 50–53 |
| 6 | OWASP Top 10 for LLM Applications | Gün 57 |

Her gün için daha spesifik bir kaynak istersen o günün konusunu söyle, arayıp güncel ve iyi olanı bulurum.
