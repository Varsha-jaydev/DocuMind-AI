from langchain_community.document_loaders import DirectoryLoader, BSHTMLLoader
import pickle


class UTF8BSHTMLLoader(BSHTMLLoader):
    def __init__(self, file_path, **kwargs):
        super().__init__(
            file_path,
            open_encoding="utf-8",
            **kwargs
        )


def load_documents():

    loader = DirectoryLoader(
        "../../data/docs",
        glob="**/*.html",
        loader_cls=UTF8BSHTMLLoader,
        show_progress=True,
        silent_errors=True
    )

    docs = loader.load()

    print(f"Loaded {len(docs)} documents")

    for doc in docs[:3]:
        print(doc.metadata)

    return docs   # <-- add this


if __name__=="__main__":

    docs = load_documents()

    with open("../../vectorstore/docs.pkl", "wb") as f:
        pickle.dump(docs, f)

    print(f"Saved {len(docs)} documents")