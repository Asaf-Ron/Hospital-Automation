class AddPatientPage:
    def __init__(self, page):
        self.page = page
        
    def add_patient(self, patientID, patientName, category, patientStatus, doctor, ward):
        self.add_patient_button = self.page.locator("#addPatientBtn").click()
        self.patient_id = self.page.locator("#patientId").fill(patientID)
        self.patient_name = self.page.locator("#patientName").fill(patientName)
        self.category = self.page.locator("#patientCategory").select_option(category)
        self.status = self.page.locator("#patientStatus").select_option(patientStatus)
        self.assigned_doctor = self.page.locator("#patientDoctor").fill(doctor)
        self.ward = self.page.locator("#patientWard").fill(ward)
    
    def admit_patient(self):
        self.page.locator("#submitPatientBtn").click()

    def cancel_admit_patient(self):
        self.page.locator(".btn-secondary").click()