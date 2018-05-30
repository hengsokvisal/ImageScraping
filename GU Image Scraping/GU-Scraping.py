from selenium import webdriver
import time
import guImageLink as guLink

#Make sure file is empty and setup URL String
with open("guImageLink.py",'w') as f:
    f.write("URLS = [ ")

# Have to be the latest google chrome driver
chromeDriver = "/Users/doublevv/Downloads/chromedriver2"
driver = webdriver.Chrome(chromeDriver)

guURLS = "http://www.gu-global.com/jp/lookbook/pc/all"
# tell chrome to go to the given URL
driver.get(guURLS)


#Scroll Bot Scripts
def scrollbot():
    driver.execute_script("""setTimeout(scrolltobot, 1000);
     function scrolltobot()
     {
     window.scrollTo(0,0);
     window.scrollTo(0, document.body.scrollHeight);
     setTimeout(scrolltobot, 1000);   
     }""")


#Get Image URL
scrollbot()
time.sleep(50)
image = driver.find_elements_by_class_name("img-centered-container")
for url in image:
    imageURL = url.get_attribute('href')
    with open("guImageLink.py",'a') as write:
        write.write('"'+ imageURL +'",'+'\n' )

# Close ] in guImageLink File
with open("guImageLink.py",'a') as write:
    write.write("]")


#Get all the url from guImageLink
URLs = guLink.URLS

#Get ProductName
for url in URLs:
    driver.get(url)
    time.sleep(3)
    print(url)
    details = driver.find_elements_by_class_name('item-name')
    for detail in details:
        print(detail.text)
