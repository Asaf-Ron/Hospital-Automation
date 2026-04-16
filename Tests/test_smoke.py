from Pages.A_logInPage import LoginPage
from Pages.B_DashboardPage import DashboardPage
from Pages.C_AddPatient import AddPatientPage
from playwright.sync_api import expect
import time

def test_smoke(hospital_url):
    login_page = LoginPage(hospital_url)
    dashboard_page = DashboardPage(hospital_url)
    add_patient_page = AddPatientPage(hospital_url)

    login_page.login("nurse_admin", "clinical2026")
    
    dashboard_page.click_patients_tab()
    dashboard_page.click_laboratory_tab()
    dashboard_page.click_pharmacy_tab()
    dashboard_page.click_patients_tab()

    add_patient_page.add_patient("12345", "John Doe", "ICU", "Stable", "Dr. Smith", "Ward A")
    add_patient_page.admit_patient()

    dashboard_page.search_patient("John Doe")

    expect(hospital_url.locator("#dataContainer")).to_be_visible()
    expect(hospital_url).to_have_url("https://qahackeru3.netlify.app/")

    dashboard_page.logout()
    time.sleep(3)

    


