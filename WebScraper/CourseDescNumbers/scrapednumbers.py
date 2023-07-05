from selenium import webdriver

#This code Setups the driver
PATH = '/Users/joshuaguiman/Downloads/chromedriver_mac64/chromedriver'
driver = webdriver.Chrome(PATH)

#Goes to the main page of the course catalog
driver.get('https://catalog.ucsd.edu/front/courses.html')

#Lists to keep track of DOM elements
Course_URL = driver.find_elements_by_link_text('courses')
string_URL = []


for url in Course_URL:
    string_URL.append((url.get_attribute('href')))

with open('Scraped_Info.txt', 'w') as file:
    for url in string_URL:
        driver.get(url)
        file.write(url + "\n")
        course_cache = driver.find_elements_by_class_name('course-name')
        descriptions_cache = driver.find_elements_by_class_name('course-descriptions')
        file.write("Courses Scraped: "+ str(len(course_cache))+ "\n")
        file.write("Descriptions Scraped: " + str(len(descriptions_cache)) + "\n")
    
driver.close()

