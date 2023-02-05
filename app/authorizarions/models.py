# from uuid import UUID
#
# import ormar
#
# from app.users.models import User
# from config.database import BaseMeta
#
#
# class Permissions(ormar.Model):
#     class Meta(BaseMeta):
#         tablename = 'permissions'
#
#     id: UUID = ormar.UUID(primary_key=True, editable=False)
#     user: User = ormar.ForeignKey(User)
#     action: str = ormar.String(max_length=16)