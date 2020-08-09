# NguyenMInhQuang_19020405_Nhom3_Crawler

 week_2_assigments
 
 
2 file mô tả README.md em để trong 2 thu muc News va online_trading _ 2 des file I put in 2 project folders



**Mô tả chung các chương trình**

**các đoạn code đã được giản lược vì em sử dụng chung mẫu cho nhiều chương trình**

**1.** **Phương pháp lấy link tiếp theo trong page hiện tại:**

    class Web(scrapy.Spider): 
    # khai báo tên lớp (mỗi trang cần khai thác dữ liệu sẽ được xử lí qua các lớp khác nhau)
    
     page_count = 0   
     # biến điếm số trang đã duyệt hoặc lượng dữ liệu đã lấy (tùy biến)
    
      allowed_domains = ['web.vn']
     # các tên miền được phép duyệt để lấy dữ liệu
    
      name = 'web'
     # tên đại diện cho lớp ( khi gọi qua command line )
    
      start_urls = ['https://web.vn/start_link/']
     # link ban đầu muốn khai thác dữ liệu  
  
      def parse(self, response):
     # hàm xử lí dữ liệu, trong đó response là kết quả trả về khi request url 
    
	      if (condition) :
     # điều kiện để dữ liệu được thu thập
    
		      self.page_count += 1
		      data = { ‘item_1’: response.item_1, ‘item_2’: response.item_2, …..}
     # thu thập các dữ liệu từ response, lưu trong biến data,v.v..
    
		      with open('web.json', 'a+', encoding='utf8') as f:  
		      json.dump(data, f, ensure_ascii=False)
     # ghi dữ liệu từ data vào file
    
     links=response.css('a::attr(href)').getall()
     # lấy toàn bộ link có trong page hiện tại (có điều kiện nhất định)
     for link in links:
	     yield response.follow(link, self.parse)  
     # tạo ra các bước thu thập dữ liệu tiếp theo

**2.** **Phương pháp thử các link tiếp theo qua id**

    class Web(scrapy.Spider):
    # tên lớp
    
     page_count = 0
     # biến điếm ( tùy theo mục đích sử dụng) 
    
      af_id = be_id = 31565625
     # khởi tạo 2 id trước và sau
    
      allowed_domains = ['web.com']
     # tên miền được khai thác sữ liệu
    
     name = 'web'
     # tên đại diện cho lớp (khi gọi qua command line)
     
     def start_requests(self):
     # hàm khởi tạo yêu cầu
    
      while (condition): 
	      yield scrapy.Request('https://web.com/' + str(self.af_id) + '.epi', self.parse) 
	      self.af_id += 1 
	      yield scrapy.Request('https://web.com/ ' + str(self.be_id) + '.epi', self.parse) 
	      self.be_id -= 1
    
     # các hàm trên khởi tạo các yêu cầu được đặt rong vòng lặp khi một điều kiện nào đó được thỏa mãn (vd số dữ liệu thu  thập được) bằng cách thay đổi 2 id để tạo các url mới
     
    def parse(self, response):  
      # hàm xử lí dữ liệu, trong đó response là kết quả trả về khi request url	
    
      if (condition) :
     # điều kiện để dữ liệu được thu thập
    
	      self.page_count += 1
	      data = { ‘item_1’: response.item_1, ‘item_2’: response.item_2, …..}
     # thu thập các dữ liệu từ response, lưu trong biến data, thay đổi biến đếm v.v...
    
	      with open('web.json', 'a+', encoding='utf8') as f:  
	      json.dump(data, f, ensure_ascii=False) 
      # ghi dữ liệu từ data vào file

**3.** **Sử dụng thêm user agent khi khai thác thông tin từ amazon ( trong setting.py)**

    DOWNLOADER_MIDDLEWARES = { 
	    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
	    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, }

em đang tìm hiểu cái này 

