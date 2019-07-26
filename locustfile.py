from locust import HttpLocust, TaskSet, task
from PIL import Image
import tempfile


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.token = self.client.post("/api/v1/auth/jwt/obtain/", {
            "email": "admin@admin.com",
            "password": "Ee199407#"
        }).json().get('token')

        self.headers = {'Authorization': 'Bearer ' + self.token}

    def get_temporary_image(self):
        """create a temporary image"""
        image = Image.new('RGB', (100, 100))
        temporary_image = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(temporary_image, 'jpeg')
        temporary_image.seek(0)
        return temporary_image

    @task
    def login(self):
        self.client.post("/api/v1/auth/jwt/obtain/", {
            "email": "admin@admin.com",
            "password": "Ee199407#"
        })

    @task
    def upload_user_passport(self):
        self.client.patch("/api/v1/user/b808ada9-9423-4604-895a-d2921235d8fb", headers=self.headers, data={"first_name":"RandomName"})
    
    @task
    def flights(self):
        self.client.get("/api/v1/flights/")

    @task
    def single_flight(self):
        self.client.get("/api/v1/flight/21423068-d03a-4992-a2fa-902d3512deac")

    @task
    def flight_reservations(self):
        self.client.get("/api/v1/reservations/?search=Frontier+Airlines+Inc.+43", headers=self.headers)

    @task
    def all_reservations(self):
        """
        View reservations for all flights
        :return:
        """
        self.client.get("/api/v1/reservations/", headers=self.headers)


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000