from tortoise import fields
from tortoise.models import Model


class File(Model):
    uuid = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=255)
    path = fields.CharField(max_length=255)
    file_type = fields.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.name}'