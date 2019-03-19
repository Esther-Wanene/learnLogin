from main import db


# create a table called users with columns id, username & password
class UserAuthentication(db.Model):
    __tablename__ = 'Test'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    firstname = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


    # a method that crates a user
    def create_user(self):
        db.session.add(self)
        db.session.commit()

    # # method to fetch user based on email
    # @classmethod
    # def get_user_by_email(cls, email):
    #     user = UserAuthentication.query.filter_by(email=email).first()
    #     if user:
    #         return True
    #     else:
    #         return False



        # check if email exists
    @classmethod
    def check_email(cls, email):
        user_exist = UserAuthentication.query.filter_by(email=email).first()
        if user_exist:
            return True
        else:
            return False
    #fetch a record
    @classmethod
    def fetch_user(cls, email, password):
        user =UserAuthentication.query.filter_by(email=email, password=password).first_or_404()
        if user:
            return True
        else:
            return False




    # # get user password
    # @classmethod
    # def get_p
