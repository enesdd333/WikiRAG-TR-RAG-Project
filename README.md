# WikiRAG-TR – Türkçe RAG Sistemi

Bu proje, WikiRAG-TR veri seti üzerinde Türkçe bir Retrieval-Augmented Generation (RAG) sistemi geliştirmek ve farklı retrieval yaklaşımlarını deneysel olarak karşılaştırmak amacıyla hazırlanmıştır.

## Proje Özeti

Sistem temel olarak şu aşamalardan oluşmaktadır:

1. WikiRAG-TR veri setinin hazırlanması
2. Dokümanların chunk'lara ayrılması
3. Dense Retrieval
4. BM25 Retrieval
5. Hybrid Retrieval (Dense + BM25)
6. RRF (Reciprocal Rank Fusion)
7. Cross-Encoder Reranking
8. Farklı chunking stratejilerinin karşılaştırılması
9. Parent-Child Retrieval
10. Query Decomposition
11. Answerability / Abstention analizi
12. RAG Generation
13. Retrieval ve Generation Evaluation
14. Latency, maliyet ve hata analizi
15. Prompt Injection / Guardrail testi
16. Observability / Trace analizi

## Kullanılan Teknolojiler

- Python
- Hugging Face Transformers
- Sentence Transformers
- FAISS
- BM25 (`rank_bm25`)
- Qwen2.5-1.5B-Instruct
- Google Colab

Embedding modeli:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

Generation modeli:

`Qwen/Qwen2.5-1.5B-Instruct`

## Retrieval Sonuçları

### V0 – Dense Retrieval

| Metrik | Sonuç |
|---|---:|
| Recall@3 | 0.8600 |
| Recall@5 | 0.9000 |
| Recall@10 | 0.9200 |
| MRR@10 | 0.8347 |

### V1 – Hybrid Retrieval

Dense Retrieval ve BM25 sonuçları Reciprocal Rank Fusion (RRF) ile birleştirilmiştir.

| Metrik | Sonuç |
|---|---:|
| Recall@3 | 0.9600 |
| Recall@5 | 1.0000 |
| Recall@10 | 1.0000 |
| MRR@10 | 0.9200 |

### V2 – Hybrid + Cross-Encoder Reranker

| Metrik | Sonuç |
|---|---:|
| Recall@3 | 0.9600 |
| Recall@5 | 0.9800 |
| Recall@10 | 0.9800 |
| MRR@10 | 0.9083 |

Deneylerde en yüksek genel retrieval performansı V1 Hybrid sisteminde elde edilmiştir.

## Chunking Deneyleri

Fixed-size, Recursive ve Parent-Child chunking yaklaşımları karşılaştırılmıştır.

Recursive Dense Retrieval:

| Metrik | Sonuç |
|---|---:|
| Recall@3 | 0.8600 |
| Recall@5 | 0.8600 |
| Recall@10 | 0.9200 |
| MRR@10 | 0.8358 |

Parent-Child Dense Retrieval:

| Metrik | Sonuç |
|---|---:|
| Recall@3 | 0.8200 |
| Recall@5 | 0.8600 |
| Recall@10 | 0.8600 |
| MRR@10 | 0.7290 |

## Context Evaluation

| Metrik | Sonuç |
|---|---:|
| Context Recall | 1.0000 |
| Context Precision | 0.3200 |

Yüksek Context Recall, gerekli dokümanların retrieval sistemi tarafından bulunabildiğini göstermektedir. Düşük Context Precision ise getirilen bağlam içerisinde ilgisiz içeriklerin de bulunduğunu göstermektedir.

## Generation Evaluation

| Metrik | Sonuç |
|---|---:|
| Faithfulness | 0.4650 |
| Answer Correctness | 0.4220 |
| Answer Relevancy | 0.21 |

Retrieval performansı yüksek olmasına rağmen generation katmanının daha zayıf olduğu görülmüştür.

## Latency

Dense ve Hybrid retrieval için ölçülen ortalama süreler:

| Sistem | Ortalama |
|---|---:|
| Dense | 0.0409 saniye |
| Hybrid | 0.0780 saniye |
| Dense P95 | 0.0483 saniye |
| Hybrid P95 | 0.1051 saniye |

Tek bir uçtan uca RAG trace deneyinde retrieval yaklaşık 0.1538 saniye, yerel LLM generation ise yaklaşık 401.84 saniye sürmüştür. Bu nedenle uçtan uca sistemin temel latency darboğazı generation katmanıdır.

## Answerability ve Abstention

Cevaplanamaz sorular üzerinde sistemin cevap vermekten kaçınma davranışı ayrıca değerlendirilmiştir.

İlk deneyde:

- Doğru abstention: 7/10
- Yanlış cevap: 3/10
- Abstention Rate: 0.70
- False Answer Rate: 0.30

Threshold tabanlı deneylerde `0.72` threshold değeri ayrıca test edilmiştir.

## Prompt Injection / Guardrail

Kaynaklar arasına kötü niyetli talimatlar içeren yapay bir doküman eklenerek prompt injection testi gerçekleştirilmiştir.

Model, kaynak içerisindeki "önceki talimatları yoksay" benzeri komutları uygulamamış ve sistem talimatlarını açıklamamıştır. Bununla birlikte cevap relevancy problemi devam etmiştir.

Bu deney güvenlik başarısı ile cevap kalitesinin birbirinden ayrı değerlendirilmesi gerektiğini göstermiştir.

## Maliyet

Projede açık kaynak ve yerel modeller kullanıldığı için doğrudan API maliyeti bulunmamaktadır.

1.000 sorgu için tahmini doğrudan API maliyeti:

**0 USD**

Gerçek bir production ortamında GPU/CPU, depolama ve operasyon maliyetleri ayrıca değerlendirilmelidir.

## Temel Bulgular

Deneyler sonucunda:

- Hybrid Retrieval, Dense Retrieval'a göre daha yüksek retrieval başarısı sağlamıştır.
- Reranking her metrikte Hybrid Retrieval'ı geliştirmemiştir.
- Chunking stratejisinin retrieval performansını önemli ölçüde etkilediği görülmüştür.
- Retrieval başarısının yüksek olması tek başına kaliteli cevap üretimini garanti etmemektedir.
- Generation katmanı sistemin en önemli kalite ve latency darboğazlarından biri olmuştur.
- Prompt injection guardrail saldırı talimatının uygulanmasını engellemiştir.

## Proje Yapısı

```text
WikiRAG-TR-RAG-Project/
├── notebook/
│   └── rag_project.ipynb
├── report/
│   └── report.pdf
├── README.md
└── requirements.txt
## Demo

Proje için Gradio tabanlı basit bir kullanıcı arayüzü geliştirilmiştir.

Demo akışı:

1. Kullanıcı Türkçe bir soru girer.
2. Dense Retrieval ve BM25 ile aday dokümanlar getirilir.
3. Sonuçlar Reciprocal Rank Fusion (RRF) ile birleştirilir.
4. İlk 5 kaynak Qwen2.5-1.5B-Instruct modeline context olarak verilir.
5. Model, verilen kaynaklara dayanarak cevap üretir.
6. Arayüzde hem üretilen cevap hem de retrieval sonucunda getirilen kaynaklar gösterilir.

Demo Gradio ile notebook içerisinde çalıştırılabilir.

### Demo Notu

Demo testinde retrieval sistemi Bermuda sorusu için doğru dokümanı (`doc_id: 3`) ilk sırada getirmiştir. Buna rağmen generation modeli kaynaktaki "Birleşik Krallık" bilgisini yanlış yorumlayarak hatalı cevap üretmiştir.

Bu örnek, projenin evaluation sonuçlarıyla uyumludur: retrieval katmanı güçlü performans gösterirken generation katmanı sistemin temel darboğazıdır.
## Dataset ve Lisans

Bu projede ana veri kaynağı olarak WikiRAG-TR veri seti kullanılmıştır.

Ham veri dosyaları repository içerisinde tutulmamaktadır. Veri setinin
yeniden elde edilmesi için proje kapsamında veri indirme/yükleme adımı
ayrı olarak tanımlanmaktadır.

Ana deney corpus'u 5.723 benzersiz WikiRAG-TR dokümanından oluşmaktadır.

Ayrıca sistemin çoklu veri formatı ingestion desteğini göstermek amacıyla
Markdown (.md) formatında ek bir dokümanla ingestion testi yapılmıştır.
Bu ek doküman ana benchmark sonuçlarına dahil edilmemiştir.

Veri setinin kullanım ve lisans koşulları için WikiRAG-TR veri setinin
orijinal dağıtım sayfasındaki lisans bilgileri esas alınmalıdır.