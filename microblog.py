from app import app, db
from app.models import User, Post

@app.shell_context_processor    # registers this function as a shell context function
def make_shell_context():
    """Function called when 'flask shell' command is run

    Returns: Dictionary of (key-> item_name_referenced_in_shell, value-> item)

    """
    return {'db': db, 'User': User, 'Post': Post}