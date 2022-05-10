from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = """insert into survey (name, location, comment)
                    values ( %(name)s, %(location)s, %(comment)s );"""
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results
    
    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['name']) < 1 or survey['name'] == "":
            flash("Name is required")
            is_valid = False
        if len(survey['location']) < 1:
            flash("location is required")
            is_valid = False
        if len(survey['language']) < 1:
            flash("language is required")
            is_valid = False
        if len(survey['comment']) < 1 or survey['comment'] == "":
            flash("comment is required")
            is_valid = False

        return is_valid
