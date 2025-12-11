# financial_chatbot.py

def simple_chatbot(user_query):
    # Predefined queries and responses
    responses = {
        "What is the total revenue?": "The total revenue is $1,200,000.",
        "How has net income changed over the last year?": "The net income has increased by $150,000 over the last year.",
        "What are the total assets and liabilities?": "Total assets are $5,000,000 and total liabilities are $2,500,000.",
        "What is the operating cash flow trend?": "Operating cash flow has remained stable with minor fluctuations over the last year.",
        "Which company is the most profitable?": "Apple is the most profitable among the companies analyzed."
    }
    
    # Match the query
    return responses.get(user_query, "Sorry, I can only provide information on predefined queries.")

# Command-line interaction
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    print("You can ask predefined queries like:")
    print(" - What is the total revenue?")
    print(" - How has net income changed over the last year?")
    print(" - What are the total assets and liabilities?")
    print(" - What is the operating cash flow trend?")
    print(" - Which company is the most profitable?")
    
    while True:
        user_input = input("\nEnter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Thank you for using the Financial Chatbot. Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(response)
