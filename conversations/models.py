# conversations은
from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStamptedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)


class Message(core_models.TimeStamptedModel):
    message = models.TextField()
    # 누가 메세지를 만들지?
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
