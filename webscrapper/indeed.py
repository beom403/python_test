import requests
from bs4 import BeautifulSoup

LIMIT = 10
URL = f"https://kr.indeed.com/jobs?q=%EC%9E%84%EB%B2%A0%EB%94%94%EB%93%9C&l&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class" : "pagination"})
    links = pagination.find_all('a')
    pages = []

    # for link in links[:-1]:
    for link in links:
        # pages.append(link.find('span').string)
        if link.string != None:
            pages.append(int(link.string))

    max_page = pages[-1]
    # print(pages[:-1])   # get all items except last one
    # print(pages[0:2])   # get 0~2 items
    # print(pages)
    # print(max_page)
    return max_page


def extract_indeed_job_info(job):
    # find job title
    job_info = job.find('h2', {"class" : "jobTitle jobTitle-color-purple"})
    if job_info != None:
        title = job_info.string
        # find job company
        job_info = job.find('span', {"class" : "companyName"})
        if job_info != None:
            company = job_info.string
            # find job location
            job_info = job.find('div', {"class" : "companyLocation"})
            if job_info != None:
                location = job_info.string
                # return result
                return {
                    'title': title,
                    'company': company,
                    'location': location
                }


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        job_list = soup.find_all("div", {"class" : "slider_container"})
        for job in job_list:
            result = extract_indeed_job_info(job)
            if result != None:
                jobs.append(result)

    return jobs

