import scrapy

from webscraper.items import BookItem

class BookscrapySpider(scrapy.Spider):
    name = "bookscrapy"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/index.html"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books :
            next_book = book.css("h3 a::attr(href)").get()

            if next_book is not None:
                yield response.follow(next_book, self.parse_book_page)

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_book_page(self, response):   
        page_info = response.css(".page")
        table_rows = response.css("table.table.table-striped tr")
        book_item = BookItem()

        book_item  ["url"] = response.url
        book_item  ["title"]= page_info.css(".product_main h1::text").get()
        book_item  ["price"]= page_info.css(".price_color::text").get()
        book_item  ["upc"]= table_rows[0].css("td ::text").get()
        book_item  ["product_type"]= table_rows[1].css("td ::text").get()
        book_item  ["category"]= page_info.css(".breadcrumb li a::text").getall()[2]
        book_item  ["price_excl_tax"]= table_rows[2].css("td ::text").get()
        book_item  ["price_incl_tax"]= table_rows[3].css("td ::text").get()
        book_item  ["tax"]= table_rows[4].css("td ::text").get()
        book_item  ["availability"]= table_rows[5].css("td ::text").get()
        book_item  ["num_reviews"]= table_rows[6].css("td ::text").get()
        book_item  ["stars"]= page_info.css("p.star-rating").attrib["class"]
        book_item  ["description"]= page_info.xpath('//*[@id="content_inner"]/article/p/text()').get()
         
        yield book_item

