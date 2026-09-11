# ADR-003: Cross-Encoder Reranking Kararı

## Durum

Baseline Dense Retrieval sisteminin ardından retrieval performansını geliştirmek amacıyla Hybrid Search uygulanmıştır.

Hybrid sistemde Dense Retrieval ve BM25 sonuçları Reciprocal Rank Fusion (RRF) yöntemi ile birleştirilmiştir.

Bunun üzerine retrieval sonuçlarının sıralamasını daha da iyileştirmek amacıyla Cross-Encoder Reranking yöntemi test edilmiştir.

## Karar

Cross-Encoder Reranking yöntemi deneysel olarak uygulanmış ancak final RAG pipeline'ına dahil edilmemiştir.

Final retrieval sistemi olarak **Dense + BM25 + RRF Hybrid Search** kullanılmıştır.

## Gerekçe

Deney sonuçlarında Hybrid Search güçlü retrieval performansı sağlamıştır.

Hybrid Search sonuçları:

- Recall@3: 0.96
- Recall@5: 1.00
- Recall@10: 1.00
- MRR@10: 0.9200
- nDCG@10: 0.9443

Cross-Encoder Reranking eklendiğinde ise:

- Recall@3: 0.96
- Recall@5: 0.98
- Recall@10: 0.98
- MRR@10: 0.9083

Reranking katmanı beklenen performans artışını sağlamamış ve bazı retrieval metriklerinde küçük bir düşüş oluşturmuştur.

## Alternatifler

### Hybrid Search

Dense Retrieval semantik benzerliği, BM25 ise kelime tabanlı eşleşmeleri yakalamaktadır. RRF ile iki yöntemin sonuçlarının birleştirilmesi projede en başarılı retrieval yaklaşımını oluşturmuştur.

### Cross-Encoder Reranking

İlk retrieval sonuçlarının daha güçlü bir model ile yeniden sıralanması amaçlanmıştır. Ancak bu proje kapsamında ek karmaşıklığa rağmen ölçülebilir bir performans artışı sağlamamıştır.

## Sonuç

Final sistemde Cross-Encoder Reranking kullanılmamıştır.

Bu deney negatif sonuç olarak korunmuştur. Böylece final mimari yalnızca teorik olarak daha gelişmiş olan yönteme göre değil, ölçülen retrieval performansına göre seçilmiştir.
