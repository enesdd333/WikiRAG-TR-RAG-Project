# RAG Ek Dokümanı

## Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG), büyük dil modellerinin harici bir bilgi kaynağından getirilen bağlamı kullanarak yanıt üretmesini sağlayan bir yaklaşımdır.

Bu projede WikiRAG-TR veri seti temel veri kaynağı olarak kullanılmıştır. Ayrıca sistemin birden fazla dosya formatından veri alabilme yeteneğini göstermek amacıyla bu Markdown dokümanı ek veri kaynağı olarak kullanılmıştır.

## Projede Kullanılan Yaklaşım

RAG pipeline temel olarak şu aşamalardan oluşmaktadır:

1. Dokümanların yüklenmesi
2. Metinlerin chunk'lara ayrılması
3. Embedding oluşturulması
4. Retrieval işlemi
5. İlgili bağlamın LLM'e verilmesi
6. Kaynaklara dayalı yanıt üretilmesi

Bu doküman, projenin multi-format veri ingestion desteğini göstermek amacıyla hazırlanmıştır.
