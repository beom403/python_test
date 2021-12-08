from indeed import extract_indeed_pages, extract_indeed_jobs
from save import save_to_file

last_indeed_page = extract_indeed_pages()
save_to_file(extract_indeed_jobs(last_page = last_indeed_page))