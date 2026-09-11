# WikiRAG-TR RAG Sistem Mimarisi

## 1. Genel Bakış

Bu proje WikiRAG-TR veri seti üzerinde Türkçe bir
Retrieval-Augmented Generation (RAG) sistemi geliştirmektedir.

Sistem retrieval ve generation katmanlarını birbirinden ayrı
değerlendirecek şekilde tasarlanmıştır.

## 2. Sistem Akışı

Kullanıcı Sorusu
↓
Query Processing
↓
Dense Retrieval + BM25
↓
Reciprocal Rank Fusion (RRF)
↓
Top-5 Doküman
↓
Context Oluşturma
↓
Kaynak Temelli Prompt
↓
Qwen2.5-1.5B-Instruct
↓
Kaynak Temelli Cevap

## 3. Retrieval Katmanı

Dense retrieval için:

- sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
- FAISS

Lexical retrieval için:

- BM25
- rank_bm25

Final retrieval sisteminde Dense ve BM25 sonuçları
Reciprocal Rank Fusion (RRF) ile birleştirilmektedir.

## 4. Chunking

Projede üç farklı chunking yaklaşımı test edilmiştir:

1. Fixed-size chunking
2. Recursive chunking
3. Parent-Child chunking

Deney sonuçlarına göre final sistemde fixed-size chunking
kullanılmıştır.

## 5. Advanced RAG Teknikleri

Projede aşağıdaki teknikler uygulanmıştır:

- Hybrid Search (Dense + BM25 + RRF)
- Cross-Encoder Reranking
- Parent-Document Retrieval
- Query Decomposition

Her teknik retrieval performansı üzerindeki etkisi açısından
deneysel olarak incelenmiştir.

## 6. Generation

Generation modeli:

Qwen/Qwen2.5-1.5B-Instruct

Model yalnızca retrieval sonucunda elde edilen kaynakları
kullanarak cevap üretmeye yönlendirilmiştir.

Kaynaklarda yeterli bilgi bulunmadığında sistemin cevap
vermekten kaçınması hedeflenmiştir.

## 7. Observability

RAG pipeline gözlemlenebilirliği için Arize Phoenix
kullanılmıştır.

Hybrid retrieval işlemleri OpenTelemetry trace olarak
Phoenix'e gönderilmiştir.

Trace içerisinde:

- Kullanıcı sorusu
- Retrieval yöntemi
- Top-k
- Retrieval latency
- Getirilen document ID'leri

kaydedilmektedir.

## 8. Production Sınırlamaları

Retrieval katmanı düşük gecikmeyle çalışmasına rağmen
generation katmanı önemli bir latency darboğazıdır.

Ölçülen değerler:

- Hybrid Retrieval P50: 0.1727 saniye
- Hybrid Retrieval P95: 0.5877 saniye
- Generation P50: 257.9184 saniye
- Generation P95: 308.08 saniye

Bu nedenle mevcut sistem ödev senaryosundaki 5 saniyelik
production latency hedefini karşılamamaktadır.

Daha hızlı bir generation modeli, quantization, inference
optimizasyonu veya uygun GPU altyapısı production ortamında
değerlendirilmelidir.