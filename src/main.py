def print_author():
    from dotenv import load_dotenv
    import os

    load_dotenv(dotenv_path='.env')

    author = os.getenv('AUTHOR')

    print(f"Author of project: {author}")

print_author()
