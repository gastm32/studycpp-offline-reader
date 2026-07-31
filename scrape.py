import os
import re
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import time

BASE_URL = 'https://www.studycpp.cn'
INDEX_URL = f'{BASE_URL}/'
TARGET_DIR = '.'

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def main():
    print("Fetching index page...")
    resp = requests.get(INDEX_URL)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    chapters_elements = soup.select('ul.list-group')
    
    for chapter_idx, ul in enumerate(chapters_elements):
        title_li = ul.find('li', class_='active')
        if not title_li:
            continue
        
        chapter_name = title_li.get_text(strip=True)
        chapter_dir_name = f"{chapter_idx:02d}_{sanitize_filename(chapter_name)}"
        chapter_dir_path = os.path.join(TARGET_DIR, chapter_dir_name)
        
        os.makedirs(chapter_dir_path, exist_ok=True)
        print(f"Created chapter dir: {chapter_dir_name}")
        
        links = ul.find_all('a')
        for link_idx, link_a in enumerate(links):
            article_url = link_a['href']
            if article_url.startswith('/'):
                article_url = BASE_URL + article_url
                
            article_title = link_a.get_text(strip=True)
            article_filename = f"{sanitize_filename(article_title)}.md"
            article_filepath = os.path.join(chapter_dir_path, article_filename)
            
            print(f"Fetching {article_title} from {article_url}...")
            try:
                art_resp = requests.get(article_url, timeout=10)
                art_resp.encoding = 'utf-8'
                art_soup = BeautifulSoup(art_resp.text, 'html.parser')
                
                content_div = art_soup.find('div', class_='col-md-8')
                if not content_div:
                    print(f"Could not find content div for {article_url}")
                    continue
                
                # Fix highlight code blocks
                for highlight in content_div.find_all('div', class_='highlight'):
                    table = highlight.find('table', class_='lntable')
                    if table:
                        tds = table.find_all('td')
                        if len(tds) >= 2:
                            code_td = tds[1]
                            code_tag = code_td.find('code')
                            lang = ''
                            if code_tag and code_tag.has_attr('class'):
                                classes = code_tag['class']
                                for c in classes:
                                    if c.startswith('language-'):
                                        lang = c.replace('language-', '')
                            
                            new_pre = art_soup.new_tag('pre')
                            new_code = art_soup.new_tag('code', **{'class': f'language-{lang}'})
                            new_code.string = code_td.get_text()
                            new_pre.append(new_code)
                            highlight.replace_with(new_pre)
                
                # Try to remove waline comments and bottom navigation
                waline = content_div.find('div', id='waline')
                if waline:
                    waline.decompose()
                
                # Removing the bottom prev/next buttons
                row_divs = content_div.find_all('div', class_='row')
                if row_divs:
                    # Usually the last row is the navigation
                    row_divs[-1].decompose()
                    
                for script in content_div(["script", "style"]):
                    script.decompose()
                
                md_content = md(str(content_div), heading_style="ATX", strip=['a'])
                
                with open(article_filepath, 'w', encoding='utf-8') as f:
                    f.write(md_content)
                
                # Be polite
                time.sleep(0.5)
            except Exception as e:
                print(f"Failed to fetch {article_url}: {e}")

if __name__ == "__main__":
    main()
