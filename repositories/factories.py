from repositories.users_sqlite_repository import UsersSQLiteRepository


def create_users_repository():
    return UsersSQLiteRepository()