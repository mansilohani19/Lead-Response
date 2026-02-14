from src.app import handle_query

if __name__ == "__main__":
    query = input("Enter customer query: ")
    reply = handle_query(query)
    print("\nAI Response:\n")
    print(reply)
