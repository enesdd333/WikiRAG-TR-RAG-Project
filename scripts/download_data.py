from datasets import load_dataset


def main():
    print("WikiRAG-TR veri seti yükleniyor...")

    dataset = load_dataset("Metin/WikiRAG-TR")

    print("Veri seti başarıyla yüklendi.")
    print(dataset)


if __name__ == "__main__":
    main()