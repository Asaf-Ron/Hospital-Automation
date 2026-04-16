class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.patients_tab = self.page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[1]")
        self.laboratory_tab = self.page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[2]")
        self.pharmacy_tab = self.page.locator("//*[@id='dashboard']/div[2]/div[2]/div[2]/button[3]")

    def click_patients_tab(self):
        self.patients_tab.click()

    def click_laboratory_tab(self):
        self.laboratory_tab.click()

    def click_pharmacy_tab(self):
        self.pharmacy_tab.click()
    
    def search_patient(self, search):
        self.page.locator("#searchInput").fill(search)