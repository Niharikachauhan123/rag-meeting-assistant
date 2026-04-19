from app.rag_pipeline import ingest_data, get_retriever, answer_query
from app.summarizer import generate_summary

def main():
    file_path = "data/uploads/ml.txt"

    print("Ingesting document...")
    vectorstore = ingest_data(file_path)
    retriever = get_retriever(vectorstore)

    print("\n1. Ask Question")
    print("2. Generate Summary")

    choice = input("Choose option: ")

    if choice == "1":
        query = input("Ask a question: ")
        answer = answer_query(retriever, query)
        print("\nAnswer:\n")
        print(answer)

    elif choice == "2":
        summary = generate_summary(retriever)
        print("\nMeeting Summary:\n")
        print(summary)

if __name__ == "__main__":
    main()