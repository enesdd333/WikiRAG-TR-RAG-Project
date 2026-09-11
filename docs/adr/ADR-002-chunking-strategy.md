# ADR-002: Chunking Stratejisinin Seçilmesi

## Durum

RAG sisteminde dokümanların nasıl parçalara ayrıldığı retrieval performansını doğrudan etkilemektedir. Bu nedenle projede birden fazla chunking yaklaşımı karşılaştırılmıştır.

Test edilen stratejiler:

- Fixed-size chunking
- Recursive Character Text Splitter
- Parent-Child / Parent-Document yaklaşımı

## Karar

Final sistemde **Fixed-size chunking** kullanılmasına karar verilmiştir.

## Gerekçe

Deneylerde Fixed-size chunking daha dengeli retrieval performansı göstermiştir.

Recall@5 sonuçları:

- Fixed-size: 0.90
- Recursive: 0.86
- Parent-Child: 0.86

Fixed-size yaklaşımı ayrıca daha basit ve yeniden üretilebilir bir yapı sağlamaktadır.

## Alternatifler

### Recursive Chunking

Metin yapısını korumada avantajlı olmasına rağmen bu projede Fixed-size yaklaşımından daha yüksek retrieval performansı sağlamamıştır.

### Parent-Child Retrieval

Küçük child chunk'lar üzerinden retrieval yapıp daha büyük parent dokümanları bağlam olarak kullanmayı amaçlamaktadır. Ancak daha fazla chunk üretmiş ve bu projede beklenen performans artışını sağlamamıştır.

## Sonuç

Final pipeline için Fixed-size chunking seçilmiştir. Recursive ve Parent-Child yaklaşımları deneysel karşılaştırma amacıyla notebook içerisinde korunmuştur.
