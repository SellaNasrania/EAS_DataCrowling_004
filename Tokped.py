import time
from selenium import webdriver
from bs4 import BeautifulSoup 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.tokopedia.com/search?st=product&q=logitech'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

data = []
for i in range(5): 
     WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zeus-root")))
     time.sleep(2)
     
     for j in range (23):
          driver.execute_script("window.scrollBy(0, 250);")
          time.sleep(1)
     
     driver.execute_script("window.scrollBy(50, 0)")
     time.sleep(1)
     soup = BeautifulSoup(driver.page_source, 'html.parser')
     #print(soup)

     for item in soup.findAll('a', class_= 'pcv3__info-content'):
          nama_produk = item.find(class_= 'prd_link-product-name').text
          harga_produk = item.find(class_= 'prd_link-product-price').text
          diskon_elm = item.find(class_= 'prd_badge-product-discount')
          potongan_harga = diskon_elm.text if diskon_elm else '0'
          harga_normal =  item.find(class_='prd_label-product-slash-price')
          normal = harga_normal.text if harga_normal else '0'
          status_penanganan = item.find(class_='prd_link-shop-loc')
          status = status_penanganan.text if status_penanganan else '0'
          penilaian = item.find(class_='prd_rating-average-text')
          rating = penilaian.text if penilaian else '0'
          total_penjualan = item.find(class_='prd_label-integrity').text

          data.append(
               (nama_produk, harga_produk, potongan_harga, normal, status, rating, total_penjualan)
          )

     #     print(nama_produk)
     #     print(harga_produk)
     #     print(potongan_harga)
     #     print(normal)
     #     print(status)
     #     print(penilaian)
     #     print(total_penjualan)
     #     print('=============================')

     df = pd.DataFrame(data, columns=['Nama Produk', 'Harga Produk', 'Potongan Harga', 'Harga Normal', 'Status Penanganan', 'Penilaian', 'Total Penjualan'])
     print (df)

     df.to_csv('Logitech_TOKOPEDIA.csv', index = False)
     print('Data Telah Tersimpan')            

driver.close()