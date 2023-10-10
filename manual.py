from selenium import webdriver
import pandas as pd
from pynput import keyboard
import time

topic = 'Professional, Scientific, and Technical Services'
df = pd.read_csv(f'data/repo_by_topic/{topic}/data_{topic}.csv')

driver = webdriver.Chrome()

good_urls = []
bad_urls = []

def on_press(key):
    try:
        if key.char == 'g':
            good_urls.append(url)
            return False 
        elif key.char == 'b':
            bad_urls.append(url)
            return False  
    except AttributeError:
        pass

for url in df.sample(min(len(df), 100))['url (HTML)']:
    driver.execute_script(f"window.open('{url}', '_blank');")
    time.sleep(1) 
        
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.quit()

filtered_df = df[df['url (HTML)'].isin(good_urls)]
filtered_df.to_csv(f'data/repo_by_topic/{topic}/filtered_data_{topic}.csv', index=False)