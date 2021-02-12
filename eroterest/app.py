from selenium import webdriver
from datetime import date


def make_title_array(URL):
    title_array = []
    driver.get(URL)
    titles = driver.find_elements_by_class_name('itemTitle')
    for title in titles:
        try:
            raw_title = title.find_element_by_tag_name('a').get_attribute('title')
            title_array.append(raw_title)
        except:
            pass
    
    return title_array

def write_title_array(array):
    try:
        with open(f'{BASE_PATH}/{TODAY}.txt', mode='w', encoding='utf-8') as f:
            f.write('\n'.join(array))
        flag = True
    except Exception as e:
        print(e)
        flag = False
    
    return flag

def main(URL):
    title_array = make_title_array(URL)
    result =  write_title_array(title_array)

    return result

if __name__ == '__main__':
    URL = 'https://movie.eroterest.net/popular/?days=0'
    BASE_PATH = './title'
    TODAY = str(date.today())
    driver = webdriver.Chrome()

    result = main(URL)
    result_comment = 'all done.' if result else 'something wen\'t wrong.'
    print(result_comment)