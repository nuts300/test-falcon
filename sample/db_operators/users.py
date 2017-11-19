from sample.db_operators.documents.user import UserDocument

class UsersOperator(object):
    def createUser(user):
        user = UserDocument(**user)
        user.save()
        return user.to_json()

    def getUser(id):
        user = UserDocument.objects(id=ObjectId(id))
        return user.to_json()

    def getUsers():
        users =UserDocument.objects.all()
        return users.to_json()