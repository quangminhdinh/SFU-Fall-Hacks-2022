from dotenv import load_dotenv
from rytr.usecases import UseCases
from rytr.content import Content
import os
load_dotenv()

class EmailGenerator:

    def __init__(self):
        self.LANGUAGE_ID_ENGLISH = os.getenv('LANGUAGE_ID_ENGLISH')
        self.TONE_ID_CONVINCING = os.getenv('TONE_ID_CONVINCING')
        self.USE_CASE_ID_EMAIL = os.getenv('USE_CASE_ID_EMAIL')
        self.EMAIL_KEY_LABEL = 'KEY_POINTS_LABEL'
        self.API_URL = "https://api.rytr.me/v1"

    def acquire_email(self):
        usecase = UseCases.get(id=self.USE_CASE_ID_EMAIL)
        usecase = usecase["data"]

        content = Content.generate(
            user_id=1,
            language_id=self.LANGUAGE_ID_ENGLISH,
            tone_id=self.TONE_ID_CONVINCING,
            usecase_id=usecase["_id"],
            input_contexts={
                usecase["contextInputs"][0]["keyLabel"]: "late assignment\napology\nhospital",
            },
            format="html",
        )
        return content['data'][0]['text']
