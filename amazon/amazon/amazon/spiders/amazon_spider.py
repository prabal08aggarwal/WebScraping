import scrapy
from ..items import AmazonItem


class AmazonProductSpider(scrapy.Spider):
    name = "Amazon"
    allowed_domains = ["amazon.in"]

   
    start_urls = ["https://www.amazon.in/Power-your-Subconscious-Mind/dp/8192910962/ref=sr_1_3?dchild=1&keywords=book&qid=1585640609&sr=8-3"]
    # "https://www.amazon.com/Samsung-Galaxy-Factory-Unlocked-Smartphone/dp/B06Y16RL4W/ref=sxin_0_ac_d_rm?ac_md=0-0-czggcGx1cw%3D%3D-ac_d_rm&cv_ct_cx=s8+plus&dchild=1&keywords=s8+plus&pd_rd_i=B06Y16RL4W&pd_rd_r=415a8b98-35d3-42e8-820a-910c73218966&pd_rd_w=67NR2&pd_rd_wg=1g1HZ&pf_rd_p=ab7e4d6d-4494-43e9-8915-3a4910aefd56&pf_rd_r=5A2TZVTTQCB1E1Q1XT0F&psc=1&qid=1585640466&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"]

    def parse(self, response):
        items = AmazonItem()
        title = response.xpath('//*[(@id = "productTitle")]').extract()
        sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
        category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        availability = response.xpath('//div[@id="availability"]//text()').extract()
        items['product_name'] = ''.join(title).strip()
        items['product_sale_price'] = ''.join(sale_price).strip()
        items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
        items['product_availability'] = ''.join(availability).strip()
        yield items
