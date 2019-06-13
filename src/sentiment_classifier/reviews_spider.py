import scrapy
import re

# Получить оценку на отзыве
def get_mark(raw_str):
    result = re.findall(r'(\d{3})px', raw_str)
    if len(result) != 0:
        mark = int(result[0])//26
    else:
        result = re.findall(r'(\d{2})px', raw_str)
        mark = int(result[0])//26
        
    if mark <= 3:
        return 0
    else:
        return 1

# Получить текст отзыва
def get_review(review_response):
    review = review_response.xpath('div')
    if len(review) != 0:
        mark = get_mark(review[0].xpath('div/div').extract_first())
        raw_text = ' '.join(review[1].xpath('text()').extract())
        
        review_text = raw_text.replace('\r', '')
        review_text = review_text.replace('Достоинства:', '')
        review_text = review_text.replace('Недостатки:', '')
        review_text = review_text.replace('Комментарий:', '')
        
        return (review_text, mark)
    else:
        return None
        
class ReviewsSpider(scrapy.Spider):
    name = "Отзывы на мобильные телефоны"
    
    # начальный запрос
    def start_requests(self):
        start_urls = urls
        
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # парсинг страницы
    def parse(self, response):
        for element in response.xpath('/html/body/div[1]/div[2]/div[1]/div/div/div[5]/div'):
            review = get_review(element)
            
            if review != None:
                yield {
                    'review' : review[0],
                    'target' : review[1]
                }

# список страниц для парсинга
urls = [
    'https://slonrekomenduet.com/model/htc-wildfire-s.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/2.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/3.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/4.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/5.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/6.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/7.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/8.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/9.html',
    'https://slonrekomenduet.com/model/htc-wildfire-s/page/10.html',
    'https://slonrekomenduet.com/model/nokia-asha-200.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/2.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/3.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/4.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/5.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/6.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/7.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/8.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/9.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/10.html',
    'https://slonrekomenduet.com/model/nokia-asha-200/page/11.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/2.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/3.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/4.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/5.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/6.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/7.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/8.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/9.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/10.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/11.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/12.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/13.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/14.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/15.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/16.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-s-iii-gt-i9300-16gb/page/17.html',
    'https://slonrekomenduet.com/model/htc-desire-310.html',
    'https://slonrekomenduet.com/model/htc-desire-310/page/2.html',
    'https://slonrekomenduet.com/model/htc-desire-310/page/3.html',
    'https://slonrekomenduet.com/model/htc-desire-310/page/4.html',
    'https://slonrekomenduet.com/model/htc-desire-310/page/5.html',
    'https://slonrekomenduet.com/model/htc-desire-500-dual-sim.html',
    'https://slonrekomenduet.com/model/htc-desire-500-dual-sim/page/2.html',
    'https://slonrekomenduet.com/model/htc-desire-500-dual-sim/page/3.html',
    'https://slonrekomenduet.com/model/htc-desire-500-dual-sim/page/4.html',
    'https://slonrekomenduet.com/model/htc-desire-500-dual-sim/page/5.html',
    'https://slonrekomenduet.com/model/htc-desire-616-dual-sim.html',
    'https://slonrekomenduet.com/model/htc-desire-616-dual-sim/page/2.html',
    'https://slonrekomenduet.com/model/htc-desire-616-dual-sim/page/3.html',
    'https://slonrekomenduet.com/model/nokia-5230.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/2.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/3.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/4.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/5.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/6.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/7.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/8.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/9.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/10.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/11.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/12.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/13.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/14.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/15.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/16.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/17.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/18.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/19.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/20.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/21.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/22.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/23.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/24.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/25.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/26.html',
    'https://slonrekomenduet.com/model/nokia-5230/page/27.html',
    'https://slonrekomenduet.com/model/nokia-500.html',
    'https://slonrekomenduet.com/model/nokia-500/page/2.html',
    'https://slonrekomenduet.com/model/nokia-500/page/3.html',
    'https://slonrekomenduet.com/model/nokia-500/page/4.html',
    'https://slonrekomenduet.com/model/nokia-500/page/5.html',
    'https://slonrekomenduet.com/model/nokia-500/page/6.html',
    'https://slonrekomenduet.com/model/nokia-500/page/7.html',
    'https://slonrekomenduet.com/model/nokia-500/page/8.html',
    'https://slonrekomenduet.com/model/nokia-asha-305.html',
    'https://slonrekomenduet.com/model/nokia-asha-305/page/2.html',
    'https://slonrekomenduet.com/model/nokia-asha-305/page/3.html',
    'https://slonrekomenduet.com/model/nokia-asha-305/page/4.html',
    'https://slonrekomenduet.com/model/nokia-asha-305/page/5.html',
    'https://slonrekomenduet.com/model/nokia-asha-305/page/6.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/2.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/3.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/4.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/5.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/6.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/7.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/8.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/9.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/10.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/11.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/12.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/13.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/14.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/15.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/16.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/17.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/18.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/19.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/20.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/21.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/22.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/23.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/24.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/25.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/26.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/27.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/28.html',
    'https://slonrekomenduet.com/model/nokia-lumia-520/page/29.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/2.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/3.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/4.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/5.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/6.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/7.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/8.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/9.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/10.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/11.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/12.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/13.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/14.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/15.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/16.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/17.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/18.html',
    'https://slonrekomenduet.com/model/nokia-lumia-720/page/19.html',
    'https://slonrekomenduet.com/model/nokia-x7.html',
    'https://slonrekomenduet.com/model/nokia-x7/page/2.html',
    'https://slonrekomenduet.com/model/nokia-e7.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/2.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/3.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/4.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/5.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/6.html',
    'https://slonrekomenduet.com/model/nokia-e7/page/7.html',
    'https://slonrekomenduet.com/model/nokia-asha-500-dual-sim.html',
    'https://slonrekomenduet.com/model/nokia-asha-500-dual-sim/page/2.html',
    'https://slonrekomenduet.com/model/nokia-asha-311.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/2.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/3.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/4.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/5.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/6.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/7.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/8.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/9.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/10.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/11.html',
    'https://slonrekomenduet.com/model/nokia-asha-311/page/12.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/2.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/3.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/4.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/5.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/6.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/7.html',
    'https://slonrekomenduet.com/model/samsung-wave-y-gt-s5380/page/8.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/2.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/3.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/4.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/5.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/6.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/7.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/8.html',
    'https://slonrekomenduet.com/model/samsung-sm-g355h-galaxy-core-2-duos/page/9.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/2.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/3.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/4.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/5.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/6.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/7.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/8.html',
    'https://slonrekomenduet.com/model/samsung-galaxy-star-plus-gt-s7262/page/9.html',
    'https://slonrekomenduet.com/model/htc-one-v.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/2.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/3.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/4.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/5.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/6.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/7.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/8.html',
    'https://slonrekomenduet.com/model/htc-one-v/page/9.html',
    'https://slonrekomenduet.com/model/htc-desire-v.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/2.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/3.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/4.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/5.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/6.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/7.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/8.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/9.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/10.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/11.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/12.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/13.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/14.html',
    'https://slonrekomenduet.com/model/htc-desire-v/page/15.html',
]    
            