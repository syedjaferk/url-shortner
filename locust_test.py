
import json
import uuid
import logging
from locust import task, constant
from locust.contrib.fasthttp import FastHttpUser


log = logging.getLogger("rest-api-short-urls")


def get_headers():
    """    It generates the API headers.

    Returns:
        dict: A dictionary containing the API headers.
    """
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def get_api_payload():
    """    It generates the body of a request.

    Returns:
        dict: A dictionary containing the URL for the request.
    """
    payload = {
        "url": "https://stackoverflow.com/questions/15261000/how-can-i-generate-a-random-url-of-a-certain-length-every-time-a-page-is-created/" + str(uuid.uuid4())
    }
    return payload


class LocustClient(FastHttpUser):
    wait_time = constant(0)

    def __init__(self, environment):
        """        Class constructor.

        Args:
            environment: The environment for the class.
        """
        super().__init__(environment)

    def on_start(self):
        """        on_start is called when a Locust start before any task is scheduled

        This function is called when a Locust instance starts before any task is scheduled.
        """
        pass

    def on_stop(self):
        """        on_stop is called when the TaskSet is stopping

        This method is called when the TaskSet is stopping. It can be used to perform any cleanup or finalization tasks.
        """
        pass

    @task
    def load_rest_api_based_service(self):
        """        This method contains all the APIs that need to be load tested for a service.

        It sends a POST request to a specified host with the API payload and headers.
        If the response status code is 200, it asserts the success of the API call; otherwise, it logs the failure.


        Raises:
            Exception: If an unexpected error occurs during the API call.
        """
        headers = get_headers()

        try:

            # Build your query parameter for GET API requests
            api_payload = json.dumps(get_api_payload())
            host = "http://localhost:8090/create"
            with self.client.post(host,headers=headers, catch_response=True, data=api_payload,
                                 name="url shortner test") as resp_of_api:

                if resp_of_api.status_code == 200:
                    resp_body_of_api = resp_of_api.json()
                    assert resp_body_of_api.get("result") == "success"
                    resp_of_api.success()

                    # Avoid too much logging in load test script as it may slow it
                    log.info("API call resulted in success.")

                else:
                    resp_of_api.failure(resp_of_api.text)
                    # Avoid too much logging in load test script as it may slow it
                    log.error("API call resulted in failed.")

        except Exception as e:
            log.error(f"Exception occurred! details are {e}")