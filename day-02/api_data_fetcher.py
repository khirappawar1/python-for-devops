import requests
import json  # <-- Needed for saving JSON file

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        # Make GET request to API
        response = requests.get(url, timeout=5)

        # Check HTTP response status
        if response.status_code == 200:
            print("Post fetched successfully")
        else:
            print("Failed to fetch the data")
            return None

        # Parse the JSON response
        post = response.json()

        # Modify / extract meaningful information
        modified_post = {
            "post_id": post["id"],
            "title": post["title"],
            "body_length": len(post["body"])
        }

        # Print processed output
        print("\nProcessed Post:")
        print(modified_post)

        # Save processed data into a JSON file
        with open("processed_post.json", "w", encoding="utf-8") as file:
            json.dump(modified_post, file, indent=4)

        print("\nData saved to 'processed_post.json'")

        return modified_post

    except requests.exceptions.Timeout as error:
        print("Request timed out:", error)
    


if __name__ == "__main__":
    get_posts()
