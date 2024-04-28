import scrapy.http as http
from scrapy.spiders import Spider

class FormSpider(Spider):
    name = "Horse Form"

    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        form_data = {'firstname': 'John',
                     'lastname': 'Doe',
                     'jobtitle': 'Software Engineer'}
        
        return FormRequest.from_response(response,
                                         formnumber=0,
                                         formdata=form_data,
                                         callback=self.after_post)
    
    def after_post(response):
        print('Form processed \n')
        print(response)