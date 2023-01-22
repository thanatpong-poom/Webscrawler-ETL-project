from playwright.sync_api import sync_playwright, Page, Request
import re
import json

LIMIT = 1

with sync_playwright() as p:

    data_list = []
    detail_dict = {}

    # def handle_request(req: Request):
    #     if req.url include jpg | png:
            
        
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()


    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    page = context.new_page()
    page.route(re.compile(r"\.(jpg|png|svg|gif)$"), lambda route: route.abort())

    # First page
    page.goto("https://www.tripadvisor.com/Restaurants-g293916-Bangkok.html")
    restaurantDivs = page.locator('//html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[6]/div[3]/div[5]/div[1]/div/div/div[not(@class)]')
    sponsor = 0                  
    i = 0
    data = []           
    

    #function extracts detail
    def get_detail(target_page: Page):
        target_page.wait_for_function('() => window.__WEB_CONTEXT__ && window.__WEB_CONTEXT__.pageManifest')
        dataJson = target_page.evaluate('''() => {
    return JSON.stringify(Object.entries(window.__WEB_CONTEXT__.pageManifest.redux.api.responses).find(([key]) => {
        return /^\/data\/1.0\/location\/\d+$/.test(key)
    })[1].data)
}''')
        data = json.loads(dataJson)

        return data

        
    # # All restuarants in first page
    
    i = 1
    while True:
        if i > LIMIT and LIMIT != 0:
                break
        for div in restaurantDivs.all():
            if i > LIMIT and LIMIT != 0:
                break
            
            # Ignore sponsored restuarants
            if div.locator('//div/span/div/div[1]/div[2]/div[1]/div[1]/div/div/span').is_visible():
                continue
                
            elif div.locator('//div/span/div[1]/div[2]/div[1]/div/span/a').is_visible():
                with context.expect_page() as new_page_info:
                    div.locator('//div/span/div[1]/div[2]/div[1]/div/span/a').click()
                
                new_page = new_page_info.value
                new_page.route(re.compile(r"\.(jpg|png|svg)$"), lambda route: route.abort())

                data_list.append(get_detail(new_page))
                new_page.close()
                
            else:
                with context.expect_page() as new_page_info:
                    div.locator('//div/span/div[1]/div[2]/div[2]/div/span/a').click()
                new_page = new_page_info.value
                new_page.route(re.compile(r"\.(jpg|png|svg)$"), lambda route: route.abort())

            
                data_list.append(get_detail(new_page))
                new_page.close()
            i+=1
            print(data_list)

        page.locator("//html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[6]/div[3]/div[5]/div[2]/div/a").click()
        page.wait_for_timeout(1000)
        # print("********")
        # print(data_list[1])
        # print("********")
        # print(data_list[2])
        # print("********")
        # print(data_list[3])
        # print("********")
        # print(data_list[4])
        
    # go to next page for first page
    # page.locator("//html/body/div[4]/div[3]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[6]/div[3]/div[5]/div[2]/div/a").click()
    # page.wait_for_timeout(1000)
    # print(data_list)
    
    
    # while loop in other pages until next is not visible

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path = "trace.zip")
