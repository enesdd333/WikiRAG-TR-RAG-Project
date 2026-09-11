# ADR-001: Final Retrieval Mimarisi Olarak Hybrid Search Seçimi

## Durum

Kabul Edildi

## Bağlam

WikiRAG-TR üzerinde geliştirilen RAG sisteminde başlangıçta
dense retrieval kullanılmıştır.

Baseline sistem sonuçları:

- Recall@3: 0.86
- Recall@5: 0.90
- Recall@10: 0.92
- MRR@10: 0.8347

Retrieval performansını geliştirmek amacıyla lexical BM25
arama ile dense retrieval birleştirilmiştir.

## Karar

Final retrieval mimarisi olarak:

Dense Retrieval + BM25 + Reciprocal Rank Fusion (RRF)

kullanılmasına karar verilmiştir.

## Gerekçe

Hybrid sistemin ölçülen sonuçları:

- Recall@3: 0.96
- Recall@5: 1.00
- Recall@10: 1.00
- MRR@10: 0.9200
- nDCG@10: 0.9443

Bu sonuçlar dense baseline sisteminden daha yüksek retrieval
performansı göstermiştir.

## Alternatifler

### Dense Retrieval

Daha basit ve hızlıdır ancak Hybrid Search'e göre daha düşük
Recall ve MRR sonucu vermiştir.

### Cross-Encoder Reranking

Hybrid retrieval sonuçlarına Cross-Encoder reranking
uygulanmıştır.

Sonuç:

- Recall@5: 0.98
- Recall@10: 0.98
- MRR@10: 0.9083

Reranking ek hesaplama maliyetine rağmen Hybrid Search
sonuçlarını geliştirmemiştir.

Bu nedenle final pipeline'a dahil edilmemiştir.

## Sonuçlar

Hybrid Search retrieval doğruluğunu artırmıştır ancak lexical
ve dense retrieval'ın birlikte çalıştırılması nedeniyle
retrieval latency artmıştır.

Buna rağmen retrieval latency generation latency ile
karşılaştırıldığında sistemin ana darboğazı değildir.

Final sistem:

Fixed-size Chunking
→ Dense Retrieval
→ BM25
→ Reciprocal Rank Fusion
→ Top-5 Context
→ Qwen Generation