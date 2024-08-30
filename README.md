<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
</head>
<body>
    <div class="container">
        <h1>BookScrapy</h1>
        <p>This project is a web scraping spider built using the Scrapy framework to extract detailed information about books from the <a href="https://books.toscrape.com/" target="_blank">Books to Scrape</a> website. The spider navigates through the website's pages, extracts book details, and stores them in a structured format for further analysis or use.</p>
        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#overview">Project Overview</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#data">Scraped Data</a></li>
            <li><a href="#customization">Customization</a></li>
            <li><a href="#contributing">Contributing</a></li>
            <li><a href="#license">License</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
        <h2 id="overview">Project Overview</h2>
        <p>The <strong>BookScrapy</strong> spider is designed to efficiently scrape data from the "Books to Scrape" website, capturing a wide range of information about each book, including the title, price, availability, category, and more. This data can be used for various purposes, such as data analysis, price comparison, or building a recommendation system.</p>
        <h2 id="features">Features</h2>
        <ul>
            <li><strong>Comprehensive Scraping:</strong> The spider navigates through the website and extracts detailed information about each book.</li>
            <li><strong>Pagination Handling:</strong> Automatically follows pagination links to scrape all books listed on the website.</li>
            <li><strong>Data Extraction:</strong> Captures a variety of fields including title, price, availability, category, product type, and more.</li>
            <li><strong>Structured Output:</strong> The scraped data is organized and stored in a structured format, making it easy to analyze or use in other applications.</li>
        </ul>
        <h2 id="installation">Installation</h2>
        <p>To run this project, you need to have Python and Scrapy installed on your machine.</p>
        <ol>
            <li><strong>Clone the repository:</strong></li>
        </ol>
        <pre><code>git clone https://github.com/yourusername/bookscrapy.git
cd bookscrapy</code></pre>
        <ol start="2">
            <li><strong>Create and activate a virtual environment (optional but recommended):</strong></li>
        </ol>
        <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        <ol start="3">
            <li><strong>Install the required dependencies:</strong></li>
        </ol>
        <pre><code>pip install scrapy</code></pre>
        <h2 id="usage">Usage</h2>
        <p>To run the spider and start scraping data from the website, use the following command:</p>
        <pre><code>scrapy crawl bookscrapy </code></pre>
        <p>This command will run the <strong>BookScrapy</strong> spider and store the scraped data in a <code>books_data.json</code> file.</p>
        <h2 id="data">Scraped Data</h2>
        <p>The spider extracts the following fields from each book:</p>
        <ul>
            <li><strong>URL:</strong> The URL of the book's detail page.</li>
            <li><strong>Title:</strong> The title of the book.</li>
            <li><strong>Price:</strong> The price of the book.</li>
            <li><strong>UPC:</strong> Universal Product Code of the book.</li>
            <li><strong>Product Type:</strong> The type of the product.</li>
            <li><strong>Category:</strong> The category under which the book is listed.</li>
            <li><strong>Price Excl. Tax:</strong> The price excluding tax.</li>
            <li><strong>Price Incl. Tax:</strong> The price including tax.</li>
            <li><strong>Tax:</strong> The tax amount.</li>
            <li><strong>Availability:</strong> The number of copies available in stock.</li>
            <li><strong>Number of Reviews:</strong> The number of reviews for the book.</li>
            <li><strong>Stars:</strong> The star rating of the book.</li>
            <li><strong>Description:</strong> A brief description of the book.</li>
        </ul>
        <h2 id="customization">Customization</h2>
        <p>You can customize the spider to scrape additional fields or modify its behavior by editing the <code>parse_book_page</code> method in the <code>BookscrapySpider</code> class.</p>
        <p>For example, to scrape a different website, update the <code>allowed_domains</code> and <code>start_urls</code> variables accordingly.</p>
        <h2 id="contributing">Contributing</h2>
        <p>Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request. You can also open issues for any bugs or feature requests.</p>
        <h2 id="license">License</h2>
        <p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>
        <h2 id="contact">Contact</h2>
        <p>If you have any questions or feedback, feel free to reach out to me:</p>
        <ul>
            <li><strong>GitHub:</strong> <a href="https://github.com/AbderraoufIdel/" target="_blank">AbderraoufIdel</a></li>
            <li><strong>Email:</strong> <a href="mailto:abderraoufidel@gmail.com">abderraoufidel@gmail.com</a></li>
        </ul>
        <a href="https://github.com/yourusername/bookscrapy" class="button">View on GitHub</a>
    </div>
</body>
</html>
