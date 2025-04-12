import requests

# Function to fetch data from Gemini or any API
def fetch_data_from_gemini():
    # Replace with the actual Gemini API endpoint
    url = "https://api.gemini.com/v1/symbols"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Gemini: {e}")
        return []

# Update the HTML generation function to include a script for scroll detection
def generate_html(blocks):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>inSight - Dynamic Blocks</title>
        <style>
            body {{
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: url('Images/sea_img.jpg') no-repeat center center/cover;
                background-size: 120%;
                transition: background-size 0.5s ease;
            }}
            .rounded-box {{
                width: 300px;
                height: 200px;
                margin: auto;
                border: 2px solid rgba(255, 255, 255, 0.5);
                border-radius: 15px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
                padding: 15px;
                text-align: left;
                color: white;
                font-size: 16px;
                font-family: Arial, sans-serif;
                backdrop-filter: blur(5px);
                background-color: rgba(0, 0, 0, 0.4);
                position: relative;
                overflow: hidden;
                word-wrap: break-word;
                word-break: break-word;
                white-space: normal;
            }}
            #block-container {{
                margin-top: 80px;
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 40px;
                position: relative;
                overflow-x: auto;
                white-space: nowrap;
                padding: 10px;
                scroll-behavior: smooth;
            }}
            .rounded-box:last-child .arrow {{
                display: none;
            }}
            header {{
                position: fixed;
                top: 0;
                width: 100%;
                color: white;
                text-align: left;
                padding: 10px;
                font-size: 24px;
                border-bottom: 2px solid rgba(255, 255, 255, 0.5);
                backdrop-filter: blur(5px);
                font-family: Arial, sans-serif;
                z-index: 1000;
            }}
            header h1 {{
                margin: 0;
                padding-left: 20px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>inSight</h1>
        </header>
        <div id="block-container">
    """

    # Add blocks dynamically
    for block in blocks:
        html_content += f"""
        <div class="rounded-box">
            <h4>{block['title']}</h4>
            <p>{block['description']}</p>
        </div>
        """

    # Close HTML tags and add JavaScript
    html_content += """
        </div>
        <script>
            const container = document.getElementById('block-container');
            container.addEventListener('scroll', () => {
                if (container.scrollLeft + container.clientWidth >= container.scrollWidth - 10) {
                    console.log('Scrolled to the right end!');
                    // Add logic to load more content dynamically if needed
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content

# Main function
def main():
    # Fetch data from Gemini
    data = fetch_data_from_gemini()

    # Transform the data into blocks
    blocks = []
    for symbol in data[:5]:  # Limit to the first 5 items for simplicity
        blocks.append({
            "title": symbol.upper(),
            "description": f"Symbol {symbol.upper()} represents a trading pair on Gemini."
        })

    # Generate the HTML content
    html_content = generate_html(blocks)

    # Write the HTML content to a file
    output_file = "../Frontend/Pages/index.html"  # Adjust the path as needed
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"HTML file generated successfully: {output_file}")
    except Exception as e:
        print(f"Error writing to HTML file: {e}")

if __name__ == "__main__":
    main()