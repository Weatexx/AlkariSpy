from googlesearch import search

def email_search(email, language):
    """Search for an email address on various platforms."""
    query = f"\"{email}\""
    dorks = [
        f"site:linkedin.com {query}",
        f"site:twitter.com {query}",
        f"site:github.com {query}",
        f"site:stackoverflow.com {query}",
        f"site:medium.com {query}"
    ]
    
    if language == "en":
        print(f"\nSearching for the email '{email}' on popular platforms...\n")
    else:
        print(f"\n'{email}' e-posta adresiyle popüler platformlarda arama yapıyorum...\n")
    
    for dork in dorks:
        print(f"\nSearching with query: {dork}")
        results = search(dork, num_results=5)  # Modify num_results as needed
        for result in results:
            print(result)
